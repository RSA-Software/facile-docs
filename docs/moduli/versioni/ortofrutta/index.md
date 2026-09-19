---
title: Ortofrutta
description: Il ramo di menu della versione per il commercio all'ingrosso di ortofrutta: partite in conto deposito, chiusura della vendita, imballaggi e resa al produttore.
modulo: Ortofrutta
maschera_id: nessuna dialog propria
---

# Ortofrutta

Il menu **Ortofrutta** c'è solo nella versione di Facile allestita per il
**commercio all'ingrosso di prodotti ortofrutticoli**. Serve a chi riceve la
merce dai produttori, la vende nel mercato e poi rende conto a ciascuno di
quanto ha venduto e a che prezzo.

!!! warning "Se non trovi il menu, la tua versione non lo prevede"

    Come gli altri rami delle [versioni specifiche](../index.md), all'avvio il
    programma toglie dalla barra l'intero menu quando la versione non è quella.

---

## La partita: il concetto su cui gira tutto

Il modulo ruota intorno a una sola cosa, la **partita**.

Una partita è **la merce che un produttore ha conferito in una volta**: tanti
colli di un certo prodotto, arrivati in una certa data. Si registra con un
[carico merci](../../magazzino/carico-merci.md), e **il numero del documento di
carico è il numero della partita**.

Da quel momento la partita ha una vita propria:

1. **entra** — colli, quantità, prezzo di carico e imballaggio;
2. **si vende**, un po' per volta, giorno per giorno: ogni riga venduta resta
   legata alla sua partita;
3. **si consuma** — quello che resta è la giacenza della partita;
4. **si chiude**, quando è finita: prende una *data di fine vendita*;
5. **si fa il conto al produttore**: dal ricavo si tolgono le spese e gli
   acconti già dati, e quello che resta è il suo netto.

È il meccanismo del **conto deposito**: la merce non si compra, si riceve e si
vende per conto di chi l'ha prodotta, trattenendo le spese e la provvigione.
Per questo il modulo parla sempre di due prezzi — **il prezzo di vendita**, che
paga il cliente, e **il prezzo fornitore**, che va al produttore: la differenza
è il guadagno del grossista.

!!! note "Le partite attraversano l'anno"

    La merce in giacenza al 31 dicembre non sparisce con il cambio esercizio: le
    partite ancora aperte si **esportano dal vecchio anno e si importano nel
    nuovo**, dove ricominciano con un numero nuovo che ricorda da quale partita
    vengono. Vedi [Partite](partite.md).

## Le pagine di questa sezione

| Pagina | Cosa contiene |
|---|---|
| [Partite](partite.md) | Il riepilogo della singola partita e di tutte insieme, i fogli di intestazione e il passaggio delle partite aperte da un anno all'altro. |
| [Chiusura della vendita](chiusura-vendita.md) | La chiusura giornaliera e il suo annullamento. |
| [Estratti e schede](estratti-e-schede.md) | Estratto vendita, estratto per fornitore, movimenti cliente, provvigioni, rimanenze e anomalie. |
| [Ordini cumulativi e imballaggi](ordini-e-imballaggi.md) | Gli ordini delle catene, i fornitori preferiti per operatore e il giro degli imballaggi. |

## Vedi anche

- [Carico Merci](../../magazzino/carico-merci.md) — dove nasce la partita
- [Versioni specifiche](../index.md)
