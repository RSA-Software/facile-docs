---
title: Connettore Shopify
description: Cosa scambiano Facile e un negozio Shopify, le operazioni del connettore, i requisiti del negozio e i dati che Facile non tocca.
modulo: E-commerce ▸ Shopify
---

# Connettore Shopify

Il connettore Shopify tiene allineato un negozio Shopify con Facile: pubblica
gli articoli con le loro fotografie e categorie, ne aggiorna giacenze e
prezzi, e importa in Facile gli ordini dei clienti del sito.

!!! info "In sintesi"

    - **Programma:** [FacileToWeb](../index.md)
    - **Configurazione:** un file `.ini`, descritto in
      [Il file di configurazione](configurazione.md)
    - **Prima volta:** [Prima installazione](installazione.md)
    - **Uso quotidiano:** [Esecuzione continua](ciclo.md), che fa tutte le
      operazioni a giri

---

## A cosa serve

Una volta preparati gli articoli in Facile, il negozio si alimenta da solo:

| Verso | Che cosa | Pagina |
|---|---|---|
| Facile ▸ Shopify | Prodotti: nome, descrizione, marchio, peso, categorie del catalogo, taglie e colori | [Prodotti e immagini](prodotti-e-immagini.md) |
| Facile ▸ Shopify | Fotografie degli articoli | [Prodotti e immagini](prodotti-e-immagini.md#le-immagini) |
| Facile ▸ Shopify | Giacenze disponibili | [Giacenze e prezzi](giacenze-e-prezzi.md) |
| Facile ▸ Shopify | Prezzi, prezzi barrati e promozioni | [Giacenze e prezzi](giacenze-e-prezzi.md#i-prezzi) |
| Facile ▸ Shopify | Listino ingrosso per i clienti professionali | [Giacenze e prezzi](giacenze-e-prezzi.md#il-listino-ingrosso) |
| Shopify ▸ Facile | Ordini dei clienti del sito, con clienti e indirizzi di spedizione | [Ordini](ordini.md) |
| Facile ▸ Shopify | Ordini evasi o annullati in Facile | [Ordini](ordini.md#comunicare-a-shopify-gli-ordini-evasi-o-annullati) |

Ogni invio manda **solo quello che è cambiato** dall'ultima volta: un giro
in cui non è cambiato niente dura pochi secondi anche con migliaia di
articoli.

## Le operazioni

| Numero | Operazione | Che cosa fa | Quando |
|---|---|---|---|
| 988 | Configurazione | Controlla i permessi dell'app sul negozio, sceglie l'ubicazione delle giacenze e il canale di vendita, prepara il negozio a riconoscere gli articoli di Facile. | All'installazione, e quando cambia l'app o l'ubicazione. |
| 987 | Abbinamento | Collega agli articoli di Facile i prodotti già presenti sul negozio. | Una volta, se il negozio aveva già un catalogo. |
| 984 | Prodotti | Crea e aggiorna prodotti e collezioni. | A ogni giro, o a intervalli. |
| 985 | Immagini | Invia le fotografie degli articoli nuove o cambiate. | A intervalli più lunghi: è l'operazione più lenta. |
| 982 | Giacenze | Invia le disponibilità cambiate. La 981 fa la stessa cosa. | A ogni giro. |
| 983 | Prezzi | Invia i prezzi cambiati, comprese le promozioni che iniziano o finiscono. | A ogni giro. |
| 991 | Listino ingrosso | Crea le aziende clienti e invia i prezzi del listino ingrosso. | Solo con la vendita ai professionisti. |
| 980 | Ordini | Importa gli ordini nuovi del sito. | A ogni giro. |
| 990 | Stato degli ordini | Comunica a Shopify gli ordini evasi o annullati in Facile. | A ogni giro, se attivata. |
| 979 | Esecuzione continua | Esegue le operazioni scelte, una dopo l'altra, poi aspetta e ricomincia. | Sempre accesa. |

## Requisiti

### Il negozio

Serve un negozio Shopify e, al suo interno, un'**app personalizzata** che dà
a Facile l'accesso al negozio. L'app si crea dall'amministrazione del
negozio ed è descritta in [Prima installazione](installazione.md#1-crea-lapp-sul-negozio).

All'app servono questi permessi:

- prodotti, in lettura e scrittura;
- magazzino, in lettura e scrittura;
- ubicazioni, in lettura;
- ordini, in lettura e scrittura;
- clienti, in lettura;
- file, in lettura e scrittura;
- evasioni gestite dal commerciante, in lettura e scrittura.

La [configurazione](installazione.md#4-lancia-la-configurazione) controlla i
permessi e scrive nel registro quelli che mancano.

### La versione dei dati di Shopify

Shopify pubblica una nuova versione del suo sistema di scambio dati ogni tre
mesi e ritira le vecchie dopo circa un anno. Il connettore usa la versione
indicata nel file di configurazione (`api_version`, oggi `2026-10`). Quando
Shopify annuncia il ritiro della versione in uso, il connettore va
aggiornato insieme a Facile.

### I limiti dei piani Shopify

| Piano | Effetto sul connettore |
|---|---|
| **Basic** | Negli ordini Shopify non fornisce né nome, né email, né indirizzi del cliente. Gli ordini entrano lo stesso, intestati a un [cliente generico](ordini.md#a-quale-cliente-va-lordine). |
| Tutti | Il connettore assegna i prezzi ingrosso alle aziende attraverso un mercato dedicato. È il metodo che non richiede il piano Plus. |

<!-- DA VERIFICARE: da quale piano Shopify mette a disposizione le aziende B2B (prova fatta solo sul negozio di sviluppo) -->

## Come Facile riconosce i propri prodotti

Per ogni oggetto che crea sul negozio — prodotto, variante, collezione,
fotografia, ordine — Facile ricorda il collegamento con l'articolo, la
categoria o il documento da cui viene. Inoltre ogni prodotto porta il codice
dell'articolo di Facile in un suo campo aggiuntivo (**facile.codice**), e
ogni variante ha come **SKU** il codice dell'articolo. Grazie a questo:

- un articolo modificato aggiorna il **suo** prodotto, non ne crea un altro;
- un ordine del sito ritrova l'articolo di Facile riga per riga;
- un catalogo già presente sul negozio si può
  [abbinare](installazione.md#5-abbina-il-catalogo-gia-presente) agli
  articoli senza ricaricarlo.

## I dati che Facile non tocca

Facile aggiorna solo i dati che gestisce. Sul prodotto restano come li hai
lasciati sul negozio:

- le **collezioni manuali** create sul negozio, anche quando Facile aggiorna
  le collezioni che vengono dalle sue categorie;
- i **tag**, i dati per i motori di ricerca, i campi aggiuntivi diversi da
  quelli di Facile;
- le **fotografie aggiunte a mano** sul negozio;
- il **tipo di prodotto**, a meno che tu non chieda a Facile di
  [compilarlo](prodotti-e-immagini.md#tipo-di-prodotto) con la categoria
  merceologica.

Vengono invece riscritti a ogni aggiornamento, perché il dato è di Facile:
nome, descrizione, marchio, stato (attivo o bozza), SKU, peso e collezioni
delle categorie di Facile.

!!! warning "Cosa succede se cancelli un prodotto sul negozio"

    Un prodotto, una variante, una collezione o un listino ingrosso
    cancellato a mano sul negozio **viene ricreato** al giro successivo,
    finché in Facile l'articolo resta pubblicabile. Per togliere un
    articolo dal sito, togli **Includi WEB** in Facile: il prodotto passa
    in bozza e smette di essere visibile.

## Vedi anche

- [Prima installazione](installazione.md)
- [Il file di configurazione](configurazione.md)
- [Messaggi del registro](messaggi.md)
- [E-commerce: avvio e registro di FacileToWeb](../index.md)
