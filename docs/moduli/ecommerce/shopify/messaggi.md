---
title: Messaggi del registro del connettore Shopify
description: Le righe che il connettore Shopify scrive nel registro quando qualcosa non va, con la causa e il rimedio.
modulo: E-commerce ▸ Shopify
---

# Messaggi del registro

Il connettore Shopify non mostra messaggi a video: scrive tutto nel registro
della cartella `log`, in un file per operazione e per giorno, che si può
leggere anche mentre il programma lavora (vedi
[Il registro delle operazioni](../index.md#il-registro-delle-operazioni)).

Questa pagina raccoglie i messaggi che chiedono un intervento. I riepiloghi
di ciascuna operazione sono descritti nelle rispettive pagine. Nei messaggi
qui sotto, `...` sta per il dato che cambia di volta in volta: un codice, un
nome, un numero.

!!! info "In sintesi"

    - **Dove:** cartella `log`, file `operation_<numero>_<AAAAMMGG>.txt`
    - **Ultima riga di ogni operazione:** il riepilogo, con il numero di
      errori
    - **Per l'assistenza:** con `log_json = 1` nella sezione `[DEBUG]` il
      connettore salva anche le richieste a Shopify e le risposte

---

## Accesso al negozio

| Riga del registro | Causa | Cosa fare |
|---|---|---|
| `Shopify: [ECOMMERCE] incompleta (web_host e token, oppure client_id e client_secret)` | Nel file mancano l'indirizzo del negozio o le credenziali dell'app. | Compila `web_host` e `token`, oppure `client_id` e `client_secret`. |
| `Shopify: impostare in [ECOMMERCE] il token oppure client_id e client_secret` | Mancano le credenziali dell'app. | Come sopra. |
| `Shopify: richiesta del token fallita - ...` | Il negozio non risponde alla richiesta di accesso: rete, indirizzo sbagliato. | Controlla `web_host` e la connessione a Internet del computer. |
| `Shopify: token negato (HTTP ...) - ...` | Client ID o segreto sbagliati, oppure l'app non è installata sul negozio. | Ricopia le credenziali dal Dev Dashboard e controlla che l'app sia installata. |
| `Shopify ...: HTTP 401 ...` | Il token non è valido o è stato revocato. | Genera un token nuovo nell'app e aggiornalo nel file. |
| `Shopify ...: token scaduto o revocato, se ne chiede uno nuovo` | Con le credenziali del Dev Dashboard l'accesso dura 24 ore: il connettore lo rinnova da solo. | Niente. |
| `Shopify ...: nessuna risposta, tentativo ... - ...` | Il negozio non ha risposto. Il connettore riprova fino a cinque volte. | Se dopo i tentativi l'operazione va avanti, niente; altrimenti controlla la connessione. |
| `Shopify ...: limite di frequenza raggiunto, attesa e nuovo tentativo ...` | Shopify limita il numero di richieste al secondo di ogni app. Il connettore aspetta e riprova. | Niente: è normale durante i caricamenti grandi. |
| `Shopify ...: abbandonata dopo 5 tentativi` | Il negozio non ha risposto a nessun tentativo. | L'operazione riprova al giro successivo. Se si ripete, controlla lo stato di Shopify e la connessione. |
| `Shopify ...: errore GraphQL ... - ...` | Shopify ha rifiutato la richiesta. | Annota il messaggio e contatta l'assistenza. |

## Configurazione (988)

| Riga del registro | Causa | Cosa fare |
|---|---|---|
| `Permesso mancante nell'app Shopify: ...` | All'app manca un permesso. | Aggiungilo nella configurazione dell'app, reinstallala e rilancia la configurazione. |
| `Nessuna ubicazione attiva di nome '...' su Shopify (chiave location_name)` | Il nome in `location_name` non corrisponde a nessuna ubicazione attiva. | Correggi il nome, come compare nelle impostazioni del negozio, oppure lascia la chiave vuota. |
| `Nessuna ubicazione attiva su Shopify` | Il negozio non ha ubicazioni attive. | Attivane una nelle impostazioni del negozio. |
| `Canale di vendita '...' non trovato (chiave canale): prodotti e collezioni nuovi non verranno pubblicati` | Il canale indicato non esiste sul negozio. | Correggi `canale`, oppure toglila per usare il negozio online. |
| `Configurazione Shopify NON completata: vedere i messaggi precedenti` | Uno dei controlli precedenti è fallito. | Risolvi i problemi elencati sopra e rilancia. |
| `Shopify non configurato: lanciare prima la configurazione (988)` | Un'operazione è stata lanciata prima della configurazione. | Lancia la configurazione. |
| `Ubicazione Shopify non configurata: lanciare prima la configurazione (988)` | Le giacenze sono state lanciate prima della configurazione. | Lancia la configurazione. |

## Abbinamento (987)

| Riga del registro | Causa | Cosa fare |
|---|---|---|
| `Ci sono ... collegamenti del vecchio connettore REST: lanciare prima la configurazione (988). Abbinamento non eseguito.` | Il negozio era collegato con il connettore precedente e i collegamenti non sono ancora stati convertiti. | Lancia la configurazione, poi l'abbinamento. |
| `Nessuna variante sul negozio Shopify: niente da abbinare` | Il negozio è vuoto. | Niente: passa al primo caricamento. |
| `Esportazione incompleta (...): i collegamenti non visti NON vengono tolti` | Shopify ha consegnato l'elenco dei prodotti solo in parte. Per prudenza il connettore non toglie nessun collegamento. | Rilancia l'abbinamento. |
| `Esportazione varianti non conclusa entro un'ora` | Shopify non ha preparato l'elenco dei prodotti in tempo. | Rilancia l'abbinamento più tardi. |

L'elenco delle varianti non abbinate, con il motivo, è nel file
`shopify_non_abbinati.csv`: vedi
[Abbina il catalogo già presente](installazione.md#5-abbina-il-catalogo-gia-presente).

## Prodotti e immagini (984, 985)

| Riga del registro | Causa | Cosa fare |
|---|---|---|
| `Articolo ...: il codice non da' uno SKU EAN-13 di variante (servono 6 cifre): non inviato` | Un articolo a taglie e colori ha un codice che non è di 6 cifre. | Il connettore non può formare gli SKU delle varianti: l'articolo resta fuori dal negozio. |
| `Articolo ... a taglie e colori senza combinazioni pubblicabili: non inviato` | Nessuna combinazione di taglia e colore ha movimenti nei depositi di `depositi_disp`. | Controlla i depositi indicati, oppure carica l'articolo. |
| `Articolo ...: gruppo taglie ... inesistente` | L'articolo indica un gruppo di taglie che non esiste. | Correggi il gruppo taglie nell'anagrafica dell'articolo. |
| `Articolo ...: immagine formato ... illeggibile, saltata` | Un'immagine dell'articolo è danneggiata. | Ricarica l'immagine in Facile. |
| `Caricamento ... fallito - ...` | Una fotografia non è arrivata sul negozio. | Al giro successivo l'articolo viene ritentato. |

## Giacenze, prezzi e listino ingrosso (982, 983, 991)

| Riga del registro | Causa | Cosa fare |
|---|---|---|
| `Variante ... non c'e' piu' su Shopify: collegamento tolto, l'articolo si rimanda con la 984` | La variante è stata cancellata sul negozio. | Niente: l'operazione prodotti la ricrea. |
| `Modalita' ...: il listino ingrosso B2B si usa solo con modalita = MISTO` | La 991 è stata lanciata con un'altra modalità. | Imposta `modalita = MISTO`, oppure spegni l'operazione. |
| `Cliente ... (...): senza email, non diventa azienda B2B` | Il cliente sul listino ingrosso non ha email. | Compila l'email del cliente. |
| `... non c'e' piu' sul negozio: si ricrea` | Listino, mercato o catalogo ingrosso cancellati sul negozio. | Niente: vengono ricreati. |

## Ordini (980, 990)

| Riga del registro | Causa | Cosa fare |
|---|---|---|
| `Shopify ordini: risposta parziale (... errori), primo: This app is not approved to access the Customer object...` | Il piano del negozio non dà i dati personali dei clienti. | Niente: gli ordini entrano sul [cliente generico](ordini.md#ordini-senza-dati-personali). |
| `Ordine Shopify ... del ...: l'esercizio ... non e' stato creato, ordine non importato` | L'ordine è di un anno per cui la ditta non ha l'esercizio. | Crea l'esercizio in Facile: al giro successivo l'ordine entra, se è ancora dentro i giorni di `interval`. |
| `Ordine Shopify ... del ...: errore nell'esercizio ..., ordine non importato - ...` | Scrivendo l'ordine nell'esercizio del suo anno c'è stato un errore, per esempio un archivio di quell'anno non aggiornato alla versione di Facile. | Apri quell'esercizio con Facile, che lo aggiorna; l'ordine viene ritentato a ogni giro. |
| `Ordine Shopify ...: importazione interrotta da un errore, l'ordine ... incompleto e' stato tolto` | L'ordine si è interrotto a metà ed è stato tolto. | Leggi l'errore nelle righe vicine; l'ordine viene ritentato. |
| `Ordine Shopify ...: importazione interrotta da un errore, l'ordine ... e' rimasto incompleto e va tolto a mano` | L'ordine si è interrotto a metà e non è stato possibile toglierlo. | Elimina in Facile l'ordine indicato: finché c'è, l'ordine Shopify risulta già importato. |
| `Cliente ... non trovato: se ne crea uno nuovo` | Il cliente di Facile collegato al cliente del negozio è stato cancellato. | Niente: ne viene creato uno nuovo. |
| `Cliente generico ... di [ECOMMERCE] cliente_generico non trovato: si usa quello automatico` | Il cliente indicato nella chiave non esiste. | Correggi `cliente_generico`, oppure mettilo a `0`. |
| `Nessuno stato da comunicare: impostare [STATO_ORDINI] evaso e/o annullato` | La 990 gira con gli interruttori spenti. | Accendi gli stati da comunicare, oppure spegni l'operazione. |
| `Annullamento ordine ...: ...` | Shopify ha rifiutato l'annullamento. | Annulla l'ordine dall'amministrazione del negozio. |

## Esecuzione continua (979)

I messaggi del ciclo sono descritti in
[Esecuzione continua](ciclo.md#messaggi-principali).

## Vedi anche

- [E-commerce: i messaggi all'avvio di FacileToWeb](../index.md#controlli-e-messaggi)
- [Connettore Shopify](index.md)
