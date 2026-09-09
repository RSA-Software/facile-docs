"""Perche' la cattura non parte: fotografia dello stato, senza toccare niente.

Stampa quali finestre vede lo script, se riconosce Facile, e — con --comando —
prova a mandare un singolo comando e racconta cosa succede.

    .venv\\Scripts\\python.exe tools\\diagnostica.py
    .venv\\Scripts\\python.exe tools\\diagnostica.py --comando 32798

La causa piu' frequente e' il livello di privilegi: se Facile gira come
amministratore e il terminale no, Windows scarta in silenzio i messaggi che
gli mandiamo. Nessun errore, nessun effetto.
"""

import argparse
import ctypes
import sys
import time
from pathlib import Path

try:
    import win32api
    import win32con
    import win32gui
    import win32process
except ImportError:
    sys.exit("manca pywin32: .venv\\Scripts\\pip.exe install -r tools\\requisiti-cattura.txt")


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


def modulo(pid: int) -> str:
    try:
        h = win32api.OpenProcess(0x0410, False, pid)
        return win32process.GetModuleFileNameEx(h, 0)
    except Exception:
        return "(non leggibile)"


def figli(hwnd, ricorsivo=False):
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


def mdi_client(hwnd):
    for h in figli(hwnd):
        if win32gui.GetClassName(h) == "MDIClient":
            return h
    return None


def finestre():
    trovate = []

    def visita(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            trovate.append((hwnd, pid))
        return True

    win32gui.EnumWindows(visita, None)
    return trovate


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--comando", type=int, action="append", default=[],
                    help="comando da provare; ripetibile")
    ap.add_argument("--attesa", type=float, default=8.0)
    ap.add_argument("--controlli", action="store_true",
                    help="elenca i controlli della finestra aperta, con il nome da resource.h")
    args = ap.parse_args()

    print(f"python: {sys.executable}")
    print(f"terminale amministratore: {elevato()}")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import offusca

    pytesseract = offusca._tesseract()
    if pytesseract:
        try:
            print(f"tesseract: {pytesseract.get_tesseract_version()} "
                  f"({pytesseract.pytesseract.tesseract_cmd})")
            print(f"lingue: {', '.join(pytesseract.get_languages())}")
        except Exception as e:
            print(f"tesseract: trovato ma non risponde ({e})")
    else:
        print("tesseract: non disponibile")
    print()

    principali = []
    print("--- finestre visibili con titolo ---")
    for hwnd, pid in finestre():
        classe = win32gui.GetClassName(hwnd)
        titolo = win32gui.GetWindowText(hwnd)[:60]
        ha_menu = bool(win32gui.GetMenu(hwnd))
        client = mdi_client(hwnd)
        esci = modulo(pid)
        marchio = ""
        if client and Path(esci).name.lower() == "facwin.exe":
            principali.append((hwnd, pid))
            marchio = "  <== candidata finestra principale"
        if "facwin" in esci.lower() or marchio:
            print(f"  hwnd={hwnd} pid={pid} classe={classe!r}")
            print(f"      titolo={titolo!r} menu={ha_menu} mdi={bool(client)} admin={elevato(pid)}")
            print(f"      exe={esci}{marchio}")
    print()

    if not principali:
        print("NESSUNA finestra principale riconosciuta (serve menu + area MDI).")
        print("Se Facile e' aperto, incolla qui l'elenco qui sopra.")
        return

    hwnd_main, pid = principali[0]
    print(f"userei hwnd={hwnd_main} (pid {pid}) — admin Facile: {elevato(pid)}, admin terminale: {elevato()}")
    if elevato(pid) == "si" and elevato() == "no":
        print()
        print(">>> Facile gira come amministratore e questo terminale no.")
        print(">>> Windows scarta i messaggi: riapri il terminale come amministratore.")
        return

    if not args.comando:
        print("\nper provare un comando:  tools\\diagnostica.py --comando 32798 --controlli")
        return

    def istantanea():
        insieme = set()
        for h, p in finestre():
            if p == pid:
                insieme.add(h)
        client = mdi_client(hwnd_main)
        if client:
            insieme |= {h for h in figli(client) if win32gui.IsWindowVisible(h)}
        insieme.discard(hwnd_main)
        return insieme

    nomi = {}
    if args.controlli:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import offusca

        nomi = offusca.nomi_dei_controlli(Path("C:/rsawin/Facile"))
        print(f"nomi dei controlli letti dai sorgenti: {len(nomi)}")

    for comando in args.comando:
        prima = istantanea()
        print(f"\n=== comando {comando} ===")
        win32gui.PostMessage(hwnd_main, win32con.WM_COMMAND, comando, 0)

        scadenza = time.time() + args.attesa
        nuove = set()
        while time.time() < scadenza:
            time.sleep(0.3)
            nuove = istantanea() - prima
            if nuove:
                break

        if not nuove:
            print("  nessuna finestra nuova.")
            continue

        for h in nuove:
            l, t_, r, b = win32gui.GetWindowRect(h)
            print(f"  APERTA hwnd={h} classe={win32gui.GetClassName(h)!r} "
                  f"titolo={win32gui.GetWindowText(h)!r} {r-l}x{b-t_} "
                  f"controlli={len(figli(h, True))}")
            if args.controlli:
                print("      id  classe                      x,y     largxalt   nome / testo")
                for c in figli(h, True):
                    if not win32gui.IsWindowVisible(c):
                        continue
                    cl, ct, cr, cb = win32gui.GetWindowRect(c)
                    cid = win32gui.GetDlgCtrlID(c)
                    simbolici = ", ".join(nomi.get(cid, [])[:2])
                    testo = (win32gui.GetWindowText(c) or "").replace("\n", " ")[:35]
                    print(f"  {cid:>6}  {win32gui.GetClassName(c)[:26]:<26} "
                          f"{cl-l:>4},{ct-t_:<4} {cr-cl:>4}x{cb-ct:<4}  "
                          f"{simbolici:<40} {testo}")

            # si chiude sempre con Annulla, mai con Invio
            for messaggio in (win32con.WM_COMMAND, win32con.WM_CLOSE):
                if not win32gui.IsWindowVisible(h):
                    break
                win32gui.PostMessage(h, messaggio, 2 if messaggio == win32con.WM_COMMAND else 0, 0)
                time.sleep(1.0)
            if win32gui.IsWindow(h) and win32gui.IsWindowVisible(h):
                print("  ! finestra rimasta aperta: chiudila tu con ESC prima del prossimo giro")
                return



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
    _avvia_con_log(main, "diagnostica.log")
