---
title: Corrispettivi in XML
description: Generazione del file XML dei corrispettivi dei distributori di carburante e del file dei periodi di inattività.
modulo: Energy
maschera_id: IDD_ENE_CORRISPETTIVI_TO_XML
---

# Corrispettivi in XML

Due voci che producono **lo stesso tipo di file** — un XML da trasmettere — ma
raccontano due cose opposte: quanto si è venduto, e quando non si è venduto
niente perché l'impianto era fermo.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Energy ▸ Generazione File XML Corrispettivi ▸ *(una delle due voci)*
    - **Scorciatoia:** ++f2++ genera, ++esc++ esce
    - **Dove finisce il file:** cartella **out** del programma

---

## La maschera

È la stessa per tutte e due le voci; cambia quello che il file dichiara.

| Campo | Descrizione |
|---|---|
| **Data Iniziale**, **Ora Iniziale** | L'inizio del periodo. |
| **Data Finale**, **Ora Finale** | La fine. |
| **Sezione** | La [sezione](../../contabilita/sezioni.md) — cioè l'impianto — a cui il file si riferisce. |
| **Motivazione** | Solo per l'inattività: `1 - FERIE`, `2 - MANUTENZIONE`, `3 - EVENTI STRAORDINARI`, ` 4- ALTRO`. |
| **Descrizione** | Il testo che accompagna la motivazione. |

{: .campi }

## Esportazione File XML Corrispettivi

Raccoglie i corrispettivi del periodo indicato e scrive il file nella cartella
**out**, con il nome che porta dentro le due date:

```
corrispettivi_20260901_20260930.xml
```

Alla fine Facile dice come è andata:

| Messaggio | Che cosa vuol dire |
|---|---|
| *Il file è stato salvato correttamente!* | Tutto a posto. |
| *Il file è stato salvato con un errore!* | Il file c'è, ma una riga ha un problema. |
| *Il file è stato salvato con N errori!* | Come sopra, con più righe. |
| *Impossibile salvare il file!* | La cartella **out** non esiste o non è scrivibile. |

!!! warning "Il file viene salvato anche quando ci sono errori"

    Il messaggio conta gli errori ma **il file resta scritto**: non è una
    generazione fallita, è una generazione con dei buchi. Trasmetterlo così
    porta il problema all'Agenzia invece di risolverlo, quindi conviene sempre
    leggere il numero degli errori prima di mandarlo.

### I controlli sui dati della ditta

Prima di generare, Facile verifica tre dati e, se ne manca uno, **chiede se
andare avanti lo stesso**:

| Messaggio | Che cosa manca |
|---|---|
| *Partita IVA Ditta non impostata o non valida! Vuoi continuare?* | La partita IVA della [ditta](../../anagrafiche/ditte.md). |
| *Codice Distributore Carburanti non impostato o non valido! Vuoi continuare?* | Il codice del distributore. |
| *Partita IVA Marchio carburante non impostata o non valida! Vuoi continuare?* | La partita IVA del marchio. |

Rispondendo **Sì** il file viene generato senza quel dato. È una scelta
consapevole, non una scorciatoia: un XML privo della partita IVA non viene
accettato.

## Esportazione File XML Periodo Inattività

Dichiara un periodo in cui l'impianto non ha venduto: ferie, manutenzione,
eventi straordinari.

Valgono gli stessi campi, con due regole in più:

- se l'inattività comincia e finisce **nello stesso giorno**, l'**Ora Finale**
  deve essere successiva all'**Ora Iniziale**;
- scegliendo la motivazione ` 4- ALTRO` la **Descrizione** diventa
  obbligatoria: bisogna dire di che cosa si è trattato.

In entrambi i casi il programma non spiega: **emette un segnale acustico** e
porta il cursore sul campo da sistemare.

!!! note "Il periodo deve stare nell'anno di lavoro"

    La data finale deve appartenere all'esercizio su cui si sta lavorando. Con
    una data di un altro anno il programma si limita al solito segnale acustico:
    prima si cambia esercizio, poi si genera il file.

## Vedi anche

- [Movimenti](movimenti.md)
- [Flussi e riepiloghi](flussi-e-riepiloghi.md)
