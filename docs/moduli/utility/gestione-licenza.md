---
title: Gestione della licenza
description: Come si attiva Facile su un computer, come si rimuove la licenza e come si trasferisce su un'altra macchina.
modulo: Utility
maschera_id: IDD_RSAREGISTER_ATTIVAZIONE
---

# Gestione della licenza

Facile è legato al computer su cui è installato. Queste tre voci servono ad
attivarlo la prima volta, a liberarlo quando il computer viene dismesso e a
spostare la licenza su una macchina nuova.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Utility ▸ Gestione Licenza ▸ Attivazione Licenza
        - Menu ▸ Utility ▸ Gestione Licenza ▸ Rimozione Licenza
        - Menu ▸ Utility ▸ Gestione Licenza ▸ Trasferimento Licenza
    - **Scorciatoia:** ++f2++ conferma, ++f3++ stampa il modulo, ++f4++ attiva via internet, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Attivazione Licenza** | Registra l'installazione presso R.S.A. e attiva il programma su questo computer. La finestra si chiama *Attivazione*. |
| **Rimozione Licenza** | Disattiva la licenza su questo computer, liberandola. |
| **Trasferimento Licenza** | Sposta la licenza su un'altra macchina. |

Il livello di licenza decide **quali voci di menu si vedono**. I livelli sono
quattro, e a video si chiamano `LIGHT`, `SMALL`, `PROFESSIONAL` e `EVOLUTION`:
mostrano menu via via più ampi. Questo manuale descrive il menu completo;
nelle licenze inferiori alcune voci non compaiono.

## Prerequisiti

Prima di attivare occorre avere i dati della ditta intestataria della licenza —
ragione sociale, indirizzo, partita IVA — e il codice fornito da R.S.A.

Prima di trasferire, il computer di destinazione deve essere pronto: la licenza
viene liberata da questo e va attivata sull'altro.

## La maschera

![Attivazione](../../assets/img/utility/gestione-licenza.png)

**Attivazione** è una scheda con i dati dell'intestatario, il riquadro
**C O D I C I** e i pulsanti in fondo.

Le altre due voci chiedono prima conferma con un riepilogo di quello che
stanno per fare, e poi aprono una finestrella:

- **Rimozione** mostra *CLICCARE SUL PULSANTE "F2 - RIMUOVI" PER RIMUOVERE LA
  LICENZA* e, sotto, *PRENDERE NOTA DEL CODICE RIMOZIONE PER RICHIEDERE UNA
  NUOVA LICENZA*, con il riquadro in cui il codice comparirà;
- **Trasferimento** chiede il **Nuovo Cod. Sito** e, premuto **F2 -
  Trasferisci**, scrive nel riquadro in basso la **NUOVA CHIAVE DI
  ATTIVAZIONE**.

## Campi

### Attivazione

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Nome Computer** | | Il nome della macchina su cui si sta attivando. Lo propone il programma. | testo |
| **Rag. Soc. Ditta** | ● | La ragione sociale dell'intestatario della licenza. | testo |
| **Indirizzo** | ● | L'indirizzo. | testo |
| **Città** | ● | Il comune. | testo |
| **Cap** | ● | Il codice di avviamento postale. | numero |
| **Prov** | ● | La sigla della provincia. | due lettere |
| **Telefono**, **Fax** | | I recapiti. | testo |
| **Partita IVA** | ● | La partita IVA dell'intestatario. | 11 cifre |
| **Cod. Fiscale** | | Il codice fiscale. | codice |
| **Email** | ● | L'indirizzo di posta a cui R.S.A. manda le comunicazioni sulla licenza. | indirizzo |
| **Tipo Licenza** | ● | Il livello acquistato. | `LIGHT`, `SMALL`, `PROFESSIONAL`, `EVOLUTION` |

{: .campi }

Nel riquadro **C O D I C I**:

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Cod. Sito** | | Identifica questa installazione. Lo calcola il programma e **non si tocca**: è il numero da comunicare a R.S.A. | Sola lettura |
| **Cod. Macchina** | | Identifica il computer. Lo calcola il programma. | Sola lettura |
| **Numero Serie** | ● | Il numero di serie ricevuto all'acquisto. | codice |
| **Chiave Attivazione** | ● | La chiave che R.S.A. restituisce. È l'unica cosa che si digita a mano. | codice |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Attiva** | ++f2++ | Attiva il programma con la **Chiave Attivazione** scritta nel campo. |
| **F3 - Stampa** | ++f3++ | Stampa il modulo *Richiesta Attivazione* da mandare a R.S.A. |
| **F4 - Attiva On Line** | ++f4++ | Si collega al server R.S.A. e prende la chiave da sé. |
| **Esci** | ++esc++ | Chiude senza attivare. |

Nelle altre due finestre i pulsanti sono **F2 - Rimuovi** e **F2 -
Trasferisci**.

## Come si fa

### Attivare Facile, con il computer collegato a internet

1. Apri **Menu ▸ Utility ▸ Gestione Licenza ▸ Attivazione Licenza**.
2. Compila i dati della ditta intestataria: sono quelli che compariranno sulla
   licenza, quindi vanno scritti giusti la prima volta.
3. Scrivi il **Numero Serie** e scegli il **Tipo Licenza**.
4. Premi **F4 - Attiva On Line** e, quando richiesto, indica il tuo **codice
   cliente** e la **password** R.S.A.
5. Il programma prende la chiave da sé e si attiva.

### Attivare Facile senza internet

1. Apri la stessa maschera e compila i dati come sopra.
2. Premi **F3 - Stampa**: esce il modulo *Richiesta Attivazione*, con i dati
   della ditta, il **Numero Serie**, il **Cod. Sito** e il **Cod. Macchina**.
3. Manda il modulo a R.S.A.
4. Quando ti arriva la **Chiave Attivazione**, riapri la maschera, scrivila
   nel campo e premi **F2 - Attiva**.

### Spostare Facile su un altro computer

L'ordine è quello che dice il programma, ed è il contrario di quello che
verrebbe da fare: **prima si prepara il computer nuovo**.

1. **Installa Facile sul computer nuovo.**
2. Sul computer nuovo apri **Attivazione Licenza** e **prendi nota del Cod.
   Sito**.
3. Torna sul computer vecchio, apri **Trasferimento Licenza** e conferma.
4. Scrivi quel numero in **Nuovo Cod. Sito** e premi **F2 - Trasferisci**.
5. **Prendi nota della chiave di attivazione** che compare.
6. Sul computer nuovo, scrivi la chiave in **Chiave Attivazione** e premi
   **F2 - Attiva**.

### Dismettere un computer

1. Apri **Rimozione Licenza** e conferma.
2. **Prendi nota del codice di rimozione** che compare: senza quel numero
   R.S.A. non può rilasciare una nuova attivazione.

Da quel momento su quel computer il programma non è più attivo, e le tre voci
del menu Gestione Licenza si spengono.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Licenza non ancora attivata !* | Si prova a rimuovere o trasferire una licenza mai attivata. | Non c'è nulla da rimuovere. |
| *Software non protetto!* | L'installazione non ha protezione attiva. | Nessuna azione: è una versione senza licenza. |
| *Errore interfaccia protezione!* | Il componente di protezione non risponde. | Chiama l'assistenza. |

Le due conferme, per esteso:

!!! note "Rimozione Licenza"

    *La procedura permette la rimozione della licenza del software.*

    *Per riattivare il software è necessario prendere nota del codice di
    rimozione e richiedere un nuovo codice di attivazione alla R.S.A.*

    *Vuoi continuare ?*

!!! note "Trasferimento Licenza"

    *La procedura permette il trasferimento della licenza su un altro
    computer.*

    *Per effettuare il trasferimento effettuare le seguenti operazioni*

    *1 - Installare il software sull' altro computer*
    *2 - Andare nella maschera di attivazione della licenza e prendere nota sel
    cod. sito*
    *3 - Inserire il cod. sito in questa maschera e d effettuare il
    trasferimento di licenza*
    *4 - Prendere nota della chiave di attivazione ed attivare il software
    sull' altro computer*

    *Vuoi continuare ?*

In tutte e due la risposta preimpostata è **No**.

## Note

!!! warning "La licenza è una sola, e il trasferimento va fatto nell'ordine giusto"

    Rimozione e trasferimento **liberano** la licenza da questo computer: finché
    non la si attiva altrove, non è attiva da nessuna parte.

    Per il trasferimento serve il **Cod. Sito del computer nuovo**, e quel
    numero si legge solo dopo aver installato Facile lì. Chi libera prima la
    licenza sul computer vecchio resta senza programma da nessuna delle due
    parti finché non completa l'installazione sull'altro.

!!! note "Il livello di licenza cambia il menu"

    Con `LIGHT` e `SMALL` alcune voci descritte in questo manuale non compaiono
    affatto. Non è un malfunzionamento: è il livello di licenza. Vedi
    [Convenzioni del manuale](../../introduzione/convenzioni.md).

!!! info "Internet serve solo se si vuole"

    Ci sono **due strade** per farsi dare la chiave, e si scelgono con due
    pulsanti diversi:

    | | **F4 - Attiva On Line** | **F3 - Stampa** |
    |---|---|---|
    | Serve internet | sì | no |
    | Cosa chiede | codice cliente e password R.S.A. | niente |
    | Come arriva la chiave | il programma la prende da sé | R.S.A. la manda, e si digita a mano |
    | Quanto ci vuole | subito | il tempo di una risposta |

    Il modulo stampato porta i dati della ditta, il **Numero Serie**, il **Cod.
    Sito** e il **Cod. Macchina**: sono i tre numeri con cui R.S.A. calcola la
    chiave, e servono tutti e tre.

    Se il collegamento non riesce il programma prova tre server diversi prima
    di rinunciare.

!!! warning "Nel testo del trasferimento ci sono due refusi"

    *prendere nota **sel** cod. sito* e *inserire il cod. sito in questa
    maschera **e d** effettuare*. Non sono errori di questo manuale: il
    messaggio è scritto così nel programma.

## Vedi anche

- [Impostazioni della postazione](impostazioni-postazione.md)
- [Ditte](../anagrafiche/ditte.md)
- [Convenzioni del manuale](../../introduzione/convenzioni.md)
