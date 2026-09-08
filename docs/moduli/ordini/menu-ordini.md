---
title: Ordini
description: Il menu Ordini di Facile — ordini dei clienti, ordini ai fornitori, richieste offerta, generazione automatica e scambio con l'esterno.
---

# Ordini

Il menu **Ordini** tiene i due versi dell'impegno: quello che i clienti hanno
chiesto e non hanno ancora ricevuto, e quello che è stato chiesto ai fornitori
e non è ancora arrivato. In mezzo stanno le voci che fanno passare dall'uno
all'altro senza riscrivere nulla.

L'ordine si registra e si consulta con le stesse maschere degli altri
[documenti di vendita](../vendite/documento-di-vendita.md): questo menu
raccoglie quello che agli ordini è proprio.

## Registrare e seguire gli ordini

- [Ordini in lavorazione e in ricezione](ordini-in-lavorazione-e-ricezione.md) —
  gli ordini dei clienti da evadere e quelli ai fornitori in attesa di arrivo,
  con la cancellazione degli ordini ricevuti.
- [Ordini tabacchi](ordini-tabacchi.md) — la maschera dedicata ai tabacchi e ai
  prodotti da inalazione, con acquisizione dal venduto e adeguamento alle
  scorte.
- [Richieste offerta](richieste-offerta.md) — il documento con cui si chiede un
  preventivo al fornitore, e come diventa un ordine.

## Far scrivere gli ordini a Facile

- [Generazione degli ordini](generazione-ordini.md) — dagli ordini dei clienti,
  dal venduto dei punti vendita, e i DDT per gli ordini a centro servizi.
- [Riordino articoli con analisi prezzi](riordino-articoli.md) — il confronto
  fra più fornitori sullo stesso articolo, con il miglior prezzo in evidenza.

## Rileggere e scambiare

- [Stampe degli ordini](stampe-ordini.md) — per cliente, per fornitore, per
  articolo, più la situazione articoli.
- [Scambio degli ordini con l'esterno](scambio-ordini.md) — invio al server,
  ricezione da Facile Mobile, dal server FTP e da file.

## Le voci che usano le maschere dei documenti

| Voce di menu | Dove è descritta |
|---|---|
| **Gestione** | [Gestione documenti](../vendite/gestione-documenti.md) |
| **Inserimento**, **Modifica** | [Inserimento e Modifica documenti](../vendite/documento-di-vendita.md) |
| **Ristampa** | [Ristampa dei documenti](../vendite/ristampa-documenti.md) |
| **Fatturazione da Ordini** | [Emissione fatture da documenti](../vendite/emissione-fatture-da-documenti.md) |
| **Cancellazione Ordini Evasi** | [Ordini clienti](../vendite/ordini-clienti.md) |
| **Duplica**, **Esporta** | [Esportazione, duplicazione e ricezione](../vendite/esporta-duplica-documenti.md) |
| **Stampa Riepilogo** e **Stampa Riepilogo con Dettaglio Articoli e Commesse** | [Riepiloghi e statistiche](../vendite/riepiloghi-e-statistiche.md) |

!!! tip "Dal bisogno del cliente all'ordine al fornitore"

    1. Gli ordini dei clienti arrivano e si registrano, a mano o
       [dall'esterno](scambio-ordini.md).
    2. **Stampa Ordini per Articolo**, fra le [stampe](stampe-ordini.md), dice
       quanto è impegnato di ogni cosa.
    3. **Generazione Ordini a Fornitori da Ordini Clienti** scrive gli ordini
       corrispondenti; se i fornitori sono più d'uno e i prezzi contano, si
       passa dal [riordino con analisi prezzi](riordino-articoli.md).
    4. La merce arriva: gli ordini si chiudono da **Ordini in Ricezione** e con
       il [carico merci](../magazzino/carico-merci.md).
    5. Gli ordini dei clienti si evadono da **Ordini in Lavorazione**, che
       genera i documenti di vendita.

!!! note "Due menu per gli stessi ordini"

    Alcune voci degli ordini dei clienti compaiono anche sotto **Vendite ▸
    Ordini Clienti**: è lo stesso archivio e sono le stesse maschere, solo un
    sottoinsieme più breve a portata di mano di chi lavora nel menu Vendite.
