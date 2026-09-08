---
title: Scadenze
description: Il menu Scadenze di Facile — scadenziario clienti e fornitori, distinte di incasso e pagamento, effetti, stampe e controllo crediti.
---

# Scadenze

Il menu **Scadenze** tiene il conto di quello che si deve incassare e di quello
che si deve pagare. Le scadenze nascono da sole quando si registra un documento
o una fattura d'acquisto — il [tipo di pagamento](../contabilita/tipi-di-pagamento.md)
decide quante rate e a che distanza — e da qui si consultano, si correggono, si
chiudono e si stampano.

Il menu è diviso in due rami gemelli, **Scadenziario Clienti** e **Scadenziario
Fornitori**: le maschere sono le stesse, cambia il verso.

## Consultare e correggere

- [Gestione scadenze](gestione-scadenze.md) — l'elenco delle scadenze con i
  filtri per data, stato e soggetto: da qui si aggiunge, si modifica, si cerca.

## Incassare e pagare

- [Distinte di incasso e di pagamento](distinte-incasso-pagamento.md) — il gesto
  con cui una o più scadenze si chiudono, con la ricezione degli incassi
  raccolti dagli agenti.
- [Effetti e RI.BA.](effetti-e-riba.md) — portafoglio effetti, stampa delle
  ricevute bancarie, contabilizzazione, file di flusso per la banca e stampa
  degli assegni.

## Stampare

- [Stampe delle scadenze](stampe-scadenze.md) — elenco, sintesi, solleciti,
  interessi di mora ed estratto conto per documento.
- [Controllo crediti e debiti](controllo-crediti.md) — controllo crediti,
  ritardi medi di incasso, credito circolante, crediti per agente, estratti
  conto ed esposizione verso i fornitori.

## Tenere in ordine

- [Manutenzione dello scadenziario](manutenzione-scadenze.md) — il controllo
  fra scadenze e schede contabili, l'eliminazione delle scadenze chiuse, i
  totali e il cruscotto finanziario.

!!! tip "Quando lo scadenziario non torna con la contabilità"

    1. **Controllo Scadenze <-> Schede Contabili**, fra le voci di
       [manutenzione](manutenzione-scadenze.md): dice dove le due cose
       divergono.
    2. La [gestione scadenze](gestione-scadenze.md) con **Stato** su `NON
       PAGATE`, per vedere cosa risulta ancora aperto.
    3. La [scheda contabile](../contabilita/schede-contabili.md) del
       soggetto, per confrontare riga per riga.

!!! note "Le scadenze si generano dai documenti"

    Non si inseriscono a mano se non per eccezione: nascono dalla
    [fattura](../vendite/documento-di-vendita.md) o dalla
    [fattura d'acquisto](../contabilita/registrazione-prima-nota.md), con
    le rate previste dal tipo di pagamento del soggetto.
