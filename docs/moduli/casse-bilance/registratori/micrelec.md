---
title: Registratori telematici Micrelec
description: Come si collegano a Facile i registratori telematici Axon Micrelec, attraverso il programma di Micrelec oppure, per la serie G100, direttamente in rete.
modulo: Casse e Bilance
---

# Registratori telematici Micrelec

Facile pilota i registratori telematici Axon Micrelec in due modi, che
corrispondono a due voci dell'elenco **Stampante Fiscale**: attraverso il
programma di Micrelec, come è sempre stato, oppure — per i registratori della
serie **G100** con il firmware recente — direttamente in rete, senza programmi
intermedi.

!!! info "In sintesi"

    - **Dove si sceglie:** Menu ▸ Utility ▸ [Impostazioni Postazione](../../utility/impostazioni-postazione.md), campo **Stampante Fiscale**
    - **Voci:** `MICRELEC`, `MICRELEC G100`
    - **Configurazione:** per `MICRELEC G100` il file [micrelec_g100.ini](../../../assets/modelli/micrelec_g100.ini) nella cartella `cfg` di Facile

---

## Quale collegamento scegliere

| Voce in **Stampante Fiscale** | Come funziona | Collegamento |
|---|---|---|
| `MICRELEC` | Facile scrive i comandi dello scontrino in un file; il programma di Micrelec installato sulla postazione lo consegna al registratore. | Quello configurato nel programma di Micrelec |
| `MICRELEC G100` | Facile manda ogni comando direttamente al registratore, mentre batte lo scontrino, e legge la risposta. | Rete |

- Con `MICRELEC` lo scontrino parte solo alla chiusura e Facile non sa se è
  stato stampato: un comando rifiutato si vede sul display e sulla stampa della
  cassa.
- Con `MICRELEC G100` non serve il programma di Micrelec. Facile riceve
  l'esito di ogni riga: un errore — carta finita, reparto inesistente, cassa
  spenta — compare subito sulla riga che l'ha causato, e puoi riprovare dopo
  averlo risolto. Legge anche dalla cassa il numero dello scontrino, l'ultimo
  azzeramento e la matricola.

I comandi sono gli stessi nei due casi: una cassa che funziona con `MICRELEC`
funziona con `MICRELEC G100` senza riprogrammarla, se il firmware è
aggiornato.

## Collegamento diretto: MICRELEC G100

### Che cosa serve

- Un registratore della serie G100 collegato alla rete della postazione, con
  un firmware G100 recente. La lettura della matricola dalla cassa c'è dalla
  versione **G100.127**: con un firmware precedente il resto funziona, e la
  matricola resta quella scritta nelle impostazioni.
- L'indirizzo IP del registratore, che si legge dal menu del registratore.

### Impostare la postazione

1. In [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
   scegli `MICRELEC G100` in **Stampante Fiscale**.
2. In **Porta** scrivi un numero diverso da zero, per esempio `1`. Il
   collegamento è in rete e la porta non si usa, ma con zero la vendita non
   parte.
3. Compila la **Matricola** del registratore, di 11 caratteri, come è stampata
   sugli scontrini.
4. Nella cartella `cfg` di Facile metti il file `micrelec_g100.ini` — se non
   c'è, [scarica il modello](#il-file-micrelec_g100ini) — e scrivi in `ip`
   l'indirizzo del registratore.

### Il file micrelec_g100.ini

Il modello è già commentato: basta salvarlo nella cartella `cfg` di Facile e
cambiare l'indirizzo in `ip`. Le altre chiavi vanno bene così come sono.

[:material-download: Scarica micrelec_g100.ini](../../../assets/modelli/micrelec_g100.ini){ .md-button download="micrelec_g100.ini" }

| Sezione | Chiave | Predefinito | Descrizione |
|---|---|---|---|
| `[OPTIONS]` | `ip` | — | Indirizzo IP del registratore, senza la porta. |
| `[OPTIONS]` | `porta` | 80 | Porta del registratore. Lasciala a 80: è quella su cui il registratore accetta i comandi da Facile. La 9101 è un'altra cosa e non funziona. |
| `[OPTIONS]` | `timeout_ms` | 15000 | Attesa massima della risposta a un comando, in millisecondi. |
| `[OPTIONS]` | `timeout_chiusura_ms` | 120000 | Attesa massima per le letture e la chiusura giornaliera, che stampano a lungo. |
| `[OPTIONS]` | `display_colonne` | 20 | Caratteri di una riga del display, per il display cliente `MICRELEC G100`. |

Il contenuto del modello:

```ini
--8<-- "docs/assets/modelli/micrelec_g100.ini"
```

### Lo scontrino

Mentre batti lo scontrino Facile manda le righe alla cassa una alla volta.
Prima della prima riga controlla che sulla cassa non ci sia già un documento
aperto, per esempio uno scontrino iniziato dalla tastiera del registratore: le
righe nuove gli si sommerebbero, e Facile si ferma con un avviso.

Se interrompi uno scontrino a metà — scegliendo di annullare o di interrompere
quando una riga o un pagamento danno errore — le righe già mandate sono sulla
cassa, in un documento ancora aperto. Facile lo annulla sulla cassa e te lo
dice; allo stesso modo chiude un preconto rimasto a metà. Un documento che non
ha iniziato Facile non viene mai annullato. Se invece la cassa aveva già
chiuso lo scontrino — per esempio quando l'ultimo pagamento è rimasto senza
risposta — lo scontrino è emesso ma la vendita non è registrata in Facile:
Facile ti avvisa con il numero dello scontrino, da controllare sulla stampa.

Dopo il pagamento Facile controlla che lo scontrino sia davvero chiuso sulla
cassa. Di norma lo è e non succede nient'altro. Se invece i pagamenti non
coprono il totale del registratore — per esempio per un centesimo di
arrotondamento — lo scontrino resterebbe aperto: Facile salda il residuo **in
contanti** e lo chiude. Sullo scontrino il residuo si somma al contante già
dato oppure, se l'ultimo pagamento era elettronico, esce su una riga
*PAGAMENTO CONTANTE* a parte. Se la cassa non chiude lo scontrino, o non
risponde, compare un avviso con **Riprova** e **Annulla** (vedi
[Controlli e messaggi](#controlli-e-messaggi)): con **Annulla** la vendita non
viene registrata, il buono sconto non esce e Facile annulla sulla cassa lo
scontrino rimasto aperto, come ogni scontrino interrotto.

Il codice fiscale, la partita IVA e il codice lotteria del cliente sono
alternativi: il registratore ne accetta uno solo per scontrino.

Nelle descrizioni degli articoli le lettere accentate diventano lettere
semplici (`è` diventa `e`), il simbolo dell'euro diventa `EUR`, le virgolette
e i trattini tipografici diventano quelli normali e il simbolo dei gradi
diventa `o`. La parola TOTALE, che il registratore tiene per il totale del
documento, diventa `TOT.`, e la barra `/` diventa uno spazio.

Una maggiorazione a valore sulla riga esce sullo scontrino come
`MAGGIORAZIO`, come le altre maggiorazioni.

Ogni riga di vendita porta il reparto e l'aliquota IVA dell'articolo, e il
registratore controlla che il reparto abbia proprio quell'aliquota: se non
coincidono la riga viene rifiutata con *Errore 0x17 (23) della cassa: aliquota
IVA errata*. Il **Reparto Cassa** di Facile — nelle
[aliquote IVA](../../contabilita/aliquote-iva.md) o nei
[reparti](../../magazzino/reparti.md) di magazzino, secondo come è impostata la
ditta — deve quindi indicare un reparto del registratore programmato con la
stessa aliquota.

### Resi e annulli

Il reso apre sul registratore il documento di reso che richiama lo scontrino
originale, e le righe da rendere seguono come normali vendite. L'annullo, invece,
il registratore lo emette da solo solo se lo scontrino originale è nel suo
giornale elettronico: se è di un'altra cassa, o non c'è più, Facile chiude il
documento rimasto aperto e ti avvisa, e l'annullo va fatto dalla tastiera della
cassa.

### Il buono sconto

Il [buono sconto](../../vendite/buoni-sconto.md) esce dopo lo scontrino, come
documento a parte. Nelle sue righe le lettere accentate escono senza accento:
`CAFFÈ` diventa `CAFFE`.

Se la cassa rifiuta un comando mentre stampa il buono — per esempio per la
carta finita — la stampa **si ferma al primo errore** e il buono esce
incompleto. Non compare nessuna finestra: il buono resta registrato in
archivio, gli eventuali buoni successivi dello stesso scontrino non si emettono
e il motivo, con il testo dell'errore della cassa, va nel file degli errori
(vedi [Quando la cassa non stampa il buono](../../vendite/buoni-sconto.md#quando-la-cassa-non-stampa-il-buono)).

### La matricola

Facile legge la matricola dal registratore — dall'ultimo scontrino, oppure,
subito dopo la chiusura giornaliera, dallo stato della cassa — e la salva sullo
scontrino. La **Matricola** delle impostazioni
va compilata comunque: nei [resi](../../vendite/vendita-al-banco.md#registrare-un-reso)
e negli annulli Facile la confronta con quella dello scontrino originale, per
sapere se è stato emesso da questa stessa cassa.

### Cosa non si può fare

- **La fattura da cassa.** Il registratore G100 non la emette con questo
  collegamento: la fattura si fa da Facile.
- **Versamenti e prelievi di cassa**, come con `MICRELEC`.

## Le forme di pagamento

Ogni pagamento di Facile finisce su una forma di pagamento del registratore,
indicata con un numero. I numeri sono gli stessi con le due voci:

| Pagamento in Facile | Forma | Pagamento in Facile | Forma |
|---|---|---|---|
| Contanti | 1 | Sconto a pagare | 11 |
| Buoni pasto | 3 | Buono multiuso | 12 |
| Bancomat | 4 | Buoni celiachia | 13 |
| Carta di credito | 5 | Non riscosso servizi | 14 |
| Assegni | 6 | Non riscosso SSN | 15 |
| | | Non riscosso fatture | 16 |
| | | Non riscosso altro | 17 |

!!! warning "Controlla la tabella dei pagamenti della cassa"

    Le forme da 11 a 17 devono essere programmate sul registratore con il
    significato della tabella. Sulla programmazione di fabbrica del G100 non
    lo sono tutte: per esempio la forma 17 è il DCR a SSN. Un pagamento sulla
    forma sbagliata non dà errore e finisce sul totale sbagliato, che si scopre
    in chiusura. Controlla la programmazione della cassa installata.

## Il display cliente

Il display attaccato al registratore si pilota attraverso il registratore. In
[Impostazioni Postazione](../../utility/impostazioni-postazione.md) scegli in
**Customer Display - 1** il tipo che corrisponde alla stampante fiscale, con la
stessa **Porta**:

| Stampante Fiscale | Customer Display |
|---|---|
| `MICRELEC` | `MICRELEC` |
| `MICRELEC G100` | `MICRELEC G100` |

La parola TOTALE viene abbreviata in TOT.

## Collegamento con il programma di Micrelec: MICRELEC

Con la voce `MICRELEC` Facile scrive ogni scontrino in un file `.cmd`, per
impostazione nella cartella `out` di Facile; alla chiusura lo rinomina in `.TXT` e il programma di
Micrelec, installato sulla postazione, lo consegna al registratore. Le
risposte che Facile legge — numero dello scontrino e azzeramento — arrivano
dalla cartella di log del programma di Micrelec, per impostazione
`C:\axonFPiD_Pro_v7\Cartella_LOG`.

Sulla carta lo scontrino esce come con `MICRELEC G100`:

- nelle descrizioni degli articoli e nelle righe di testo la parola TOTALE
  diventa `TOT.`, la barra `/` diventa uno spazio e le lettere accentate
  escono senza accento, come descritto in [Lo scontrino](#lo-scontrino);
- il codice fiscale o la partita IVA del cliente arrivano al registratore come
  dato del documento, non più come riga di commento stampata;
- la maggiorazione a valore sulla riga esce come `MAGGIORAZIO`;
- il codice a barre del [buono sconto](../../vendite/buoni-sconto.md) esce in
  formato EAN-13, e le lettere accentate delle righe del buono escono senza
  accento.

Facile non vede l'esito dei comandi: un errore durante la stampa del buono non
ferma la stampa e non finisce nel file degli errori, ma si vede solo sul
display e sulla carta.

## Diagnostica

| Cosa | Dove |
|---|---|
| I comandi e le risposte di `MICRELEC G100` | `log\micrelec_g100_log.txt`, con il log seriale attivo nelle impostazioni |
| I comandi di uno scontrino `MICRELEC` non consegnato | Nella cartella dei file, un file `SCO<postazione>-<progressivo>.cmd` |

## Controlli e messaggi

Con `MICRELEC G100` il motivo di un errore compare dentro la finestra d'errore
della vendita, sotto l'intestazione — per esempio *Errore !*, *Cassa
OFF-LINE !* o *Comando non accettato dalla Cassa !* — insieme ai pulsanti per
riprovare o annullare. Il pulsante **Ignora**, che con le altre casse salta il
comando e prosegue, con `MICRELEC G100` non c'è: lo scontrino perderebbe una
riga o un pagamento senza avvisare. **Annulla** interrompe lo scontrino e lo
annulla sulla cassa; sugli errori di comunicazione è il pulsante proposto,
perché riprovare un comando rimasto senza risposta potrebbe registrarlo due
volte.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impossibile inizializzare il driver di comunicazione con la cassa !* | All'apertura della vendita, con `MICRELEC G100`: in `micrelec_g100.ini` manca l'indirizzo del registratore, o il file non c'è. | Copia il file di esempio nella cartella `cfg` e scrivi l'indirizzo in `ip`. |
| *Cassa non raggiungibile all'indirizzo …* | Il registratore non risponde all'indirizzo di `micrelec_g100.ini`: è spento, scollegato dalla rete o l'indirizzo è sbagliato. Il comando non è partito. | Controlla il registratore e il cavo di rete, poi riprova. |
| *La cassa non ha risposto: controllare sul display se l'operazione e' stata registrata prima di riprovare* | Il comando è partito ma la risposta non è arrivata, o è arrivata incomprensibile: non si sa se il registratore l'ha eseguito. | Guarda il display della cassa. Se la riga è stata registrata, non riprovare: annulla e rifai lo scontrino oppure prosegui. Se non c'è, riprova. |
| *Errore 0x… (…) della cassa: …* | Il registratore ha rifiutato il comando; dopo i due punti c'è il motivo, per esempio *carta esaurita* o *il reparto non esiste*, e fra parentesi lo stato della cassa. | Risolvi la causa e riprova. |
| *Errore 0x17 (23) della cassa: aliquota IVA errata* | Il reparto del registratore su cui va la riga ha un'aliquota diversa da quella dell'articolo. | Correggi il **Reparto Cassa** dell'aliquota o del reparto in Facile, oppure la programmazione del reparto sul registratore. |
| *Sulla cassa c'e' un documento aperto. Chiuderlo o annullarlo dalla cassa, poi riprovare.* | Prima della prima riga, sul registratore c'è già un documento aperto, per esempio iniziato dalla tastiera. | Chiudi o annulla il documento dalla cassa, poi riprova. |
| *La cassa non ha risposto: controllare che sia accesa e collegata, poi riprovare* | Facile non ha potuto leggere dal registratore lo stato, il numero dello scontrino o l'azzeramento. | Controlla che la cassa sia accesa e in rete, poi riprova. |
| *Lo scontrino e' rimasto aperto sulla cassa: la chiusura non e' riuscita (…).<br>Controllare la cassa e riprovare.* | Dopo il pagamento lo scontrino era ancora aperto sul registratore, Facile ha provato a chiuderlo saldando il residuo in contanti, e la cassa non l'ha chiuso. Fra parentesi c'è l'errore della cassa, per esempio *Errore 0x4E (78) della cassa: inserire l'importo del pagamento*; se la cassa non ha rifiutato il comando, le parentesi non ci sono. | Guarda il display e la carta, risolvi la causa e premi **Riprova**. **Annulla** non registra la vendita, non emette il buono sconto e annulla lo scontrino sulla cassa. |
| *Chiusura dello scontrino non verificata: la cassa non risponde.<br>Controllare la cassa e riprovare.* | Dopo la chiusura del residuo Facile non è riuscito a rileggere dal registratore se lo scontrino è chiuso. Se anche il comando di chiusura è stato rifiutato, prima del punto c'è l'errore della cassa fra parentesi. | Controlla che la cassa sia accesa e in rete, poi premi **Riprova**: Facile rilegge lo stato e, se lo scontrino è chiuso, prosegue senza mandare altro. **Annulla** non registra la vendita. |
| *Lo scontrino interrotto e' stato annullato sulla cassa.* | Hai interrotto uno scontrino o un preconto a metà: le righe già mandate sono state annullate sul registratore. | Nessuna: la vendita successiva parte pulita. |
| *Sulla cassa potrebbe essere rimasto aperto lo scontrino interrotto. Controllare il display e, se serve, annullarlo dalla cassa prima della vendita successiva.* | Hai interrotto uno scontrino, ma Facile non è riuscito ad annullarlo sul registratore. | Controlla il display e annulla il documento dalla cassa. |
| *La cassa ha emesso lo scontrino n. …, ma la vendita non e' stata registrata in Facile. Controllare la stampa.* | Hai interrotto la vendita dopo che il registratore aveva già chiuso lo scontrino, per esempio perché l'ultimo pagamento è rimasto senza risposta. | Controlla lo scontrino stampato. La vendita è ancora sul banco: se lo scontrino è giusto, scarica il magazzino con **F2 - Scarica**, che non emette un secondo scontrino (vedi [Vendita al banco](../../vendite/vendita-al-banco.md#pulsanti-e-comandi)); altrimenti annulla lo scontrino e rifai la vendita. |
| *La cassa non ha emesso l'annullo: lo scontrino originale non e' nel suo giornale elettronico o e' di un'altra cassa. Fare l'annullo dalla tastiera della cassa.* | Il registratore emette l'annullo da solo solo per gli scontrini che ha nel suo giornale elettronico. | Fai l'annullo dalla tastiera della cassa. |
| *Risposta della cassa incompleta* | Una lettura dal registratore — numero dello scontrino, azzeramento, stato — è arrivata troncata. | Riprova; se si ripete, controlla la rete e il log dei comandi. |
| *Attenzione! Il driver della cassa ha segnalato un errore: Il documento e' rimasto aperto sulla cassa. Controllare la stampa prima di proseguire.* | Alla fine dello scontrino il documento è ancora aperto sul registratore, per esempio perché un pagamento non è stato accettato. | Controlla la stampa e il display; chiudi o annulla il documento dalla cassa. |

## Vedi anche

- [Registratori telematici](index.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
