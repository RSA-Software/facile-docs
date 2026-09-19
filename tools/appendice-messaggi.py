"""Rigenera l'appendice dei messaggi da tutte le schede del manuale.

Legge, in ogni scheda, la sezione «Controlli e messaggi» e ne prende le righe
delle tabelle con le colonne | Messaggio | Causa | Cosa fare |. I messaggi
identici che compaiono su piu' schede diventano una riga sola.

Uso, dalla radice del repository:

    .venv/Scripts/python.exe tools/appendice-messaggi.py
"""

import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = DOCS / "appendici" / "messaggi-errore.md"

# Oltre questo numero di schede il messaggio non e' di una maschera in
# particolare: elencarle tutte occuperebbe piu' spazio del messaggio.
MOLTE = 6

INTESTAZIONE = "| Messaggio | Causa | Cosa fare |"


def sezione_messaggi(testo: str) -> str:
    """La sezione «Controlli e messaggi» della scheda, vuota se non c'e'."""
    m = re.search(r"^## Controlli e messaggi\s*$(.*?)(?=^## |\Z)", testo, re.M | re.S)
    return m.group(1) if m else ""


def righe_tabella(sezione: str):
    """Le righe delle sole tabelle con le tre colonne attese."""
    dentro = False
    for riga in sezione.splitlines():
        r = riga.strip()
        if r.startswith("|"):
            if r.rstrip("| ").replace(" ", "") == INTESTAZIONE.rstrip("| ").replace(" ", ""):
                dentro = True
                continue
            if set(r) <= set("|-: "):
                continue
            if dentro:
                celle = [c.strip() for c in r.strip("|").split(" | ")]
                if len(celle) == 3:
                    yield tuple(celle)
        else:
            if r == "":
                continue
            dentro = False


def chiave_ordine(messaggio: str) -> str:
    return re.sub(r"[^0-9a-zà-ù]", "", messaggio.lower())


def rilega(testo: str, scheda: pathlib.Path) -> str:
    """Riscrive i collegamenti della cella rispetto alla cartella appendici.

    Nelle schede i collegamenti sono relativi alla cartella della scheda:
    portati qui cosi' come sono, punterebbero a pagine inesistenti.
    """
    def sostituisci(m: re.Match) -> str:
        dest = m.group(2)
        if dest.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        ancora = ""
        if "#" in dest:
            dest, ancora = dest.split("#", 1)
            ancora = "#" + ancora
        assoluto = (scheda.parent / dest).resolve()
        try:
            rel = assoluto.relative_to(DOCS.resolve())
        except ValueError:
            return m.group(0)
        return f"[{m.group(1)}](../{rel.as_posix()}{ancora})"

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", sostituisci, testo)


def main() -> None:
    # (messaggio, causa, cosa fare) -> schede in cui compare
    voci: dict[tuple[str, str, str], list[tuple[str, str]]] = {}

    for f in sorted(DOCS.rglob("*.md")):
        if f.parent.name == "appendici":
            continue
        testo = f.read_text(encoding="utf-8")
        sez = sezione_messaggi(testo)
        if not sez:
            continue
        tit = re.search(r"^title:\s*(.+)$", testo, re.M)
        titolo = tit.group(1).strip() if tit else f.stem
        rel = "../" + f.relative_to(DOCS).as_posix()
        for voce in righe_tabella(sez):
            voce = tuple(rilega(c, f) for c in voce)
            voci.setdefault(voce, [])
            if (titolo, rel) not in voci[voce]:
                voci[voce].append((titolo, rel))

    righe = []
    for (messaggio, causa, azione), schede in sorted(
        voci.items(),
        key=lambda kv: (chiave_ordine(kv[0][0]), sorted(kv[1])[0][0], kv[0][1]),
    ):
        if len(schede) > MOLTE:
            dove = f"Molte maschere ({len(schede)})"
        else:
            dove = ", ".join(f"[{t}]({p})" for t, p in sorted(schede))
        righe.append(f"| {messaggio} | {dove} | {causa} | {azione} |")

    testa = (
        "---\n"
        "title: Messaggi di errore\n"
        "description: Elenco alfabetico dei messaggi di Facile, con la maschera "
        "che li mostra, la causa e la soluzione.\n"
        "---\n\n"
        "# Messaggi di errore\n\n"
        "Tutti i messaggi documentati nelle schede, in un elenco solo. Cerca il\n"
        "testo comparso a video con il campo di ricerca in alto.\n\n"
        f"Aggiornato al {datetime.date.today().isoformat()} — **{len(righe)} messaggi**.\n\n"
        "!!! note \"Come leggere la colonna «Dove»\"\n\n"
        "    Porta alla scheda della maschera che mostra il messaggio. Quando lo\n"
        "    stesso messaggio compare su molte maschere — succede per quelli che il\n"
        "    programma usa dappertutto, come la conferma di cancellazione — la\n"
        "    colonna dice **Molte maschere** con il numero: in quel caso la\n"
        "    spiegazione vale per tutte.\n\n"
        "    L'elenco è **generato dalle schede**: ogni messaggio è spiegato anche\n"
        "    in fondo alla pagina della sua maschera, insieme agli altri che si\n"
        "    incontrano nello stesso momento.\n\n"
        "| Messaggio | Dove | Causa | Cosa fare |\n"
        "|---|---|---|---|\n"
    )
    OUT.write_text(testa + "\n".join(righe) + "\n", encoding="utf-8", newline="\r\n")
    print(f"{len(righe)} messaggi -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
