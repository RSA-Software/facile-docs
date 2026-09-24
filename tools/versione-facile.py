"""Porta nel manuale la versione corrente di Facile.

La versione ha una sola fonte: le tre costanti in testa a
RSAFacile\\RSAFacileDB.h, le stesse con cui il programma scrive
«C/S 2026 B08.00» nella barra di stato.

    #define RELEASE_YEAR   2026
    #define RELEASE_DBVER  8
    #define RELEASE_BUILD  0

Lo script le legge e aggiorna due punti:

- includes/versione-facile.md, il frammento che la home e la pagina delle
  novita' includono con --8<--;
- la riga copyright di mkdocs.yml, che il tema stampa a piede di ogni pagina.

Uso:
    .venv\\Scripts\\python.exe tools\\versione-facile.py [percorso di RSAFacileDB.h]

Senza argomento cerca C:\\rsawin\\Facile\\RSAFacile\\RSAFacileDB.h.
Va lanciato a ogni cambio di versione del programma, prima della build.
"""

import re
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
HEADER_PREDEFINITO = Path(r"C:\rsawin\Facile\RSAFacile\RSAFacileDB.h")
FRAMMENTO = RADICE / "includes" / "versione-facile.md"
MKDOCS = RADICE / "mkdocs.yml"
COPYRIGHT = "© R.S.A. S.a.s. — Tutti i diritti riservati · Manuale aggiornato a Facile {v}"


def leggi_versione(header: Path) -> str:
    testo = header.read_text(encoding="latin-1")
    valori = {}
    for nome in ("RELEASE_YEAR", "RELEASE_DBVER", "RELEASE_BUILD"):
        m = re.search(rf"^\s*#define\s+{nome}\s+(\d+)", testo, re.M)
        if not m:
            sys.exit(f"{nome} non trovato in {header}")
        valori[nome] = int(m.group(1))
    # stesso formato della barra di stato: "%04ld B%02ld.%02ld"
    return "{:04d} B{:02d}.{:02d}".format(
        valori["RELEASE_YEAR"], valori["RELEASE_DBVER"], valori["RELEASE_BUILD"]
    )


def scrivi(percorso: Path, testo: str) -> bool:
    """Scrive in CRLF, come vuole la copia di lavoro; False se non cambia nulla."""
    testo = testo.replace("\r\n", "\n").replace("\n", "\r\n")
    if percorso.exists() and percorso.read_bytes() == testo.encode("utf-8"):
        return False
    percorso.parent.mkdir(parents=True, exist_ok=True)
    percorso.write_bytes(testo.encode("utf-8"))
    return True


def main() -> None:
    header = Path(sys.argv[1]) if len(sys.argv) > 1 else HEADER_PREDEFINITO
    if not header.exists():
        sys.exit(f"Non trovo {header}: passa il percorso di RSAFacileDB.h")
    versione = leggi_versione(header)

    cambiato = scrivi(
        FRAMMENTO,
        "!!! info \"Versione documentata\"\n\n"
        f"    Il manuale descrive **Facile {versione}**. La versione installata la\n"
        "    leggi in basso a destra, nella barra di stato del programma.\n",
    )

    yml = MKDOCS.read_bytes().decode("utf-8")
    # [^\r\n]*: con .* si porterebbe via il \r e la riga resterebbe senza CRLF
    nuovo, n = re.subn(r"(?m)^copyright:[^\r\n]*", "copyright: " + COPYRIGHT.format(v=versione), yml)
    if n != 1:
        sys.exit("Riga copyright non trovata in mkdocs.yml")
    if nuovo != yml:
        MKDOCS.write_bytes(nuovo.encode("utf-8"))
        cambiato = True

    print(f"Facile {versione}" + ("" if cambiato else " (gia' allineato)"))


if __name__ == "__main__":
    main()
