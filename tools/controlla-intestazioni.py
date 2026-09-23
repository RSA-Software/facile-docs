"""Controlla che l'intestazione di ogni scheda sia YAML valido.

Uso, dalla radice del repository:

    .venv\\Scripts\\python.exe tools\\controlla-intestazioni.py

Il blocco fra i due `---` in cima a una scheda non e' testo libero: MkDocs lo
legge come YAML e ne ricava il titolo della pagina e la descrizione che
finisce nel tag <meta> dei motori di ricerca.

Se quel blocco non e' YAML valido il sito **non da' errore**: si limita a
stampare le righe cosi' come sono, in cima alla pagina, dove il lettore le
vede. Nemmeno `mkdocs build --strict` se ne accorge, perche' per lui e'
soltanto del testo.

La causa quasi sempre e' la stessa: un **due punti seguito da spazio** dentro
al valore, che in YAML apre una mappa —

    description: Gli stati avanzamento lavori: quanto e' stato eseguito

Il rimedio e' racchiudere il valore fra virgolette. Il 23/09/2026 il difetto
era su venti schede, alcune da mesi.
"""

import pathlib
import sys

try:
    import yaml
except ImportError:
    sys.exit("manca pyyaml: .venv\\Scripts\\pip.exe install pyyaml")

RADICE = pathlib.Path(__file__).resolve().parent.parent
DOCS = RADICE / "docs"


def intestazione(testo: str):
    """Il blocco fra i due `---`, o None se la scheda non ne ha."""
    if not testo.startswith("---"):
        return None
    fine = testo.find("\n---", 3)
    return None if fine < 0 else testo[3:fine].strip("\r\n")


def main() -> int:
    rotte = []
    for scheda in sorted(DOCS.rglob("*.md")):
        blocco = intestazione(scheda.read_bytes().decode("utf-8"))
        if blocco is None:
            continue
        try:
            letto = yaml.safe_load(blocco)
            if not isinstance(letto, dict):
                raise ValueError("non e' un elenco di campi")
        except Exception as errore:
            rotte.append((scheda, str(errore).split("\n")[0]))

    if not rotte:
        print("intestazioni: tutte valide")
        return 0

    print(f"{len(rotte)} schede con l'intestazione non valida:\n")
    for scheda, errore in rotte:
        print(f"  {scheda.relative_to(RADICE)}")
        print(f"      {errore}")
    print("\nSono finite a video in cima alla pagina. Di solito basta")
    print("racchiudere fra virgolette il valore che contiene i due punti.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
