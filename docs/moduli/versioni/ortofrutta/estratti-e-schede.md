---
title: Estratti e schede
description: Estratto vendita, estratto per fornitore, scheda movimenti cliente, provvigioni del periodo, rimanenze e anomalie degli articoli.
modulo: Ortofrutta
maschera_id: IDD_ORT_ESTRATTO_VENDITE
---

# Estratti e schede

Sei voci di menu che guardano lo stesso venduto da sei punti di vista: il
cliente, il produttore, il periodo, la merce che resta.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Ortofrutta ▸ *(Estratto Vendita e voci seguenti)*
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce

---

## Estratto Vendita

Il venduto di un periodo, dal lato del cliente.

| Campo | Descrizione |
|---|---|
| **Dal**, **Al** | Il periodo. |
| **Cliente** | Un cliente solo, oppure vuoto per tutti. |
| **Fornitore** | Restringe al venduto proveniente da un produttore. |
| **Solo Causali Preimpostate** | Considera soltanto le causali di vendita previste dalle impostazioni della ditta, lasciando fuori tutto il resto. |

{: .campi }

Produce la stampa **Estratto Vendite**.

## Estratto Vendita Fornitore

Lo stesso venduto, ma **dal lato del produttore**: che cosa è stato venduto
della sua merce, a chi e a quanto.

| Campo | Descrizione |
|---|---|
| **Dal**, **Al** | Il periodo. |
| **Cliente** | Restringe a un cliente. |
| **Fornitore** | Il produttore di cui si vuole l'estratto. |
| **Filtro** | Quali movimenti prendere: `CAUSALI VENDITA PREIMPOSTATE`, `CAUSALE VENDITA`, `CAUSALE VENDITA S.D.` o `RESI`. |
| **Ordinamento** | `CODICE` o `DESCRIZIONE`. |

{: .campi }

Produce la stampa **Estratto Vendite Fornitore**.

!!! tip "I resi si guardano da soli"

    Scegliendo `RESI` nel **Filtro** si ottiene solo la merce tornata indietro:
    è il modo rapido per capire se un produttore ha un problema di qualità
    prima che se ne accorga il mercato.

## Scheda Movimenti Cliente

Il conto di un cliente, movimento per movimento.

| Campo | Descrizione |
|---|---|
| **Date Iniziale**, **Data Finale** | Il periodo. L'etichetta del primo campo è scritta così nel programma. |
| **Cliente** | Di chi si vuole la scheda. |
| **Tipo Stampa** | `TUTTI`, `FATTURATI` o `NON FATTURATI`. |
| **Stampa Iva** | Aggiunge l'IVA alla stampa. |
| **Dettaglio** | Elenca le singole righe invece dei soli documenti. |

{: .campi }

!!! tip "«Non fatturati» è la lista di quello che manca"

    `NON FATTURATI` mostra le consegne che non sono ancora diventate fattura:
    è il controllo da fare prima della fatturazione di fine mese, per non
    lasciare indietro niente.

## Scheda Provvigioni Periodo

Quanto si è trattenuto di provvigione in un periodo.

| Campo | Descrizione |
|---|---|
| **Dal**, **Al** | Il periodo. |
| **Causale** | Restringe a una causale di magazzino. |
| **Fornitori** | Uno o più produttori; il pulsante **…** apre l'elenco da cui spuntarli. |

{: .campi }

Produce la stampa **Provvigione Periodo**, in due modelli diversi secondo che si
sia scelto un solo produttore o più d'uno.

## Schede Rimanenze

Che cosa è rimasto invenduto a una certa data.

| Campo | Descrizione |
|---|---|
| **Data** | La data a cui fotografare le rimanenze. |
| **Fornitore** | Restringe a un produttore. |
| **Raggruppamento** | Come raccogliere le righe: `PARTITA`, `ARTICOLO + FORNITORE` o `ARTICOLO`. Ogni scelta ha il suo modello di stampa. |

{: .campi }

Nel riquadro **Partita in fase di controllo** si indicano una **Partita** e un
**Fornitore** e la griglia mostra come sta quella partita, per verificarla
prima di stampare.

!!! warning "Le rimanenze sono una fotografia salvata, non un calcolo al volo"

    Premendo ++f2++ Facile chiede prima:

    *Vuoi effettuare il ricalcolo ?*

    - **Sì** rifà i conti dai movimenti e **riscrive** le rimanenze di quella
      data — cancellando quelle salvate prima.
    - **No** stampa quelle già registrate, così come sono.

    La risposta preimpostata è **No**, ed è quella giusta quando si vuole
    ristampare una situazione già chiusa. Il ricalcolo serve invece dopo aver
    corretto dei movimenti: senza, la stampa continua a mostrare i numeri
    vecchi senza dirlo.

## Scheda Anomalie Articoli

Non chiede niente: parte e stampa.

Facile raccoglie **l'esistenza attuale di ogni articolo** nell'anno di lavoro —
limitata alla [sezione](../../contabilita/sezioni.md) dell'utente, se ne ha una —
e la passa al modello **Anomalie Articoli**, che elenca le discordanze. Quali
differenze meritino di comparire lo decide il modello di stampa.

!!! note "Due utenti possono vedere anomalie diverse"

    Chi è legato a una sezione vede solo le sue: la stessa stampa, lanciata da
    due persone, può dare elenchi diversi. Non è un errore, ma è bene saperlo
    prima di confrontare due fogli.

## Vedi anche

- [Partite](partite.md)
- [Chiusura della vendita](chiusura-vendita.md)
