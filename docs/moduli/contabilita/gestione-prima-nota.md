---
title: Gestione prima nota
description: L'elenco delle registrazioni di prima nota, da cui si cercano, si aprono, si stampano e vi si allegano i documenti.
modulo: Contabilità
maschera_id: IDD_CON_GEST_PNOTA
---

# Gestione prima nota

L'elenco delle registrazioni contabili: si filtra per periodo, sezione o
causale, si trova quella che serve e la si apre. È il punto da cui si entra
nella contabilità tutti i giorni.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Contabilità ▸ Gestione Prima Nota
    - **Scorciatoia:** ++f2++ apre la registrazione, ++f3++ ne crea una nuova
    - **Permessi richiesti:** nessun profilo predefinito; la voce di menu si abilita per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Le voci **Inserimento** e **Modifica** aprono direttamente la
[registrazione](registrazione-prima-nota.md); questa invece mostra **quello che
c'è già**, e da lì si lavora.

Serve per ritrovare una fattura registrata, per controllare cosa è stato
registrato in un periodo, per allegare a una registrazione il documento
scansionato, e per stampare l'elenco.

## Prerequisiti

Prima di usare questa maschera occorre avere il piano dei conti — [mastri](mastri.md),
[conti](conti.md), [sottoconti](sottoconti.md) — e le
[causali contabili](causali-contabili.md) con cui si registra.

## La maschera

![Gestione prima nota](../../assets/img/contabilita/gestione-prima-nota.png)

In alto la barra dei comandi, sotto i campi del filtro, e nel resto della
finestra la griglia delle registrazioni trovate.

La griglia ha queste colonne:

| Colonna | Contenuto |
|---|---|
| **Codice** | Numero della registrazione. |
| **Data** | Data di registrazione. |
| **Numero Doc.**, **Data Doc.** | Gli estremi del documento registrato. |
| **Totale Doc.** | Totale del documento. |
| **Sez.** | La [sezione](sezioni.md) contabile. |
| **Cau.** | La [causale](causali-contabili.md) usata. |
| **Analitica** | Se la registrazione ha imputazioni di contabilità analitica. |
| **Registro** | Il registro IVA su cui è finita. |
| **Verif.** | È spuntata sulle registrazioni **a posto**. Resta vuota su quelle marcate come *da verificare*. |
| **Descrizione** | La descrizione della registrazione. |
| **Rel.** | La relazione: cliente, fornitore o conto. |
| **Cliente/Fornitore** | Il nominativo. |
| **Dare**, **Avere** | Gli importi. |

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice Iniziale**, **Codice Finale** | | Intervallo di numeri di registrazione. | numeri |
| **Data Iniziale**, **Data Finale** | | Il periodo da mostrare. | date |
| **Riferimento** | | Quale data usare per il filtro del periodo. | `DATA REGISTRAZIONE`, `DATA DOCUMENTO` |
| **Sezione** | | Restringe a una [sezione](sezioni.md) contabile. | codice |
| **Causale** | | Restringe a una [causale](causali-contabili.md). | codice |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Modifica** | ++f2++ | Apre in [modifica](registrazione-prima-nota.md) la registrazione selezionata. |
| **F3 - Nuova** | ++f3++ | Apre una [registrazione nuova](registrazione-prima-nota.md). |
| **F7 - Allegati** | ++f7++ | Allega alla registrazione un documento — tipicamente la scansione della fattura — o apre quelli già allegati. |
| **F9 - Stampa** | ++f9++ | Stampa l'elenco delle registrazioni trovate. |
| **Trova** | | Cerca un testo nella griglia. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Ritrovare una fattura registrata

1. Apri **Menu ▸ Contabilità ▸ Gestione Prima Nota**.
2. Metti **Riferimento** su `DATA DOCUMENTO` e indica il periodo in cui la
   fattura è datata.
3. Se sai la causale, indicala per stringere l'elenco.
4. Trova la riga e premi **F2 - Modifica**.

### Allegare la scansione di una fattura

1. Trova la registrazione nella griglia.
2. Premi **F7 - Allegati** e scegli il file.

### Controllare le registrazioni da verificare

1. Imposta il periodo.
2. Guarda la colonna **Verif.**: le righe con la casella **vuota** sono
   quelle che qualcuno ha marcato come da ricontrollare.
3. Aprile una per una con **F2 - Modifica**, sistema quello che c'è da
   sistemare e togli la spunta a **Registrazione da Verificare** prima di
   salvare.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Un campo del filtro non è valido. | Guarda dove si è posizionato il cursore: è il campo da correggere. |

## Note

!!! note "Due date diverse"

    **Riferimento** decide se il periodo si applica alla data di registrazione
    o a quella del documento. Le due raramente coincidono: una fattura di
    dicembre registrata a gennaio si trova con `DATA DOCUMENTO` cercando in
    dicembre, e con `DATA REGISTRAZIONE` cercando in gennaio.

!!! info "Gli allegati stanno dentro l'archivio, non su disco"

    Il file scelto con **F7 - Allegati** viene **copiato dentro il
    database**, insieme al nome e alla dimensione: da quel momento il file
    originale sul disco non serve più, e spostarlo o cancellarlo non fa
    perdere l'allegato. Chiunque apra quella registrazione da un'altra
    postazione lo vede.

    La finestra di scelta parte dalla cartella `in` dell'utente, ma il file
    si può prendere da dove si vuole; per riaverlo si usa il comando di
    salvataggio, che propone la cartella `out`.

    **Non c'è nessun limite di dimensione**, e non c'è nessun avviso. Ma
    ogni allegato pesa sull'archivio e su ogni copia di sicurezza: per le
    fatture conviene il PDF, non la scansione a piena risoluzione.

!!! note "Chi marca e chi smarca una registrazione"

    Non da qui: la casella **Registrazione da Verificare** sta sulla
    [maschera di registrazione](registrazione-prima-nota.md), sotto i dati
    di testata.

    La si spunta mentre si registra, quando un dato non torna e si vuole
    tornarci sopra. La toglie chi riapre la registrazione e la sistema. Non
    c'è nessun automatismo: né il programma la mette da solo, né la toglie.

!!! note "Che cosa stampa F9"

    Stampa **esattamente la selezione che hai davanti**: lo stesso
    intervallo di numeri, lo stesso periodo, la stessa sezione e la stessa
    causale dei filtri in alto, ordinati per data e poi per numero di
    registrazione.

    Non è il brogliaccio contabile e non è il libro giornale: è l'elenco
    che stai guardando, messo su carta in orizzontale. Non tiene conto di
    eventuali righe selezionate: conta solo il filtro.

## Vedi anche

- [Registrazione di prima nota](registrazione-prima-nota.md)
- [Causali contabili](causali-contabili.md)
- [Stampe contabili](stampe-contabili.md)
