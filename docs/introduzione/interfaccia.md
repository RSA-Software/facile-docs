---
title: L'interfaccia di Facile
description: Struttura di una maschera di Facile, barra dei comandi, scorciatoie da tastiera e navigazione tra i moduli.
---

# L'interfaccia di Facile

Facile è fatto di poche finestre tipo, sempre uguali a sé stesse: imparata una
scheda si sanno usare tutte. Questa pagina raccoglie quello che vale ovunque,
così le singole schede non devono ripeterlo.

---

## La finestra principale

Dall'alto in basso:

| | Che cosa contiene |
|---|---|
| **Barra del titolo** | `FACILE - 00001  NOME DITTA - Anno : 2026` — la ditta e l'anno su cui si sta lavorando. Con archivi SQL comincia con `FACILE SQL`. |
| **Menu** | Le voci dei moduli, da **Archivi** a **Utility**, più **File** e **?**. Contiene solo quello che l'utente collegato può aprire. |
| **Barre degli strumenti** | I pulsanti con l'icona, per le operazioni più frequenti. |
| **Area di lavoro** | Dove si aprono le maschere. Se ne possono tenere aperte più d'una insieme. |
| **Barra di stato** | In basso: l'**utente** con cui si è entrati, la **versione** dell'eseguibile e i tre indicatori **CAPS**, **NUM** e **SCRL**. |

Le barre degli strumenti si possono spostare, agganciare ai quattro lati o
lasciare staccate, e si nascondono da **Menu ▸ File ▸ Toolbar ▸ Barra degli
strumenti**. La loro disposizione è **per utente**: ognuno ritrova la sua al
prossimo accesso.

!!! note "Personalizzare le barre è riservato agli amministratori"

    Chi non è amministratore può spostarle e nasconderle, ma non aggiungere o
    togliere pulsanti.

## Le due famiglie di finestre

Quasi tutte le maschere di Facile appartengono a una di due famiglie, e ciascuna
ha i suoi tasti.

### La scheda: un record per volta

È la finestra dell'inserimento e della modifica — un cliente, un articolo, un
deposito. In basso ha la sua fila di pulsanti.

| Pulsante | Tasto | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra. In inserimento la maschera si svuota, pronta per il record successivo. |
| **F3 - Prec.** | ++f3++ | Va al record precedente. |
| **F4 - Succ.** | ++f4++ | Va al record successivo. |
| **F5 - Cerca** | ++f5++ | Apre la finestra di ricerca. |
| **F6 - Elimina** | ++f6++ | Cancella il record, previa conferma. |
| **Ricarica** | | Rilegge il record dall'archivio e **butta via le modifiche non salvate**. |
| **Esci** | ++esc++ | Chiude la maschera. |

Un pulsante spento vuol dire che l'operazione, lì, non si può fare: in
inserimento non c'è un record precedente, a un utente senza il permesso di
cancellare manca **F6**.

### L'elenco: molti record insieme

È la griglia che si apre per scegliere o per consultare.

| Pulsante | Tasto | Effetto |
|---|---|---|
| **Seleziona** | ++f2++ oppure ++enter++ | Prende la riga su cui si è. |
| **Nuovo** | ++f3++ | Crea un record nuovo. |
| **Apri** | ++f4++ | Apre in modifica la riga su cui si è. |
| **Elimina** | ++f6++ | Cancella la riga. |
| **Stampa** | ++f7++ | Stampa l'elenco. |
| **Esci** | ++esc++ | Chiude. |

Dentro la griglia ++up++ e ++down++ cambiano riga; arrivati in fondo (o in cima)
il cursore esce dalla griglia e passa al campo seguente. Con ++shift++ premuto
si esce subito.

## I tasti che valgono dappertutto

| Comando | Tasto | Effetto |
|---|---|---|
| **Guida** | ++f1++ | Apre nel browser la pagina di questo manuale che parla della maschera aperta. |
| **Elenco dei codici** | ++f10++ o ++space++ | Su un campo che vuole un codice, apre l'elenco da cui sceglierlo. Stesso effetto del doppio clic sul campo. |
| **Consultazione** | ++f11++ | Apre la finestra **Consultazione** (vedi sotto). |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice di Windows. |
| **Campo successivo** | ++enter++ | Sposta il cursore sul campo seguente. |
| **Chiusura** | ++esc++ | Chiude la finestra. |
| **Tastiera a video** | ++f24++ | Sulle postazioni touch, mostra e nasconde la tastiera a schermo. |

!!! tip "Il doppio clic vale quanto F10"

    Su qualunque campo che chiede un codice — cliente, articolo, deposito,
    aliquota — un doppio clic apre l'elenco. Chi lavora col mouse non ha bisogno
    di ricordare i tasti funzione.

## La Consultazione (F11)

++f11++ apre una finestra che risponde alla domanda «quanto ne ho e quanto
costa?» **senza chiudere quello che si sta facendo**: si può consultare un
articolo mentre si compila un documento, e tornare indietro dove si era.

Mostra, per l'articolo scelto e per il deposito indicato:

- **descrizione**, **fornitore**, **codice del fornitore** e **aliquota IVA**;
- l'**esistenza**, con l'avviso **SOTTOSCORTA** quando è scesa sotto la scorta
  minima;
- **esistenza iniziale**, **quantità caricata** e **quantità scaricata**
  dell'esercizio;
- l'**ultimo prezzo di acquisto**, l'**incidenza spese** e il **totale costo**;
- una griglia con i **primi tre listini** a confronto: costo, ricarico,
  margine, prezzo imponibile, IVA, prezzo ivato, i sette sconti e i netti;
- in fondo il **costo medio**.

Si passa da un articolo all'altro con ++f3++ e ++f4++, e se ne cerca uno con
++f5++.

## I campi

I campi si compilano con ++enter++ per passare al successivo. Quando un campo è
obbligatorio e si prova a salvare lasciandolo vuoto, Facile **non dice niente**:
emette un segnale acustico e porta il cursore sul campo da riempire. È il
comportamento normale di tutto il programma — un *bip* senza messaggio vuol dire
«manca qualcosa qui».

Nelle tabelle dei campi di questo manuale la colonna **Obbl.** segna con ● i
campi che il programma pretende.

## I messaggi che si incontrano ovunque

Queste risposte non appartengono a una maschera in particolare: le dà il
programma per conto di tutte.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Confermi la Cancellazione....* | Conferma richiesta da **F6 - Elimina**. | **Sì** elimina. La risposta preimpostata è **No**. |
| *Non è possibile eliminare il record poiché utilizzato in alcuni record del database.* | Il record è richiamato da qualche altro archivio. | Non si cancella finché è in uso. |
| *In archivio è già presente un record con lo stesso codice.* | Il codice digitato è di un altro record. | Cambiare codice. |
| *Il record richiesto non è presente in archivio.* | Il codice cercato non esiste. | Controllare il codice, o sceglierlo dall'elenco con ++f10++. |
| *Il record è stato modificato da un altro nodo della rete.* | Un collega ha salvato lo stesso record mentre lo si modificava. | **Ricarica**, guardare che cosa è cambiato e rifare le proprie modifiche. |
| *Il record è stato cancellato da un altro nodo della rete.* | Un collega l'ha eliminato mentre lo si modificava. | La maschera si chiude: non c'è più niente da salvare. |
| *La data è esterna all' esercizio corrente.* | La data digitata non appartiene all'anno su cui si sta lavorando. | Correggere la data, oppure cambiare esercizio. |

I messaggi delle singole maschere stanno in fondo a ciascuna pagina, e tutti
insieme nell'[appendice dei messaggi](../appendici/messaggi-errore.md).

## La guida in linea

++f1++ apre **la pagina di questo manuale che riguarda la maschera aperta**, al
paragrafo giusto, nel browser predefinito del computer. Da **Menu ▸ ? ▸
Argomenti della Guida** si apre invece la copertina.

Il manuale sta su Internet, e si aggiorna senza toccare il programma. Le
postazioni che non hanno un collegamento possono puntare a una **copia locale**:
è una impostazione della postazione, che mette l'assistenza.
