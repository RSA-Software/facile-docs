"""Costruisce l'inventario delle schermate da catturare.

Ogni scheda del manuale dichiara gia' tutto il necessario: il titolo, la
`maschera_id`, la riga "Percorso:" con la voce di menu e il segnaposto da
sostituire. Questo script mette insieme quei dati con la mappa prodotta da
`comandi-menu.py` e scrive `tools/schermate.yml`, che e' l'unico file letto
poi dal motore di cattura.

    python tools/inventario-schermate.py

Le voci che il .rc non risolve restano nel file con `stato: da-mappare`:
si correggono a mano in `tools/schermate-override.yml`, che vince sempre
sul generato.
"""

import difflib
import re
import sys
import unicodedata
from pathlib import Path

import yaml

RADICE = Path(__file__).resolve().parent.parent
DOCS = RADICE / "docs"
MAPPA = RADICE / "tools" / "comandi-menu.json"
USCITA = RADICE / "tools" / "schermate.yml"
OVERRIDE = RADICE / "tools" / "schermate-override.yml"

SEP = "▸"
RE_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)
RE_IMMAGINE = re.compile(r"!\[[^\]]*\]\(([^)]+\.png)\)")
RE_PERCORSO = re.compile(r"\*\*Percorso:\*\*(?P<resto>.*?)(?=\n\s*-\s+\*\*|\n\s*\n)", re.S)


def semplifica(testo: str) -> str:
    """Toglie la punteggiatura Markdown e normalizza gli spazi."""
    testo = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", testo)  # link
    testo = re.sub(r"[*_`]", "", testo)
    return re.sub(r"\s+", " ", testo).strip()


def chiave(testo: str) -> str:
    """Forma confrontabile: senza accenti, senza maiuscole, senza doppi spazi."""
    testo = unicodedata.normalize("NFKD", testo)
    testo = "".join(c for c in testo if not unicodedata.combining(c))
    testo = testo.replace("'", "'").replace("-", " ")
    return re.sub(r"\s+", " ", testo).casefold().strip()


def percorsi_dalla_scheda(corpo: str) -> list:
    """Estrae le catene 'Menu > A > B > C', espandendo gli '(oppure X)'."""
    m = RE_PERCORSO.search(corpo)
    if not m:
        return []

    grezzo = semplifica(m.group("resto"))
    catene = []
    for pezzo in re.split(r"(?=Menu\s*" + SEP + ")", grezzo):
        pezzo = pezzo.strip(" -")
        if not pezzo.startswith("Menu"):
            continue

        alternative = []
        oppure = re.search(r"\(\s*oppure\s+(?P<voci>[^)]*)\)", pezzo, re.I)
        if oppure:
            alternative = [
                v.strip(" ,")
                for v in re.split(r",|\bo\b", oppure.group("voci"))
                if v.strip(" ,")
            ]
            pezzo = pezzo[: oppure.start()].strip()

        segmenti = [s.strip() for s in pezzo.split(SEP)]
        segmenti = [s for s in segmenti[1:] if s]  # via la parola "Menu"
        if not segmenti:
            continue
        if any("una delle voci" in s.lower() or "..." in s for s in segmenti):
            catene.append({"segmenti": segmenti, "incerta": True, "alternative": []})
            continue

        catene.append({"segmenti": segmenti, "incerta": False, "alternative": alternative})
    return catene


def main() -> None:
    if not MAPPA.exists():
        raise SystemExit(f"manca {MAPPA}: eseguire prima tools/comandi-menu.py")

    import json

    voci = json.loads(MAPPA.read_text(encoding="utf-8"))["voci"]
    per_chiave = {}
    for v in voci:
        per_chiave.setdefault(chiave(" ".join(v["segmenti"])), v)

    def risolvi(segmenti):
        return per_chiave.get(chiave(" ".join(segmenti)))

    def somiglianti(segmenti, quante=2):
        """Il manuale non sempre cita la voce con le parole esatte del
        programma ("Scadenziario" contro "Scadenzario"): qui si propone la
        voce di menu piu' vicina, che poi un umano conferma."""
        vicine = difflib.get_close_matches(
            chiave(" ".join(segmenti)), list(per_chiave), n=quante, cutoff=0.75
        )
        return [per_chiave[v]["percorso"] for v in vicine]

    schermate = []
    for scheda in sorted(DOCS.rglob("*.md")):
        testo = scheda.read_text(encoding="utf-8")
        fm = RE_FRONTMATTER.match(testo)
        if not fm:
            continue
        try:
            meta = yaml.safe_load(fm.group(1)) or {}
        except yaml.YAMLError:
            continue
        if "maschera_id" not in meta:
            continue

        corpo = testo[fm.end():]
        img = RE_IMMAGINE.search(corpo)
        if not img:
            continue
        immagine = (scheda.parent / img.group(1)).resolve().relative_to(RADICE)

        catene = percorsi_dalla_scheda(corpo)
        principale = catene[0] if catene else None
        comando = risolvi(principale["segmenti"]) if principale and not principale["incerta"] else None

        alternative = []
        if principale and not principale["incerta"]:
            for alt in principale["alternative"]:
                voce = risolvi(principale["segmenti"][:-1] + [alt])
                if voce:
                    alternative.append(
                        {"percorso": voce["percorso"], "comando": voce["comando"]}
                    )

        schermate.append(
            {
                "slug": scheda.stem,
                "scheda": str(scheda.relative_to(RADICE)).replace("\\", "/"),
                "titolo": str(meta.get("title", scheda.stem)),
                "modulo": str(meta.get("modulo", "")),
                "maschera_id": str(meta.get("maschera_id", "")),
                "immagine": str(immagine).replace("\\", "/"),
                "percorso": comando["percorso"] if comando else (
                    (" " + SEP + " ").join(principale["segmenti"]) if principale else ""
                ),
                "voce_id": comando["voce_id"] if comando else None,
                "comando": comando["comando"] if comando else None,
                "alternative": alternative,
                "suggerimenti": (
                    somiglianti(principale["segmenti"])
                    if principale and not principale["incerta"] and not comando
                    else []
                ),
                "stato": "pronta" if comando else "da-mappare",
            }
        )

    if OVERRIDE.exists():
        correzioni = yaml.safe_load(OVERRIDE.read_text(encoding="utf-8")) or {}
        for s in schermate:
            fix = (correzioni.get("schermate") or {}).get(s["slug"])
            if fix:
                s.update(fix)
                s["stato"] = fix.get("stato", "pronta")

    USCITA.write_text(
        "# Generato da tools/inventario-schermate.py — non modificare a mano.\n"
        "# Le correzioni vanno in tools/schermate-override.yml.\n"
        + yaml.safe_dump(
            {"schermate": schermate}, allow_unicode=True, sort_keys=False, width=100
        ),
        encoding="utf-8",
    )

    pronte = sum(1 for s in schermate if s["stato"] == "pronta")
    print(f"{len(schermate)} schede con immagine — {pronte} risolte, {len(schermate) - pronte} da mappare")
    for s in schermate:
        if s["stato"] != "pronta":
            print(f"  da mappare: {s['slug']:38} {s['percorso'] or '(nessun percorso)'}", file=sys.stderr)
            for sug in s.get("suggerimenti") or []:
                print(f"      forse: {sug}", file=sys.stderr)


if __name__ == "__main__":
    main()
