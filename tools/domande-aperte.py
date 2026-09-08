"""Raccoglie i marcatori DA VERIFICARE delle schede in DOMANDE-APERTE.md.

Uso, dalla radice del repository:

    .venv/Scripts/python.exe tools/domande-aperte.py
"""

import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "DOMANDE-APERTE.md"


def main() -> None:
    righe: list[str] = []
    totale = 0
    pagine = 0

    for f in sorted(DOCS.rglob("*.md")):
        testo = f.read_text(encoding="utf-8")
        marker = re.findall(r"<!--\s*DA VERIFICARE:\s*(.*?)\s*-->", testo, re.S)
        if not marker:
            continue
        pagine += 1
        tit = re.search(r"^title:\s*(.+)$", testo, re.M)
        titolo = tit.group(1).strip() if tit else f.stem
        righe.append(f"## {titolo}\n")
        righe.append(f"`{f.relative_to(ROOT).as_posix()}`\n")
        for m in marker:
            righe.append("- [ ] " + " ".join(m.split()))
            totale += 1
        righe.append("")

    testa = (
        "# Domande aperte del manuale Facile\n\n"
        "Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.\n"
        f"Aggiornato al {datetime.date.today().isoformat()} — "
        f"**{totale} domande** su {pagine} pagine.\n\n"
        "Ogni voce corrisponde a un commento HTML dentro la pagina indicata: rispondendo\n"
        "alla domanda, la correzione va fatta nella pagina e il marcatore va tolto.\n"
        "Per rigenerare questo elenco:\n\n"
        "    .venv/Scripts/python.exe tools/domande-aperte.py\n\n"
    )
    OUT.write_text(testa + "\n".join(righe), encoding="utf-8")
    print(f"{totale} domande da {pagine} pagine -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
