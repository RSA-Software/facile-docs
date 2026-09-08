# Manuale Facile — repository della documentazione

Manuale utente online del gestionale **Facile**, scritto in Markdown e
pubblicato come sito statico con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

Un file `.md` per ogni maschera del programma. Il sito viene ricompilato e
pubblicato automaticamente a ogni `push` su `main`.

---

## Contenuto del repository

```
mkdocs.yml                             configurazione del sito e struttura del menu
requirements.txt                       dipendenze Python
templates/documento-maschera.md        template da copiare per ogni nuova maschera
docs/                                  il manuale vero e proprio
  index.md                             home page
  introduzione/                        primo accesso, interfaccia, convenzioni
  moduli/<modulo>/<maschera>.md         una scheda per maschera
  appendici/                           glossario, elenco messaggi di errore
  assets/img/<modulo>/                 screenshot delle maschere
.claude/skills/manuale-maschere/        skill per Claude Code (vedi sotto)
.github/workflows/pubblica-manuale.yml  build e deploy su GitHub Pages
```

## Avvio in locale

Serve Python 3.9 o superiore.

```bash
pip install -r requirements.txt
mkdocs serve
```

Il manuale è consultabile su <http://127.0.0.1:8000> e si aggiorna da solo a
ogni salvataggio: è il modo più comodo per rileggere una scheda mentre la si
scrive.

Per verificare che non ci siano link rotti o pagine fuori dal menu:

```bash
mkdocs build --strict
```

## Pubblicazione

1. Su GitHub: **Settings ▸ Pages ▸ Source** → *GitHub Actions*.
2. In `mkdocs.yml` sostituire `site_url` e `repo_url` con quelli reali.
3. `git push` su `main`: il workflow compila e pubblica.

Per un dominio personalizzato (es. `manuale.rsasoftware.it`), aggiungere un
record CNAME presso il gestore DNS e indicarlo in **Settings ▸ Pages ▸ Custom
domain**.

## Generare le schede con Claude Code

La cartella `.claude/skills/manuale-maschere/` contiene una skill che insegna a
Claude Code come scrivere una scheda di manuale a partire dal codice sorgente
di una dialog.

**Va copiata nel repository del codice di Facile**, non lasciata qui: Claude
Code deve poter leggere i sorgenti mentre scrive. Il modo più semplice è
tenere i due repository affiancati e lanciare Claude Code dalla cartella che li
contiene entrambi.

```
C:\RSA.CLAUDE\
  Facile\           <- codice sorgente (qui va .claude/skills/manuale-maschere/)
  facile-docs\      <- questo repository
```

Poi, da Claude Code:

```
Documenta la maschera Anagrafica clienti e salva la scheda in ../facile-docs
```

La skill si attiva da sola sulle richieste di documentazione. Impone il
template, vieta i riferimenti tecnici nel testo rivolto all'utente e, dove il
codice non basta a capire il senso funzionale di un campo, lascia un marcatore
`<!-- DA VERIFICARE: ... -->` invece di inventare.

## Screenshot

Unica parte manuale del lavoro. Convenzione:

- percorso `docs/assets/img/<modulo>/<slug-maschera>.png`
- stesso nome del file `.md` della scheda
- catture a finestra intera, tema chiaro, dati di esempio non reali

## Come si scrive una scheda

Le regole di stile sono nel template e nella skill. In sintesi:

- si scrive per l'utente finale: mai nomi di variabili, classi o tabelle;
- le etichette dei campi si riportano **esatte** come appaiono a video;
- le procedure sono elenchi numerati, un'azione per passo;
- i messaggi di errore si riportano con il testo esatto, con causa e rimedio;
- le sezioni del template non si aggiungono né si tolgono: l'uniformità tra le
  schede è ciò che rende il manuale consultabile.
