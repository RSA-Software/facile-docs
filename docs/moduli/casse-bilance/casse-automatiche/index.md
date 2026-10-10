---
title: Casse automatiche
description: Le casse automatiche rendiresto che Facile sa pilotare dalla vendita al banco, dove si sceglie il modello e come si configura ciascuna.
modulo: Casse e Bilance
---

# Casse automatiche

La cassa automatica — il *rendiresto* — è la macchina in cui il cliente
inserisce monete e banconote e che restituisce il resto da sola. Dal
[banco](../../vendite/vendita-al-banco.md) Facile le chiede di incassare il
totale dello scontrino e registra quanto è stato pagato.

!!! info "In sintesi"

    - **Dove si sceglie:** Menu ▸ Utility ▸ [Impostazioni Postazione](../../utility/impostazioni-postazione.md), campo **Cassa Automatica**
    - **Configurazione:** un file nella cartella `cfg` di Facile, diverso per ogni marca
    - **Al banco:** ++f6++ **Rendiresto**, oppure il tasto della cassa sul **Pos Touchscreen**
    - **Pagine dei modelli:** [PagAmico](pagamico.md)
    - **Licenza:** separata, in aggiunta a quella di Facile

---

!!! info "Licenza"

    Il collegamento con le casse automatiche è soggetto a una **licenza
    separata**, in aggiunta a quella di Facile.

## A cosa serve

Con la cassa automatica l'operatore non tocca il contante: chiude lo scontrino,
il cliente paga alla macchina e Facile riceve l'esito — pagato, pagato in parte,
annullato — insieme al resto che la macchina non è riuscita a erogare, da dare
a mano.

Ogni postazione ha la sua cassa automatica, scelta nelle impostazioni della
postazione. Le funzioni di gestione — stato dei livelli, prelievi, chiusure —
si aprono dal **Pos Touchscreen** con **Funzioni ▸ Cassa Automatica**.

## I modelli in elenco

| Voce in **Cassa Automatica** | Come la pilota Facile | File di configurazione |
|---|---|---|
| `NESSUNA` | Nessuna cassa automatica. | — |
| `CASHDRO WEB SERVICE` | Direttamente, in rete. | `cfg\cashdro_ws.ini` |
| `CASHDRO FILES` | Scambiando file con il programma della CashDro. | `cfg\cashdro.ini` |
| `CASHLOGY` | Direttamente, in rete. | `cfg\cashlogy.ini` |
| `CASHMATIC` | Scambiando file con il programma della Cashmatic. | `cfg\cashmatic.ini` |
| `VIRTUO VNE` | Direttamente, in rete. | `cfg\vne.ini` |
| `PAGAMICO` | Attraverso il FacileWebApiService. | `cfg\pagamico.ini` e la configurazione del servizio — vedi [PagAmico](pagamico.md) |

Con `VIRTUO VNE` nelle impostazioni della postazione compare anche **Arrotonda
ai 5 Centesimi Superiori**.

## La configurazione delle singole marche

Il file di ciascuna marca sta nella cartella `cfg` di Facile; le chiavi sono
nella sezione `[OPTIONS]`, salvo dove indicato.

### CashDro

| File | Chiave | Predefinito | Descrizione |
|---|---|---|---|
| `cashdro_ws.ini` | `indirizzo_ip` | — | Indirizzo della macchina. Obbligatorio. |
| `cashdro_ws.ini` | `user`, `password` | — | Le credenziali della macchina. |
| `cashdro_ws.ini` | `ssl` | 0 | `1` per il collegamento cifrato. |
| `cashdro.ini` | `path` | `c:\cashdro` | La cartella in cui Facile e il programma della CashDro si scambiano i file. |
| `cashdro.ini` | `full_screen` | 0 | `1` per mostrare la schermata della cassa a tutto schermo. |

### Cashlogy

| Sezione | Chiave | Predefinito | Descrizione |
|---|---|---|---|
| `[OPTIONS]` | `indirizzo_ip` | — | Indirizzo della macchina. Obbligatorio. |
| `[OPTIONS]` | `port` | 8092 | Porta della macchina. |
| `[OPTIONS]` | `connector_path`, `connector_close` | — , 1 | Il programma di collegamento della Cashlogy e se chiuderlo a fine operazione. |
| `[VENDITA]` | `mostra_schermo_2`, `posizione_x_schermo_2`, `posizione_y_schermo_2`, `schermo_on_top` | 0 | Dove e come mostrare la schermata della cassa durante la vendita. |
| `[VENDITA]` | `mostra_pulsante_accetta`, `accetta_importo_parziale`, `accetta_cent_manuali`, `mostra_pulsante_deposito` | 0 | Le scelte offerte durante l'incasso. |
| `[BACKOFFICE]` | `show_status`, `show_add_change`, `show_remove_cash`, `show_complete_empty`, … | 0 | Quali comandi di gestione della cassa compaiono: `1` li mostra. |

### Cashmatic

| Chiave | Predefinito | Descrizione |
|---|---|---|
| `path` | `c:\cashmatic` | La cartella in cui Facile e il programma della Cashmatic si scambiano i file. |
| `sleep_time` | 250 | Millisecondi fra due controlli dei file di risposta. |
| `max_iter` | 40 | Quanti controlli fare prima di considerare la cassa non raggiungibile. |

### Virtuo VNE

| Chiave | Predefinito | Descrizione |
|---|---|---|
| `ip_address` | `127.0.0.1` | Indirizzo della macchina. |
| `ssl` | 0 | `1` per il collegamento cifrato. |

### PagAmico

Vedi la [pagina dedicata](pagamico.md).

## Vedi anche

- [PagAmico](pagamico.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
- [Registratori telematici](../registratori/index.md)
