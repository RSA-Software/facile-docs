---
title: Connettore PrestaShop
description: Come Facile manda a un negozio PrestaShop 1.6 clienti, categorie, prodotti, prezzi, giacenze e immagini, e ne importa gli ordini, attraverso FacileToWeb.
modulo: E-commerce
---

# Connettore PrestaShop

Il connettore PrestaShop collega Facile a un negozio **PrestaShop 1.6** usando
il webservice del negozio: con un'unica operazione manda al negozio tutto quello
che è cambiato, e con un'altra ne importa gli ordini.

!!! info "In sintesi"

    - **Programma:** [FacileToWeb](index.md), operazioni **900** (invio al negozio) e **901** (ordini)
    - **Collegamento:** il webservice di PrestaShop, con la sua chiave
    - **Licenza:** separata, in aggiunta a quella di Facile

---

!!! info "Licenza"

    Il connettore PrestaShop è soggetto a una **licenza separata**, in
    aggiunta a quella di Facile.

## Il collegamento

Sul negozio va abilitato il **webservice** di PrestaShop e creata una chiave,
con i permessi sulle risorse che Facile scrive (clienti, indirizzi, gruppi,
marchi, fornitori, categorie, prodotti, giacenze, prezzi specifici, immagini) e
sugli ordini.

!!! warning "Solo collegamento non cifrato"

    Il connettore si collega al negozio in `http` sulla porta 80: non c'è modo
    di usare `https`. La chiave del webservice viaggia quindi in chiaro. Tienine
    conto nella configurazione del negozio.

## Il file di configurazione

Oltre alle sezioni comuni descritte in [E-commerce](index.md#il-file-di-configurazione):

| Sezione | Chiave | Predefinito | Descrizione |
|---|---|---|---|
| `[COMMAND]` | `interval` | 0 | Il periodo da considerare, vedi più sotto. |
| `[ECOMMERCE]` | `web_host` | — | L'indirizzo del negozio. Obbligatorio. |
| `[ECOMMERCE]` | `api_path` | — | Il percorso del webservice, di solito `api`. Obbligatorio. |
| `[ECOMMERCE]` | `token` | — | La chiave del webservice. Obbligatoria. |
| `[ECOMMERCE]` | `listino` | 1 | Il listino del prezzo base dei prodotti. |
| `[ECOMMERCE]` | `euro` | 1 | La valuta euro sul negozio. |
| `[ECOMMERCE]` | `iva_22`, `iva_10`, `iva_04` | 1, 2, 3 | La regola fiscale del negozio per ciascuna aliquota. |
| `[ECOMMERCE]` | `deposito` | il deposito attivo della ditta | Il deposito da cui si prende l'ubicazione dell'articolo. |
| `[TAXONOMIES]` | `parent_id` | 1 | La categoria del negozio sotto cui creare le tassonomie. |
| `[TAXONOMIES]` | `root` | 1 | Se le tassonomie sono categorie principali. |
| `[TAXONOMIES]` | `home_id` | 0 | Se diverso da 0, una tassonomia non ancora sul negozio viene collegata a questa categoria invece di essere creata. |
| `[TAXONOMIES]` | `category_default` | 0 | La categoria predefinita dei prodotti che non hanno tassonomie. |
| `[OPTION]` | `exp_clienti` | 0 | `1` per mandare al negozio anche clienti e indirizzi. |
| `[DEBUG]` | `log_avanzamento`, `log_xml_before`, `log_xml_after` | 0 | Per l'assistenza: avanzamento nel registro e scambi salvati nella cartella `log`. |

Dalla [ditta](../anagrafiche/ditte.md), scheda **E-Commerce**, il connettore usa
anche il registro degli ordini, la categoria economica dei clienti nuovi e il
listino.

### Il periodo considerato

Le due operazioni lavorano solo su quello che è cambiato nel periodo indicato
da `interval`:

| `interval` | Periodo |
|---|---|
| `0` | Dall'ultima esecuzione riuscita, con un'ora e dieci minuti di margine. La prima volta: tutto per l'invio, dal 1° gennaio per gli ordini. |
| `1` | Da oggi |
| `2` | Gli ultimi 7 giorni |
| `3` | Gli ultimi 31 giorni |
| `4` | Dal 1° gennaio |
| `5` | Tutto |

L'ultima esecuzione si considera riuscita solo se tutto è andato a buon fine;
altrimenti al giro dopo si riparte dalla stessa data.

## L'invio al negozio (900)

Un'unica operazione manda, in quest'ordine, tutto quello che è cambiato:

1. **Gruppi:** i listini diventano gruppi di clienti.
2. **Clienti e indirizzi**, solo con `exp_clienti = 1`. Si mandano i clienti con
   un'email valida; un cliente cessato viene disattivato. Le destinazioni
   diverse diventano indirizzi del cliente.
3. **Marchi** e **fornitori**.
4. **Categorie:** le tassonomie e i loro elementi.
5. **Prodotti**, cioè gli articoli con **Includi WEB** o già sul negozio, con la
   loro **giacenza**:
    - nome, descrizioni e meta dai testi di [Impostazione Dati Web](../anagrafiche/impostazione-dati-web.md);
    - prezzo del listino `listino`, al netto dell'IVA; prezzo d'acquisto;
      regola fiscale secondo l'aliquota;
    - codice EAN dal codice articolo o dal primo codice a barre di 8 o 13 cifre;
    - attivo e acquistabile secondo **Includi WEB**; prezzo nascosto con
      **Nascondi Prezzo WEB**;
    - *nuovo* per 60 giorni dalla creazione;
    - categorie dalle tassonomie dell'articolo;
    - quantità: la disponibilità nei depositi pubblicati, arrotondata per eccesso.
6. **Prezzi specifici:** per ogni listino, il prezzo e lo sconto rispetto al
   netto. Un prezzo con netto a zero viene tolto dal negozio.
7. **Articoli collegati**.
8. **Immagini** degli articoli pubblicati.

Nella versione di Facile con le taglie e i colori si mandano anche taglie,
colori e combinazioni.

Se un singolo elemento viene rifiutato dal negozio, il registro lo riporta e
l'elemento viene ritentato al giro successivo; un errore di altro tipo
interrompe l'invio.

## Gli ordini (901)

- **Quali ordini:** quelli modificati sul negozio nel periodo indicato, di
  qualsiasi stato, non già importati.
- **Documento:** un ordine cliente sul registro degli ordini web della ditta,
  con il riferimento *ORDINE WEB N. … (…) del …*.
- **Cliente:** si cerca quello collegato al cliente del negozio, poi per email;
  se non c'è viene creato con i dati dell'indirizzo di fatturazione e il
  listino del suo gruppo. Un indirizzo di consegna diverso diventa una
  destinazione del cliente.
- **Righe:** l'articolo si ritrova dal suo codice; se non esiste la riga entra
  come descrittiva, con il codice e l'IVA predefinita della ditta. Seguono le
  righe di sconto, spese di trasporto e confezionamento.

<!-- DA VERIFICARE: la destinazione di consegna creata dall'importazione non viene collegata all'ordine (resta quella del titolare) -->

## Ripartire da capo: l'operazione 899

L'operazione **899** cancella in Facile tutti i collegamenti con il negozio —
clienti, destinazioni, tassonomie, articoli, listini, immagini, marchi,
fornitori — e segna tutto come modificato. Non tocca il negozio.

!!! warning "Dopo l'899 il negozio si ripopola"

    Al primo invio successivo Facile non riconosce più niente di quello che è
    sul negozio e ricrea tutto. Si usa solo quando il negozio è stato svuotato,
    o se ne sta collegando uno nuovo.

## Messaggi del registro

| Riga del registro | Che cosa significa |
|---|---|
| `Inizio Esportazione …` / `Fine Esportazione … - POST … - PUT … - DELETE … - ERROR … - SKIP … - TOTAL …` | Inizio e riepilogo di ogni parte dell'invio: elementi creati, aggiornati, tolti, in errore e saltati. |
| `POST -> Response Status Code = …` (anche `PUT`, `DELETE`), seguita da `XML Response` | Il negozio ha rifiutato un elemento; le righe seguenti dicono quale (`Cod. Articolo : …`, `Cod. Cliente : …` e simili) e perché. |
| `Carico Ordine …` | Un ordine sta entrando. |
| `Salto Ordine … (già trovato in archivio)` | L'ordine era già stato importato. |
| `Salto Ordine … (Anno ordine diverso da anno attivo)` | L'ordine è di un altro anno. |
| `xml.FindChild("…"); return NULL pointer!` | Nella risposta del negozio manca un dato atteso. |

## Vedi anche

- [E-commerce](index.md)
- [Impostazione Dati Web](../anagrafiche/impostazione-dati-web.md)
- [Ditte](../anagrafiche/ditte.md)
