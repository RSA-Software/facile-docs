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
    - **Al banco:** il tasto della cassa sul **Pos Touchscreen**; con Virtuo VNE e PagAmico anche ++f6++ **Rendiresto** nella chiusura della vendita
    - **Pagine dei modelli:** [CashDro](cashdro.md), [Cashlogy](cashlogy.md), [Cashmatic](cashmatic.md), [Virtuo VNE](vne.md), [PagAmico](pagamico.md)
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
postazione. Per tutte le marche tranne la CashDro, le funzioni di gestione —
livelli, prelievi, caricamenti, chiusure — si aprono dal **Pos Touchscreen**
con **Funzioni ▸ Cassa Automatica**.

## I modelli in elenco

| Voce in **Cassa Automatica** | Come la pilota Facile | Configurazione | Pagina |
|---|---|---|---|
| `NESSUNA` | Nessuna cassa automatica. | — | — |
| `CASHDRO WEB SERVICE` | Direttamente, in rete. | `cfg\cashdro_ws.ini` | [CashDro](cashdro.md) |
| `CASHDRO FILES` | Scambiando file con il programma della CashDro. | `cfg\cashdro.ini` | [CashDro](cashdro.md) |
| `CASHLOGY` | Attraverso il programma di collegamento della Cashlogy. | `cfg\cashlogy.ini` | [Cashlogy](cashlogy.md) |
| `CASHMATIC` | Scambiando file con il programma della Cashmatic. | `cfg\cashmatic.ini` | [Cashmatic](cashmatic.md) |
| `VIRTUO VNE` | Direttamente, in rete. | `cfg\vne.ini` | [Virtuo VNE](vne.md) |
| `PAGAMICO` | Attraverso il FacileWebApiService. | `cfg\pagamico.ini` e la configurazione del servizio | [PagAmico](pagamico.md) |

Con `VIRTUO VNE` e `PAGAMICO` nelle impostazioni della postazione compare anche
**Arrotonda ai 5 Centesimi Superiori**.

## Che cosa si fa con ciascuna

| | CashDro | Cashlogy | Cashmatic | Virtuo VNE | PagAmico |
|---|:---:|:---:|:---:|:---:|:---:|
| Incasso dal **Pos Touchscreen** | ● | ● | ● | ● | ● |
| Incasso con ++f6++ **Rendiresto** in vendita | | | | ● | ● |
| Erogazione automatica di resi e vincite | | ● | | | ● |
| Avviso del resto non erogato | | ● | ● | ● | ● |
| Gestione da **Funzioni ▸ Cassa Automatica** | | ● | ● | ● | ● |

## Vedi anche

- [CashDro](cashdro.md), [Cashlogy](cashlogy.md), [Cashmatic](cashmatic.md), [Virtuo VNE](vne.md), [PagAmico](pagamico.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
- [Registratori telematici](../registratori/index.md)
