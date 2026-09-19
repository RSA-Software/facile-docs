---
title: Impostazioni della postazione
description: Le impostazioni che valgono per il singolo computer — stampante fiscale, display, bilancia, stampanti, POS, messaggi e comportamento della vendita.
modulo: Utility
maschera_id: IDD_IMPOSTAZIONI
---

# Impostazioni della postazione

Non tutto in Facile è uguale per tutti: la stampante fiscale collegata, il
display del cliente, la bilancia di cassa e decine di preferenze di lavoro sono
**di quel computer**, non della ditta. Si impostano da qui, e cambiarle su una
postazione non tocca le altre.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Utility ▸ Impostazioni Postazione
        - Menu ▸ Utility ▸ Impostazioni Stampanti
        - Menu ▸ Utility ▸ Impostazione FacileWebApiService
        - Menu ▸ Utility ▸ Impostazioni Sistemi di Pagamento Elettronico
        - Menu ▸ Utility ▸ Impostazioni EFT Pos
        - Menu ▸ Utility ▸ Impostazioni Messaggi SMS e WhatsApp
        - Menu ▸ Utility ▸ Impostazioni Stampanti Comande
    - **Scorciatoia:** ++f2++ salva, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | Cosa imposta | Titolo della finestra |
|---|---|---|
| **Impostazioni Postazione** | Il grosso: stampante fiscale e porta, display cliente, bilancia di checkout, cassa automatica, formato etichette e tutte le preferenze di comportamento della vendita. | *Impostazioni* |
| **Impostazioni Stampanti** | Quale stampante di Windows usare per ciascun tipo di documento. | *Impostazione Stampanti* |
| **Impostazione FacileWebApiService** | Il collegamento al servizio web di Facile. | *Impostazione FacileWebApiService* |
| **Impostazioni Sistemi di Pagamento Elettronico** | I sistemi di pagamento elettronico collegati. | *Impostazione Sistemi di Pagamento Elettronico* |
| **Impostazioni EFT Pos** | Quale POS bancario è collegato alla postazione. | *Selezione EFT POS* |
| **Impostazioni Messaggi SMS e WhatsApp** | Le credenziali per mandare SMS e messaggi WhatsApp. | *Impostazioni per Invio SMS e Messaggi WhatsApp* |
| **Impostazioni Stampanti Comande** | Compare solo nella versione Ristorazione, e **non apre niente**: vedi la nota in fondo. | — |

## Prerequisiti

Prima di impostare occorre sapere **come è collegato l'apparecchio**: modello,
porta seriale o indirizzo di rete. Sono dati che dà l'installatore, non il
programma.

Per SMS e WhatsApp servono le credenziali del servizio di invio.

## La maschera

![Impostazioni](../../assets/img/utility/impostazioni-postazione.png)

**Impostazioni** è la finestra più densa del programma: gli apparecchi
collegati nella parte alta, e sotto una lunga colonna di caselle che decidono
come si comporta la vendita.

**Impostazione Stampanti** è una tabella a due colonne. Le altre sono
finestrelle di pochi campi.

## Campi

### Apparecchi collegati

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Stampante Fiscale** | | Il modello di registratore di cassa collegato. L'elenco copre una quarantina di modelli, dai vecchi seriali ai driver moderni: `ELSI RETAIL`, `OLIVETTI`, `DITRON`, `CUSTOM PROTOCOL`, `RCH NUCLEO`, `RCH GLOBE`, `RCH ONDA`, `EPSON FP90`, `MICRELEC`, `DATAPROCESS FPCONNECTOR`, `FASY FSEDRIVER` e altri. Ogni voce riporta fra parentesi i parametri della porta. | voce dell'elenco, `NESSUNA` per nessuna |
| **Porta** | | La porta seriale a cui è collegata. | `NESSUNA`, `COM1` … `COM9` |
| **Data Attivazione RT** | | Da quando il registratore telematico è attivo. | data |
| **Matricola** | | La matricola del registratore. | testo |
| **N. Cassa** | | Il numero della cassa. | numero |
| **Num. Negozio** | | Il numero del negozio. | numero |
| **Customer Display - 1** e **Porta** | | Il display rivolto al cliente e la sua porta. | voce dell'elenco |
| **Customer Display - 2** e **Porta** | | Un secondo display. | voce dell'elenco |
| **Bilancia Checkout** e **Porta** | | La bilancia della cassa. | voce dell'elenco |
| **Cassa Automatica** | | Il sistema di cassa automatica collegato. | voce dell'elenco |
| **Ditta Conv. HACCP** | | La ditta convenzionata per la parte HACCP. | codice |
| **Formato Etichette** | | Il formato predefinito delle [etichette](etichette-barcode.md). | voce dell'elenco |

{: .campi }

### Preferenze di lavoro

Sono caselle da attivare o disattivare. Le principali:

| Casella | Cosa fa quando è attiva |
|---|---|
| **Descrizione completa** | Mostra la descrizione estesa dell'articolo. |
| **Disabilita Numerazione Scontrini** | Toglie la numerazione automatica degli [scontrini](../vendite/scontrini.md). |
| **Calcolo Predefinito per Scontrini** | Applica il calcolo predefinito. |
| **Arrotonda ai 5 Centesimi Superiori** | Arrotonda i totali per eccesso ai cinque centesimi. |
| **Abilita Ricerca Articolo su Vendita con Spazio** | La barra spaziatrice apre la ricerca articolo. |
| **Aggiungi Sempre Nuovo Rigo su Vendita** | Ogni lettura crea una riga nuova invece di sommare. |
| **Posizionamento Iniziale su Codice Articolo su Vendita** | Il cursore parte dal codice articolo. |
| **Abilita Scelta Tipo Vendita** | Fa scegliere il tipo di vendita. |
| **Blocca Scarico Senza Doc. su Vendita** | Impedisce di scaricare merce senza documento. |
| **Fatture da Scontrino su Vendita** | Permette di emettere fattura da uno scontrino. |
| **Stampa Scontrino Sintetico** | Scontrino in forma breve. |
| **Abilita Preferenza Stampe Modalità Testo** | Preferisce le stampe in modalità testo. |
| **Stampa Prezzo Scontato su Etichette** | Sulle etichette compare il prezzo già scontato. |
| **Utilizza Server SQL ove Possibile** | Fa passare dal server SQL le operazioni che lo consentono. |
| **Abilita Modalità TouchScreen** | Interfaccia a sfioramento per la [vendita al banco](../vendite/vendita-al-banco.md). |
| **Abilita Tastiera Virtuale** | Mostra la tastiera a video. |
| **Cerca prima codice a barre e poi articolo** | Inverte l'ordine di ricerca. |
| **Blocca Emissione …** | Undici caselle che impediscono di emettere, dalla vendita, un certo tipo di documento: **Fatture**, **Fatture Acc.**, **Fatture Ric. Fiscali**, **D.D.T.**, **Bolle**, **Buoni Consegna**, **Ricevute Fiscali**, **Ordini**, **Preventivi**, **Note Credito**, **Fatture Pro Forma**. |

{: .campi }

### Impostazione Stampanti

Per ogni voce si sceglie una stampante fra quelle installate in Windows.
Lasciandola vuota si usa la stampante predefinita.

| Campo | Descrizione |
|---|---|
| **Fatture**, **Doc. di Trasporto**, **Buoni di Consegna**, **Bolle Accompagn.**, **Ricevute Fiscali** | La stampante di ciascun documento di vendita. |
| **Ordini Clienti**, **Ordini Fornitori**, **Preventivi**, **Autofatture**, **Fatture Pro Forma** | Le altre stampanti dei documenti. |
| **Preconto Vendita** | La stampante del preconto della [vendita al banco](../vendite/vendita-al-banco.md). |
| **Preconto POS** e **Colonne** | La stampante del preconto del POS e quante colonne ha. |
| **Frontalini** | La stampante dei [frontalini](../casse-bilance/frontalini.md). |
| **Stampante Testo**, **Righe**, **Tipo Stampante** | La stampante per le stampe in modalità testo, quante righe stanno in una pagina e di che tipo è: `AGHI`, `PCL3`, `LASERJET`. |
| **Etichette Barcode** e **Tipo Stampante** | La stampante delle [etichette](etichette-barcode.md) e il suo linguaggio: Zebra EPL2 o ZPL II, TSC TSPL, Intermec, Toshiba, Meteor, EZ-2/EZ-4, `GENERICA` e gli altri. |
| **Etichette Colli** e **Tipo Stampante** | La stampante delle etichette dei colli: `GENERICA` o Intermec Easycoder / Bixolon SLP. |

{: .campi }

### Impostazione FacileWebApiService

| Campo | Descrizione |
|---|---|
| **Nome Servizio** | Il nome con cui il servizio è installato in Windows. |
| **URL Servizio** | L'indirizzo a cui il programma lo interroga. |
| **User**, **Password** | Le credenziali del servizio. |

{: .campi }

Oltre a **F2 - OK** ci sono **F3 - Test**, che prova il collegamento, e **F4 -
Avvia** e **F5 - Arresta**, che fermano e fanno ripartire il servizio di
Windows — ma solo se il servizio sta su questo computer.

### Impostazione Sistemi di Pagamento Elettronico

| Campo | Descrizione |
|---|---|
| **Sistema di Pagamento** | Quale sistema si sta configurando. |
| **Url** | L'indirizzo del servizio. |
| **Token** | La chiave di accesso. |
| **Merchant ID** | Il codice esercente. |

{: .campi }

I tre campi valgono per il sistema scelto in alto: si configura un sistema per
volta e si salva, poi si passa al successivo.

### Impostazioni EFT Pos

La voce apre prima una finestrella, *Selezione EFT POS*, con **sei pulsanti**
— da **EFT POS 1** a **EFT POS 6** — e **Annulla**: si possono configurare
fino a sei terminali. Scelto il numero si apre *Impostazione Parametri EFT
Pos*:

| Campo | Descrizione |
|---|---|
| **Tipo** | Il protocollo del terminale: `PROTOCOLLO INGENICO 17`, `SUMUP`, `DOJO`, `NON CONNESSO`. |
| **Descrizione** | Un nome per riconoscerlo. |
| **Terminal Id** | L'identificativo del terminale. |
| **Pairing Code** e **F3 - Associa** | Il codice di abbinamento e il comando che lo esegue. |
| **Indirizzo IP**, **Porta TCP** | Per i terminali collegati in rete. |
| **Dojo URL**, **Api Key** | Per i terminali che si raggiungono via internet. |
| **Terminali Associati** e **F4 - Cerca** | L'elenco dei terminali trovati e il comando che li cerca. |

{: .campi }

I campi che servono cambiano con il **Tipo**: il programma svuota e nasconde
quelli che non c'entrano.

### Impostazioni Messaggi SMS e WhatsApp

Un campo solo, **Token**: la chiave del servizio di invio.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Salva le impostazioni della postazione. |
| **Esci** | ++esc++ | Chiude senza salvare. |
| Elenco valori | ++f10++ o ++space++ | Sui campi con il codice, apre l'elenco. |

## Come si fa

### Collegare il registratore di cassa

1. Apri **Menu ▸ Utility ▸ Impostazioni Postazione**.
2. Scegli il modello in **Stampante Fiscale**: l'elenco riporta fra parentesi i
   parametri della porta, che devono corrispondere a come l'apparecchio è
   configurato.
3. Indica la **Porta** seriale.
4. Compila **Matricola**, **N. Cassa** e **Num. Negozio**.
5. Premi **F2 - OK** e prova uno scontrino.

### Impedire a una cassa di emettere fatture

1. Apri **Impostazioni Postazione** sulla postazione della cassa.
2. Attiva **Blocca Emissione Fatture su Vendita** e le altre che servono.
3. Premi **F2 - OK**: da quella postazione quei documenti non si emettono più.

È il modo di tenere la cassa alla sola vendita al banco, lasciando la
fatturazione all'ufficio.

### Passare alla vendita a sfioramento

Attiva **Abilita Modalità TouchScreen** e, se il monitor non ha tastiera,
**Abilita Tastiera Virtuale**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Un campo non è valido. | Guarda dove si è posizionato il cursore. |
| *Impostazioni salvate correttamente!* | Pagamenti elettronici o messaggi: il salvataggio è andato. | Nessuna azione. |
| *Impostazioni salvate con successo!* | Lo stesso, per il FacileWebApiService. | Nessuna azione. |
| *Impossibile scriver il file!* | Non si riesce a scrivere il file di configurazione del sistema di pagamento. Il percorso è indicato sotto. | Verifica che la cartella `cfg` sia scrivibile. |
| *Impossibile salvare il file!* | Lo stesso, per il FacileWebApiService. | Come sopra. |
| *Il servizio deve essere installato sulla macchina locale!* | **F4 - Avvia** o **F5 - Arresta** su un servizio che sta su un altro computer. | Va avviato da lì. |
| *Il servizio è stato avviato!* — *Il servizio è stato arrestato!* | Il comando è riuscito. | Nessuna azione. |
| *Impossibile avviare il servizio!* — *Impossibile arrestare il servizio!* | Windows non lo ha permesso. | Servono i diritti di amministratore. |
| *FacileWebApiService non configurato!* | Le funzioni del POS che passano dal servizio web non trovano il servizio. | Configuralo con la voce apposita prima di associare il terminale. |
| *Non è stato possibile identificare il dispositivo!* | L'associazione del terminale POS non è riuscita. | Controlla il **Pairing Code** e che il terminale sia acceso e in rete. |
| *Lettura terminali fallita!* | **F4 - Cerca** non ha ottenuto l'elenco. | Come sopra. |

## Note

!!! warning "Queste impostazioni sono del computer, non della ditta"

    Cambiarle su una postazione non le cambia sulle altre. Quando si aggiunge un
    computer, vanno rifatte da capo: è la causa più comune di «sulla cassa di
    là funziona e qui no».

!!! note "Le caselle «Blocca Emissione» non tolgono i permessi"

    Impediscono l'emissione **da quella postazione**, non all'utente: lo stesso
    operatore, su un altro computer, quei documenti li emette. I permessi veri
    si danno da [Archivi ▸ Utenti](../anagrafiche/utenti.md).

!!! info "Dove stanno queste impostazioni"

    Non sono tutte nello stesso posto, e la differenza conta.

    **Impostazioni Postazione** e **Impostazione Stampanti** stanno nel
    **registro di Windows**, sotto la chiave `R.S.A. Software` dell'utente che
    sta lavorando. Sono quindi legate **a quel computer e a quell'utente
    Windows**: chi entra con un altro account trova le impostazioni vuote.

    Il nome della chiave cambia con la versione — `R.S.A. Software - Studio`,
    `- TaglieColori`, `- Calzature`, `- Oreficerie` e così via — quindi
    installazioni di versioni diverse sullo stesso computer non si pestano i
    piedi.

    **Pagamenti elettronici**, **EFT Pos**, **FacileWebApiService** e
    **Messaggi** stanno invece in **file dentro la cartella `cfg`**
    dell'installazione: un file per sistema di pagamento (`nexi.json`,
    `satispay.json`, `paypal.json`, `sumup.json`, `scalapay.json`,
    `klarna.json`, `revolut.json`, `dojo.json`), più `eftpos.json`,
    `WebApiService.json` e `messages.json`.

    Per rifare una postazione: le prime due vanno rifatte a mano — o copiate
    esportando la chiave del registro —, le altre si copiano copiando i file
    della cartella `cfg`.

!!! info "Che cosa fa «Utilizza Server SQL ove Possibile»"

    Riguarda **le stampe e gli elenchi**, non il modo in cui il programma
    lavora normalmente.

    Con la casella attiva, i report e l'elenco degli articoli **chiedono i dati
    al server** con una interrogazione, invece di scorrere gli archivi dalla
    postazione. Su archivi grandi la differenza si sente, e su alcune stampe è
    obbligatoria: la stampa degli articoli per classificazione, per esempio,
    risponde *Funzionalita' attiva solo con modalita' stampa SQL attivata!* se
    la casella è spenta.

    **Conviene tenerla attiva**, ed è così che arriva: quando l'impostazione
    non è mai stata toccata il programma la considera accesa. Si spegne solo
    per aggirare un problema, e a quel punto vale la pena capire perché.

    Non ha effetto se gli archivi sono locali o se il collegamento ODBC al
    server non è installato: in quei casi il programma legge dagli archivi
    comunque.

!!! warning "«Impostazioni Stampanti Comande» non apre niente"

    La voce compare **solo nella versione Ristorazione** — nelle altre il
    programma la toglie dal menu all'avvio — ma anche lì **non è collegata a
    nessuna finestra**: cliccandola non succede niente. Le stampanti delle
    comande si impostano altrove.

## Vedi anche

- [Vendita e POS touchscreen](../vendite/vendita-al-banco.md)
- [Scontrini](../vendite/scontrini.md)
- [Etichette codici a barre](etichette-barcode.md)
- [Utenti](../anagrafiche/utenti.md)
