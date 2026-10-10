---
title: Prodotti e immagini su Shopify
description: Quali articoli di Facile diventano prodotti Shopify, con quali dati, come nascono le collezioni dalle tassonomie e come si inviano le fotografie.
modulo: E-commerce ▸ Shopify
---

# Prodotti e immagini

L'operazione **984** crea e aggiorna sul negozio i prodotti e le collezioni;
l'operazione **985** invia le fotografie. Tutte e due mandano solo quello che
è nuovo o cambiato dall'ultimo invio.

!!! info "In sintesi"

    - **Operazioni:** 984 prodotti e collezioni, 985 immagini
    - **Si pubblica:** l'articolo con **Includi WEB** attivo
    - **Si toglie dal sito:** togliendo **Includi WEB** — il prodotto passa
      in bozza, non viene cancellato

---

## Quali articoli vanno sul negozio

La 984 considera:

- gli articoli con **Includi WEB** attivo che non sono ancora sul negozio:
  li **crea**;
- gli articoli già collegati a un prodotto, che **aggiorna** quando è
  cambiato qualcosa dall'ultimo invio.

Un articolo viene rimandato quando:

- è stato modificato in Facile;
- è stata modificata la descrizione del suo **marchio**, della sua
  **stagione**, del suo **reparto** o della sua **categoria merceologica**;
- nella versione taglie e colori, ha una taglia o un colore nuovi;
- hai cambiato nel file di configurazione il modo di compilare il tipo di
  prodotto o l'elenco delle sigle (vedi più sotto): in quel caso si rimandano
  **tutti** i prodotti, una volta.

Un articolo collegato a cui togli **Includi WEB** resta sul negozio ma passa
**in bozza**: i clienti non lo vedono più, e lo storico degli ordini non si
perde.

## Che cosa si invia

| Sul negozio | Da Facile |
|---|---|
| **Titolo** | **Web Nome**; se è vuoto, le due righe di descrizione dell'articolo. |
| **Descrizione** | **Web Des. Estesa**; se è vuota, **Web Des. Breve**; se sono vuote tutte e due, il titolo. Un testo già formattato si invia così com'è; un testo semplice mantiene gli a capo. |
| **Fornitore** | Il marchio dell'articolo. |
| **Stato** | *Attivo* con **Includi WEB**, *Bozza* senza. |
| **Tipo di prodotto** | La categoria merceologica, se lo chiedi (vedi [Tipo di prodotto](#tipo-di-prodotto)). |
| **SKU** | Il codice dell'articolo. Per le taglie e colori, un codice EAN-13 (vedi [Taglie e colori](#taglie-e-colori)). |
| **Peso** | Il peso dell'articolo, convertito in chilogrammi dalla sua unità di misura (grammi, ettogrammi, quintali, tonnellate). |
| **Giacenza** | Il prodotto viene impostato per tenere conto delle quantità; le quantità le manda l'operazione [giacenze](giacenze-e-prezzi.md). |
| **Prezzo** | Solo quando il prodotto viene **creato**. Da lì in avanti lo aggiorna l'operazione [prezzi](giacenze-e-prezzi.md#i-prezzi). |
| **Collezioni** | Le tassonomie dell'articolo (vedi [Le collezioni](#le-collezioni)). |
| Campi aggiuntivi **facile.codice**, **facile.categoria**, **facile.reparto**, **facile.stagione** | Il codice dell'articolo e le descrizioni di categoria merceologica, reparto e stagione. Il tema del negozio li può mostrare o usare nei filtri. |

### Le descrizioni in forma leggibile

In Facile categorie merceologiche, reparti e stagioni sono scritti in
maiuscolo. Sul negozio arrivano in forma leggibile:

| In Facile | Sul negozio |
|---|---|
| STRUMENTI DI SCRITTURA | Strumenti di Scrittura |
| ABBIGLIAMENTO DELL'UOMO | Abbigliamento dell'Uomo |
| T-SHIRT | T-Shirt |
| TAGLIA XL | Taglia XL |
| 25X35 | 25X35 |

Le regole:

- ogni parola comincia con la maiuscola e prosegue in minuscolo;
- articoli, preposizioni e congiunzioni (*di*, *da*, *e*, *della*, *per*…)
  restano minuscoli, salvo all'inizio;
- le sigle senza vocali (XL, PVC) e le parole con delle cifre (3D, 25X35)
  restano come sono;
- un testo che contiene già delle minuscole non viene toccato: chi l'ha
  scritto così l'ha fatto apposta.

Una sigla con delle vocali, come **USB** o **LED**, diventerebbe «Usb» o
«Led»: elencala nella chiave `sigle` del file di configurazione e resterà
maiuscola.

### Tipo di prodotto

Con `tipo_prodotto = 1` la categoria merceologica dell'articolo, in forma
leggibile, diventa anche il **tipo di prodotto** di Shopify, che il negozio
usa per filtri, ricerche e collezioni automatiche.

- Se l'articolo non ha la categoria merceologica, il tipo resta quello
  impostato sul negozio.
- Con `tipo_prodotto = 0` Facile non tocca il tipo di prodotto, che puoi
  gestire a mano sul negozio.

## Le collezioni

Le collezioni del negozio nascono dalle **tassonomie** di Facile, quelle che
si spuntano in [Impostazione Dati Web](../../anagrafiche/impostazione-dati-web.md#le-tassonomie):

- ogni tassonomia e ogni suo elemento diventano una collezione, con lo stesso
  nome;
- un prodotto entra nella collezione dell'elemento spuntato, in quelle degli
  elementi che lo contengono e in quella della tassonomia;
- una tassonomia o un elemento rinominati aggiornano la collezione;
- una tassonomia o un elemento disattivati tolgono la collezione dal
  negozio.

<!-- DA VERIFICARE: l'etichetta a video con cui si disattiva una tassonomia o un elemento -->

Le collezioni nuove vengono pubblicate sul canale indicato nella
configurazione, come i prodotti nuovi.

Le **collezioni create a mano** sul negozio restano: Facile aggiunge e toglie
solo le collezioni che vengono dalle sue tassonomie.

## Taglie e colori

Nella versione di Facile con le taglie e colori, un articolo a taglie
diventa **un solo prodotto con una variante per ogni combinazione** di
taglia e colore:

- si pubblicano le combinazioni che hanno movimenti nei depositi indicati in
  `depositi_disp`;
- le due opzioni del prodotto si chiamano *Taglia* e *Colore*, oppure come
  indicato nella sezione `[TAGLIECOL]`;
- lo **SKU** di ogni variante è un codice EAN-13 formato dal codice
  dell'articolo, dalla taglia e dal colore, più la cifra di controllo; per
  questo il codice dell'articolo deve essere di **6 cifre**;
- il **codice a barre** della variante è quello registrato in Facile per la
  combinazione, oppure lo stesso SKU;
- quando nasce una taglia o un colore nuovi, il prodotto viene rimandato con
  la variante in più; le combinazioni che non ci sono più vengono tolte.

Un articolo a taglie con un codice che non è di 6 cifre, o senza nessuna
combinazione pubblicabile, non viene inviato e il registro lo dice.

## Prodotti cancellati sul negozio

Con `verifica_spariti = 1` (il valore predefinito), a ogni giro la 984
controlla che prodotti e collezioni collegati esistano ancora sul negozio.
Quelli cancellati a mano vengono **ricreati**, finché in Facile l'articolo
resta pubblicabile. Il controllo costa poco, una richiesta ogni 250 oggetti.

## Le immagini

L'operazione **985** manda sul negozio le fotografie degli articoli
collegati:

- si inviano le immagini a grandezza piena dell'articolo, non le miniature;
- ogni immagine viene ridimensionata a **1024 pixel** sul lato più lungo e
  convertita in JPEG;
- quando un'immagine di un articolo cambia, la galleria del prodotto viene
  rifatta per intero, nell'ordine delle immagini di Facile;
- le fotografie aggiunte a mano sul negozio restano.

È l'operazione più lenta: conviene farla girare a intervalli lunghi, per
esempio una volta al giorno (vedi [Esecuzione continua](ciclo.md)).

## Messaggi principali

| Riga del registro | Che cosa significa |
|---|---|
| `Prodotti da inviare: N` | Quanti articoli sono nuovi o cambiati in questo giro. |
| `Fine sincronizzazione prodotti Shopify: articoli N - nuovi N - aggiornati N - errori N` | Il riepilogo del giro. |
| `Formato dei prodotti cambiato (...): N prodotti collegati da rimandare` | Hai cambiato `tipo_prodotto` o `sigle`: tutti i prodotti si rimandano una volta. |
| `Articolo ... a taglie e colori senza combinazioni pubblicabili: non inviato` | Nessuna combinazione di taglia e colore ha movimenti nei depositi pubblicati. |
| `Articolo ...: il codice non da' uno SKU EAN-13 di variante (servono 6 cifre): non inviato` | Il codice dell'articolo a taglie non è di 6 cifre. |
| `Articolo ...: il prodotto ... non c'e' piu' su Shopify, lo si ricrea` | Il prodotto era stato cancellato sul negozio. |
| `Fine sincronizzazione immagini Shopify: articoli N - immagini N - errori N` | Il riepilogo delle immagini. |
| `Articolo ...: immagine formato N illeggibile, saltata` | Un'immagine dell'articolo è danneggiata: ricaricala in Facile. |

Gli altri messaggi sono in [Messaggi del registro](messaggi.md).

## Vedi anche

- [Impostazione Dati Web](../../anagrafiche/impostazione-dati-web.md)
- [Marchi](../../magazzino/marchi.md), [Stagioni](../../magazzino/stagioni.md),
  [Reparti](../../magazzino/reparti.md),
  [Categorie merceologiche](../../magazzino/categorie-merceologiche.md)
- [Giacenze e prezzi](giacenze-e-prezzi.md)
- [Il file di configurazione](configurazione.md)
