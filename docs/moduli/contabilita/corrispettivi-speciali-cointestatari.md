---
title: Integrazioni, operazioni speciali e cointestatari
description: Le tre gestioni che completano i dati richiesti dalle comunicazioni IVA — integrazioni ai corrispettivi, operazioni speciali e cointestatari delle fatture.
modulo: Contabilità
maschera_id: IDD_CON_CORRISPETTIVI
---

# Integrazioni, operazioni speciali e cointestatari

Tre gestioni che servono a completare quello che la prima nota da sola non
registra: chi ha pagato un corrispettivo sopra soglia, le operazioni che non
passano dai registri ordinari, e i soggetti cointestatari di una fattura.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Contabilità ▸ Dettagli Corrispettivi ▸ Integrazioni *(oppure* Stampa*)*
        - Menu ▸ Contabilità ▸ Operazioni Speciali ▸ Inserimento *(oppure* Modifica *o* Stampa*)*
        - Menu ▸ Contabilità ▸ Cointestatari Fatture ▸ Gestione *(oppure* Stampa*)*
    - **Scorciatoia:** ++f2++ salva o avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Dettagli Corrispettivi ▸ Integrazioni** | Un corrispettivo è anonimo per sua natura; quando supera la soglia va però indicato chi ha comprato. Qui si aggiunge quel dettaglio al corrispettivo già registrato. |
| **Dettagli Corrispettivi ▸ Stampa** | Stampa le integrazioni inserite. |
| **Operazioni Speciali** | Le operazioni che vanno comunicate ma non nascono da una registrazione ordinaria: si inseriscono a mano con i dati del soggetto. |
| **Cointestatari Fatture** | I soggetti cointestatari di una fattura, oltre all'intestatario principale. |

## Prerequisiti

Prima di usare queste maschere occorre avere registrato in
[prima nota](registrazione-prima-nota.md) i corrispettivi e le fatture a cui i
dettagli si riferiscono.

## La maschera

![Integrazioni corrispettivi](../../assets/img/contabilita/corrispettivi-speciali-cointestatari.png)

**Integrazioni Corrispettivi** e **Cointestatari** hanno la stessa forma: in
alto la registrazione a cui ci si riferisce, sotto l'elenco dei soggetti che vi
si aggiungono. **Operazioni Speciali** è una scheda a sé.

## Campi

### Integrazioni Corrispettivi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Reg.** | ● | Data della registrazione del corrispettivo. | data |
| **Num. Rif. Int.** | ● | Il riferimento interno della registrazione. | numero |
| **Tot. Corrispettivo** | | Il totale del corrispettivo registrato. Solo lettura. | — |
| **TOT. INTEGRAZIONI** | | La somma delle integrazioni inserite. Solo lettura. | — |

Per ogni integrazione si compilano:

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice** | | Il codice del soggetto. | codice |
| **Cod. Fiscale** | ● | Il codice fiscale di chi ha comprato. | codice fiscale |
| **Importo** | ● | Quanto di quel corrispettivo gli si attribuisce. | importo |
| **Noleggio/Leasing** | | Segna le operazioni di noleggio o leasing. | attivo/non attivo |

### Operazioni Speciali

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice** | ● | Identificativo dell'operazione. | numero |
| **Cliente / Fornitore** | ● | Se l'operazione è attiva o passiva, e il soggetto. | codice |
| **Nazione** | | La nazione del soggetto. | codice |
| **Partita IVA**, **Cod. Fiscale** | | I dati fiscali del soggetto. | testo |
| **Data Registraz.** | ● | La data dell'operazione. | data |

### Cointestatari Fatture

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Num. Rif. Int.** | ● | Il riferimento interno della registrazione della fattura. | numero |
| **Data Reg.** | ● | Data della registrazione. | data |
| **Num. Fattura**, **Data Fattura.** | | Gli estremi della fattura. | numero e data |

Per ogni cointestatario si compilano **Codice**, **Cod. Fiscale**, **Partita
IVA** e **Persona**.

### Le stampe

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo da stampare. | date |
| **Codice Iniziale**, **Codica Finale** | | Nella stampa delle operazioni speciali, l'intervallo di codici. La seconda etichetta contiene un refuso. | numeri |

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** o **F2 - OK** | ++f2++ | Registra, oppure avvia la stampa. |
| **Esci** | ++esc++ | Chiude senza salvare. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Integrare un corrispettivo sopra soglia

1. Registra il corrispettivo in [prima nota](registrazione-prima-nota.md) e
   annota il riferimento interno.
2. Apri **Menu ▸ Contabilità ▸ Dettagli Corrispettivi ▸ Integrazioni**.
3. Indica **Data Reg.** e **Num. Rif. Int.**.
4. Aggiungi il soggetto con **Cod. Fiscale** e **Importo**.
5. Controlla che **TOT. INTEGRAZIONI** non superi **Tot. Corrispettivo**.
6. Premi **F2 - Salva**.

### Registrare i cointestatari di una fattura

1. Apri **Menu ▸ Contabilità ▸ Cointestatari Fatture ▸ Gestione**.
2. Indica **Num. Rif. Int.** e **Data Reg.** della fattura.
3. Aggiungi i cointestatari con i loro dati fiscali.
4. Premi **F2 - Salva**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! note "Servono alle comunicazioni, non alla contabilità"

    Questi dati non entrano nei saldi né nei registri: servono alle
    [comunicazioni IVA](comunicazioni-iva.md). Se non si è tenuti a quelle
    comunicazioni, le tre gestioni si lasciano vuote.

!!! warning "La soglia la conosci tu, non il programma"

    Facile **non controlla nessun importo** e non avverte mai che un
    corrispettivo andrebbe integrato: decidere quali operazioni integrare
    resta di chi registra.

    Quello che la finestra offre è un confronto a vista: in alto il **Tot.
    Corrispettivo** della giornata, in basso il **TOT. INTEGRAZIONI**, che
    si aggiorna a ogni riga aggiunta. Le integrazioni non possono superare
    il corrispettivo, ma nemmeno questo viene impedito: i due numeri stanno
    lì per essere guardati.

!!! note "Il campo Persona"

    Due sole voci, da scegliere: **FISICA** o **GIURIDICA**. Dice se il
    cointestatario è una persona o una società, ed è il dato che la
    comunicazione pretende per sapere quali campi anagrafici aspettarsi —
    cognome e nome da una parte, ragione sociale dall'altra.

    All'inserimento il programma propone **FISICA**.

!!! info "Come finiscono nella comunicazione"

    Le integrazioni **non viaggiano con la registrazione**: vivono in un
    archivio proprio, legate alla registrazione da cui sono nate.

    Quando prepari la **comunicazione delle operazioni** — lo spesometro —
    il programma le va a prendere **per data**, con lo stesso periodo della
    comunicazione, e ne fa righe a sé: codice fiscale del cliente, importo,
    tipo di pagamento e, per noleggi e leasing, il tipo di veicolo.

    Vale dall'esercizio **2011** in avanti: sugli anni precedenti la
    comunicazione non le guarda.

!!! note "Le due stampe sono la stessa finestra"

    **Stampa Operazioni Speciali** e **Stampa Cointestatari Fatture**
    aprono la stessa maschera, con gli stessi quattro campi — intervallo di
    numeri e intervallo di date.

    Cambiano due cose: il **titolo della finestra**, che dice su quale dei
    due archivi stai lavorando, e i valori proposti, che sono il primo e
    l'ultimo numero e la prima e l'ultima data **di quell'archivio**. Il
    modulo stampato, naturalmente, è diverso.

## Vedi anche

- [Comunicazioni IVA](comunicazioni-iva.md)
- [Registrazione di prima nota](registrazione-prima-nota.md)
