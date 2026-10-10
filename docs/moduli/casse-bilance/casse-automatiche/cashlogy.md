---
title: Cassa automatica Cashlogy
description: Come Facile incassa con la cassa automatica Cashlogy attraverso il suo programma di collegamento, e come si usano le funzioni di gestione dal Pos Touchscreen.
modulo: Casse e Bilance
---

# Cassa automatica Cashlogy

Con la Cashlogy Facile incassa gli scontrini del banco, eroga il denaro dei
resi e preleva contante; dal **Pos Touchscreen** offre anche le funzioni di
gestione della macchina — caricamento, svuotamenti, chiusura del fondo cassa,
statistiche — ciascuna abilitata per operatore.

!!! info "In sintesi"

    - **Voce:** `CASHLOGY` in **Cassa Automatica**, in [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
    - **Configurazione:** `cfg\cashlogy.ini`
    - **Al banco:** il tasto **CashLogy** del **Pos Touchscreen**; la gestione da **Funzioni ▸ Cassa Automatica**
    - **Licenza:** separata, in aggiunta a quella di Facile

---

!!! info "Licenza"

    Il collegamento con le casse automatiche è soggetto a una **licenza
    separata**, in aggiunta a quella di Facile.

## Come funziona

Facile non parla direttamente con la macchina ma con il **programma di
collegamento** della Cashlogy (*Cashlogy Connector*), che avvia da solo,
nascosto, all'apertura del banco e a cui si collega in rete. Le schermate di
pagamento e di gestione sono quelle della Cashlogy.

## Il file cashlogy.ini

| Sezione | Chiave | Predefinito | Descrizione |
|---|---|---|---|
| `[OPTIONS]` | `indirizzo_ip` | — | L'indirizzo del programma di collegamento. Obbligatorio. |
| `[OPTIONS]` | `port` | 8092 | La sua porta. |
| `[OPTIONS]` | `connector_path` | — | Il percorso del programma di collegamento, che Facile avvia. Obbligatorio. |
| `[OPTIONS]` | `connector_close` | 1 | `1` per chiudere il collegamento all'uscita dal banco e con il pulsante **Chiudi** della gestione. |
| `[VENDITA]` | `mostra_schermo_2`, `posizione_x_schermo_2`, `posizione_y_schermo_2` | 0 | Se e dove mostrare la schermata di pagamento su un secondo monitor. |
| `[VENDITA]` | `schermo_on_top` | 0 | `1` per tenere le schermate della Cashlogy sempre in primo piano. |
| `[VENDITA]` | `mostra_pulsante_accetta`, `accetta_importo_parziale`, `accetta_cent_manuali`, `mostra_pulsante_deposito` | 0 | Le scelte offerte sulla schermata di pagamento: chiudere con un importo inferiore, inserire i centesimi a mano e simili. |
| `[OPE_n]` | vedi sotto | 0 | I pulsanti di gestione abilitati per l'operatore numero `n`. |

<!-- DA VERIFICARE: che cosa fanno sulla schermata della Cashlogy i pulsanti Accetta e Deposito -->

!!! note "La sezione [BACKOFFICE]"

    Il file di esempio contiene anche una sezione `[BACKOFFICE]` con chiavi
    `show_…`: oggi non ha effetto. I pulsanti di gestione si abilitano con le
    sezioni `[OPE_n]`.

### I pulsanti per operatore

Per ogni operatore che deve usare la gestione si aggiunge una sezione con il
suo codice, per esempio `[OPE_1]`, e si mette a `1` ciascun pulsante da
abilitare. Un operatore senza la sua sezione vede tutti i pulsanti spenti.

| Chiave | Pulsante |
|---|---|
| `inizializza` | **Inizializza** |
| `chiudi` | **Chiudi** |
| `aggiungi_monete_banconote` | **Aggiungi Monete e Banconote** |
| `svuotamento_totale` | **Svuotamento Totale** |
| `svuotamento_monete` | **Svuotamento Monete** |
| `azzeramento_monete` | **Azzeramento Monete** |
| `chiusura_fondo_cassa` | **Chiusura Fondo Cassa** |
| `statistiche_assolute`, `statistiche_relative` | **Statistiche Assolute**, **Statistiche Relative** |
| `eroga_cambio` | **Eroga Cambio** |
| `preleva_contante` | **Preleva Contante** |
| `prelevva_banconote_stacker` | **Preleva Banconote dallo Stacker** — la chiave si scrive con due *v* |
| `mostra_stato` | **Mostra Stato** |
| `visualizza_logs` | **Visualizza Logs** |
| `manutenzione` | **Manutenzione** |

## Incassare uno scontrino

1. Batti lo scontrino sul **Pos Touchscreen** e fai il subtotale.
2. Premi **CashLogy**. Per incassare solo una parte, digita prima l'importo.
3. Il cliente paga sulla schermata della Cashlogy.
4. Facile aggiunge una riga **CONTANTI** con l'importo pagato (inserito meno
   resto) e, se il totale è coperto, chiude e stampa lo scontrino. Se è stata
   pagata solo una parte, lo scontrino resta aperto per il resto.

Se il pagamento viene annullato, lo scontrino resta aperto senza messaggi. Se
la macchina non riesce a rendere tutto il resto, Facile lo dice e indica la
cifra da dare a mano.

Con un totale negativo — un reso o una vincita — la Cashlogy **eroga** il
denaro al cliente.

!!! note "Solo dal Pos Touchscreen"

    Nella chiusura dello scontrino di **Vendita** il tasto **F6 -
    Rendiresto** non è disponibile con la Cashlogy.

### Prelevare contante dal banco

Sul **Pos Touchscreen**, a scontrino vuoto, il tasto **Prelievo** fa erogare
dalla macchina l'importo digitato. Se sono attivi i tasti sensibili, serve
l'autorizzazione del supervisore.

## La gestione della cassa

Sul **Pos Touchscreen**, a scontrino vuoto, **Funzioni ▸ Cassa Automatica**
apre la finestra **Cashlogy** con i pulsanti abilitati per l'operatore:

| Pulsante | Che cosa fa |
|---|---|
| **Inizializza** | Inizializza la macchina. |
| **Chiudi** | Chiude il collegamento con la macchina, dopo conferma. |
| **Aggiungi Monete e Banconote** | Caricamento: alla fine mostra l'importo inserito. |
| **Svuotamento Totale**, **Svuotamento Monete** | Svuotano la macchina, o le sole monete, e mostrano l'importo erogato. |
| **Azzeramento Monete** | Azzera il conteggio delle monete e mostra il valore prima e dopo. |
| **Chiusura Fondo Cassa** | Chiude il fondo cassa: mostra importo iniziale, caricato e finale. |
| **Statistiche Assolute**, **Statistiche Relative** | Mostrano le statistiche sulla schermata della Cashlogy. |
| **Eroga Cambio** | Cambia denaro: mostra quanto è stato inserito ed erogato. |
| **Preleva Contante** | Preleva contante e mostra l'importo. |
| **Preleva Banconote dallo Stacker** | Preleva le banconote dallo stacker e mostra l'importo. |
| **Mostra Stato** | Mostra l'importo presente nella macchina. |
| **Visualizza Logs**, **Manutenzione** | Aprono le schermate della Cashlogy. |
| **Esci** | Chiude la finestra. |

I risultati delle operazioni riuscite compaiono con l'icona delle
informazioni; gli errori con quella rossa.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Assenza di Comunicazione con la cassa automatica. Verificare la connessione e riavviare il dispositivo!<br><br>Vuoi riprovare?* | All'apertura del banco il programma di collegamento non risponde, o la configurazione è incompleta. | Controlla `cashlogy.ini` e la macchina; **Sì** riprova (il programma di collegamento può essere lento a partire), **No** chiude il banco. |
| *Nessuna Risposta da CashLogy!<br><br>Vuoi Attendere?* | La macchina non ha risposto per cinque minuti. | **Sì** continua ad aspettare. |
| *E' necessario reinizializzare nuovamente CashLogy!* | La macchina ha rifiutato il comando. | Segue la richiesta di riprovare il collegamento; ripeti l'incasso. |
| *Si e' verificato un problema nell'erogazione del resto.<br>Si prega di rendere manualmente Euro …* | La macchina non aveva i tagli per tutto il resto. | **Il resto va dato a mano.** |
| *…<br><br>Non e' stato erogato l'importo di Euro …* | Un **Prelievo** non è riuscito. | Controlla la macchina. |
| *Cassa Automatica Occupata!* | La macchina sta facendo un'altra operazione. | Aspetta e riprova. |
| *Path Cashlogy Connector non valida!* | `connector_path` manca o è sbagliato. | Correggi il percorso. |
| *Impossibile aprire il socket* / *Errore di comunicazione con il socket!* | Il collegamento con il programma di collegamento non riesce. | Controlla indirizzo e porta. |

## Vedi anche

- [Casse automatiche](index.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
