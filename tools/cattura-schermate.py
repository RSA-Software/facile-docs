"""Cattura gli screenshot reali delle maschere di Facile.

Idea di fondo: non si insegue il menu a video. `comandi-menu.py` ha gia'
tradotto ogni voce di menu nel suo identificatore di comando, quindi qui basta
mandare `WM_COMMAND` alla finestra principale e aspettare che compaia la
maschera. E' deterministico e ripetibile a ogni build.

    python tools/cattura-schermate.py --solo "Archivi > Clienti" --solo "Archivi > Fornitori"

Prima di partire servono `tools/schermate.yml` (da inventario-schermate.py) e
`tools/cattura.ini` (copia di cattura.ini.esempio).

Regole di prudenza, perche' il programma sta lavorando su un archivio vero:
- si chiude sempre con Annulla/ESC, mai con Invio o F2: nessuna scrittura;
- se una richiesta di conferma resta aperta, la corsa si ferma invece di
  proseguire alla cieca;
- niente doppio avvio: se Facile e' gia' aperto ci si aggancia.

Una maschera che non si apre non e' un errore dello script: spesso e' il
programma che si rifiuta perche' l'archivio non ha dati. Il messaggio viene
registrato nel report cosi' com'e', per rifare quelle poche su un archivio
popolato.
"""

import argparse
import configparser
import ctypes
import json
import subprocess
import sys
import time
import unicodedata
from datetime import datetime
from pathlib import Path

import win32api
import win32con
import win32gui
import win32process
import win32ui
import yaml
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import offusca  # noqa: E402

RADICE = Path(__file__).resolve().parent.parent
TOOLS = RADICE / "tools"
IDCANCEL = 2
CLASSI_CONTENUTO = ("EDIT", "COMBOBOX", "SYSLISTVIEW32", "SYSTABCONTROL32", "AFX", "PVTEXT", "SYSTREEVIEW32")
PULSANTI_USCITA = ("No", "Annulla", "Esci", "Chiudi", "Cancel")

# Un WM_COMMAND scavalca il controllo che il programma fa sulle voci di menu:
# la maggior parte apre una maschera e si chiude con ESC senza toccare niente,
# ma alcune voci partono e basta. Queste non si toccano se non lo si chiede.
VERBI_RISCHIOSI = (
    "azzera", "ricalcol", "elimina", "cancella", "contabilizz", "generazione",
    "ricostru", "aggiorna", "allinea", "converti", "chiusura", "ripristin",
    "importa", "ricezione", "invio", "invia", "trasferisci", "duplica",
    "annulla", "sblocca", "riorganizza", "recupera",
)


# ---------------------------------------------------------------- utilita' win32

def dpi_reale() -> None:
    """Senza questo Windows mente sulle coordinate quando lo schermo e' scalato
    e i ritagli per l'offuscamento finiscono spostati."""
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass


def _handle(valore):
    """ctypes tratta i valori di ritorno come int a 32 bit: su Windows a 64 bit
    un handle cosi' arriva troncato e ogni chiamata successiva fallisce."""
    return ctypes.c_void_p(valore)


def elevato(pid=None) -> str:
    """'si' se il processo gira come amministratore, '?' se non si riesce a dirlo."""
    k32, adv = ctypes.windll.kernel32, ctypes.windll.advapi32
    k32.GetCurrentProcess.restype = ctypes.c_void_p
    k32.OpenProcess.restype = ctypes.c_void_p
    try:
        if pid is None:
            handle = ctypes.c_void_p(k32.GetCurrentProcess())
        else:
            handle = ctypes.c_void_p(k32.OpenProcess(0x0400, False, pid))
            if not handle.value:
                return "?"
        token = ctypes.c_void_p()
        if not adv.OpenProcessToken(handle, 0x0008, ctypes.byref(token)):
            return "?"
        elevazione = ctypes.c_uint32()
        dimensione = ctypes.c_uint32()
        ok = adv.GetTokenInformation(
            token, 20, ctypes.byref(elevazione), 4, ctypes.byref(dimensione)
        )
        k32.CloseHandle(token)
        return ("si" if elevazione.value else "no") if ok else "?"
    except Exception:
        return "?"


def finestre_processo(pid: int) -> set:
    trovate = set()

    def visita(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            _, p = win32process.GetWindowThreadProcessId(hwnd)
            if p == pid:
                trovate.add(hwnd)
        return True

    win32gui.EnumWindows(visita, None)
    return trovate


def figli(hwnd: int, ricorsivo: bool = False) -> list:
    elenco = []

    def visita(h, _):
        elenco.append(h)
        if ricorsivo:
            try:
                win32gui.EnumChildWindows(h, visita, None)
            except Exception:
                pass
        return True

    try:
        win32gui.EnumChildWindows(hwnd, visita, None)
    except Exception:
        pass
    return elenco


def mdi_client(hwnd_main: int):
    for h in figli(hwnd_main):
        if win32gui.GetClassName(h) == "MDIClient":
            return h
    return None


def candidate(pid: int, hwnd_main: int) -> set:
    """Una maschera puo' aprirsi come dialog di primo livello **o** come
    finestra figlia MDI: vanno guardate entrambe."""
    insieme = finestre_processo(pid)
    client = mdi_client(hwnd_main) if hwnd_main else None
    if client:
        insieme |= {h for h in figli(client) if win32gui.IsWindowVisible(h)}
    insieme.discard(hwnd_main)
    return insieme


def finestra_principale(pid: int, attesa: float = 60.0):
    """Facile usa una barra dei menu propria, quindi GetMenu non dice niente:
    la finestra principale si riconosce dall'area MDI."""
    scadenza = time.time() + attesa
    while time.time() < scadenza:
        for h in finestre_processo(pid):
            if mdi_client(h):
                return h
        time.sleep(0.4)
    return None


def descrizione(hwnd: int) -> dict:
    return {
        "hwnd": hwnd,
        "classe": win32gui.GetClassName(hwnd),
        "titolo": win32gui.GetWindowText(hwnd),
        "rect": win32gui.GetWindowRect(hwnd),
    }


def e_messaggio(hwnd: int) -> bool:
    """Distingue un avviso ('Nessun dato presente') da una maschera vera:
    l'avviso ha solo scritte e pulsanti, nessun campo da compilare."""
    controlli = figli(hwnd)
    if len(controlli) > 8:
        return False
    classi = [win32gui.GetClassName(h).upper() for h in controlli]
    if any(any(c.startswith(p) for p in CLASSI_CONTENUTO) for c in classi):
        return False
    return any(c == "BUTTON" for c in classi)


def testo_finestra(hwnd: int) -> str:
    pezzi = [win32gui.GetWindowText(hwnd)]
    for h in figli(hwnd):
        if win32gui.GetClassName(h).upper() == "STATIC":
            t = win32gui.GetWindowText(h).strip()
            if t:
                pezzi.append(t)
    return " — ".join(p for p in pezzi if p).strip()


def controlli_di(hwnd: int) -> list:
    x0, y0, _, _ = win32gui.GetWindowRect(hwnd)
    elenco = []
    for h in figli(hwnd, ricorsivo=True):
        if not win32gui.IsWindowVisible(h):
            continue
        l, t, r, b = win32gui.GetWindowRect(h)
        elenco.append(
            {
                "id": win32gui.GetDlgCtrlID(h),
                "classe": win32gui.GetClassName(h),
                "testo": win32gui.GetWindowText(h),
                "rect": (l - x0, t - y0, r - l, b - t),
            }
        )
    return elenco


def porta_in_primo_piano(hwnd: int) -> None:
    """Windows concede il primo piano solo al processo che ha l'input: senza
    agganciarsi al suo thread, SetForegroundWindow fallisce in silenzio e la
    finestra resta dietro, mezza disegnata."""
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        davanti = win32gui.GetForegroundWindow()
        suo = win32process.GetWindowThreadProcessId(davanti)[0]
        mio = win32api.GetCurrentThreadId()
        agganciato = suo != mio and ctypes.windll.user32.AttachThreadInput(mio, suo, True)
        win32gui.BringWindowToTop(hwnd)
        win32gui.SetForegroundWindow(hwnd)
        if agganciato:
            ctypes.windll.user32.AttachThreadInput(mio, suo, False)
    except Exception:
        pass


def sistema_dimensioni(hwnd: int) -> bool:
    """Alcune maschere si aprono massimizzate e, se hanno pochi dati, vengono
    fuori immagini enormi quasi tutte vuote: si riportano alla dimensione
    normale prima dello scatto."""
    try:
        if ctypes.windll.user32.IsZoomed(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            time.sleep(0.6)
            return True
    except Exception:
        pass
    return False


def ridisegna(hwnd: int) -> None:
    """I controlli ActiveX di Facile (etichette, linguette) si disegnano solo
    quando qualcuno glielo chiede: senza questo escono finestre senza scritte."""
    RDW = 0x0001 | 0x0004 | 0x0080 | 0x0100  # INVALIDATE|ERASE|ALLCHILDREN|UPDATENOW
    try:
        ctypes.windll.user32.RedrawWindow(hwnd, None, None, RDW)
    except Exception:
        pass


def immagine_finestra(hwnd: int, metodo: str = "schermo") -> Image.Image:
    l, t, r, b = win32gui.GetWindowRect(hwnd)
    larg, alt = r - l, b - t

    dc_finestra = win32gui.GetWindowDC(hwnd)
    src = win32ui.CreateDCFromHandle(dc_finestra)
    dest = src.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(src, larg, alt)
    dest.SelectObject(bmp)

    riuscito = False
    if metodo == "schermo":
        pass
    elif metodo in ("auto", "printwindow"):
        # il flag 2 (PW_RENDERFULLCONTENT) serve ai controlli che si disegnano
        # per conto loro; senza, alcuni riquadri escono neri
        riuscito = bool(
            ctypes.windll.user32.PrintWindow(hwnd, dest.GetSafeHdc(), 2)
        )
    if not riuscito and metodo in ("auto", "schermo"):
        porta_in_primo_piano(hwnd)
        ridisegna(hwnd)
        time.sleep(0.5)
        schermo = win32ui.CreateDCFromHandle(win32gui.GetWindowDC(0))
        dest.BitBlt((0, 0), (larg, alt), schermo, (l, t), win32con.SRCCOPY)
        schermo.DeleteDC()
        riuscito = True

    info = bmp.GetInfo()
    grezza = bmp.GetBitmapBits(True)
    img = Image.frombuffer(
        "RGB", (info["bmWidth"], info["bmHeight"]), grezza, "raw", "BGRX", 0, 1
    )

    win32gui.DeleteObject(bmp.GetHandle())
    dest.DeleteDC()
    src.DeleteDC()
    win32gui.ReleaseDC(hwnd, dc_finestra)
    return img


def quasi_vuota(img: Image.Image) -> bool:
    piccola = img.convert("L").resize((32, 32))
    valori = list(piccola.getdata())
    return max(valori) - min(valori) < 8


def premi(hwnd: int, testi=PULSANTI_USCITA) -> bool:
    for h in figli(hwnd, ricorsivo=True):
        if win32gui.GetClassName(h).upper() != "BUTTON":
            continue
        etichetta = win32gui.GetWindowText(h).replace("&", "").strip()
        if any(etichetta.casefold() == t.casefold() for t in testi):
            win32gui.PostMessage(h, win32con.BM_CLICK, 0, 0)
            return True
    return False


def chiudi(hwnd: int, attesa: float = 4.0) -> bool:
    """ESC / Annulla, mai Invio: la maschera non deve salvare niente."""
    for tentativo in (0, 1, 2):
        if not win32gui.IsWindow(hwnd) or not win32gui.IsWindowVisible(hwnd):
            return True
        if tentativo == 0:
            win32gui.PostMessage(hwnd, win32con.WM_COMMAND, IDCANCEL, 0)
        elif tentativo == 1:
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        else:
            premi(hwnd)
        scadenza = time.time() + attesa
        while time.time() < scadenza:
            if not win32gui.IsWindow(hwnd) or not win32gui.IsWindowVisible(hwnd):
                return True
            time.sleep(0.2)
    return False


# ---------------------------------------------------------------- corsa

def normalizza(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.replace("▸", ">"))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return " ".join(t.split()).casefold()


def carica_configurazione(percorso: Path) -> configparser.ConfigParser:
    if not percorso.exists():
        raise SystemExit(f"manca {percorso}: copiare tools/cattura.ini.esempio")
    cfg = configparser.ConfigParser()
    cfg.read(percorso, encoding="utf-8")
    return cfg


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--solo", action="append", default=[], help="prefisso di percorso, ripetibile")
    ap.add_argument("--slug", action="append", default=[], help="cattura solo questi slug")
    ap.add_argument("--ocr", action="store_true", help="rete di sicurezza OCR sui dati a video")
    ap.add_argument("--senza-offuscamento", action="store_true")
    ap.add_argument("--prova", action="store_true", help="elenca cosa farebbe e si ferma")
    ap.add_argument("--includi-rischiose", action="store_true",
                    dest="includi_rischiose",
                    help="non saltare le voci che potrebbero avviare un'elaborazione")
    ap.add_argument("--config", default=str(TOOLS / "cattura.ini"))
    args = ap.parse_args()

    cfg = carica_configurazione(Path(args.config))
    sorgenti = Path(cfg["facile"]["sorgenti"])
    attesa_dialog = cfg.getfloat("cattura", "attesa_dialog", fallback=8.0)
    attesa_disegno = cfg.getfloat("cattura", "attesa_disegno", fallback=2.0)
    metodo = cfg.get("cattura", "metodo", fallback="schermo")
    preferisci_modifica = cfg.getboolean("cattura", "preferisci_modifica", fallback=True)

    schermate = yaml.safe_load((TOOLS / "schermate.yml").read_text(encoding="utf-8"))["schermate"]
    scelte = [s for s in schermate if s.get("comando")]
    if args.solo:
        scelte = [s for s in scelte if any(normalizza(s["percorso"]).startswith(normalizza(p)) for p in args.solo)]
    if args.slug:
        scelte = [s for s in scelte if s["slug"] in args.slug]
    if not scelte:
        raise SystemExit("nessuna schermata selezionata")

    if not args.includi_rischiose:
        rischiose = [s for s in scelte
                     if any(v in normalizza(s["percorso"]) for v in VERBI_RISCHIOSI)]
        if rischiose:
            print(f"{len(rischiose)} voci saltate perche' potrebbero eseguire "
                  f"un'elaborazione invece di aprire una maschera:")
            for s in rischiose:
                print(f"  - {s['percorso']}")
            print("  (per farle comunque: --includi-rischiose, meglio una alla volta"
                  " e su un archivio di scarto)")
            scelte = [s for s in scelte if s not in rischiose]

    if preferisci_modifica:
        # Inserimento apre una maschera vuota e, sulle anagrafiche, senza
        # linguette: per il manuale serve la Modifica, che mostra un record vero
        for s in scelte:
            for alt in s.get("alternative") or []:
                if alt["percorso"].rstrip().endswith("Modifica"):
                    s["percorso"], s["comando"] = alt["percorso"], alt["comando"]
                    break

    print(f"{len(scelte)} schermate da catturare:")
    for s in scelte:
        print(f"  {s['comando']:>6}  {s['percorso']}  ->  {s['immagine']}")
    if args.prova:
        return

    dpi_reale()
    regole = offusca.carica_regole(TOOLS / "regole-privacy.yml")
    mappa_nomi = offusca.nomi_dei_controlli(sorgenti)
    ocr = offusca._tesseract()
    print(f"regole privacy: {len(regole.get('etichette_sensibili') or [])} etichette, "
          f"{len(regole.get('colonne_sensibili') or [])} colonne di griglia")
    print(f"OCR per le griglie: {'attivo' if ocr else 'NON disponibile — gli elenchi restano in chiaro'}")

    eseguibile = Path(cfg["facile"]["eseguibile"])

    def gia_aperto():
        """Una finestra con menu e area MDI e' la finestra principale di Facile."""
        trovati = []

        def visita(hwnd, _):
            if win32gui.IsWindowVisible(hwnd) and mdi_client(hwnd):
                _, p = win32process.GetWindowThreadProcessId(hwnd)
                try:
                    percorso = win32process.GetModuleFileNameEx(
                        win32api.OpenProcess(0x0410, False, p), 0
                    )
                except Exception:
                    percorso = ""
                if Path(percorso).name.lower() == eseguibile.name.lower():
                    trovati.append((p, hwnd))
            return True

        win32gui.EnumWindows(visita, None)
        return trovati

    esistenti = gia_aperto() if cfg.getboolean("facile", "aggancia_se_aperto", fallback=True) else []

    if esistenti:
        pid, hwnd_main = esistenti[0]
        print(f"agganciato a Facile gia' avviato (pid {pid})")
        if elevato(pid) == "si" and elevato() != "si":
            raise SystemExit(
                "Facile gira come amministratore e questo terminale no: Windows\n"
                "scarta i messaggi senza dire niente. Riapri il terminale come\n"
                "amministratore e rilancia."
            )
    else:
        proc = subprocess.Popen([str(eseguibile)], cwd=str(eseguibile.parent))
        pid = proc.pid
        print(f"avviato {eseguibile} (pid {pid})")
        hwnd_main = None

    if not hwnd_main:
        input("Esegui il login e apri l'azienda dimostrativa, poi premi INVIO qui... ")
        hwnd_main = finestra_principale(pid)
    if not hwnd_main:
        raise SystemExit("non trovo la finestra principale di Facile")
    print(f"finestra principale: {win32gui.GetWindowText(hwnd_main)!r}")

    esiti = []
    for s in scelte:
        prima = candidate(pid, hwnd_main)
        win32gui.PostMessage(hwnd_main, win32con.WM_COMMAND, s["comando"], 0)

        nuova = None
        scadenza = time.time() + attesa_dialog
        while time.time() < scadenza:
            time.sleep(0.25)
            differenza = candidate(pid, hwnd_main) - prima
            visibili = [h for h in differenza if win32gui.IsWindowVisible(h)]
            if visibili:
                nuova = max(visibili, key=lambda h: (lambda r: (r[2] - r[0]) * (r[3] - r[1]))(win32gui.GetWindowRect(h)))
                break

        esito = {
            "slug": s["slug"],
            "titolo": s["titolo"],
            "percorso": s["percorso"],
            "scheda": s["scheda"],
            "immagine": s["immagine"],
        }

        if nuova is None:
            esito.update(stato="non-aperta", messaggio="nessuna finestra comparsa")
            print(f"  [ ] {s['slug']}: nessuna finestra")
            esiti.append(esito)
            continue

        if e_messaggio(nuova):
            messaggio = testo_finestra(nuova)
            esito.update(stato="non-aperta", messaggio=messaggio)
            print(f"  [ ] {s['slug']}: {messaggio}")
            premi(nuova, ("OK", "Ok", "No", "Annulla"))
            chiudi(nuova)
            esiti.append(esito)
            continue

        if sistema_dimensioni(nuova):
            print(f"      {s['slug']}: era massimizzata, riportata a dimensione normale")
        porta_in_primo_piano(nuova)
        ridisegna(nuova)
        time.sleep(attesa_disegno)
        try:
            img = immagine_finestra(nuova, metodo)
            if quasi_vuota(img) and metodo == "auto":
                img = immagine_finestra(nuova, "schermo")

            regioni = []
            if not args.senza_offuscamento:
                elenco = controlli_di(nuova)
                maschera_id = s.get("maschera_id", "")
                regioni = offusca.regioni_da_etichette(elenco, regole, maschera_id)
                regioni += offusca.regioni_da_griglia(img, elenco, regole, maschera_id)
                if regole.get("usa_nomi_controllo"):
                    regioni += offusca.regioni_da_controlli(
                        elenco, regole, mappa_nomi, maschera_id
                    )
                if args.ocr:
                    regioni += offusca.regioni_da_ocr(img)
                img = offusca.applica(img, regioni)

            destinazione = RADICE / s["immagine"]
            destinazione.parent.mkdir(parents=True, exist_ok=True)
            img.save(destinazione)
            esito.update(
                stato="catturata",
                dimensioni=list(img.size),
                offuscate=len(regioni),
                finestra=win32gui.GetWindowText(nuova),
            )
            print(f"  [x] {s['slug']}: {img.size[0]}x{img.size[1]}, {len(regioni)} zone offuscate")
        except Exception as errore:  # una maschera storta non deve fermare la corsa
            esito.update(stato="errore", messaggio=repr(errore))
            print(f"  [!] {s['slug']}: {errore}")

        if not chiudi(nuova):
            esito["nota"] = "finestra rimasta aperta"
            print("  ! finestra rimasta aperta: mi fermo per non lavorare alla cieca")
            esiti.append(esito)
            break
        esiti.append(esito)
        time.sleep(0.4)

    report = {
        "eseguito": datetime.now().isoformat(timespec="seconds"),
        "eseguibile": str(eseguibile),
        "totale": len(esiti),
        "catturate": sum(1 for e in esiti if e["stato"] == "catturata"),
        "non_aperte": [e for e in esiti if e["stato"] == "non-aperta"],
        "esiti": esiti,
    }
    (TOOLS / "catture-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    righe = [
        f"# Catture schermate Facile — {report['eseguito']}",
        "",
        f"Catturate **{report['catturate']}** su {report['totale']}.",
        "",
    ]
    if report["non_aperte"]:
        righe += [
            "## Maschere non aperte",
            "",
            "Da rifare su un archivio con i dati:",
            "",
            "| Maschera | Percorso | Messaggio del programma |",
            "|---|---|---|",
        ]
        for e in report["non_aperte"]:
            righe.append(f"| {e['titolo']} | {e['percorso']} | {e.get('messaggio', '')} |")
        righe.append("")
    (TOOLS / "catture-report.md").write_text("\n".join(righe), encoding="utf-8")

    print(f"\n{report['catturate']}/{report['totale']} catturate — report in tools/catture-report.md")


class _Doppio:
    """Tutto quello che si stampa finisce anche in un file di log: cosi' un
    problema si legge dopo, senza dover ricopiare il terminale."""

    def __init__(self, *canali):
        self.canali = canali

    def write(self, testo):
        for c in self.canali:
            c.write(testo)
            c.flush()

    def flush(self):
        for c in self.canali:
            c.flush()


def _avvia_con_log(funzione, nome_log):
    import traceback

    registro = Path(__file__).resolve().parent / nome_log
    with registro.open("w", encoding="utf-8") as f:
        originale = sys.stdout
        sys.stdout = sys.stderr = _Doppio(originale, f)
        try:
            funzione()
        except SystemExit as uscita:
            if uscita.code not in (0, None):
                print(f"\n[uscita] {uscita.code}")
        except BaseException:
            print("\n[errore]")
            traceback.print_exc(file=sys.stdout)
        finally:
            sys.stdout = sys.stderr = originale
    print(f"\nlog completo in {registro}")


if __name__ == "__main__":
    _avvia_con_log(main, "cattura.log")
