---
title: Cassa automatica Cashmatic
description: Come Facile incassa con la cassa automatica Cashmatic scambiando file con il suo programma, e come si usano livelli, prelievi, versamenti e svuotamenti.
modulo: Casse e Bilance
---

# Cassa automatica Cashmatic

Con la Cashmatic Facile incassa gli scontrini del banco e, dal **Pos
Touchscreen**, ne gestisce livelli, prelievi, versamenti, svuotamenti e
trasferimenti. Facile e la macchina si parlano scambiando file in una cartella
con il programma di interfaccia della Cashmatic.

!!! info "In sintesi"

    - **Voce:** `CASHMATIC` in **Cassa Automatica**, in [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
    - **Configurazione:** `cfg\cashmatic.ini`
    - **Al banco:** il tasto **Cashmatic** del **Pos Touchscreen**; la gestione da **Funzioni ▸ Cassa Automatica**
    - **Licenza:** separata, in aggiunta a quella di Facile

---

!!! info "Licenza"

    Il collegamento con le casse automatiche è soggetto a una **licenza
    separata**, in aggiunta a quella di Facile.

## Il file cashmatic.ini

| Chiave in `[OPTIONS]` | Predefinito | Descrizione |
|---|---|---|
| `path` | `c:\cashmatic` | La cartella condivisa con il programma di interfaccia della Cashmatic. |
| `sleep_time` | 250 | I millisecondi fra due controlli delle risposte. |
| `max_iter` | 40 | Quanti controlli fare, per la lettura dei livelli e per gli svuotamenti, prima di rinunciare (con i valori predefiniti, dieci secondi). |

Il programma di interfaccia della Cashmatic deve essere avviato: Facile
controlla, all'apertura del banco, che segnali il collegamento con la macchina.

<!-- DA VERIFICARE: quale programma della Cashmatic elabora i file nella cartella di scambio -->

## Incassare uno scontrino

1. Batti lo scontrino sul **Pos Touchscreen** e fai il subtotale.
2. Premi **Cashmatic**. Per incassare solo una parte, digita prima l'importo.
3. Il cliente paga alla macchina; Facile resta in attesa.
4. Facile aggiunge una riga **CONTANTI** con l'importo pagato (inserito meno
   resto) e, se il totale è coperto, chiude e stampa lo scontrino.

Se dopo una ventina di secondi il pagamento non è completo, Facile chiede se
continuare ad aspettare (**OK**) o annullare l'incasso (**Annulla**). Se in
quel tempo il programma della Cashmatic non ha dato nessun segno, Facile chiede
la stessa cosa con un messaggio diverso. Se la macchina non riesce a rendere
tutto il resto, Facile lo dice.

Con un totale negativo — un reso o una vincita — la Cashmatic **eroga**
l'importo al cliente. Se ne eroga solo una parte, Facile indica la differenza
da dare a mano.

!!! note "Solo dal Pos Touchscreen"

    Nella chiusura dello scontrino di **Vendita** il tasto **F6 -
    Rendiresto** non è disponibile con la Cashmatic.

## La gestione della cassa

Sul **Pos Touchscreen**, a scontrino vuoto, **Funzioni ▸ Cassa Automatica**
apre la finestra **Cashmatic**:

| Pulsante | Che cosa fa |
|---|---|
| **Mostra Livelli** | Apre il **contenuto della cassa**: quanti pezzi ci sono di ogni taglio, da 500 € a 1 centesimo. |
| **Preleva Contante** | Chiede un importo e lo fa erogare. Mostra l'importo prelevato e, se c'è, quello non erogato. |
| **Versa Contante** | Chiede un importo da inserire nella macchina. Mostra l'importo versato e, se c'è, quello non versato. |
| **Svuotamento Parziale Monete** | Svuota in parte le monete. |
| **Svuotamento Totale Monete** | Svuota tutte le monete. |
| **Svuotamento Banconote** | Svuota le banconote. |
| **Trasferimento Parziale Banconote**, **Trasferimento Totale Banconote** | Trasferiscono le banconote nel cassetto di raccolta. |
| **Esci** | Chiude la finestra. |

I risultati delle operazioni riuscite compaiono con l'icona delle
informazioni; gli errori con quella rossa.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Assenza di Comunicazione con la cassa automatica. Verificare la connessione e riavviare il dispositivo!<br><br>Vuoi riprovare?* | All'apertura del banco il programma della Cashmatic non segnala il collegamento con la macchina. | Avvia il programma e controlla la macchina; **No** chiude il banco. |
| *Pagamento non completato!<br><br>Scegliere:<br>OK - Per continuare a ricevere denaro<br>Annulla - per annullare l'incasso* | Il cliente non ha ancora pagato tutto. | **OK** continua ad aspettare; **Annulla** annulla l'incasso e lo scontrino resta aperto. |
| *Erogazione non completata!<br><br>Scegliere:<br>SI - Per accettare l'erogazione parziale<br>NO - Per continuare a erogare denaro<br>Annulla - per annullare l'erogazione* | Un prelievo non è ancora concluso. | Scegli come proseguire. |
| *Attenzione!<br><br>Impossibile erogare resto per € …* | La macchina non aveva i tagli per tutto il resto. | **Il resto va dato a mano.** |
| *Impossibile creare il file nella cartella specificata!* / *Impossibile leggere il file nella cartella specificata!* | La cartella di scambio non esiste o non è accessibile. | Controlla `path`. |
| *Nessuna risposta* | Il programma della Cashmatic non ha risposto in tempo. | Controlla che sia avviato. |
| *La cassa automatica non ha ancora risposto.<br><br>Scegliere:<br>OK - Per continuare ad attendere<br>Annulla - Per annullare l'operazione* | Durante un incasso o un'erogazione il programma della Cashmatic non dà segni da una ventina di secondi. | Controlla che il programma sia avviato. **OK** continua ad aspettare; **Annulla** annulla l'operazione. |
| *La cassa automatica non ha risposto: l'operazione e' stata annullata.<br><br>Controllare la cassa automatica prima di ripetere l'operazione.* | Hai annullato dopo la domanda precedente. | Guarda la macchina prima di ripetere. |
| *Attenzione!<br><br>La cassa automatica ha erogato Euro … di ….<br><br>Consegnare a mano al cliente Euro ….* | In un reso o in una vincita la macchina non ha erogato tutto. | Dai a mano la differenza indicata. |
| *Errore generico!* | La macchina non ha eseguito il comando, per esempio perché lo stacker non è stato rimosso. | Controlla la macchina e riprova. |

## Vedi anche

- [Casse automatiche](index.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
