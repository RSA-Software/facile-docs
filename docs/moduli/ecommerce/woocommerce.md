---
title: Connettore WooCommerce
description: Come Facile scambia ordini, giacenze, prezzi, prezzi all'ingrosso, prodotti e immagini con un negozio WooCommerce attraverso FacileToWeb.
modulo: E-commerce
---

# Connettore WooCommerce

Il connettore WooCommerce collega Facile a un negozio **WooCommerce**
(WordPress): manda al negozio categorie, attributi, prodotti, immagini,
giacenze e prezzi, e porta in Facile gli ordini dei clienti del sito.

!!! info "In sintesi"

    - **Programma:** [FacileToWeb](index.md), operazioni **930**-**936**
    - **Collegamento:** il sistema di scambio dati REST di WooCommerce, con le chiavi *consumer key* e *consumer secret*
    - **Licenza:** separata, in aggiunta a quella di Facile

---

!!! info "Licenza"

    Il connettore WooCommerce è soggetto a una **licenza separata**, in
    aggiunta a quella di Facile.

## Le operazioni

| Numero | Operazione | Direzione | Che cosa fa |
|---|---|---|---|
| 934 | Prodotti | Facile ▸ negozio | Crea categorie e attributi mancanti, crea gli articoli nuovi e aggiorna quelli cambiati. |
| 935 | Immagini | Facile ▸ negozio | Carica nella libreria di WordPress le immagini nuove o cambiate. |
| 932 | Giacenze | Facile ▸ negozio | Manda le disponibilità cambiate. |
| 933 | Prezzi | Facile ▸ negozio | Manda prezzi e promozioni cambiati. |
| 936 | Prezzi all'ingrosso | Facile ▸ negozio | Manda i prezzi del listino ingrosso ai gruppi di clienti professionali. |
| 931 | Azzeramento giacenze | Facile ▸ negozio | Mette a zero e *non disponibile* gli articoli pubblicati che nei depositi indicati non hanno contatori nell'anno. |
| 930 | Ordini | negozio ▸ Facile | Importa gli ordini come ordini cliente. |

Ogni operazione ha il suo file di configurazione con il numero in `operation`,
e si pianifica come descritto in [E-commerce](index.md#come-si-avvia).

## Il collegamento

Sul negozio va creata una **chiave del sistema di scambio dati** di
WooCommerce, con permessi di lettura e scrittura: *consumer key* e *consumer
secret* vanno nelle chiavi `api_key` e `api_secret`. Il percorso è di solito
`wp-json/wc/v3`.

- Le **immagini** si caricano nella libreria di WordPress (`wp-json/wp/v2`):
  servono credenziali di WordPress con i permessi sui media.
- I **prezzi all'ingrosso** usano il percorso `wp-json/wholesale/v1` di
  un'estensione per la vendita all'ingrosso, che va installata sul negozio.

<!-- DA VERIFICARE: quale estensione del negozio espone wp-json/wholesale/v1, e quali credenziali WordPress servono per le immagini -->

## Il file di configurazione

Oltre alle sezioni comuni descritte in [E-commerce](index.md#il-file-di-configurazione):

| Sezione | Chiave | Predefinito | Usata da | Descrizione |
|---|---|---|---|---|
| `[ECOMMERCE]` | `web_host` | — | tutte | L'indirizzo del negozio. |
| `[ECOMMERCE]` | `api_path` | — | tutte | Il percorso del sistema di scambio dati, di solito `wp-json/wc/v3`. |
| `[ECOMMERCE]` | `api_key`, `api_secret` | — | tutte | *Consumer key* e *consumer secret*. |
| `[ECOMMERCE]` | `port` | 80 | tutte | La porta del negozio. |
| `[ECOMMERCE]` | `ssl` | 0 | tutte | `1` per il collegamento cifrato (https). |
| `[ECOMMERCE]` | `on_url` | 0 | 931-936 | `1` per passare le chiavi nell'indirizzo invece che con la firma della richiesta. |
| `[ECOMMERCE]` | `depositi_disp` | 1 | 931, 932 | I depositi sommati per la disponibilità, separati da virgole. |
| `[ECOMMERCE]` | `listino_uff` | 1 | 933, 934 | Il listino del prezzo pieno. |
| `[ECOMMERCE]` | `listino_web` | 1 | 933 | Il listino del prezzo di vendita. |
| `[ECOMMERCE]` | `listino_ing` | 1 | 936 | Il listino all'ingrosso. |
| `[ECOMMERCE]` | `b2b_id` | 0 | 933 | Il gruppo di clienti di un'estensione B2B: con un valore diverso da 0 i prezzi vanno a quel gruppo. |
| `[ECOMMERCE]` | `deposito` | il deposito attivo della ditta | 930, 933 | Il deposito delle righe degli ordini e delle promozioni. |
| `[ECOMMERCE]` | `registro` | vuoto | 930 | Il registro degli ordini importati. |
| `[ECOMMERCE]` | `pagamento`, `cateco` | 0 | 930 | Pagamento e categoria economica dei clienti. |
| `[ARTICOLI]` | `cod_buono_sco`, `cod_spese_tra` | — | 930 | Gli articoli delle righe di sconto e commissioni e di quelle delle spese di trasporto. Se mancano si usano gli articoli `SCONTO` e `TRASPORTO`. |
| `[STATO]` | `ultimo_import` | — | 930 | Data e ora dell'ultima importazione riuscita. **La scrive Facile**: serve a `interval = 0`. |
| `[OPTIONS]` | `GRUPPO_0000` … `GRUPPO_0099` | — | 936 | I nomi dei gruppi all'ingrosso sul negozio. |
| `[OPTIONS]` | `tags` | 0 | 934 | Diverso da 0: le stagioni diventano tag del prodotto. |
| `[OPTIONS]` | `backorders` | `no` | 934 | Se accettare ordini di articoli esauriti: `yes`, `notify` o `no`. |
| `[STATI]` | *stato dell'ordine* | 0 | 930 | `1` per importare gli ordini in quello stato (per esempio `processing = 1`). |
| `[PAGAMENTI]` | `pag_` + *metodo di pagamento* | 0 | 930 | Il pagamento di Facile per quel metodo, per esempio `pag_bacs`. |
| `[COMMAND]` | `interval` | 0 | 930 | Il periodo degli ordini da rileggere, vedi più sotto. |
| `[DEBUG]` | `log_json`, `log_json_orders`, `log_json_order` | 0 | — | Per l'assistenza: salvano nella cartella `log` le richieste e le risposte. |

## Prodotti, categorie e immagini

- **Categorie e attributi (934):** le tassonomie e i loro elementi diventano
  categorie; marchi, stagioni, reparti e le tabelle aggiuntive diventano
  attributi del prodotto, creati sul negozio se mancano.
- **Articoli nuovi (934):** si creano gli articoli con **Includi WEB** non
  ancora collegati, con nome, codice, prezzo del listino `listino_uff`, peso in
  chilogrammi e descrizioni, inizialmente *non disponibili*: la quantità arriva
  con l'operazione giacenze. Se un prodotto con lo stesso codice esiste già sul
  negozio, l'articolo viene collegato a quello.
- **Articoli cambiati (934):** si aggiornano nome, descrizioni, prezzo, peso,
  categorie con tutti i livelli superiori, attributi, codici a barre, articoli
  collegati e alternativi, immagini già caricate. Un articolo che perde
  **Includi WEB** passa in bozza e non disponibile, senza essere cancellato.
- **Immagini (935):** si caricano le immagini a grandezza piena, ridimensionate
  a 1024 pixel e convertite in JPEG. L'aggancio al prodotto lo fa la successiva
  operazione prodotti. Un'immagine cambiata viene tolta dal negozio e ricaricata
  al giro successivo.

## Giacenze e prezzi

- **Giacenze (932):** per gli articoli pubblicati, la somma di
  *esistenza − ordinato clienti − impegnato* nei depositi `depositi_disp`. Si
  manda solo se è diversa da quella del negozio. Con meno di una unità, con
  **Includi WEB** spento o con un [marchio](../magazzino/marchi.md) che ha
  **Stock Ecommerce** impostato a non esporre le giacenze, il prodotto risulta
  non disponibile.
- **Prezzi (933):** il prezzo pieno è il maggiore fra il listino `listino_uff`
  e il listino web. Il prezzo scontato è quello della promozione attiva, con le
  sue date, altrimenti quello del listino web. Un articolo con **Nascondi Prezzo
  WEB** viene mandato senza prezzi. Gli articoli in promozione vengono rimandati
  ogni giorno.
- **Prezzi all'ingrosso (936):** il prezzo del listino `listino_ing`, lo stesso
  per tutti i gruppi elencati in `[OPTIONS]`.

## Gli ordini

| `interval` | Ordini riletti |
|---|---|
| `0` | Dall'ultima importazione riuscita, con un'ora e dieci minuti di margine; la prima volta dal 1° gennaio dell'esercizio |
| `1` | Di oggi |
| `2` | Degli ultimi 7 giorni |
| `3` | Degli ultimi 31 giorni |
| `4` | Dal 1° gennaio dell'esercizio |
| `5` | Tutti |

Il negozio restituisce gli ordini a pagine di cento: Facile le legge tutte.
L'importazione si considera riuscita solo se tutti gli ordini sono entrati;
altrimenti con `interval = 0` il giro dopo riparte dalla stessa data.

- **Quali ordini:** quelli negli stati accesi in `[STATI]`, creati nell'anno
  dell'esercizio della ditta e non già importati.
- **Cliente:** si cerca il cliente collegato al cliente del negozio, poi per
  email; se non c'è viene creato dai dati di **fatturazione**, come persona
  giuridica se c'è l'azienda. Se esiste, i suoi dati vengono **aggiornati** con
  quelli dell'ordine. Tutto in maiuscolo.
- **Destinazione:** dall'indirizzo di spedizione; da quello di fatturazione se
  la spedizione è vuota. Se il cliente ha già una destinazione uguale, si usa
  quella.
- **Righe:** l'articolo si ritrova dal codice (SKU); se non esiste la riga entra
  come descrittiva, con lo SKU e l'IVA predefinita della ditta. Il prezzo è
  quello **prima dello sconto**.
- **Sconto:** una riga in negativo con lo sconto dell'ordine, sull'articolo
  `cod_buono_sco`. Le commissioni del negozio entrano sullo stesso articolo,
  ciascuna con il suo nome.
- **Spese di trasporto:** una riga sull'articolo `cod_spese_tra`. Con i prezzi
  IVA esclusa la riga è netta e l'IVA la calcola Facile.

Se nella sezione `[ARTICOLI]` mancano `cod_buono_sco` o `cod_spese_tra`, si
usano gli articoli **`SCONTO`** e **`TRASPORTO`**; se non esistono nemmeno quelli,
la riga entra descrittiva con l'IVA predefinita della ditta, così il totale
dell'ordine torna comunque. Se le righe non arrivano al totale del negozio, il
registro lo segnala.

## Messaggi del registro

| Riga del registro | Che cosa significa |
|---|---|
| `Salto Ordine … (anno esercizio diverso)` | L'ordine è di un altro anno. |
| `Salto Ordine … (già trovato in archivio)` | L'ordine era già stato importato. |
| `ORDER KEY - ordine non trovato` | Un ordine del negozio non ha il suo identificativo: l'importazione si ferma. |
| `Ordine … : le righe differiscono dal totale del negozio di …` | Le righe importate non arrivano al totale dell'ordine sul negozio, per arrotondamenti o per voci che Facile non conosce: controlla l'ordine in Facile. |
| `Codice articolo per spese di trasporto (cod_spese_tra) non impostato nel file di configurazione!` (e gli analoghi) | Manca una chiave della sezione `[ARTICOLI]`. |
| `Articolo … : Nessuna risposta dal server` | Il negozio non ha risposto. |
| `Impossibile aggiornare Art. … : …` | Il negozio ha rifiutato l'aggiornamento di un prodotto; segue il motivo. |
| `Impossibile aggiornare Art. … - Disp. …` / `Impossibile aggiornare Art. … - Prezzo …` | Il negozio ha rifiutato la disponibilità o il prezzo. |
| `Errore Tassonomia … : …`, `Errore Marchio … : …` e simili | Il negozio ha rifiutato una categoria o un attributo. |
| `Impossibile determinare il tipo di file` | Un'immagine dell'articolo non è leggibile: l'invio delle immagini si ferma. |

## Vedi anche

- [E-commerce](index.md)
- [Impostazione Dati Web](../anagrafiche/impostazione-dati-web.md)
- [Marchi](../magazzino/marchi.md)
