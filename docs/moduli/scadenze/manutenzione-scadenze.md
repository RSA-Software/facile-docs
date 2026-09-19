---
title: Manutenzione dello scadenziario
description: Il controllo fra scadenze e schede contabili, l'eliminazione delle scadenze, i totali e il cruscotto finanziario.
modulo: Scadenze
maschera_id: IDD_CON_SCADENZE_ELIMINA
---

# Manutenzione dello scadenziario

Le voci che tengono in ordine lo scadenziario: il confronto con la contabilità,
la pulizia, i totali e il quadro d'insieme.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Controllo Scadenze <-> Schede Contabili
        - Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Controllo Scadenze <-> Schede Contabili
        - Menu ▸ Scadenze ▸ Elimina Scadenze
        - Menu ▸ Scadenze ▸ Totali Scadenze
        - Menu ▸ Scadenze ▸ Cruscotto Finanziario
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Controllo Scadenze <-> Schede Contabili** | Confronta lo scadenziario con le schede contabili e segnala le discordanze. Esiste in due copie, una per lo scadenziario clienti e una per quello fornitori. |
| **Elimina Scadenze** | Toglie dall'archivio le scadenze chiuse, per non trascinarsele dietro. |
| **Totali Scadenze** | I totali dello scadenziario. |
| **Cruscotto Finanziario** | Il quadro d'insieme di incassi e pagamenti attesi. |

## Prerequisiti

Prima di usare queste maschere occorre:

- avere lo scadenziario popolato e la
  [prima nota](../contabilita/registrazione-prima-nota.md) registrata, perché
  il controllo confronta le due cose;
- per l'eliminazione, **una copia di sicurezza recente degli archivi**.

## La maschera

![Elimina scadenze](../../assets/img/scadenze/manutenzione-scadenze.png)

Sono finestre di selezione con il periodo e i filtri, e i pulsanti **F2 - OK**
ed **Esci**. Il **Cruscotto Finanziario** si apre invece come un quadro a video.

### Elimina Scadenze

Tre caselle e nient'altro: niente date, niente filtri per soggetto.

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Elimina Scadenze Clienti Incassate** | | Comprende le scadenze dei clienti già incassate. | attivo/non attivo |
| **Elimina Scadenze Fornitori Pagate** | | Comprende quelle dei fornitori già pagate. | attivo/non attivo |
| **Elimina anche se non Contabilizzate** | | Allarga la pulizia alle scadenze mai passate in contabilità. | attivo/non attivo |

{: .campi }

### Controllo Scadenze ↔ Schede Contabili

Non ha campi di selezione: appena aperta fa il confronto e riempie una
griglia. La finestra si chiama **Clienti** o **Fornitori** secondo la voce da
cui si entra.

### Cruscotto Finanziario

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Periodo da Analizzare** | ● | Quanto avanti guardare. | `30`, `60`, `90`, `120`, `150`, `180 GIORNI` |

{: .campi }

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo da esaminare o da ripulire. | date |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia il controllo, l'eliminazione o il calcolo. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |

## Come si fa

### Verificare che scadenze e contabilità coincidano

1. Apri **Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Controllo Scadenze <->
   Schede Contabili**.
2. Indica il periodo e avvia.
3. Ogni discordanza segnalata è una scadenza senza registrazione o una
   registrazione senza scadenza: si sistema dalla
   [gestione scadenze](gestione-scadenze.md) o dalla
   [prima nota](../contabilita/gestione-prima-nota.md).

### Ripulire le scadenze chiuse

1. **Fai una copia di sicurezza degli archivi.**
2. Stampa prima lo scadenziario, per avere traccia di cosa stai per togliere.
3. Apri **Menu ▸ Scadenze ▸ Elimina Scadenze**.
4. Indica il periodo e avvia.

### Avere il quadro di incassi e pagamenti

Apri **Menu ▸ Scadenze ▸ Cruscotto Finanziario**.

## Controlli e messaggi

| Messaggio | Dove | Causa | Cosa fare |
|---|---|---|---|
| *Confermi la Cancellazione?* | Elimina Scadenze | Chiesto prima di partire, con **No** già selezionato. | È l'unica rete di sicurezza: leggere le caselle spuntate prima di rispondere. |

!!! note "Sono maschere silenziose"

    A parte quella conferma non dicono quasi niente: il controllo lavora e
    riempie la griglia, il cruscotto ricalcola e mostra i numeri. Quando
    qualcosa va storto arriva l'errore SQL della casa, non un messaggio loro.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca una delle date. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! warning "L'eliminazione è definitiva"

    Le scadenze cancellate spariscono con la loro storia, e i controlli
    successivi fra scadenziario e contabilità segnaleranno le registrazioni
    rimaste senza scadenza. Fallo solo su periodi chiusi e dopo una copia di
    sicurezza.

!!! warning "Toglie solo le chiuse, e solo degli anni passati"

    Due condizioni valgono **sempre**, spunte o non spunte:

    - la scadenza dev'essere **chiusa** — incassata o pagata;
    - dev'essere di un **esercizio precedente** a quello in cui si sta
      lavorando.

    Quindi lo scadenziario aperto non si tocca mai, e nemmeno l'anno in corso.

    Le tre caselle **restringono** da lì: senza la prima i clienti non vengono
    toccati, senza la seconda i fornitori, e le scadenze **mai contabilizzate**
    si salvano a meno di spuntare la terza. **Senza nessuna spunta non viene
    cancellato niente**, e il programma parte lo stesso senza dirlo.

!!! info "Che cosa mette in fila il Cruscotto"

    È una fotografia della liquidità nei prossimi giorni, con due colonne
    contrapposte. Da entrare:

    - **Saldo Banche**;
    - **Scadenze Attive**, con il dettaglio *di cui con Data Certa* e *di cui in
      Sofferenza*;
    - **Credito Circolante**;
    - **Ordini Clienti da Evadere** e **Pratiche in Lavorazione**, cioè quello
      che diventerà fatturato ma non lo è ancora.

    Da uscire: **Scadenze Passive**, con lo stesso dettaglio di data certa e
    sofferenza, e **Ordini Fornitori da Ricevere**.

    I numeri non sono in tempo reale: si aggiornano con **F2 - Ricalcola**.

    ⚠ Se l'azienda non ha la gestione **multiesercizio**, il cruscotto si apre
    solo stando sull'**anno corrente**.

!!! tip "Le discordanze sono una griglia, non una stampa"

    Il controllo confronta soggetto per soggetto il saldo dello scadenziario
    con quello della scheda contabile e mette tutto in una griglia: ci sono
    anche i soggetti che tornano.

    Il comando che serve davvero è **Solo diff. <> 0**, che nasconde i quadrati
    e lascia le sole discordanze. Da lì si può **Stampare** o **Esportare**.

    Nessun messaggio a fine controllo: se la griglia filtrata è vuota, vuol
    dire che torna tutto.

## Vedi anche

- [Gestione scadenze](gestione-scadenze.md)
- [Registrazione di prima nota](../contabilita/registrazione-prima-nota.md)
- [Schede contabili](../contabilita/schede-contabili.md)
