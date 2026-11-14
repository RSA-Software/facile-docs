---
title: Registratori telematici Custom
description: Come si collegano a Facile i registratori telematici Custom, con il web service XML dei modelli di terza generazione oppure con il protocollo XON/XOFF e il protocollo Custom.
modulo: Casse e Bilance
---

# Registratori telematici Custom

Facile pilota i registratori telematici Custom in tre modi, che corrispondono a
tre voci dell'elenco **Stampante Fiscale**. Questa pagina spiega quale
scegliere e descrive il collegamento con il **web service**, che è quello
nuovo.

!!! info "In sintesi"

    - **Dove si sceglie:** Menu ▸ Utility ▸ [Impostazioni Postazione](../../utility/impostazioni-postazione.md), campo **Stampante Fiscale**
    - **Voci:** `CUSTOM WEB SERVICE` (versione beta), `CUSTOM XON / XOFF (19200,N,8,1)`, `CUSTOM PROTOCOL`
    - **Configurazione del web service:** il file [Custom_WebService.ini](../../../assets/modelli/Custom_WebService.ini) nella cartella `cfg` di Facile

!!! warning "CUSTOM WEB SERVICE è in versione beta"

    Il collegamento `CUSTOM WEB SERVICE` è in **versione beta**: è stato
    scritto sul manuale del costruttore (*Web services – Commands manual for
    3rd generation fiscal devices*, rev. 2.00) e non è ancora stato provato su
    un registratore Custom. Prima di usarlo da un cliente va collaudato sulla
    macchina: uno scontrino, un reso, un annullo e una chiusura giornaliera,
    controllando che numero e azzeramento registrati da Facile siano quelli
    stampati. Le altre due voci non sono in beta.

---

## File di configurazione da scaricare

Il file del web service, con le impostazioni predefinite e i commenti che
spiegano ogni voce. Scaricalo, copialo nella cartella `cfg` di Facile e
correggi l'indirizzo e le forme di pagamento del registratore installato.

| File | Per la voce | Impostazioni predefinite |
|---|---|---|
| [Custom_WebService.ini](../../../assets/modelli/Custom_WebService.ini) | `CUSTOM WEB SERVICE` | porta 80, forme di pagamento di fabbrica |

Le voci `CUSTOM XON / XOFF (19200,N,8,1)` e `CUSTOM PROTOCOL` non hanno un
file di configurazione: si impostano dalle Impostazioni Postazione.

## Quale collegamento scegliere

| Voce in **Stampante Fiscale** | Come funziona | Collegamento |
|---|---|---|
| `CUSTOM WEB SERVICE` (beta) | Facile manda al registratore il documento intero e il registratore risponde. | Ethernet |
| `CUSTOM XON / XOFF (19200,N,8,1)` | Facile manda i comandi e il registratore non risponde. | Seriale |
| `CUSTOM PROTOCOL` | Facile manda un comando per volta e il registratore risponde a ciascuno. | — |

Il **web service** è il collegamento da preferire dove il modello lo permette:
non serve installare niente, e il registratore risponde. Facile sa se lo
scontrino è uscito, mostra l'errore della cassa con il suo codice e la sua
descrizione, annulla da solo un documento rimasto aperto, e registra su ogni
scontrino numero, azzeramento e matricola letti dalla macchina.

### Quali modelli

Il web service esiste solo sui registratori Custom di **terza generazione**:

| Famiglia | Modelli |
|---|---|
| K3 | K3-F RT, K3-N RT |
| Q3X | Q3X-F RT, Q3X-N RT |
| P3 | P3-N RT |
| JSmart | JSMART RT, JSMART-N RT |
| Big Plus | BIG PLUS RT, BIG PLUS-N RT |
| KubeX | KUBEX-F RT, KUBEX-N RT |
| VKP | VKP80III-F RT |
| Fusion ed Edge | FUSION-K, FUSION-N, EDGE-N, EDGE-N+ |

I registratori di seconda generazione (BIG II RT, KUBE II-F ETH RT, MAX-COM RT)
e di quarta (BIG 3 RT, BIG 3 TOUCH RT) non hanno il web service: per quelli
restano le altre due voci.

---

## Preparare il registratore

1. Collega il registratore alla rete e assegnagli un indirizzo fisso.
2. Fai impostare al tecnico il collegamento con il computer sul **protocollo
   XML** del web service. Con un'altra impostazione il registratore rifiuta i
   documenti con l'errore **219** (protocollo errato) o **220** (modalità
   errata), e Facile lo mostra.
3. Copia [Custom_WebService.ini](../../../assets/modelli/Custom_WebService.ini)
   nella cartella `cfg` di Facile e scrivi l'indirizzo del registratore.
4. Nelle [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
   scegli `CUSTOM WEB SERVICE` in **Stampante Fiscale** e lascia la **Porta**
   della cassa su un valore diverso da zero, per esempio `LAN`: non viene
   usata, ma con zero la vendita non parte.

### La matricola

All'apertura del [Pos Touchscreen](../../vendite/vendita-al-banco.md) Facile
chiede la matricola al registratore. Se è diversa da quella delle Impostazioni
Postazione, mostra le due matricole e chiede se aggiornare quella impostata:
con **Sì** la salva e prosegue, con **No** il Pos non si apre.

La matricola serve anche per l'accesso al web service: Facile la presenta al
registratore come nome utente e password. Se il registratore rifiuta
l'accesso, il messaggio dice di controllare la matricola nelle Impostazioni.

---

## Web service (versione beta) { #web-service }

### Come funziona

Facile compone lo scontrino mentre vendi e lo manda al registratore tutto
insieme, quando lo chiudi. Prima di mandarlo chiede al registratore se è
libero: se la carta è finita, il coperchio è aperto o c'è già un documento
aperto, lo dice e non stampa niente.

Dalla risposta Facile prende il numero dello scontrino e il numero di
azzeramento, e li registra sulla vendita insieme alla matricola.

Se il registratore rifiuta un comando, il documento resta aperto sulla
macchina: Facile lo annulla da solo e mostra l'errore con codice e
descrizione. Se la risposta non arriva, Facile rilegge lo stato e i contatori
del registratore per capire se lo scontrino è uscito; quando non riesce a
stabilirlo lo dice, e prima di riemetterlo va controllato il giornale della
cassa.

!!! note "Scontrino emesso senza numero"

    I registratori con un programma interno meno recente possono non
    comunicare il numero dello scontrino. In quel caso lo scontrino esce
    regolarmente, Facile avvisa che il numero *va letto sullo scontrino* e
    registra la vendita senza numero.

### Il file Custom_WebService.ini

| Sezione | Voce | Significato | Valore predefinito |
|---|---|---|---|
| `[OPTIONS]` | `ip` | Indirizzo del registratore | nessuno: va scritto |
| `[OPTIONS]` | `port` | Porta del web service | `80` |
| `[OPTIONS]` | `COL_PRIMA_RIGA` | Caratteri della descrizione sulla riga di vendita, da 1 a 44 | `22` |
| `[OPTIONS]` | `COL_RIGHE_AGG` | Caratteri delle righe aggiuntive con il resto della descrizione, da 1 a 42 | `32` |
| `[PAGAMENTI]` | una voce per forma di pagamento | Il numero del pagamento nella tabella del registratore | vedi sotto |

### Le forme di pagamento

Ogni forma di pagamento di Facile va sul numero che ha nella tabella dei
pagamenti del registratore. I valori predefiniti sono quelli di fabbrica:

| Voce del file | Forma di pagamento | Valore predefinito |
|---|---|---|
| `contante` | Contanti | `1` |
| `assegni` | Assegni | `2` |
| `carta_credito` | Carta di credito | `3` |
| `bancomat` | Bancomat (carta di debito) | `8` |
| `tickets` | Buoni pasto | `5` |
| `non_riscosso_beni` | Non riscosso, beni | `7` |
| `non_riscosso_servizi` | Non riscosso, servizi | `50` |
| `non_riscosso_fattura` | Non riscosso, segue fattura | `51` |
| `non_riscosso_ssn` | Non riscosso, a carico del Servizio Sanitario | `52` |
| `sconto_a_pagare` | Sconto a pagare | `53` |
| `buoni_multiuso` | Buoni multiuso | `53` |
| `buoni_celiachia` | Buoni celiachia | `5` |

Con il valore `0` la forma di pagamento è disabilitata: Facile la rifiuta
invece di mandarla al registratore.

!!! warning "Un numero sbagliato non dà errore"

    La tabella dei pagamenti del registratore si può riprogrammare. Se il
    numero scritto nel file non corrisponde a quello della cassa installata,
    lo scontrino esce lo stesso ma l'incasso finisce sul totalizzatore
    sbagliato: lo si scopre solo in chiusura. I numeri vanno verificati con il
    tecnico sulla programmazione della macchina.

### Sconti, omaggi, resi e annulli

- Gli **sconti** e le **maggiorazioni**, di riga e sul totale, arrivano al
  registratore sempre come importo, anche quando in Facile sono in
  percentuale.
- L'**omaggio** esce come riga di vendita trasformata in omaggio.
- Il **reso** e l'**annullo** di uno scontrino indicano al registratore
  azzeramento, numero e data dell'originale, e la matricola se l'originale è
  di un altro registratore. Se il registratore non trova l'originale o non
  ammette l'operazione, Facile annulla il documento e lo dice.
- Il **codice lotteria** e il **codice fiscale** del cliente vanno dentro lo
  scontrino.

### Punti fidelity, codice a barre e buoni sconto

I punti della carta fedeltà e il codice a barre dello scontrino escono dentro
lo scontrino. I [buoni sconto](../../vendite/buoni-sconto.md) escono su un
documento non fiscale, dopo lo scontrino.

### Cosa non si può fare

Il web service del registratore non ha un comando per queste operazioni, e
Facile lo dice con un messaggio:

- **versamento** e **prelievo** di cassa: vanno fatti dalla tastiera del
  registratore;
- **acconto** e **buono monouso**;
- **fattura** stampata dal registratore;
- **lettura dei reparti**.

---

## Il display cliente

Per scrivere sul display del registratore scegli, nelle Impostazioni
Postazione, `CUSTOM WEB SERVICE` anche in **Customer Display - 1**, con la
stessa **Porta** della cassa.

## Diagnostica

Con il registro delle comunicazioni attivo, Facile scrive richieste e risposte
del registratore nel file `log\custom_webservice_log.txt` della sua cartella.

## Controlli e messaggi

I messaggi compaiono nel Pos dopo l'intestazione *Cassa OFF-LINE !*, *Comando
non accettato dalla Cassa !* o *Cassa occupata !*.

| Messaggio | Causa | Rimedio |
|---|---|---|
| *Indirizzo della cassa non configurato in cfg\Custom_WebService.ini* | Nel file manca l'indirizzo del registratore. | Scrivi l'indirizzo alla voce `ip`. |
| *Cassa non raggiungibile all'indirizzo … (…): non e' stato eseguito niente* | Il registratore è spento, scollegato o ha un altro indirizzo. | Controlla accensione, cavo di rete e indirizzo nel file. Non è stato stampato niente: puoi riprovare. |
| *La cassa non ha risposto (…): controllare che sia accesa e collegata, poi riprovare* | Il registratore non ha risposto alla richiesta dello stato. | Controlla il registratore e riprova. |
| *… la cassa rifiuta l'accesso (HTTP …): controllare la matricola della cassa nelle Impostazioni* | Il registratore non accetta la matricola presentata per l'accesso. | Correggi la matricola nelle Impostazioni Postazione. |
| *La cassa e' occupata (…): non e' stato eseguito niente. Riprovare fra poco* | Il registratore sta facendo altro: un'operazione dalla tastiera, un invio telematico, un'esportazione. | Aspetta che finisca e riprova. |
| *Stampante della cassa: carta esaurita. Non e' stato stampato niente* (oppure *coperchio aperto*, *giornale elettronico pieno*) | Il registratore non può stampare. | Sistema il registratore e riprova. |
| *Sulla cassa c'e' gia' un documento aperto (…): chiuderlo o annullarlo dalla cassa, poi riprovare. Non e' stato stampato niente* | Sul registratore è rimasto aperto un documento, per esempio iniziato dalla tastiera. | Chiudilo o annullalo dal registratore. |
| *Cassa: errore … al comando …. Il documento in corso e' stato annullato: non e' stato emesso nessun documento* | Il registratore ha rifiutato un comando; Facile ha annullato il documento rimasto aperto. | Leggi il codice e la descrizione dell'errore, correggi la causa (per esempio un reparto o un pagamento non programmato) e riemetti. |
| *Cassa: la risposta non e' arrivata: …. La cassa e' libera e il progressivo non e' avanzato: non e' stato emesso nessun documento* | La risposta si è persa, ma il registratore non ha emesso niente. | Riprova. |
| *La cassa non ha confermato il documento (…): non si sa se e' uscito; controllare sul giornale della cassa se il documento e' uscito prima di riemetterlo* | La risposta si è persa e Facile non è riuscito a stabilire se lo scontrino è uscito. | Guarda se lo scontrino è stato stampato o leggi il giornale del registratore. Riemetti solo se non è uscito. |
| *Cassa: il documento originale non e' stato trovato. Non e' stato emesso nessun documento* | Reso o annullo di uno scontrino che il registratore non trova. | Controlla azzeramento, numero, data e matricola dell'originale. |
| *Cassa: l'operazione sul documento originale non e' ammessa. Non e' stato emesso nessun documento* | Il registratore non permette il reso o l'annullo di quello scontrino, per esempio perché già annullato. | Verifica l'originale sul giornale del registratore. |
| *Il documento aperto sulla cassa (…) non si annulla: controllare sulla cassa* | Facile non è riuscito ad annullare il documento rimasto aperto. | Annullalo dalla tastiera del registratore. |
| *Attenzione! Cassa: il documento e' stato emesso, ma la cassa non ha riportato il numero del documento: va letto sullo scontrino.* | Lo scontrino è uscito, ma il registratore non ne ha comunicato il numero. | La vendita è registrata senza numero: leggilo sullo scontrino. Se succede sempre, fai aggiornare il registratore. |
| *La forma di pagamento … non e' abilitata in cfg\Custom_WebService.ini* | Nel file quella forma di pagamento è a `0`. | Scrivi il numero che ha sul registratore, oppure usa un'altra forma di pagamento. |
| *Chiusura giornaliera non riuscita: errore …* | Il registratore ha rifiutato la chiusura. | Leggi il codice dell'errore; se la chiusura è già stata fatta e non ci sono vendite, non serve ripeterla. |
| *La risposta della cassa non e' arrivata (…): non si sa se la chiusura giornaliera e' stata fatta. Controllare sulla cassa prima di ripeterla* | La risposta alla chiusura si è persa. | Controlla sul registratore se la chiusura è stata stampata. |
| *Il versamento non e' previsto dal web service dei registratori Custom: va fatto dalla tastiera della cassa* (lo stesso per *Il prelievo*) | Operazione che il web service non ha. | Falla dalla tastiera del registratore. |
| *L'acconto non e' gestito col tipo CUSTOM WEB SERVICE: il web service della cassa non ha un comando per incassarlo* | Operazione che il web service non ha. | Non applicabile. |
| *Il buono monouso non e' gestito col tipo CUSTOM WEB SERVICE: il web service della cassa non ha un comando per venderlo* | Operazione che il web service non ha. | Non applicabile. |
| *La fattura su cassa non e' gestita col tipo CUSTOM WEB SERVICE* | La fattura non si stampa dal registratore con questo collegamento. | Emetti la fattura da Facile. |
| *La lettura dei reparti non e' prevista dal web service dei registratori Custom* | Operazione che il web service non ha. | Non applicabile. |

## Vedi anche

- [Registratori telematici](index.md)
- [Registratori telematici RCH](rch.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
