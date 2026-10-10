---
title: Cassa automatica CashDro
description: Come Facile incassa con la cassa automatica CashDro, collegata in rete o tramite scambio di file, e come si configura.
modulo: Casse e Bilance
---

# Cassa automatica CashDro

Con la CashDro Facile **incassa** gli scontrini del banco: manda l'importo alla
macchina, il cliente paga sullo schermo della CashDro e Facile registra quanto è
stato pagato. Tutte le altre operazioni — caricamento, prelievi, chiusure — si
fanno con il programma della CashDro.

!!! info "In sintesi"

    - **Voci:** `CASHDRO WEB SERVICE` o `CASHDRO FILES` in **Cassa Automatica**, in [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
    - **Configurazione:** `cfg\cashdro_ws.ini` o `cfg\cashdro.ini`
    - **Al banco:** il tasto **CashDro** del **Pos Touchscreen**
    - **Licenza:** separata, in aggiunta a quella di Facile

---

!!! info "Licenza"

    Il collegamento con le casse automatiche è soggetto a una **licenza
    separata**, in aggiunta a quella di Facile.

## I due collegamenti

| Voce | Come parla con la macchina |
|---|---|
| `CASHDRO WEB SERVICE` | In rete, con il servizio web della CashDro, con utente e password della macchina. |
| `CASHDRO FILES` | Scambiando file in una cartella condivisa con il programma della CashDro. |

### CASHDRO WEB SERVICE: cashdro_ws.ini

| Chiave in `[OPTIONS]` | Predefinito | Descrizione |
|---|---|---|
| `indirizzo_ip` | — | L'indirizzo della macchina. Obbligatorio. |
| `user` | — | L'utente del servizio web della macchina. Obbligatorio. |
| `password` | — | La password. Obbligatoria. |

Il collegamento è sempre cifrato (https). Ogni risposta della macchina durante
l'incasso viene salvata in `log\cashdro.json`, utile all'assistenza.

### CASHDRO FILES: cashdro.ini

| Chiave in `[OPTIONS]` | Predefinito | Descrizione |
|---|---|---|
| `path` | `c:\cashdro` | La cartella condivisa con il programma della CashDro. |
| `full_screen` | 0 | `1` per mostrare la schermata della CashDro a tutto schermo, `0` per una barra in alto. |
| `sleep_time` | 0 | I millisecondi fra due controlli della risposta. |
| `max_iter` | 0 | Quanti controlli fare prima di rinunciare. |

!!! warning "Indica sempre sleep_time e max_iter"

    Se mancano, Facile controlla la risposta una volta sola e dà subito
    *Nessuna risposta*. Il file di esempio usa `sleep_time = 500` e
    `max_iter = 60`, cioè mezzo minuto di attesa.

## Incassare uno scontrino

1. Batti lo scontrino sul **Pos Touchscreen** e fai il subtotale.
2. Premi **CashDro**. Per incassare solo una parte, digita prima l'importo.
3. Il cliente paga sullo schermo della CashDro; Facile resta in attesa.
4. A pagamento concluso Facile aggiunge una riga **CONTANTI** con l'importo
   pagato e, se il totale è coperto, chiude e stampa lo scontrino. Se è stata
   pagata solo una parte, lo scontrino resta aperto per il resto.

Se il pagamento viene annullato sulla CashDro, lo scontrino resta aperto senza
messaggi.

!!! warning "Il resto non erogato non viene segnalato"

    Facile non avvisa se la CashDro non è riuscita a rendere tutto il resto:
    controlla lo schermo della macchina.

!!! note "Solo dal Pos Touchscreen"

    La CashDro si usa solo dal **Pos Touchscreen**: nella chiusura dello
    scontrino di **Vendita** il tasto **F6 - Rendiresto** non è disponibile.
    Con un totale negativo (reso o vincita) la CashDro non eroga denaro.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Assenza di Comunicazione con la cassa automatica. Verificare la connessione e riavviare il dispositivo!<br><br>Vuoi riprovare?* | All'apertura del banco la configurazione della CashDro è incompleta. | Controlla `cashdro_ws.ini`; **No** chiude il banco. |
| *Indirizzo ip non indicato in cashdro_ws.ini!* / *User non indicato in cashdro_ws.ini!* / *Password non indicata in cashdro_ws.ini!* | Manca una chiave del file. | Compila il file. |
| *Errore sulla richiesta http!* | La macchina non è raggiungibile. | Controlla rete e indirizzo. |
| *Autenticazione fallita!* | Utente o password sbagliati. | Correggi `user` e `password`. |
| *L'utente non ha diritti sufficienti!* | L'utente della macchina non può fare incassi. | Usa un utente con i permessi. |
| *Sistema occupato!* | La CashDro sta facendo un'altra operazione. | Aspetta e riprova. |
| *Servizio cashdro non operativo!* | Il servizio della CashDro non è avviato. | Riavvia la macchina. |
| *Impossibile creare il file nella cartella specificata!* | Con `CASHDRO FILES` la cartella non esiste o non è scrivibile. | Controlla `path`. |
| *Nessuna risposta* | Con `CASHDRO FILES` il programma della CashDro non ha risposto in tempo. | Controlla che sia avviato e i valori di `sleep_time` e `max_iter`. |
| *File XML di risposta non valido!* / *File JSON di risposta non valido!* | La risposta della macchina non è leggibile. | Contatta l'assistenza con il file di risposta. |

## Vedi anche

- [Casse automatiche](index.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
