---
title: Connettore nopCommerce
description: Come Facile importa gli ordini di un negozio nopCommerce con FacileToWeb, e come si configura il collegamento.
modulo: E-commerce
---

# Connettore nopCommerce

Il connettore nopCommerce porta in Facile gli **ordini** del negozio: ognuno
diventa un ordine cliente, con il cliente, l'indirizzo di spedizione e le righe.
Non manda nulla al negozio: articoli, giacenze e prezzi si gestiscono sul
negozio.

!!! info "In sintesi"

    - **Programma:** [FacileToWeb](index.md), operazione **902**
    - **Direzione:** dal negozio a Facile, solo ordini
    - **Licenza:** separata, in aggiunta a quella di Facile

---

!!! info "Licenza"

    Il connettore nopCommerce è soggetto a una **licenza separata**, in
    aggiunta a quella di Facile.

## Come funziona

FacileToWeb interroga un indirizzo del negozio che restituisce gli ordini di un
periodo in formato XML. Non si tratta del sistema di scambio dati standard di
nopCommerce, ma di un servizio predisposto sul negozio per Facile: va
installato e configurato sul negozio prima di usare il connettore.

<!-- DA VERIFICARE: quale estensione del negozio nopCommerce espone l'indirizzo con gli ordini in XML -->

## Il file di configurazione

Oltre alle sezioni comuni descritte in [E-commerce](index.md#il-file-di-configurazione):

```ini
[COMMAND]
operation = 902
interval  = 2

[ECOMMERCE]
web_host  = www.nomenegozio.it
api_path  = percorso/del/servizio
token     = CHIAVE
registro  =

[PAGAMENTI]
pag_0001  = 1
```

| Sezione | Chiave | Predefinito | Descrizione |
|---|---|---|---|
| `[COMMAND]` | `interval` | 0 | Il periodo da rileggere, vedi sotto. |
| `[ECOMMERCE]` | `web_host` | — | L'indirizzo del negozio. Obbligatorio. |
| `[ECOMMERCE]` | `api_path` | — | Il percorso del servizio degli ordini sul negozio. Obbligatorio. |
| `[ECOMMERCE]` | `token` | — | La chiave del servizio. |
| `[ECOMMERCE]` | `registro` | vuoto | Il registro degli ordini importati. |
| `[ECOMMERCE]` | `deposito` | il deposito web della ditta | Serve a tenere la data dell'ultima importazione, quando `interval` non è indicato. |
| `[PAGAMENTI]` | `pag_NNNN` | 0 | Il codice del pagamento di Facile per il metodo di pagamento del negozio con numero `NNNN`, sempre di quattro cifre (per esempio `pag_0001`). |
| `[DEBUG]` | `log_http_request`, `log_xml_orders`, `log_xml_order` | 0 | Per l'assistenza: scrivono nel registro l'indirizzo interrogato e salvano nella cartella `log` gli ordini ricevuti. |

Il collegamento usa sempre HTTPS sulla porta 443.

!!! warning "La chiave finisce nell'indirizzo"

    La chiave del servizio viaggia nell'indirizzo interrogato: con
    `log_http_request = 1` compare anche nel registro. Attivalo solo per le
    prove.

### Il periodo riletto

| `interval` | Ordini riletti |
|---|---|
| `1` | Di oggi |
| `2` | Degli ultimi 7 giorni |
| `3` | Degli ultimi 31 giorni |
| `4` | Dal 1° gennaio |
| `5` | Tutti |
| `0`, o qualsiasi altro valore | Dall'ultima importazione riuscita, con un margine di due ore e mezza |

L'ultima importazione si considera riuscita solo se tutti gli ordini sono
entrati: se uno dà errore, l'importazione si ferma e al giro dopo riparte dalla
stessa data.

## Come entra un ordine

- **Quali ordini:** tutti tranne quelli **cancellati** sul negozio, e solo
  quelli creati nell'anno dell'esercizio su cui lavora la ditta.
- **Doppioni:** un ordine già importato non entra di nuovo.
- **Cliente:** si cerca il cliente collegato al cliente del negozio, poi per
  email; se non c'è viene creato. Se esiste, i suoi dati vengono **aggiornati**
  con quelli dell'ordine: ragione sociale o cognome e nome, telefono,
  indirizzo, codice fiscale, partita IVA, PEC e codice destinatario. La
  provincia si ricava dalla città.
- **Destinazione:** l'indirizzo di spedizione diventa una destinazione diversa
  del cliente; se il cliente ne ha già una con lo stesso nome e indirizzo, si
  usa quella.
- **Data:** l'ordine entra con la data dell'ordine sul negozio.
- **Righe:** l'articolo si ritrova dal codice della variante venduta; se non
  esiste in Facile la riga entra come descrittiva, con il codice indicato e
  l'IVA predefinita della ditta. I prezzi sono IVA inclusa.
- **Righe aggiuntive**, con l'IVA predefinita della ditta, solo quando
  l'importo non è zero:

| Codice della riga | Che cosa |
|---|---|
| `SCONTO` | Lo sconto dell'ordine |
| `WELCOME5` | Lo sconto del coupon di benvenuto |
| `SCONTOPUNTI` | Lo sconto pagato con i punti |
| `SCONTOBUONO` | Lo sconto pagato con un buono regalo |
| `TRASPORTO` | Le spese di spedizione |
| `SPESEPAG` / `SCONTOPAG` | Il costo aggiuntivo, o lo sconto, del metodo di pagamento |

- **Ordini Amazon** (metodo di pagamento numero 77): l'ordine entra già
  **evaso**, con i movimenti di scarico del magazzino. Se l'ordine era già stato
  importato ed evaso, viene annullato e reimportato.

## Messaggi del registro

| Riga del registro | Che cosa significa |
|---|---|
| `Carico Ordine …` | Un ordine sta entrando. |
| `Salto Ordine … (cancellato)` | L'ordine è cancellato sul negozio. |
| `Salto Ordine … (già trovato in archivio)` | L'ordine era già stato importato. |
| `Salto Ordine … (Anno ordine diverso da anno attivo)` | L'ordine è di un altro anno: crea o apri l'esercizio di quell'anno. |
| `Salto Ordine … (Documento non trovato in archivio)` | Un ordine Amazon già importato non si trova più in Facile. |
| `xml.FindChild("…"); return NULL pointer!` | Nella risposta del negozio manca un dato che il connettore si aspetta: il servizio del negozio va controllato. |
| `Impossibile accedere all' ennesimo ordine!` | La risposta del negozio non è leggibile. |

## Vedi anche

- [E-commerce](index.md)
- [Anagrafica clienti](../anagrafiche/anagrafica-clienti.md)
- [Destinazioni diverse](../anagrafiche/destinazioni-diverse.md)
