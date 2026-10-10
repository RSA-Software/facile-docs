---
title: Ordini da Shopify
description: Come gli ordini del negozio Shopify diventano ordini cliente in Facile, a quale cliente vengono intestati e come si comunicano a Shopify gli ordini evasi o annullati.
modulo: E-commerce ▸ Shopify
---

# Ordini

L'operazione **980** porta in Facile gli ordini del negozio: ognuno diventa
un **ordine cliente**, con le sue righe, il cliente e l'indirizzo di
spedizione. L'operazione **990** fa il viaggio inverso e comunica a Shopify
gli ordini che in Facile sono stati evasi o annullati.

!!! info "In sintesi"

    - **Operazioni:** 980 importa gli ordini, 990 comunica evasione e
      annullamento
    - **Si importano:** gli ordini non annullati, negli stati di pagamento
      accesi nella sezione `[STATI]`
    - **Ogni ordine entra una volta sola**, anche se l'operazione gira di
      continuo

---

## Quali ordini si importano

A ogni giro la 980 rilegge gli ordini creati sul negozio negli ultimi giorni,
quanti lo dice la chiave `interval` della sezione `[COMMAND]`:

| `interval` | Ordini riletti |
|---|---|
| `1` (o assente) | Dell'ultimo giorno |
| `2` | Degli ultimi 7 giorni |
| `3` | Degli ultimi 31 giorni |
| `4` | Dal 1° gennaio dell'esercizio |

Shopify rende disponibili al connettore solo gli ordini degli ultimi 60
giorni: oltre, anche con `interval = 4`, non ne arrivano.

Di questi, si importano gli ordini che:

- **non sono già stati importati**, nemmeno dal connettore precedente;
- **non sono annullati** su Shopify;
- hanno uno **stato di pagamento acceso** nella sezione `[STATI]`.

La sezione `[STATI]` elenca gli stati di pagamento di Shopify, con `1` per
quelli da importare:

| Chiave | Stato su Shopify |
|---|---|
| `paid` | Pagato |
| `partially_paid` | Pagato in parte |
| `authorized` | Autorizzato: il pagamento è bloccato ma non ancora incassato |
| `pending` | In attesa: per esempio un bonifico non ancora arrivato |
| `partially_refunded` | Rimborsato in parte |
| `refunded` | Rimborsato |
| `voided` | Annullato prima dell'incasso |
| `expired` | Scaduto |

Gli stati non elencati, o elencati con `0`, non si importano. Un ordine in
attesa di pagamento che non importi oggi entra al giro in cui diventa pagato,
purché sia ancora dentro i giorni riletti.

### Ordini di un altro anno

Ogni ordine entra nell'**esercizio del suo anno**, anche se non è quello su
cui lavora la ditta: un ordine del 30 dicembre importato il 2 gennaio va
nell'esercizio dell'anno prima, con la sua numerazione.

Se l'esercizio dell'anno dell'ordine **non è stato creato**, l'ordine non
entra: il registro lo segnala e l'ordine viene ritentato a ogni giro.
Basta creare l'esercizio in Facile perché al giro successivo entri, purché
sia ancora dentro i giorni riletti (chiave `interval`).

!!! warning "Il cambio d'anno"

    Crea l'esercizio dell'anno nuovo prima che arrivino gli ordini di
    gennaio, oppure imposta `interval` in modo che il connettore li rilegga
    finché l'esercizio non c'è: con `2` restano ritentabili per sette
    giorni.

Se un ordine si interrompe a metà per un errore, l'ordine incompleto viene
tolto e al giro successivo l'importazione riparte da capo.

## Com'è fatto l'ordine in Facile

| Nell'ordine di Facile | Da Shopify |
|---|---|
| **Data** | La data dell'ordine sul negozio. |
| **Registro** | Quello indicato nella chiave `registro`; vuota, il registro principale. |
| **Cliente** | Vedi [A quale cliente va l'ordine](#a-quale-cliente-va-lordine). |
| **Destinatario** | L'indirizzo di spedizione, come destinazione diversa del cliente. |
| **Pagamento** | Il codice indicato nella sezione `[PAGAMENTI]` per il metodo di pagamento usato. |
| **Num. Doc. Rif.**, **Data Doc. Rif.** | Il numero dell'ordine sul negozio (per esempio *1001*) e la sua data. |

Nel [documento di vendita](../../vendite/documento-di-vendita.md) l'ordine
importato si riconosce da **Num. Doc. Rif.** e **Data Doc. Rif.**. Se l'ordine
non ha un indirizzo di spedizione, e quindi non ha un **Destinatario**, accanto
al campo **Destinatario** compare anche il riferimento completo, per esempio
*#1001 DEL 2026-10-08*.

### Le righe

- **Articoli:** ogni riga dell'ordine ritrova l'articolo di Facile dalla
  variante venduta, oppure dallo SKU. Nella versione taglie e colori, la
  riga riporta anche taglia e colore.
- **Articolo sconosciuto:** se l'articolo non si trova, la riga entra come
  riga descrittiva con il nome del prodotto e lo SKU, e l'IVA predefinita
  della ditta. Va sistemata a mano.
- **Prezzi:** sono quelli dell'ordine. Se il negozio mostra i prezzi IVA
  compresa, le righe sono IVA inclusa.
- **Deposito:** quello indicato nella chiave `deposito`; se manca, il
  deposito attivo della ditta.
- **Sconto:** lo sconto totale dell'ordine entra come una riga in negativo
  sull'articolo indicato in `cod_buono_sco`, con il codice sconto come
  descrizione (o *SCONTO*).
- **Spese di trasporto:** ogni spedizione a pagamento entra come una riga
  sull'articolo indicato in `cod_spese_tra`, con il nome della spedizione
  come descrizione.

!!! warning "Sconti e spese senza articolo"

    Se `cod_buono_sco` o `cod_spese_tra` sono vuoti, o indicano un articolo
    che non esiste, lo sconto o le spese **non entrano** e il totale
    dell'ordine in Facile è diverso da quello del negozio. Prepara due
    articoli di servizio e indicali nella sezione `[ARTICOLI]`.

### Il metodo di pagamento

La sezione `[PAGAMENTI]` collega ogni metodo di pagamento di Shopify a un
pagamento di Facile, con una chiave formata da `pag_` e dal nome del metodo
come lo indica Shopify:

```ini
[PAGAMENTI]
pag_manual           = 1
pag_shopify_payments = 1
```

Un metodo non elencato lascia l'ordine senza pagamento. Per conoscere il nome
esatto di un metodo, attiva `log_json = 1` nella sezione `[DEBUG]`, lancia
l'importazione e cerca `paymentGatewayNames` nel file
`shopify_ordini_response.json` della cartella `log`.

## A quale cliente va l'ordine

Per ogni ordine il connettore cerca il cliente in quest'ordine:

1. **Il cliente già collegato:** se lo stesso cliente del negozio ha già
   fatto un ordine, si usa il cliente di Facile di quella volta.
2. **La stessa email:** si cerca in Facile un cliente con l'email
   dell'ordine. Le email in Facile sono sempre in minuscolo, e quella
   dell'ordine viene portata in minuscolo prima del confronto.
3. **Il cliente generico**, per gli ordini senza dati personali (vedi più
   sotto).
4. **Un cliente nuovo**, con i dati di fatturazione dell'ordine: cognome e
   nome, oppure la ragione sociale se c'è l'azienda; indirizzo, città,
   provincia, CAP, nazione, telefono ed email. Pagamento e categoria
   economica sono quelli delle chiavi `pagamento` e `cateco`.

I clienti che esistono già **non vengono modificati**: se un cliente cambia
indirizzo sul negozio, in Facile resta quello di prima.

L'indirizzo di Shopify ha due righe: la seconda (scala, interno, presso)
viene accodata alla prima, separata da una virgola, perché in Facile
l'indirizzo è un campo solo.

### Ordini senza dati personali

Con il piano **Basic**, Shopify non fornisce al connettore né il nome, né
l'email, né gli indirizzi del cliente. Questi ordini vanno a un **cliente
generico**:

- quello indicato nella chiave `cliente_generico`;
- se la chiave vale `0`, o indica un cliente che non esiste, un cliente
  **CLIENTE SHOPIFY** creato dal connettore la prima volta e usato da lì in
  avanti per tutti questi ordini.

I dati del cliente vero si leggono sul negozio, nell'ordine.

### Destinazione

L'indirizzo di spedizione diventa una
[destinazione diversa](../../anagrafiche/destinazioni-diverse.md) del
cliente. Se il cliente ha già una destinazione con lo stesso indirizzo, si
usa quella. Se l'ordine non ha indirizzi, la merce va all'intestatario.

### Quello che non arriva

- **Codice fiscale e partita IVA:** il checkout standard di Shopify non li
  chiede. Per fatturare vanno completati a mano nell'anagrafica del
  cliente.
- **Sesso:** un cliente nuovo viene registrato come persona fisica di sesso
  maschile, perché Shopify non dà il dato.

## Comunicare a Shopify gli ordini evasi o annullati

L'operazione **990** guarda lo stato in Facile degli ordini importati e lo
comunica al negozio. È spenta finché non accendi almeno uno degli
interruttori della sezione `[STATO_ORDINI]`:

| Chiave | Con `1` |
|---|---|
| `evaso` | Un ordine **evaso** in Facile viene evaso anche su Shopify: il cliente lo vede come spedito. |
| `annullato` | Un ordine **annullato** in Facile viene annullato anche su Shopify, con la merce rimessa a magazzino e **nessun rimborso automatico**. |
| `avvisa_cliente` | Shopify manda al cliente l'email di evasione o di annullamento. |

Ogni ordine si comunica una volta sola. Se su Shopify l'ordine era già stato
evaso o annullato a mano, il connettore lo registra e non riprova.

!!! warning "Il rimborso resta da fare"

    L'annullamento comunicato da Facile **non rimborsa** il cliente: il
    rimborso va fatto dall'amministrazione del negozio.

Il **numero di tracciamento** della spedizione non viene inviato.

## Messaggi principali

| Riga del registro | Che cosa significa |
|---|---|
| `Ordine Shopify #N importato come ordine N/... del cliente N` | Un ordine importato, con il numero che ha preso in Facile. |
| `Cliente nuovo N (...) dall'ordine Shopify #N` | L'ordine ha creato un cliente. |
| `Cliente generico N (CLIENTE SHOPIFY) creato per gli ordini senza dati personali` | Il primo ordine senza dati personali ha creato il cliente generico. |
| `Cliente generico N di [ECOMMERCE] cliente_generico non trovato: si usa quello automatico` | Il cliente indicato nella chiave non esiste. |
| `Shopify ordini: risposta parziale (N errori), primo: This app is not approved to access the Customer object...` | Il piano del negozio non dà i dati personali dei clienti: gli ordini entrano lo stesso, sul cliente generico. |
| `Ordine Shopify #N del AAAA-MM-GG: l'esercizio AAAA non e' stato creato, ordine non importato` | Manca l'esercizio dell'anno dell'ordine: crealo in Facile. |
| `Ordine Shopify #N: importazione interrotta da un errore, l'ordine N/AAAA incompleto e' stato tolto` | Un errore ha interrotto l'ordine: è stato tolto e si riprova al giro dopo. |
| `Fine importazione ordini Shopify: letti N - importati N - saltati N - errori N` | Il riepilogo: i *saltati* sono già importati, annullati o in uno stato non acceso. |
| `Nessuno stato da comunicare: impostare [STATO_ORDINI] evaso e/o annullato` | La 990 è stata lanciata con gli interruttori spenti. |
| `Ordine ... evaso su Shopify`, `Ordine ... annullato su Shopify` | Lo stato è stato comunicato. |

Gli altri messaggi sono in [Messaggi del registro](messaggi.md).

## Vedi anche

- [Anagrafica clienti](../../anagrafiche/anagrafica-clienti.md)
- [Destinazioni diverse](../../anagrafiche/destinazioni-diverse.md)
- [Categorie economiche](../../anagrafiche/categorie-economiche.md)
- [Il file di configurazione](configurazione.md)
