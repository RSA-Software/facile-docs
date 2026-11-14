---
title: Registratori telematici
description: Quali registratori telematici Facile sa pilotare dalla vendita al banco, dove si sceglie il modello e come si abbina il display cliente.
modulo: Casse e Bilance
---

# Registratori telematici

Il registratore telematico è la stampante fiscale collegata alla postazione di
vendita: quando dal [banco](../../vendite/vendita-al-banco.md) batti uno
scontrino, Facile gli manda le righe, i pagamenti e la chiusura, e il
registratore stampa e trasmette i corrispettivi.

!!! info "In sintesi"

    - **Dove si sceglie:** Menu ▸ Utility ▸ [Impostazioni Postazione](../../utility/impostazioni-postazione.md), campo **Stampante Fiscale**
    - **Vale per:** la sola postazione su cui lo imposti
    - **Pagine dei modelli:** [Custom](custom.md), [Micrelec](micrelec.md), [RCH](rch.md); le casse 3i e le casse DTR sono qui sotto: [3i](#le-casse-3i), [DTR](#le-casse-dtr)

---

## A cosa serve

Ogni postazione di cassa parla con il suo registratore. Il modello si sceglie
una volta, nelle impostazioni della postazione, e da lì in avanti la vendita
al banco, gli scontrini, i resi, gli annulli, le letture e le chiusure
giornaliere passano dal registratore senza altre scelte.

Registratori diversi parlano lingue diverse: anche quando due modelli usano un
protocollo con lo stesso nome, i comandi possono cambiare. Per questo nell'elenco
ogni modello ha la sua voce, e per alcuni ci sono più voci, una per ciascun modo
di collegarlo.

## I modelli in elenco

Il campo **Stampante Fiscale** propone queste voci. Fra parentesi ci sono i
parametri della porta seriale, che devono corrispondere a come è configurato
l'apparecchio.

| Voce | Collegamento |
|---|---|
| `NESSUNA` | Nessun registratore: dal banco non si battono scontrini. |
| `ALTRA NON IN ELENCO` | Un modello non gestito direttamente. |
| `DITRON` | — |
| `DITRON SPOOLER` | — |
| `CUSTOM XON / XOFF (19200,N,8,1)` | Seriale — vedi [Custom](custom.md) |
| `CUSTOM PROTOCOL` | — vedi [Custom](custom.md) |
| `CUSTOM WEB SERVICE` | Rete, con il web service del registratore, **in versione beta** — vedi [Custom](custom.md#web-service) |
| `EPSON FP (9600,N,8,1)` | Seriale |
| `EPSON FP (57600,N,8,1)` | Seriale |
| `3I XON / XOFF (9600,N,8,1)` | Seriale |
| `3I FAST XON / XOFF (9600,N,8,1)` | Seriale |
| `3I XON / XOFF LAN` | Rete |
| `DTR XON / XOFF (19200,N,8,1,ECHO ON)` | Seriale |
| `DTR XON / XOFF LAN` | Rete |
| `MICRELEC` | Attraverso il programma di Micrelec — vedi [Micrelec](micrelec.md) |
| `MICRELEC G100` | Rete — vedi [Micrelec](micrelec.md) |
| `OLIVETTI XON / XOFF (9600 N 8 1)` | Seriale |
| `EDIT XON / XOFF (9600,N,8,1)` | Seriale |
| `RCH XON / XOFF (9600,N,8,1)` | Seriale — vedi [RCH](rch.md) |
| `RCH XON / XOFF LAN` | Rete — vedi [RCH](rch.md) |
| `RCH MULTIDRIVER SERVER` | Attraverso il driver di RCH — vedi [RCH](rch.md) |
| `RCH WEB SERVICE` | Rete, con il web service del registratore — vedi [RCH](rch.md#web-service) |

Per i modelli collegati in rete la porta seriale non serve: l'indirizzo del
registratore si scrive nel file di configurazione del modello, descritto nella
sua pagina.

## Il display cliente

Il display rivolto al cliente, quando è attaccato al registratore, non ha una
porta sua: si pilota attraverso il registratore. In
[Impostazioni Postazione](../../utility/impostazioni-postazione.md) va scelto, in
**Customer Display - 1**, il tipo che corrisponde al registratore — per esempio
`RCH XON/XOFF` con la stampante fiscale `RCH XON / XOFF (9600,N,8,1)` — e la
**Porta** deve essere la stessa del registratore.

## Matricola e data di attivazione

In [Impostazioni Postazione](../../utility/impostazioni-postazione.md) si
compilano anche **Matricola** e **Data Attivazione RT**. Con alcuni modelli la
matricola non si può leggere dal registratore e va scritta a mano: serve ai
documenti di reso e di annullo, che la riportano.

## Le casse 3i

Vale per le tre voci `3I XON / XOFF (9600,N,8,1)`, `3I FAST XON / XOFF
(9600,N,8,1)` e `3I XON / XOFF LAN`. Per la voce in rete l'indirizzo e la porta
del registratore stanno nel file `3i.ini` della cartella **cfg**.

### Numero dello scontrino e azzeramento

- Facile chiede al registratore il **numero dello scontrino** una volta sola,
  al pagamento, mentre lo scontrino è ancora aperto, e non lo richiede dopo la
  chiusura, quando la cassa sta stampando. Con più pagamenti nello stesso
  scontrino vale l'ultimo numero letto.
- Se la cassa non risponde a quella richiesta, o la rifiuta — lo fa quando è in
  errore: carta finita, giornale elettronico assente, testina alzata — il
  pagamento parte lo stesso, lo scontrino si stampa e si registra **senza
  numero fiscale**. Nel file degli errori `sqlerr.txt`, nella cartella `log`,
  resta una riga che comincia con *Cassa 3i: numero dello scontrino non letto*
  (vedi i [messaggi della vendita](../../vendite/vendita-al-banco.md#quando-la-cassa-o-la-bilancia-non-rispondono)).
  Per un reso o un annullo di quello scontrino il numero va indicato a mano.
- Il **numero di azzeramento** si legge prima dello scontrino, sia nel **Pos
  Touchscreen** sia in **Vendita**. Se la cassa non risponde, lo scontrino si
  registra con azzeramento 1, come prima.
- Con la casella **Disabilita Numerazione Scontrini** delle
  [Impostazioni Postazione](../../utility/impostazioni-postazione.md) Facile non
  chiede mai il numero dello scontrino: è il rimedio per una cassa che non
  risponde a quella richiesta.

### Il pagamento non riuscito

Nel **Pos Touchscreen**, se il pagamento non arriva al registratore — la porta o
la connessione non si apre, o l'invio non riesce — la finestra d'errore ha solo
**Riprova** e **Annulla**: il pulsante **Ignora**, che con le altre casse salta
il comando, con la 3i non c'è, perché registrerebbe la vendita con lo scontrino
ancora aperto sulla cassa, dove si accoderebbero le righe della vendita
successiva. **Annulla** non registra la vendita: guarda il display della cassa
e, se lo scontrino è rimasto aperto, chiudilo o annullalo dalla tastiera della
cassa prima di battere la vendita successiva. In **Vendita** la finestra aveva
già **Riprova** e **Annulla**.

### Una cassa che non risponde alla richiesta di stato

Le 3i più vecchie non rispondono alla richiesta di matricola e azzeramento.
Aprendo il **Pos Touchscreen** compare un avviso e si prosegue: fino alla
prossima apertura del POS gli scontrini si registrano senza numero di
azzeramento, e Facile non lo chiede più a ogni vendita. Se invece non si apre
nemmeno la porta o la connessione, il POS non si apre, come prima. In
**Vendita** la richiesta non riuscita fa scegliere, come prima, fra scaricare
il magazzino senza scontrino e interrompere.

### Buoni sconto e codice a barre dei resi

- Le righe del [buono sconto](../../vendite/buoni-sconto.md) non superano 38
  caratteri, il massimo che la 3i stampa su una riga: il formato 0 e il formato
  3 con `colonne` oltre 38 si stringono a 38. La virgola `,` e la barra `/`
  scritte nelle righe del file restano tali.
- Se la cassa non si raggiunge, o un comando del buono non parte, la stampa del
  buono si ferma al primo errore invece di aspettare la cassa riga per riga: il
  buono resta registrato e il motivo va nel file degli errori (vedi
  [Quando la cassa non stampa il buono](../../vendite/buoni-sconto.md#quando-la-cassa-non-stampa-il-buono)).
  Un comando rifiutato dalla cassa si vede solo sul display e sulla carta: la
  3i non dice a Facile come è andato.
- Il codice a barre dei resi, in fondo allo scontrino, ha 13 cifre (EAN-13 con
  la cifra di controllo). In **Vendita** esce subito dopo lo scontrino e prima
  del buono sconto, come nel **Pos Touchscreen**.

### Il log della comunicazione

Con il log della comunicazione attivo, per la voce `3I XON / XOFF LAN` il file
`socket_log.txt` della cartella `log` riporta, dopo ogni richiesta del numero
dello scontrino, una riga che comincia con `Risposta 89F:` con i byte arrivati dalla
cassa e il tempo di attesa in millisecondi, oppure *nessun byte* se la cassa
non ha risposto.

## Le casse DTR

Vale per le due voci `DTR XON / XOFF (19200,N,8,1,ECHO ON)` e `DTR XON / XOFF
LAN`. Per la voce in rete l'indirizzo e la porta del registratore stanno nel
file `dtr.ini` della cartella **cfg**; per la voce seriale lo stesso file
indica la velocità della porta.

La funzione **ECHO** della cassa, con cui il registratore rimanda indietro ogni
comando ricevuto, può essere accesa o spenta: Facile legge le risposte della
cassa in tutti e due i casi. Sulla voce seriale serve accesa, come dice il nome
della voce.

### Matricola, numero dello scontrino e azzeramento

- Facile chiede al registratore lo **stato della cassa**: da lì prende la
  matricola, il numero dello scontrino e il numero di azzeramento. La DTR
  risponde quando ha finito di stampare, per cui la richiesta si fa una volta
  sola, **subito dopo il pagamento**, a scontrino chiuso, sia nel **Pos
  Touchscreen** sia in **Vendita**. Prima del pagamento non si chiede niente:
  il pagamento non si ferma più per una richiesta non riuscita.
- La **matricola** letta dal registratore è quella che si registra negli
  [scontrini](../../vendite/scontrini.md), e quella che il documento di reso
  propone quando lo scontrino da rendere non la riporta. La matricola scritta
  nelle [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
  vale solo se la cassa non la dà. Se le due sono diverse, nel **Pos
  Touchscreen** compare l'avviso *La matricola impostata differisce dalla
  matricola letta sul registratore telematico!*, con la domanda se continuare:
  correggi la matricola nelle Impostazioni Postazione.
- Con la voce seriale fino a questa versione Facile non leggeva niente dalla
  cassa: gli scontrini si registravano con numero 0 e azzeramento 1. Ora li
  legge. Se all'apertura del POS o della vendita la cassa non risponde alla
  richiesta di stato, si prosegue come prima, senza numero e senza matricola
  letta, e Facile non la ripete a ogni scontrino.
- Con la voce in rete, se la cassa non risponde alla richiesta di stato
  all'apertura, il **Pos Touchscreen** non si apre e **Vendita** fa scegliere
  fra scaricare il magazzino senza scontrino e interrompere, come prima.
- Se dopo il pagamento la richiesta non riesce, lo scontrino si registra senza
  numero fiscale, e nel file degli errori `sqlerr.txt`, nella cartella `log`,
  resta una riga che comincia con *Cassa DTR: stato della cassa non letto*
  (vedi i [messaggi della vendita](../../vendite/vendita-al-banco.md#quando-la-cassa-o-la-bilancia-non-rispondono)).
  Per un reso o un annullo di quello scontrino il numero va indicato a mano.
- Con la casella **Disabilita Numerazione Scontrini** delle
  [Impostazioni Postazione](../../utility/impostazioni-postazione.md) gli
  scontrini si registrano senza numero fiscale; matricola e azzeramento si
  leggono lo stesso.

### Lo scontrino rimasto aperto

Dopo il pagamento Facile controlla sulla cassa che lo scontrino sia chiuso. Di
solito lo è, e non si manda altro. Se è rimasto aperto — per esempio un
pagamento che non copre il totale calcolato dalla cassa — Facile lo chiude
saldando il residuo in contanti e controlla di nuovo. Se resta aperto, o la
cassa non risponde più, compare un messaggio con **Riprova** e **Annulla**
(vedi [Quando si chiude lo scontrino](../../vendite/vendita-al-banco.md#quando-si-chiude-lo-scontrino)):
**Riprova** controlla e, se serve, chiude di nuovo; **Annulla** non registra la
vendita.

### La cassa in errore dopo il pagamento

Quando la DTR rifiuta un comando va in errore, mostra il codice sul display e
scarta tutti i comandi che arrivano dopo, finché non si preme **C**. Se
l'errore arriva durante la vendita, quindi, il pagamento non chiude niente e lo
scontrino non esce. Facile lo vede nello stato della cassa che legge dopo il
pagamento e non registra più la vendita come riuscita: compare il messaggio
*La cassa segnala l'errore …: lo scontrino non è stato emesso.*, con il codice
della cassa (vedi [Quando si chiude lo scontrino](../../vendite/vendita-al-banco.md#quando-si-chiude-lo-scontrino)).

- **Annulla** non registra la vendita. **Riprova** ripropone lo stesso
  messaggio: anche dopo il tasto **C** lo scontrino non c'è, e la cassa
  direbbe «chiuso» con il numero dello scontrino precedente.
- Premi **C** sulla cassa per togliere l'errore; la vendita successiva lo
  toglie comunque da sola. Poi correggi la vendita e ribattila.
- Se sulla cassa è rimasto aperto lo scontrino con le righe accettate prima
  dell'errore, il messaggio lo dice: annullalo dalla tastiera della cassa
  prima di ribattere la vendita.
- Con la **carta finita** il messaggio è *La cassa segnala la carta finita: lo
  scontrino potrebbe non essere stato emesso.*: cambia il rotolo e premi
  **Riprova**, che rilegge lo stato e registra la vendita se lo scontrino è
  uscito.

Fino a questa versione la vendita si registrava lo stesso, con numero fiscale
0, e restava solo una riga nel file degli errori.

Dopo **Annulla** il **Pos Touchscreen** non mostra più la vendita come chiusa,
con il resto e lo sfondo verde: il display dice **VENDITA NON REGISTRATA**, il
riquadro del totale **NON REGISTRATA** e lo sfondo delle righe diventa rosso.
Al tasto successivo la schermata si azzera, come dopo ogni vendita. Nel file
degli errori `sqlerr.txt` resta una riga come *Cassa DTR: la cassa segnala
l'errore 33 dopo il pagamento: scontrino non emesso*, sia dal Pos sia da
**Vendita**.

!!! note "Il reso deve corrispondere allo scontrino d'origine"

    Il reso dal **Pos Touchscreen** o da **Vendita** apre sulla cassa un
    documento di reso legato allo scontrino d'origine (azzeramento, numero,
    data, matricola), e la DTR controlla le righe su quello scontrino. Sulla
    cassa di prova un articolo reso a 0,10 € da uno scontrino in cui era
    venduto a 12,00 € è stato rifiutato con l'**errore 33**; la riga di un
    altro scontrino resa con lo stesso prezzo e la stessa descrizione è
    passata. Rendi gli articoli con il prezzo dello scontrino d'origine.

<!-- DA VERIFICARE: la DTR accetta il reso di una parte della quantita' venduta, o di una riga con la descrizione diversa ma lo stesso prezzo? Provato solo il prezzo diverso (rifiutato) e la riga identica (accettata). -->

### L'annullo di un documento commerciale

Dal **Pos Touchscreen**, **Funzioni ▸ Doc. Commerciale di Annullo** annulla
sulla cassa uno scontrino già emesso, indicato con azzeramento, numero e data.
Con la DTR Facile, dopo aver mandato l'annullo, rilegge lo stato della cassa,
come dopo il pagamento:

- se la cassa lo ha eseguito, l'annullo si registra con il numero del
  documento di annullo letto dalla cassa (prima restava il numero dell'ultima
  vendita);
- se la cassa lo ha rifiutato — sulla cassa di prova l'annullo di uno
  scontrino che non esiste ha dato l'**errore 52** — compare *Errore !* con
  *La cassa segnala l'errore …: il documento non è stato annullato.*, con
  **Riprova** e **Annulla**. **Annulla** non registra l'annullo, e il display
  dice **NON REGISTRATO**: controlla i dati e ripeti l'annullo. **Riprova**
  toglie l'errore alla cassa e rimanda lo stesso annullo;
- con la **carta finita**, cambia il rotolo e premi **Riprova**: Facile
  rilegge lo stato senza rimandare l'annullo, che sarebbe un secondo annullo;
- se sulla cassa è rimasto aperto uno scontrino, il messaggio lo dice:
  annullalo dalla tastiera della cassa, poi **Riprova**.

Fino a questa versione Facile non controllava la risposta della cassa, e un
annullo rifiutato si registrava lo stesso. I messaggi sono nella tabella
[Quando si annulla un documento commerciale](../../vendite/vendita-al-banco.md#quando-si-annulla-un-documento-commerciale).

### Il pagamento non riuscito

Nel **Pos Touchscreen**, come con le [casse 3i](#il-pagamento-non-riuscito), se
il pagamento non arriva al registratore la finestra d'errore ha solo
**Riprova** e **Annulla**: **Ignora** registrerebbe la vendita con lo
scontrino ancora aperto sulla cassa. **Annulla** non registra la vendita:
guarda il display della cassa e, se lo scontrino è rimasto aperto, chiudilo o
annullalo dalla tastiera della cassa prima di battere la vendita successiva.

### Testi, buoni pasto, codice fiscale, versamenti

- Nelle descrizioni degli articoli le lettere accentate escono senza accento
  (`CAFFÈ` esce `CAFFE`), invece di diventare spazi.
- La parola `TOTALE`, che la DTR non accetta nelle righe di testo dello
  scontrino e che nel documento gestionale fa sparire la riga, diventa `TOT.`,
  anche dentro una parola (`SUBTOTALE` → `SUBTOT.`). Vale per le descrizioni,
  per le righe dei buoni sconto e per le altre righe di testo.
- Con la voce seriale i **buoni pasto** si pagavano moltiplicati per il loro
  numero: due ticket da 7 euro valevano 28 euro. Ora valgono 14.
- Il **codice fiscale** o la **partita IVA** del cliente arrivano alla cassa
  come dato del cliente, che la cassa stampa in fondo allo scontrino: la
  partita IVA con le sue 11 cifre, il codice fiscale con i suoi 16 caratteri.
  Con la voce seriale prima usciva solo una riga di testo, e con la voce in
  rete la partita IVA arrivava allungata con degli spazi, e la cassa non la
  riconosceva.
- Con la voce in rete il **versamento** e il **prelievo** di cassa si chiudono
  sul registratore come con la voce seriale. Prima il documento restava aperto
  in pagamento sulla cassa.

### Buoni sconto

- Con la voce in rete, se la cassa non si raggiunge o un comando del
  [buono sconto](../../vendite/buoni-sconto.md) non parte, la stampa del buono
  si ferma al primo errore invece di aspettare la cassa riga per riga: il buono
  resta registrato e il motivo va nel file degli errori (vedi
  [Quando la cassa non stampa il buono](../../vendite/buoni-sconto.md#quando-la-cassa-non-stampa-il-buono)).
  Un comando rifiutato dalla cassa si vede solo sul display e sulla carta: la
  DTR non dice a Facile come è andato.
- Con la voce seriale la stampa del buono prosegue come prima.

<!-- DA VERIFICARE: sotto il codice a barre del buono Facile stampa anche il codice in chiaro; se la DTR stampa già le cifre sotto le barre, il codice esce due volte. Guardare la carta del buono sulla DTR di prova. -->

### Il log della comunicazione

Con il log della comunicazione attivo, per la voce `DTR XON / XOFF LAN` il file
`socket_log.txt` della cartella `log` riporta, dopo ogni richiesta di stato,
una riga che comincia con `Risposta 2X:` con i byte arrivati dalla cassa e il
tempo di attesa in millisecondi, oppure *nessun byte* se la cassa non ha
risposto. Le righe sopra, `SendString: 2X` e una `ReceiveBytes:` per ogni
pezzo arrivato, ora le scrive Facile: prima un pezzo ricevuto poteva comparire
come `SendString:`, come se l'avesse mandato Facile.

## Vedi anche

- [Custom](custom.md)
- [Micrelec](micrelec.md)
- [RCH](rch.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
