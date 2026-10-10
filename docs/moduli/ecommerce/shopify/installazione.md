---
title: Prima installazione del connettore Shopify
description: I passi per collegare per la prima volta un negozio Shopify a Facile, dalla creazione dell'app sul negozio al primo caricamento del catalogo.
modulo: E-commerce ▸ Shopify
---

# Prima installazione

Questa pagina segue il collegamento di un negozio Shopify dall'inizio: l'app
sul negozio, gli articoli in Facile, il file di configurazione, la
configurazione del negozio, l'eventuale abbinamento del catalogo esistente e
il primo caricamento. Alla fine si accende l'[esecuzione continua](ciclo.md).

!!! info "In sintesi"

    - **Ordine dei passi:** app ▸ articoli ▸ file `.ini` ▸ configurazione
      (988) ▸ abbinamento (987, se serve) ▸ primo caricamento ▸ esecuzione
      continua (979)
    - **Tempo:** il primo caricamento di qualche migliaio di articoli richiede
      alcune ore; i giri successivi pochi secondi

---

## 1. Crea l'app sul negozio

Facile entra nel negozio attraverso un'**app personalizzata** creata
dall'amministrazione del negozio. Ci sono due tipi di app, e il connettore
li accetta tutti e due:

| App | Cosa si copia nel file di configurazione |
|---|---|
| App creata dall'amministrazione del negozio | Il **token di accesso** all'Admin API, nella chiave `token`. |
| App creata dal Dev Dashboard di Shopify, nella stessa organizzazione del negozio | **Client ID** e **segreto**, nelle chiavi `client_id` e `client_secret`. Facile chiede da solo un accesso valido 24 ore e lo rinnova quando scade. |

Se nel file ci sono sia il token sia client ID e segreto, vale il token.

1. Crea l'app dall'amministrazione del negozio o dal Dev Dashboard.
2. Assegna all'app i permessi elencati nei
   [requisiti](index.md#il-negozio).
3. Installa l'app sul negozio.
4. Copia il token, oppure client ID e segreto: ti servono al passo 3.

<!-- DA VERIFICARE: i nomi esatti delle voci dell'amministrazione Shopify per creare l'app, e se le app create dall'amministrazione sono ancora disponibili per i negozi nuovi -->

!!! warning "Il token è una chiave del negozio"

    Con il token chiunque può modificare prodotti e ordini del negozio.
    Non mandarlo per email e conservalo solo nel file di configurazione.

## 2. Prepara gli articoli in Facile

Per ogni articolo da vendere sul sito, da
[Impostazione Dati Web](../../anagrafiche/impostazione-dati-web.md):

1. Attiva **Includi WEB**.
2. Compila **Web Nome**: è il nome del prodotto sul negozio. Se lo lasci
   vuoto, il prodotto prende le due righe di descrizione dell'articolo.
3. Compila **Web Des. Estesa**, oppure almeno **Web Des. Breve**: è la
   descrizione della scheda prodotto.
4. Spunta le **tassonomie** in cui l'articolo deve comparire: diventano le
   collezioni del negozio.
5. Carica le fotografie nell'[anagrafica dell'articolo](../../anagrafiche/anagrafica-articoli.md).

Controlla anche i [marchi](../../magazzino/marchi.md): un marchio con
**Stock Ecommerce** impostato a non esporre le giacenze manda sul negozio
disponibilità zero per tutti i suoi articoli.

## 3. Prepara il file di configurazione

1. Scarica il [file di prova](../../../assets/modelli/shopify.ini) descritto in
   [Il file di configurazione](configurazione.md#un-file-completo) e salvalo
   nella cartella `cfg` di Facile: l'installazione di Facile non lo porta.
2. Nella sezione `[LOGIN]` indica archivio, utente e password di Facile.
3. Nella sezione `[ECOMMERCE]` indica in `web_host` l'indirizzo
   *nomenegozio*`.myshopify.com` del negozio e il token, oppure client ID e
   segreto.
4. Rivedi le altre chiavi: listini, depositi, registro degli ordini,
   articoli per spese di trasporto e sconti.

Per i passi 4, 5 e 6 conviene preparare una copia del file per ciascuna
operazione, cambiando solo `operation` nella sezione `[COMMAND]`.

## 4. Lancia la configurazione

La configurazione (operazione **988**) prepara il negozio e non modifica
nessun prodotto.

1. Imposta `operation = 988` e lancia FacileToWeb, come descritto in
   [E-commerce](../index.md#come-si-avvia).
2. Apri il registro `operation_988_<data>.txt` nella cartella `log`.
3. Controlla che riporti il nome del negozio, l'**ubicazione per le
   giacenze**, il **canale per la pubblicazione** e la riga finale
   `Fine configurazione Shopify`.

Se il registro elenca dei **permessi mancanti**, aggiungili all'app,
reinstallala e ripeti la configurazione.

L'**ubicazione** è il magazzino di Shopify su cui Facile scrive le giacenze.
Se il negozio ne ha più d'una, indica quella giusta nella chiave
`location_name`; se la lasci vuota, Facile usa la prima ubicazione attiva.

Il **canale** è quello su cui vengono pubblicati prodotti e collezioni
nuovi; se non indichi niente nella chiave `canale`, è il negozio online
(*Online Store*).

Se il negozio era già collegato a Facile con il connettore precedente, la
configurazione converte i collegamenti esistenti: i prodotti già pubblicati
non vengono ricreati.

## 5. Abbina il catalogo già presente

Salta questo passo se il negozio è nuovo e vuoto.

Se sul negozio ci sono già dei prodotti, prima di mandare gli articoli di
Facile va fatto l'**abbinamento** (operazione **987**): collega ogni
variante del negozio all'articolo di Facile che ha come codice il suo
**SKU**. Senza abbinamento, Facile creerebbe un secondo prodotto accanto a
quello esistente.

1. Imposta `operation = 987` e lancia FacileToWeb.
2. Nel registro controlla la riga finale, che riporta le varianti lette,
   quelle abbinate e quelle non abbinate.
3. Apri il file `shopify_non_abbinati.csv` nella cartella `log`: elenca le
   varianti non abbinate, con il motivo.
4. Correggi lo SKU sul negozio, o il codice in Facile, e ripeti
   l'abbinamento finché l'elenco contiene solo quello che non va venduto da
   Facile.

| Motivo nell'elenco | Che cosa significa |
|---|---|
| `senza SKU` | La variante non ha SKU: Facile non ha niente su cui abbinarla. |
| `SKU non trovato in Facile` | Nessun articolo di Facile ha quel codice. |
| `EAN di variante: si abbina solo con la versione taglie e colori` | Lo SKU è il codice di una variante a taglie e colori, ma la versione di Facile non le gestisce. |
| `EAN di variante non riconosciuto (articolo inesistente o senza taglie)` | Lo SKU ha la forma di una variante a taglie e colori, ma l'articolo non esiste o non ha taglie. |
| `prodotto doppio: articolo ... gia' collegato a ...` | Due prodotti del negozio portano lo stesso articolo: ne resta collegato uno solo. |

## 6. Primo caricamento

Il primo caricamento manda tutto il catalogo e richiede tempo. Lancia le
operazioni in quest'ordine, aspettando la fine di ciascuna:

| Ordine | Operazione | Tempo misurato su 3.550 articoli |
|---|---|---|
| 1 | **984** Prodotti e collezioni | circa 1 ora e 50 minuti |
| 2 | **982** Giacenze | meno di un minuto |
| 3 | **983** Prezzi | circa 20 minuti |
| 4 | **985** Immagini (11.000 fotografie) | circa 2 ore e 40 minuti |

I tempi dipendono soprattutto dai limiti di velocità che Shopify impone a
ogni app, non dal computer. Le giacenze e i prezzi vanno dopo i prodotti
perché si possono inviare solo a varianti che esistono già.

Ogni operazione si può interrompere e rilanciare: riparte dagli articoli
che non ha ancora inviato.

## 7. Accendi l'esecuzione continua

Da qui in avanti il negozio si aggiorna da solo con l'[esecuzione
continua](ciclo.md): un unico file `.ini`, con le operazioni da fare e ogni
quanto, e un'attività pianificata che la avvia insieme al computer.

## Vedi anche

- [Connettore Shopify](index.md)
- [Il file di configurazione](configurazione.md)
- [Messaggi del registro](messaggi.md)
