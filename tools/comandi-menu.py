"""Estrae i comandi del menu principale di Facile dal file di risorse.

Il blocco `IDR_MAINFRAME MENU` di FacWin.rc associa ogni voce di menu a un
identificatore di comando (`ID_...`); `resource.h` lo traduce nel numero che
serve per inviare `WM_COMMAND` alla finestra principale. E' questo passaggio
che permette di aprire una maschera senza inseguire i menu a video: la riga
"Percorso:" delle schede del manuale diventa un comando eseguibile.

    python tools/comandi-menu.py C:/rsawin/Facile > tools/comandi-menu.json

Il .rc e' ANSI (cp1252) con terminatori CRLF: va letto con quell'encoding,
altrimenti le voci accentate saltano.
"""

import json
import re
import sys
from pathlib import Path

ENCODING = "cp1252"
SEPARATORE = " \u25b8 "  # lo stesso usato nelle schede del manuale

RE_POPUP = re.compile(r'^\s*POPUP\s+"(?P<testo>(?:[^"]|"")*)"')
RE_MENUITEM = re.compile(
    r'^\s*MENUITEM\s+"(?P<testo>(?:[^"]|"")*)"\s*,\s*(?P<id>[A-Za-z_][\w]*)'
)
RE_SEPARATORE = re.compile(r"^\s*MENUITEM\s+SEPARATOR")
RE_DEFINE = re.compile(r"^\s*#define\s+(?P<nome>\w+)\s+(?P<valore>0x[0-9A-Fa-f]+|\d+)")


def pulisci(testo: str) -> str:
    """Toglie acceleratore, puntini di sospensione e spazi doppi."""
    testo = testo.replace('""', '"').replace("&", "")
    testo = testo.split("\\t")[0]  # la scorciatoia dopo \t non fa parte del nome
    testo = testo.replace("...", "").strip()
    return re.sub(r"\s+", " ", testo)


def leggi_define(radice: Path) -> dict:
    """Numeri dei comandi. resource.h e', in pratica, l'unico che serve;
    gli altri header di primo livello fanno da rete se un ID manca."""
    valori = {}
    candidati = [radice / "resource.h"]
    candidati += sorted(p for p in radice.glob("*.h") if p.name != "resource.h")
    for header in candidati:
        if not header.exists():
            continue
        try:
            testo = header.read_text(encoding=ENCODING, errors="replace")
        except OSError:
            continue
        if "#define ID" not in testo:
            continue
        for riga in testo.splitlines():
            m = RE_DEFINE.match(riga)
            if m:
                valori.setdefault(m.group("nome"), int(m.group("valore"), 0))
    return valori


def leggi_menu(rc: Path, risorsa: str = "IDR_MAINFRAME") -> list:
    """Percorre il blocco MENU tenendo uno stack dei POPUP aperti."""
    righe = rc.read_text(encoding=ENCODING, errors="replace").splitlines()

    inizio = None
    for i, riga in enumerate(righe):
        if re.match(rf"^\s*{risorsa}\s+MENU\b", riga):
            inizio = i + 1
            break
    if inizio is None:
        raise SystemExit(f"blocco {risorsa} MENU non trovato in {rc}")

    voci = []
    stack = []
    profondita = 0
    in_blocco = False
    attesa_popup = None

    i = inizio
    while i < len(righe):
        riga = righe[i]
        nuda = riga.strip()

        if nuda == "BEGIN":
            profondita += 1
            in_blocco = True
            if attesa_popup is not None:
                stack.append(attesa_popup)
                attesa_popup = None
            i += 1
            continue

        if nuda == "END":
            profondita -= 1
            if profondita == 0:
                break
            if stack:
                stack.pop()
            i += 1
            continue

        if not in_blocco:
            i += 1
            continue

        if RE_SEPARATORE.match(riga):
            i += 1
            continue

        m = RE_POPUP.match(riga)
        if m:
            attesa_popup = pulisci(m.group("testo"))
            i += 1
            continue

        # una MENUITEM puo' andare a capo prima dell'identificatore
        blocco = riga
        j = i
        while re.match(r'^\s*MENUITEM\s+"', blocco) and not RE_MENUITEM.match(blocco):
            j += 1
            if j >= len(righe):
                break
            blocco = blocco.rstrip() + " " + righe[j].strip()

        m = RE_MENUITEM.match(blocco)
        if m:
            voci.append(
                {
                    "percorso": stack + [pulisci(m.group("testo"))],
                    "voce_id": m.group("id"),
                }
            )
            i = j + 1
            continue

        i += 1

    return voci


def main() -> None:
    radice = Path(sys.argv[1] if len(sys.argv) > 1 else "C:/rsawin/Facile")
    rc = radice / "FacWin.rc"
    if not rc.exists():
        raise SystemExit(f"non trovo {rc}")

    numeri = leggi_define(radice)
    comandi = []
    senza_numero = []
    for voce in leggi_menu(rc):
        numero = numeri.get(voce["voce_id"])
        if numero is None:
            senza_numero.append(voce["voce_id"])
        comandi.append(
            {
                "percorso": SEPARATORE.join(voce["percorso"]),
                "segmenti": voce["percorso"],
                "voce_id": voce["voce_id"],
                "comando": numero,
            }
        )

    if senza_numero:
        print(
            f"attenzione: {len(senza_numero)} voci senza numero in resource.h "
            f"(prime: {', '.join(senza_numero[:5])})",
            file=sys.stderr,
        )

    json.dump(
        {"voci": comandi}, sys.stdout, ensure_ascii=False, indent=2, sort_keys=False
    )
    print(file=sys.stdout)


if __name__ == "__main__":
    main()
