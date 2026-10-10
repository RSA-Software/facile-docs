---
title: Cassa automatica Virtuo VNE
description: Come Facile incassa con la cassa automatica Virtuo VNE in rete, dalla vendita e dal Pos Touchscreen, e come si usano le funzioni di gestione della macchina.
modulo: Casse e Bilance
---

# Cassa automatica Virtuo VNE

Con la Virtuo VNE Facile incassa gli scontrini sia dalla chiusura della
**Vendita** (++f6++ **Rendiresto**) sia dal **Pos Touchscreen**, e dalla
gestione ne comanda livelli, prelievi, ricarica, svuotamenti, reset, apertura
della porta, riavvio e chiusura.

!!! info "In sintesi"

    - **Voce:** `VIRTUO VNE` in **Cassa Automatica**, in [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
    - **Configurazione:** `cfg\vne.ini`
    - **Al banco:** ++f6++ **Rendiresto** nella chiusura della vendita, o il tasto **VNE** del **Pos Touchscreen**; la gestione da **Funzioni ▸ Cassa Automatica**
    - **Licenza:** separata, in aggiunta a quella di Facile

---

!!! info "Licenza"

    Il collegamento con le casse automatiche è soggetto a una **licenza
    separata**, in aggiunta a quella di Facile.

## Il file vne.ini

| Chiave in `[OPTIONS]` | Predefinito | Descrizione |
|---|---|---|
| `ip_address` | `127.0.0.1` | L'indirizzo della macchina. |
| `ssl` | 0 | `1` per il collegamento cifrato (https). |

Facile si presenta alla macchina come *Facile*, senza utente né password. Le
richieste e le risposte vengono salvate nella cartella `log` (file `vne_…json`),
utili all'assistenza.

### Arrotondare ai 5 centesimi

Con `VIRTUO VNE` in [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
compare **Arrotonda ai 5 Centesimi Superiori**: l'importo chiesto alla macchina
viene arrotondato per eccesso ai cinque centesimi. Il totale dello scontrino non
cambia.

## Incassare uno scontrino

All'apertura della vendita e del banco Facile verifica il collegamento con la
macchina.

**Dalla Vendita:**

1. Nella chiusura dello scontrino premi ++f6++ **Rendiresto**: Facile chiede
   alla macchina la parte del totale non ancora pagata in altro modo.
2. La finestra *Operazione di pagamento in corso* mostra quanto il cliente ha
   già inserito; con **Annulla** si interrompe e il denaro viene restituito.
3. A pagamento concluso l'importo va nei contanti e, se il totale è coperto,
   lo scontrino si chiude da solo.

**Dal Pos Touchscreen:** premi **VNE**; per incassare solo una parte digita
prima l'importo. Facile aggiunge una riga **CONTANTI** con l'importo pagato.

Se la macchina non riesce a rendere tutto il resto, Facile lo dice.

## La gestione della cassa

Sul **Pos Touchscreen**, a scontrino vuoto, **Funzioni ▸ Cassa Automatica**
apre la finestra **VNE Virtuo**:

| Pulsante | Che cosa fa |
|---|---|
| **Mostra Livelli** | Mostra il contenuto: riciclatore, stacker e monete. |
| **Preleva Contante** | Chiede un importo e lo fa erogare; alla fine mostra l'importo prelevato. |
| **Aggiungi Monete e Banconote** | Ricarica: la finestra mostra quanto è stato caricato; **Annulla** chiude la ricarica. |
| **Svuotamento Parziale Monete**, **Svuotamento Totale Monete** | Svuotano le monete. |
| **Svuotamento Parziale Banconote**, **Svuotamento Totale Banconote** | Svuotano le banconote del riciclatore. |
| **Apertura Porta** | Apre la porta della macchina. |
| **Riavvio Cassa**, **Spegni Cassa** | Riavviano o spengono la macchina, **senza chiedere conferma**. |
| **Chiusura Cassa** | Chiude la cassa e mostra il riepilogo: inserito ed erogato ai clienti, pagamenti, versamenti, prelievi, contenuto, fondo cassa, incasso in contanti. |
| **Reset Stacker**, **Reset Monete**, **Reset Totale** | Azzerano il conteggio dello stacker, delle monete o di entrambi, dopo conferma. |
| **Esci** | Chiude la finestra. |

!!! warning "I reset si fanno dopo aver svuotato a mano"

    I reset azzerano il **conteggio**, non il denaro: vanno fatti solo dopo aver
    tolto fisicamente monete e banconote, altrimenti il conteggio della macchina
    non corrisponde più al contenuto.

!!! note "Con un totale negativo"

    Con un totale negativo — un reso o una vincita — la VNE non eroga denaro:
    per restituirlo usa **Preleva Contante**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Assenza di Comunicazione con la cassa automatica. Verificare la connessione e riavviare il dispositivo!<br><br>Vuoi riprovare?* | All'apertura della vendita o del banco la macchina non risponde. | Controlla la macchina e `ip_address`. In vendita **No** lascia spento ++f6++; sul banco **No** lo chiude. |
| *Il totale inserito non è sufficiente per chiudere lo scontrino!<br><br>Chiudere lo scontrino con il tasto F2 - OK* | Dopo il rendiresto resta una parte da pagare. | Incassa il resto in altro modo e chiudi con **F2 - OK**. |
| *Impossibile effettuare la restituzione del denaro inserito!* | Annullando, la macchina non ha potuto restituire il denaro. | Controlla la macchina e restituisci a mano. |
| *Impossibile erogare completamente il resto!* / *Impossibile restituire resto per € …* | La macchina non aveva i tagli per il resto. | **Il resto va dato a mano.** |
| *Errore sulla richiesta http!* | La macchina non è raggiungibile. | Controlla rete e indirizzo. |
| *Impossibile avviare l'operazione!* | La macchina ha rifiutato l'operazione. | Controlla lo stato della macchina. |
| *Sistema occupato!* | La macchina sta facendo un'altra operazione. | Aspetta e riprova. |
| *Attenzione!<br>Il comando resetta il contenuto dello stacker delle banconote.<br><br>Effettuare l'operazione solo dopo che l'operatore ha rimosso fisicamente tutte le banconote dallo stacker.<br><br>Vuoi Continuare?* | Hai premuto **Reset Stacker**. | Rispondi **Sì** solo a stacker svuotato. Le domande di **Reset Monete** e **Reset Totale** sono analoghe. |

## Vedi anche

- [Casse automatiche](index.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
