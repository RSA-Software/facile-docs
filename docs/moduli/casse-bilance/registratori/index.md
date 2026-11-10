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
    - **Pagine dei modelli:** [Micrelec](micrelec.md), [RCH](rch.md); le casse 3i sono [qui sotto](#le-casse-3i)

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
| `CUSTOM XON / XOFF (19200,N,8,1)` | Seriale |
| `CUSTOM PROTOCOL` | — |
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

<!-- DA VERIFICARE: il manuale della 3i non dice se a scontrino aperto la cassa dia il numero dello scontrino in corso o dell'ultimo chiuso; Facile lo considera quello in corso. Confermare sulla 3i di prova confrontando il numero in Scontrini con la carta, poi togliere questa nota. -->

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

## Vedi anche

- [Micrelec](micrelec.md)
- [RCH](rch.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
