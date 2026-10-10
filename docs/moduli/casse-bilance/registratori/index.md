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
    - **Pagine dei modelli:** [RCH](rch.md)

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
| `MICRELEC` | — |
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

## Vedi anche

- [RCH](rch.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
