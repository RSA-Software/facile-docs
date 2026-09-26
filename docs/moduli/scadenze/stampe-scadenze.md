---
title: Stampe delle scadenze
description: Le stampe dello scadenziario — elenco, sintesi, solleciti, interessi di mora ed estratto conto per documento.
modulo: Scadenze
maschera_id: IDD_CON_SCADENZE_ST
---

# Stampe delle scadenze

Le stampe che leggono lo scadenziario: l'elenco completo, la sintesi, i
solleciti da mandare a chi è in ritardo, gli interessi di mora e l'estratto
conto documento per documento.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Sintesi
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Solleciti
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Interessi di Mora
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Estratto Conto per Documento
        - Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Stampa
        - Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Stampa Sintesi
        - Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Stampa Estratto Conto per Documento
    - **Scorciatoia:** ++f2++ avvia la stampa, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | Cosa stampa |
|---|---|
| **Stampa** | L'elenco delle scadenze, riga per riga. La finestra si chiama *Stampa Scadenze Clienti*. |
| **Stampa Sintesi** | Il riepilogo per soggetto, senza il dettaglio delle rate. |
| **Stampa Solleciti** | Le lettere di sollecito ai clienti in ritardo. Usa la stessa maschera di **Stampa**. |
| **Stampa Interessi di Mora** | Gli interessi maturati sul ritardo. |
| **Stampa Estratto Conto per Documento** | Lo scaduto e a scadere raggruppati per documento. |

## Prerequisiti

Prima di usare queste stampe occorre avere le scadenze in archivio, che si
consultano dalla [gestione scadenze](gestione-scadenze.md).

## La maschera

![Stampa scadenze](../../assets/img/scadenze/stampe-scadenze.png)

Sono finestre di selezione: i filtri sul soggetto e sulle condizioni, e i
pulsanti **F2 - OK** ed **Esci**.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Fornitore** | | Restringe a un soggetto. Nello scadenziario clienti l'etichetta è **Cliente**. | codice |
| **Destinatario** | | Restringe a una destinazione merce. | codice |
| **Agente** | | Restringe a un [agente](../anagrafiche/anagrafica-agenti.md). | codice |
| **Pagamento** | | Restringe a un [tipo di pagamento](../contabilita/tipi-di-pagamento.md). | codice |
| **Cat. Economica** | | Restringe a una [categoria economica](../anagrafiche/categorie-economiche.md). | codice |
| **Zona** | | Restringe a una [zona](../anagrafiche/zone.md). | codice |
| **Sezione** | | Restringe a una [sezione](../contabilita/sezioni.md) contabile. | codice |
| **Tipo Pagam.** | | Quale modalità di pagamento includere. | `TUTTI`, `RIMESSA DIRETTA`, `RI.BA.`, e le altre dell'elenco |

### Stampa Sintesi

| Campo | Descrizione |
|---|---|
| **Data Riferimento** | La data a cui fotografare la situazione. |
| **Stampa Indirizzo** | Aggiunge l'indirizzo del soggetto. |
| **Zona** | Restringe a una zona. |
| **Tipo Pagamento** | Restringe a un [tipo di pagamento](../contabilita/tipi-di-pagamento.md). |
| **Agente** | Restringe a un [agente](../anagrafiche/anagrafica-agenti.md). |
| **Sezione** | Restringe a una [sezione](../contabilita/sezioni.md). |

### Stampa Interessi di Mora

| Campo | Descrizione |
|---|---|
| **Da Cliente**, **A Cliente** | L'intervallo dei clienti. |
| **Periodo Emissione Documenti** — **Data Iniziale**, **Data Finale** | Quali documenti considerare, per data di emissione. |
| **Periodo Calcolo Interessi** — **Data Iniziale**, **Data Finale** | **Entro quali date contare i giorni di ritardo.** È il periodo che determina il conto. |
| **Sezione** | Restringe a una sezione. |

I due periodi non sono la stessa cosa: il primo sceglie **quali** scadenze
guardare, il secondo dice **da quando a quando** contare il ritardo.

### Stampa Estratto Conto per Documento

| Campo | Descrizione |
|---|---|
| **Giorni Preavviso** | Quanti giorni prima della scadenza far comparire il cliente. |
| **Conferma Invio** | Chiede conferma prima di mandare ogni lettera. |

Sotto c'è la griglia dei clienti da sollecitare, da cui si scelgono quelli a
cui mandare il sollecito.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Prepara e mostra l'anteprima della stampa. |
| **Esci** | ++esc++ | Chiude senza stampare. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Mandare i solleciti

1. Controlla lo scaduto dalla [gestione scadenze](gestione-scadenze.md),
   mettendo **Stato** su `NON PAGATE`.
2. Apri **Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Solleciti**.
3. Restringi se serve per **Agente** o per **Zona**.
4. Premi **F2 - OK**.

### Dare a un cliente il quadro della sua posizione

1. Apri **Stampa Estratto Conto per Documento**.
2. Indica il **Cliente** e stampa: la stampa raggruppa per documento, così il
   cliente ritrova le proprie fatture.

### Vedere quanto si deve ai fornitori

1. Apri **Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Stampa Sintesi**.
2. Premi **F2 - OK**: esce il riepilogo per fornitore.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Una data manca o è fuori ordine. | Guarda dove si è posizionato il cursore. |
| *Vuoi Esportare le scadenze in formato CSV?* | Compare prima della stampa dell'elenco scadenze. | **Sì** produce anche un file da aprire in Excel, **No** stampa e basta. |
| *Esportazione scadenze conclusa con successo* | Il file CSV è stato scritto. | Nessuna azione. |
| *Impossibile salvare il file* | Non si riesce a scrivere il CSV. | Verifica che la cartella sia scrivibile e che il file non sia già aperto. |

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Un campo del filtro non è valido. | Guarda dove si è posizionato il cursore. |

## Note

!!! note "Solleciti e stampa scadenze condividono la maschera"

    **Stampa** e **Stampa Solleciti** aprono la stessa finestra di selezione:
    cambia quello che viene prodotto, non i filtri da compilare.

!!! info "Con quale tasso si calcolano gli interessi di mora"

    Il tasso è **uno solo per tutta la ditta**: si scrive in **% Interessi di
    Mora**, nella scheda della [ditta](../anagrafiche/ditte.md), riquadro degli
    effetti. Non c'è un tasso per cliente né per documento.

    Il conto è l'interesse semplice su base annua:

    ```
    interesse = importo della rata × tasso / 100 × giorni / 365
    ```

    arrotondato al centesimo. I **giorni** si contano così:

    - sulle scadenze **già pagate**, dalla data di scadenza alla data di
      pagamento;
    - sulle scadenze **ancora aperte**, dalla data di scadenza alla **Data
      Finale** del periodo di calcolo.

    In tutti e due i casi il conteggio resta dentro al **Periodo Calcolo
    Interessi**: se la scadenza è anteriore alla data iniziale, si parte da
    quella.

    Le righe che vengono fuori con zero giorni o zero interessi non compaiono
    nella stampa.

!!! info "Il testo del sollecito si cambia, ma non dal programma"

    La lettera è un **modello di stampa**, scelto dal campo **Solleciti di
    Pagamento** nella scheda della ditta: quel numero punta al modello
    corrispondente fra quelli installati — il modello `3` è il file
    `sol00003.rpt` nella cartella dei report.

    Dal programma non c'è nessuna maschera in cui riscrivere il testo: per
    cambiare le frasi, aggiungere il logo o rifare l'impaginazione bisogna
    intervenire sul modello, e lo fa l'assistenza. Si possono però tenere **più
    modelli** e cambiare il numero nella ditta per passare dall'uno all'altro.

    Quello che il programma mette nella lettera da sé sono i dati della ditta —
    logo, telefono, fax, denominazione — e l'elenco delle scadenze aperte del
    cliente.

## Vedi anche

- [Gestione scadenze](gestione-scadenze.md)
- [Controllo crediti e debiti](controllo-crediti.md)
- [Effetti e RI.BA.](effetti-e-riba.md)
