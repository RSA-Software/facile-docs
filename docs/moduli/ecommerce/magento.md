---
title: Connettore Magento
description: Come Facile scambia ordini, giacenze, prezzi, prodotti, categorie e immagini con un negozio Magento 2 attraverso FacileToWeb.
modulo: E-commerce
---

# Connettore Magento

Il connettore Magento collega Facile a un negozio **Magento 2**: manda al
negozio categorie, prodotti, immagini, disponibilità e prezzi, e porta in Facile
gli ordini dei clienti del sito.

!!! info "In sintesi"

    - **Programma:** [FacileToWeb](index.md), operazioni **918**, **921**-**926**
    - **Collegamento:** il sistema di scambio dati REST di Magento 2, con un token
    - **Licenza:** separata, in aggiunta a quella di Facile

---

!!! info "Licenza"

    Il connettore Magento è soggetto a una **licenza separata**, in aggiunta a
    quella di Facile.

## Le operazioni

| Numero | Operazione | Direzione | Che cosa fa |
|---|---|---|---|
| 921 | Collegamento al catalogo esistente | negozio ▸ Facile | Per un negozio che ha già categorie, marchi e immagini: collega tassonomie, marchi e immagini di Facile a quelli del negozio, così gli invii successivi aggiornano invece di creare doppioni. Non importa altri dati. |
| 924 | Prodotti e categorie | Facile ▸ negozio | Aggiorna le categorie, crea gli articoli nuovi e aggiorna i dati di quelli già presenti. |
| 925 | Immagini | Facile ▸ negozio | Manda le immagini nuove o cambiate. |
| 922 | Disponibilità | Facile ▸ negozio | Manda le disponibilità cambiate. |
| 923 | Prezzi | Facile ▸ negozio | Manda prezzi e offerte. |
| 926 | Azzeramento disponibilità | Facile ▸ negozio | Mette a zero la disponibilità degli articoli pubblicati che nei depositi indicati non hanno contatori nell'anno, per esempio a inizio anno. |
| 918 | Ordini | negozio ▸ Facile | Importa gli ordini nuovi come ordini cliente. |

Ogni operazione ha il suo file di configurazione con il numero in `operation`,
e si pianifica come descritto in [E-commerce](index.md#come-si-avvia).

## Il file di configurazione

Oltre alle sezioni comuni descritte in [E-commerce](index.md#il-file-di-configurazione):

| Sezione | Chiave | Predefinito | Usata da | Descrizione |
|---|---|---|---|---|
| `[ECOMMERCE]` | `web_host` | — | tutte | L'indirizzo del negozio. |
| `[ECOMMERCE]` | `api_path` | — | tutte | Il percorso del sistema di scambio dati, di solito `rest/V1`. |
| `[ECOMMERCE]` | `token` | — | tutte | Il token di accesso creato sul negozio. |
| `[ECOMMERCE]` | `port` | 80 | tutte | La porta del negozio. |
| `[ECOMMERCE]` | `ssl` | 0 | tutte | `1` per il collegamento cifrato (https). |
| `[ECOMMERCE]` | `depositi_disp` | 1 | 922, 926 | I depositi sommati per la disponibilità, separati da virgole. |
| `[ECOMMERCE]` | `listino_uff` | 1 | 923, 924 | Il listino del prezzo pieno. |
| `[ECOMMERCE]` | `listino_web` | 1 | 923 | Il listino del prezzo di vendita sul sito. |
| `[ECOMMERCE]` | `deposito` | il deposito attivo della ditta | 918, 923 | Il deposito delle righe degli ordini e delle promozioni. |
| `[ECOMMERCE]` | `registro` | vuoto | 918 | Il registro degli ordini importati. |
| `[ECOMMERCE]` | `pagamento` | 0 | 918 | Il pagamento predefinito degli ordini e dei clienti nuovi. |
| `[ECOMMERCE]` | `agente` | 0 | 918 | L'agente degli ordini importati. |
| `[ECOMMERCE]` | `cateco` | 0 | 918 | La categoria economica dei clienti nuovi. |
| `[ECOMMERCE]` | `spese_pag_contanti` | — | 918 | L'importo delle spese per il pagamento in contanti o in contrassegno. |
| `[PAGAMENTI]` | *codice del metodo di pagamento di Magento* | `pagamento` | 918 | Il pagamento di Facile per quel metodo. |
| `[ARTICOLI]` | `cod_spese_tra`, `cod_buono_sco`, `cod_contanti` | — | 918 | Gli articoli di servizio per spese di trasporto, sconti e spese per i contanti. |
| `[COMMAND]` | `interval` | 0 | 918 | Il periodo degli ordini da rileggere, vedi più sotto. |
| `[DEBUG]` | `log_json`, `log_json_orders`, `log_json_order` | 0 | — | Per l'assistenza: salvano nella cartella `log` le richieste e le risposte. |

## Prodotti, categorie e immagini

- **Categorie (924):** le tassonomie e i loro elementi diventano categorie del
  negozio, con nome e stato attivo o disattivato.
- **Articoli nuovi (924):** si creano gli articoli con **Includi WEB** non
  ancora collegati, con codice, nome (il **Web Nome**, o le due righe di
  descrizione), prezzo del listino `listino_uff`, peso in chilogrammi e marchio.
  Se il codice esiste già sul negozio, l'articolo viene solo collegato.
- **Il marchio è obbligatorio:** un articolo il cui [marchio](../magazzino/marchi.md)
  non è collegato al negozio non viene creato. Collega i marchi con
  l'operazione 921.
- **Articoli già collegati (924):** si aggiornano nome, prezzo, peso,
  descrizioni (**Web Des. Estesa** e **Web Des. Breve**), titolo e
  descrizione per i motori di ricerca, articoli collegati e categorie. Un
  articolo che perde **Includi WEB** viene disattivato e nascosto sul negozio.
- **Immagini (925):** si mandano le immagini a grandezza piena, ridimensionate
  a 1024 pixel sul lato più lungo; la prima diventa l'immagine principale del
  prodotto.

## Disponibilità e prezzi

- **Disponibilità (922):** per gli articoli pubblicati, la somma di
  *esistenza − ordinato clienti − impegnato* nei depositi `depositi_disp`.
  Si manda solo se è diversa da quella del negozio. Con meno di una unità, o
  con un marchio che ha **Stock Ecommerce** impostato a non esporre le
  giacenze, il prodotto risulta non disponibile.
- **Prezzi (923):** il prezzo pieno è quello del listino `listino_uff`, ma mai
  sotto il listino web. Il prezzo di vendita è quello della promozione attiva,
  con le sue date di inizio e fine, altrimenti quello del listino web. Gli
  articoli in promozione vengono rimandati ogni giorno.

## Gli ordini

| `interval` | Ordini riletti |
|---|---|
| `2` | Degli ultimi 7 giorni |
| `3` | Degli ultimi 31 giorni |
| `4` | Dal 1° gennaio dell'esercizio |
| `1`, `0` o altri valori | Dell'ultimo giorno |

- **Quali ordini:** quelli negli stati `pending`, `processing` e
  `pagamento_ricevuto`, creati nell'anno dell'esercizio della ditta e non già
  importati.
- **Cliente:** si cerca per email; se non c'è viene creato come persona fisica.
  Se esiste, i suoi dati vengono **aggiornati** con quelli dell'ordine. Nome,
  indirizzo e città vengono scritti in maiuscolo; la provincia si ricava dalla
  città.
- **Destinazione:** l'indirizzo di spedizione diventa una destinazione diversa
  solo se è diverso da quello del cliente.
- **Righe:** l'articolo si ritrova dal codice (SKU); se non esiste la riga entra
  come descrittiva, con lo SKU e l'IVA predefinita della ditta. Prezzi IVA
  inclusa. I componenti dei prodotti configurabili non entrano come righe a sé.
- **Righe aggiuntive:** spese di trasporto sull'articolo `cod_spese_tra`, spese
  per i contanti (`spese_pag_contanti`) sull'articolo `cod_contanti` quando il
  pagamento è in contanti o in contrassegno, sconto in negativo sull'articolo
  `cod_buono_sco`.
- **Il documento** è un ordine cliente con la data dell'ordine e il riferimento
  *ORDINE WEB N. … del …*.

!!! warning "Articoli di servizio"

    Se `cod_spese_tra`, `cod_buono_sco` o `cod_contanti` non sono impostati, o
    indicano articoli che non esistono, il registro lo segnala all'avvio
    dell'importazione degli ordini.

## Messaggi del registro

| Riga del registro | Che cosa significa |
|---|---|
| `Codice articolo per spese di trasporto (cod_spese_tra) non impostato nel file di configurazione!` (e gli analoghi per buono sconto e pagamento contanti) | Manca un articolo di servizio nella sezione `[ARTICOLI]`. |
| `Codice articolo per spese di trasporto (cod_spese_tra) non trovato in archivio!` (e gli analoghi) | L'articolo indicato non esiste in Facile. |
| `Salto Ordine … (status = …)` | L'ordine è in uno stato che non si importa. |
| `Salto Ordine … (anno esercizio diverso)` | L'ordine è di un altro anno. |
| `Salto Ordine … (già trovato in archivio)` | L'ordine era già stato importato. |
| `Errore : …` | Il negozio ha risposto con un errore: il numero è il codice della risposta. |
| `Articolo … : Codice brand o product_brand non impostato sul marchio …` | Il marchio dell'articolo non è collegato al negozio: l'articolo non viene creato. |
| `Impossibile aggiornare Art. … - Disp. …` / `Impossibile aggiornare Art. … - Prezzo …` | Il negozio ha rifiutato la disponibilità o il prezzo di un articolo. |
| `… : Nessuna risposta dal server` | Il negozio non ha risposto. |

## Vedi anche

- [E-commerce](index.md)
- [Impostazione Dati Web](../anagrafiche/impostazione-dati-web.md)
- [Marchi](../magazzino/marchi.md)
