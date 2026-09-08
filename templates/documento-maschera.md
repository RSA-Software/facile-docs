---
title: <Nome della maschera>
description: <Una riga: a cosa serve la maschera. Compare nei risultati di ricerca Google.>
modulo: <Anagrafiche | Vendite | Magazzino | Contabilità | ...>
maschera_id: <identificativo interno della dialog, es. IDD_CLIENTI — utile per ritrovare il codice>
---

<!--
  TEMPLATE DOCUMENTO-MASCHERA — Manuale Facile
  Copiare questo file, rinominarlo con lo slug della maschera e compilarlo.
  Regole: non eliminare sezioni; se una sezione non si applica scrivere
  "Non applicabile." Le sezioni vuote fanno sembrare il manuale incompleto.

  Il blocco "In sintesi" è un ELENCO PUNTATO: senza il trattino Markdown
  unisce le righe in un unico paragrafo e le etichette in grassetto si
  perdono nel testo. Quando una voce ha più valori — per esempio una
  maschera raggiungibile da più voci di menu — l'etichetta va su una riga
  sua e i valori diventano un sotto-elenco:

      - **Percorso:**
          - Menu ▸ Vendite ▸ Fatture ▸ Contabilizza
          - Menu ▸ Vendite ▸ Ricevute Fiscali ▸ Contabilizza
-->

# <Nome della maschera>

<Una o due frasi che rispondono a: cosa permette di fare questa maschera e a chi
serve. Niente gergo interno, niente riferimenti al codice.>

!!! info "In sintesi"

    - **Percorso:** Menu ▸ <Voce> ▸ <Sottovoce>
    - **Scorciatoia:** ++f7++
    - **Permessi richiesti:** <profilo/i abilitati>

---

## A cosa serve

<Il contesto operativo: in quale momento del lavoro si usa questa maschera e
quale problema risolve. 3-6 righe. Un esempio concreto vale più di una
definizione.>

## Prerequisiti

Prima di usare questa maschera occorre:

- <dato o configurazione necessaria, con link alla maschera dove si imposta>
- <...>

Se non ci sono prerequisiti, scrivere: *Nessuno.*

## La maschera

![<Nome della maschera>](../../assets/img/<modulo>/<slug-maschera>.png)

<Descrizione della struttura: quante aree/schede ci sono e cosa contiene
ciascuna. Aiuta il lettore a orientarsi prima di scendere nel dettaglio dei
campi.>

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| <Etichetta esatta come appare a video> | ● | <Cosa contiene e come si compila> | <formato, lunghezza, valori da elenco> |
| <...> |  | <...> | <...> |

{: .campi }

La colonna **Obbl.** segna con ● i campi che il programma richiede
obbligatoriamente per salvare.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **Nuovo** | ++ctrl+n++ | <...> |
| **Salva** | ++f2++ | <...> |
| **Elimina** | ++canc++ | <...> |

## Come si fa

### <Operazione tipica, es. "Inserire un nuovo cliente">

1. <Passo, all'imperativo: "Premere Nuovo.">
2. <Passo.>
3. <Passo, fino al risultato osservabile: "La riga compare nell'elenco.">

### <Seconda operazione tipica>

1. <...>

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *<testo esatto del messaggio a video>* | <perché compare> | <come risolvere> |

## Note

!!! warning "Attenzione"

    <Comportamenti non ovvi, effetti irreversibili, interazioni con altri
    moduli. Se non ce ne sono, eliminare il blocco.>

## Vedi anche

- [<Maschera collegata>](../<percorso>/<file>.md)
- [<Voce di glossario>](../../appendici/glossario.md#<ancora>)
