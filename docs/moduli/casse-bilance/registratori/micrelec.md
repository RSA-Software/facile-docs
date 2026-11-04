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
4. Copia nella cartella `cfg` di Facile il
   [file di esempio](../../../assets/modelli/micrelec_g100.ini) e scrivi in
   `ip` l'indirizzo del registratore.

### Il file micrelec_g100.ini

| Sezione | Chiave | Predefinito | Descrizione |
|---|---|---|---|
| `[OPTIONS]` | `ip` | — | Indirizzo IP del registratore, senza la porta. |
| `[OPTIONS]` | `porta` | 80 | Porta del registratore. Lasciala a 80: è quella su cui il registratore accetta i comandi da Facile. La 9101 è un'altra cosa e non funziona. |
| `[OPTIONS]` | `timeout_ms` | 15000 | Attesa massima della risposta a un comando, in millisecondi. |
| `[OPTIONS]` | `timeout_chiusura_ms` | 120000 | Attesa massima per le letture e la chiusura giornaliera, che stampano a lungo. |
| `[OPTIONS]` | `display_colonne` | 20 | Caratteri di una riga del display, per il display cliente `MICRELEC G100`. |

### Lo scontrino

Mentre batti lo scontrino Facile manda le righe alla cassa una alla volta.
Prima della prima riga controlla che sulla cassa non ci sia già un documento
aperto, per esempio uno scontrino iniziato dalla tastiera del registratore: le
righe nuove gli si sommerebbero, e Facile si ferma con un avviso.

Se interrompi uno scontrino a metà — scegliendo di annullare o di interrompere
quando una riga o un pagamento danno errore — le righe già mandate sono sulla
cassa, in un documento ancora aperto. Facile lo annulla sulla cassa e te lo dice. Un documento che non
ha iniziato Facile non viene mai annullato.

Nelle descrizioni degli articoli le lettere accentate diventano lettere
semplici (`è` diventa `e`) e il simbolo dell'euro diventa `EUR`. Le righe di
vendita non riportano l'aliquota IVA: il registratore la prende dal reparto,
che deve quindi essere programmato con l'aliquota giusta.

### La matricola

Con un firmware G100.127 o successivo Facile legge la matricola dal
registratore e la salva sullo scontrino. La **Matricola** delle impostazioni
va compilata comunque: nei [resi](../../vendite/vendita-al-banco.md#registrare-un-reso)
e negli annulli Facile la confronta con quella dello scontrino originale, per
sapere se è stato emesso da questa stessa cassa.

### Cosa non si può fare

- **La fattura da cassa.** Il registratore G100 non la emette con questo
  collegamento: la fattura si fa da Facile.
- **La parola TOTALE nelle descrizioni.** Il registratore la rifiuta, perché la
  usa per il totale del documento: un articolo con TOTALE nella descrizione dà
  errore sulla sua riga.
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

## Diagnostica

| Cosa | Dove |
|---|---|
| I comandi e le risposte di `MICRELEC G100` | `log\micrelec_g100_log.txt`, con il log seriale attivo nelle impostazioni |
| I comandi di uno scontrino `MICRELEC` non consegnato | Nella cartella dei file, un file `SCO<postazione>-<progressivo>.cmd` |

## Controlli e messaggi

Con `MICRELEC G100` il motivo di un errore compare dentro la finestra d'errore
della vendita, sotto l'intestazione — per esempio *Errore !*, *Cassa
OFF-LINE !* o *Comando non accettato dalla Cassa !* — insieme ai pulsanti per
riprovare o annullare.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impossibile inizializzare il driver di comunicazione con la cassa !* | All'apertura della vendita, con `MICRELEC G100`: in `micrelec_g100.ini` manca l'indirizzo del registratore, o il file non c'è. | Copia il file di esempio nella cartella `cfg` e scrivi l'indirizzo in `ip`. |
| *Cassa non raggiungibile all'indirizzo …* | Il registratore non risponde all'indirizzo di `micrelec_g100.ini`: è spento, scollegato dalla rete o l'indirizzo è sbagliato. Il comando non è partito. | Controlla il registratore e il cavo di rete, poi riprova. |
| *La cassa non ha risposto: controllare sul display se l'operazione e' stata registrata prima di riprovare* | Il comando è partito ma la risposta non è arrivata: non si sa se il registratore l'ha eseguito. | Guarda il display della cassa. Se la riga è stata registrata, non riprovare: annulla e rifai lo scontrino oppure prosegui. Se non c'è, riprova. |
| *Errore 0x… (…) della cassa: …* | Il registratore ha rifiutato il comando; dopo i due punti c'è il motivo, per esempio *carta esaurita* o *il reparto non esiste*, e fra parentesi lo stato della cassa. | Risolvi la causa e riprova. |
| *Sulla cassa c'e' un documento aperto. Chiuderlo o annullarlo dalla cassa, poi riprovare.* | Prima della prima riga, sul registratore c'è già un documento aperto, per esempio iniziato dalla tastiera. | Chiudi o annulla il documento dalla cassa, poi riprova. |
| *Lo scontrino interrotto e' stato annullato sulla cassa.* | Hai interrotto uno scontrino a metà: le righe già mandate sono state annullate sul registratore. | Nessuna: la vendita successiva parte pulita. |
| *Sulla cassa potrebbe essere rimasto aperto lo scontrino interrotto. Controllare il display e, se serve, annullarlo dalla cassa prima della vendita successiva.* | Hai interrotto uno scontrino, ma Facile non è riuscito ad annullarlo sul registratore. | Controlla il display e annulla il documento dalla cassa. |
| *Attenzione! Il driver della cassa ha segnalato un errore: Il documento e' rimasto aperto sulla cassa. Controllare la stampa prima di proseguire.* | Alla fine dello scontrino il documento è ancora aperto sul registratore, per esempio perché un pagamento non è stato accettato. | Controlla la stampa e il display; chiudi o annulla il documento dalla cassa. |

## Vedi anche

- [Registratori telematici](index.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
