---
title: Giacenze e prezzi su Shopify
description: Come Facile calcola e invia a Shopify le disponibilità, i prezzi con promozioni e prezzi barrati, e il listino ingrosso per i clienti professionali.
modulo: E-commerce ▸ Shopify
---

# Giacenze e prezzi

L'operazione **982** invia le disponibilità, la **983** i prezzi e la
**991** il listino ingrosso per i clienti professionali. Tutte e tre
calcolano a ogni giro il valore atteso di ogni variante e mandano **solo
quelli diversi** dall'ultimo invio.

!!! info "In sintesi"

    - **Operazioni:** 982 giacenze (la 981 fa lo stesso), 983 prezzi, 991
      listino ingrosso
    - **Riguardano:** solo i prodotti già creati dall'operazione
      [prodotti](prodotti-e-immagini.md)
    - **Tipo di vendita:** chiave `modalita` — `B2C`, `B2B` o `MISTO`

---

## Le giacenze

La disponibilità di ogni variante si calcola così:

> **esistenza − ordinato clienti − impegnato**

sommando i depositi elencati nella chiave `depositi_disp` (per esempio
`depositi_disp = 1,17`). Il risultato si arrotonda all'unità per difetto e
non scende mai sotto zero.

La disponibilità inviata è **zero** quando:

- l'articolo non ha **Includi WEB**;
- il [marchio](../../magazzino/marchi.md) dell'articolo ha **Stock
  Ecommerce** impostato a non esporre le giacenze;
- nella versione taglie e colori, la combinazione non ha contatori nei
  depositi pubblicati.

Le giacenze vanno sull'**ubicazione** scelta durante la
[configurazione](installazione.md#4-lancia-la-configurazione). Si inviano a
blocchi di 250 varianti, e un giro senza variazioni dura pochi secondi anche
con migliaia di articoli.

Siccome l'ordinato clienti riduce la disponibilità, un ordine importato dal
sito abbassa la giacenza pubblicata già al giro successivo. Per questo
l'[esecuzione continua](ciclo.md) importa gli ordini prima di inviare le
giacenze.

## I prezzi

Il prezzo della variante dipende dalla chiave `modalita`:

| `modalita` | Prezzo | Prezzo barrato |
|---|---|---|
| `B2C` — negozio al pubblico | La promozione attiva oggi, se c'è; altrimenti il listino web (`listino_web`). | Il listino ufficiale (`listino_uff`), se è più alto del prezzo. |
| `MISTO` — pubblico e professionisti | Come `B2C`. I professionisti vedono il [listino ingrosso](#il-listino-ingrosso). | Come `B2C`. |
| `B2B` — solo professionisti | Il listino ingrosso (`listino_ing`). | Nessuno. |

Le regole:

- le **promozioni** sono quelle del listino web, valide oggi, nel deposito
  indicato dalla chiave `deposito`. Quando una promozione inizia o finisce,
  il prezzo cambia e viene inviato da solo, senza toccare l'articolo;
- un articolo con **Nascondi Prezzo WEB** nell'[anagrafica](../../anagrafiche/anagrafica-articoli.md)
  non riceve prezzi dal connettore;
- nella versione taglie e colori, se il listino ha un prezzo per la taglia,
  quel prezzo sostituisce quello dell'articolo e **non** riceve la
  promozione sopra;
- i prezzi si inviano con due decimali.

!!! note "Il prezzo alla creazione"

    Quando l'operazione prodotti crea un prodotto, gli dà il prezzo del
    listino web. Al primo giro dei prezzi viene quindi rimandato a tutti i
    prodotti il prezzo calcolato con le regole qui sopra: su qualche
    migliaio di articoli il primo giro dei prezzi dura alcuni minuti, i
    successivi pochi secondi.

## Il listino ingrosso

Con `modalita = MISTO`, l'operazione **991** prepara sul negozio la vendita
ai professionisti (se il piano del negozio la prevede: vedi
[I piani Shopify](index.md#i-piani-shopify)):

1. crea sul negozio un listino prezzi chiamato **Facile ingrosso**, nella
   valuta del negozio;
2. trasforma in **azienda** Shopify ogni cliente di Facile che ha come
   listino quello indicato in `listino_ing`, con un contatto che è la sua
   email;
3. raccoglie le aziende in un mercato dedicato, con il catalogo legato al
   listino;
4. invia per ogni variante il prezzo del listino ingrosso, solo quando è
   cambiato.

Un cliente sul listino ingrosso **senza email** non diventa azienda: il
registro lo segnala e lui continua a vedere i prezzi al pubblico. Compila
l'email nell'[anagrafica del cliente](../../anagrafiche/anagrafica-clienti.md)
e al giro successivo verrà aggiunto.

Con `modalita` diversa da `MISTO` l'operazione non fa niente e lo scrive nel
registro.

Se sul negozio vengono cancellati a mano il listino, il mercato o il
catalogo, la 991 li ricrea e rimanda tutti i prezzi ingrosso.

## Varianti cancellate sul negozio

Se una variante collegata non esiste più sul negozio, le operazioni giacenze,
prezzi e listino ingrosso non si bloccano: tolgono il collegamento,
proseguono con le altre varianti e lasciano all'operazione
[prodotti](prodotti-e-immagini.md#prodotti-cancellati-sul-negozio) il
compito di ricreare il prodotto.

## Messaggi principali

| Riga del registro | Che cosa significa |
|---|---|
| `Giacenze: N varianti collegate, N da inviare` | Quante disponibilità sono cambiate dall'ultimo giro. |
| `Fine sincronizzazione giacenze Shopify: inviate N - varianti sparite dal negozio N - errori N` | Il riepilogo delle giacenze. |
| `Ubicazione Shopify non configurata: lanciare prima la configurazione (988)` | Manca la configurazione del negozio. |
| `Prezzi: N varianti collegate, N da inviare (N prodotti), promozioni attive oggi: N` | Quanti prezzi sono cambiati e quante promozioni sono attive. |
| `Fine sincronizzazione prezzi Shopify: inviati N - varianti sparite dal negozio N - errori N` | Il riepilogo dei prezzi. |
| `Modalita' ...: il listino ingrosso B2B si usa solo con modalita = MISTO` | L'operazione 991 è stata lanciata con un'altra modalità. |
| `Cliente ... (...): senza email, non diventa azienda B2B` | Il cliente sul listino ingrosso non ha l'email. |
| `Fine listino ingrosso Shopify: aziende nuove N (clienti idonei N) - prezzi inviati N - errori N` | Il riepilogo del listino ingrosso. |

Gli altri messaggi sono in [Messaggi del registro](messaggi.md).

## Vedi anche

- [Marchi](../../magazzino/marchi.md)
- [Depositi](../../magazzino/depositi.md)
- [Listini di vendita](../../listini-vendita/index.md)
- [Il file di configurazione](configurazione.md)
