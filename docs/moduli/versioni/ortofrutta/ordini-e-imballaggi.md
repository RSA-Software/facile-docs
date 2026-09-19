---
title: Ordini cumulativi e imballaggi
description: La gestione degli ordini cumulativi delle catene, i fornitori preferiti per operatore e la movimentazione degli imballaggi.
modulo: Ortofrutta
maschera_id: IDD_ORT_ORDINI_SUPERMERCATI
---

# Ordini cumulativi e imballaggi

Tre voci che non riguardano la singola partita ma il contorno del lavoro: gli
ordini che arrivano dalle catene, le preferenze di chi compra, e il giro delle
cassette.

---

## Gestione Ordini Cumulativi

Una catena manda gli ordini dei suoi punti vendita, uno per negozio. Questa
maschera li **somma per articolo**, così si sa quanto va preparato in tutto, e
poi lascia decidere **da quale partita prendere** ogni quantità.

| Campo | Descrizione |
|---|---|
| **Cliente** | La catena di cui raccogliere gli ordini. |
| **Data Consegna** | Il giorno per cui la merce va consegnata. |

{: .campi }

Scelti cliente e data, la griglia si riempie con il totale per articolo:
**deposito**, **codice**, **descrizione**, **unità di misura**, **quantità** e
**colli**.

Su una riga, ++enter++ o un doppio clic aprono la **ripartizione per partita**
di quell'articolo: lì si dice quanto prendere da ciascuna partita disponibile.
È il passaggio che lega l'ordine della catena alla merce dei produttori, e
quindi che fa arrivare il ricavo alla partita giusta.

!!! tip "Prima si somma, poi si decide"

    L'utilità della maschera sta tutta in questo ordine: si guarda **il totale**
    di quello che serve per quella consegna e solo dopo si sceglie da dove
    prenderlo. Andando negozio per negozio si rischia di finire una partita a
    metà giro e doverne aprire un'altra per pochi colli.

## Fornitori Preferiti

Ogni operatore ha **i suoi produttori di riferimento, in ordine**. L'elenco
serve a proporre subito i soliti, senza cercarli ogni volta fra tutti.

| Campo | Descrizione |
|---|---|
| **Operatore** | L'[operatore](../../altre-tabelle/operatori.md) di cui si imposta l'elenco. |
| **Mostra solo fornitori preferiti** | Mostra nella griglia i soli preferiti invece di tutti. |

{: .campi }

| Pulsante | Tasto | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra l'elenco così com'è. |
| **F3 - Su** | ++f3++ | Sposta il fornitore in su di una posizione. |
| **F4 - Giù** | ++f4++ | Lo sposta in giù. |
| **F5 - Aggiungi** | ++f5++ | Apre l'elenco dei fornitori per sceglierne uno da aggiungere. |
| **F6 - Rimuovi** | ++f6++ | Toglie il fornitore dai preferiti, previa conferma. |
| **Esci** | ++esc++ | Chiude. |

**L'ordine conta**: è quello in cui i fornitori vengono proposti, e si cambia
con **F3** e **F4**. Un fornitore già in elenco non si aggiunge due volte: il
programma lo ignora senza dire niente.

La rimozione chiede *Confermi la rimozione del fornitore dai preferiti ?*, con
**No** preimpostato. Toglie la preferenza, non il fornitore dall'anagrafica.

## Movimentazione Imballaggi

Nell'ortofrutta gli imballi girano: cassette e pallet vanno al cliente con la
merce e devono tornare indietro. Questa stampa fa il conto di quel giro.

| Campo | Descrizione |
|---|---|
| **Dal**, **Al** | Il periodo. |
| **Tipo** | `TUTTI`, `CLIENTI` o `FORNITORI`. |
| **Cliente** / **Fornitore** | Compare **solo** scegliendo `CLIENTI` o `FORNITORI`, e cambia etichetta di conseguenza. Lasciandolo a zero vale per tutti. |

{: .campi }

Con `TUTTI` il campo sparisce del tutto: la stampa considera clienti e
fornitori insieme.

Produce la stampa **Movimentazione Imballaggi**.

!!! warning "Serve un reparto descritto esattamente IMBALLAGGI"

    La maschera riconosce gli imballi da un
    [reparto](../../magazzino/reparti.md) la cui descrizione è **esattamente**
    `IMBALLAGGI`. Se non c'è, all'apertura risponde

    *Reparto IMBALLAGGI non trovato in archivio !*

    e si chiude subito. Il codice del reparto non conta — conta la descrizione,
    quindi una sigla diversa o un'abbreviazione non vengono riconosciute.

## Vedi anche

- [Partite](partite.md)
- [Operatori](../../altre-tabelle/operatori.md)
- [Reparti](../../magazzino/reparti.md)
