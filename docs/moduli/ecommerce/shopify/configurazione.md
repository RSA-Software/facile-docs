---
title: Il file di configurazione del connettore Shopify
description: Tutte le sezioni e le chiavi del file ini del connettore Shopify, con il valore predefinito e le operazioni che le usano, più un file completo da copiare.
modulo: E-commerce ▸ Shopify
---

# Il file di configurazione

Il connettore Shopify si configura con un file `.ini` nella cartella `cfg`
di Facile. Lo stesso file può servire a tutte le operazioni: cambia solo il
numero in `operation`, oppure si usa l'[esecuzione continua](ciclo.md), che
le fa tutte.

!!! info "In sintesi"

    - **Dove:** nella cartella `cfg` di Facile
    - **Come si usa:** `FacileToWeb.exe -ini<nome del file> -ditta<ditta>`
    - **Le righe che cominciano con `;`** sono commenti
    - **Una chiave assente** prende il valore predefinito indicato nelle
      tabelle

---

## Un file completo

L'installazione di Facile non porta nessun file di configurazione per
Shopify: si parte da questo modello, con **tutte le operazioni accese**.

[:material-download: Scarica shopify.ini](../../../assets/modelli/shopify.ini){ .md-button download="shopify.ini" }

1. Salvalo nella cartella `cfg` di Facile.
2. Nella sezione `[LOGIN]` sostituisci `ARCHIVI`, `xxxxx` e `yyyyy` con
   l'archivio, l'utente e la password di Facile.
3. Nella sezione `[ECOMMERCE]` indica l'indirizzo del negozio e le
   credenziali dell'app: client ID e segreto, oppure il token di un'app
   creata prima del 2026.
4. Compila `[ARTICOLI]` e `[PAGAMENTI]` e rivedi le altre chiavi.
5. Metti a `0`, nella sezione `[CICLO]`, le operazioni che non ti servono:
   per esempio `ingrosso` se non vendi ai professionisti, `stato_ordini` se
   non vuoi che Facile evada o annulli gli ordini sul negozio.

!!! warning "Lo stato degli ordini è acceso"

    Nel modello `evaso` e `annullato` valgono `1`: un ordine annullato in
    Facile viene annullato anche sul negozio, senza rimborso. Se non è
    quello che vuoi, spegnili prima di avviare il ciclo.

Il contenuto del file:

```ini
--8<-- "docs/assets/modelli/shopify.ini"
```

## [LOGIN] e [COMMAND]

Le due sezioni comuni a tutti i negozi sono descritte in
[E-commerce](../index.md#il-file-di-configurazione). Per Shopify:

| Chiave | Predefinito | Descrizione |
|---|---|---|
| `operation` | — | Il numero dell'operazione: vedi l'[elenco](index.md#le-operazioni). |
| `interval` | 1 | Solo per gli ordini: quanti giorni rileggere. `1` l'ultimo giorno, `2` sette giorni, `3` trentuno giorni, `4` dall'inizio dell'esercizio. |

## [CICLO]

Usata solo dall'[esecuzione continua](ciclo.md) (operazione 979).

| Chiave | Predefinito | Descrizione |
|---|---|---|
| `pausa` | 300 | Secondi di attesa fra un giro e l'altro; minimo 10. |
| `exit` | 0 | `1` ferma il ciclo e gli impedisce di ripartire. |
| `setup`, `abbina`, `ordini`, `prodotti`, `giacenze`, `prezzi`, `ingrosso`, `stato_ordini`, `immagini` | 0 | `0` = no, `1` = a ogni giro, un numero = al massimo una volta ogni tanti secondi. |

## [ECOMMERCE]

| Chiave | Predefinito | Usata da | Descrizione |
|---|---|---|---|
| `web_host` | — | tutte | L'indirizzo del negozio, nella forma *nomenegozio*`.myshopify.com`. |
| `api_version` | 2026-10 | tutte | La versione del sistema di scambio dati di Shopify. Si cambia solo insieme a un aggiornamento di Facile. |
| `client_id`, `client_secret` | — | tutte | Le credenziali dell'app creata dal Dev Dashboard di Shopify, il modo previsto per le app nuove. |
| `token` | — | tutte | Il token di accesso di un'app creata dall'amministrazione del negozio prima del 1° gennaio 2026. Se c'è, vince su `client_id` e `client_secret`. |
| `location_name` | la prima ubicazione attiva | 988 | Il nome dell'ubicazione di Shopify su cui scrivere le giacenze. |
| `canale` | Online Store | 988 | Il nome del canale di vendita su cui pubblicare prodotti e collezioni nuovi. |
| `modalita` | B2C | 983, 991 | `B2C` negozio al pubblico, `B2B` solo professionisti, `MISTO` tutti e due. Vedi [I prezzi](giacenze-e-prezzi.md#i-prezzi). |
| `listino_web` | 1 | 983, 984 | Il listino del prezzo di vendita. |
| `listino_uff` | 1 | 983, 984 | Il listino ufficiale: se è più alto del prezzo, diventa il prezzo barrato. |
| `listino_ing` | 2 | 983, 991 | Il listino ingrosso, per i professionisti. |
| `depositi_disp` | 1 | 982, 984 | I depositi sommati per la disponibilità, separati da virgole. Nella versione taglie e colori, anche quelli le cui combinazioni diventano varianti. |
| `deposito` | il deposito attivo della ditta | 980, 983 | Il deposito delle righe degli ordini importati **e** quello delle promozioni dei prezzi. |
| `registro` | vuoto | 980 | Il registro degli ordini importati. |
| `pagamento` | 0 | 980 | Il pagamento dei clienti nuovi creati dagli ordini. |
| `cateco` | 0 | 980 | La categoria economica dei clienti nuovi creati dagli ordini. |
| `cliente_generico` | 0 | 980 | Il cliente degli ordini senza dati personali. Con `0`, il connettore ne crea uno, *CLIENTE SHOPIFY*, e usa sempre quello. |
| `verifica_spariti` | 1 | 984 | `1` = a ogni giro si controlla che prodotti e collezioni esistano ancora sul negozio, e quelli cancellati a mano si ricreano. |
| `tipo_prodotto` | 0 | 984 | `1` = la categoria merceologica diventa il tipo di prodotto. |
| `sigle` | vuoto | 984 | Le parole da lasciare maiuscole nelle descrizioni di categoria, reparto e stagione, separate da virgole. |
| `nazione` | vuoto | 984 | La nazione dei testi web (**Web Nome**, **Web Des. Breve**, **Web Des. Estesa**) da mandare sul negozio. Vuota, i testi senza nazione. |

!!! note "Cambiare tipo_prodotto, sigle o nazione"

    Quando cambi `tipo_prodotto`, `sigle` o `nazione`, al giro successivo l'operazione
    prodotti rimanda **tutti** i prodotti, una volta, per allinearli. Su un
    catalogo grande richiede qualche ora.

## [ARTICOLI]

Usata dall'importazione degli ordini (980).

| Chiave | Predefinito | Descrizione |
|---|---|---|
| `cod_spese_tra` | vuoto | L'articolo su cui registrare le spese di trasporto. Vuoto, le spese non entrano. |
| `cod_buono_sco` | vuoto | L'articolo su cui registrare lo sconto dell'ordine. Vuoto, lo sconto non entra. |

## [STATI]

Usata dall'importazione degli ordini (980): gli stati di pagamento di Shopify
da importare, con `1`. Le chiavi sono `paid`, `partially_paid`,
`authorized`, `pending`, `partially_refunded`, `refunded`, `voided`,
`expired`; il significato è in [Ordini](ordini.md#quali-ordini-si-importano).
Uno stato assente non si importa.

## [PAGAMENTI]

Usata dall'importazione degli ordini (980): per ogni metodo di pagamento di
Shopify, il codice del pagamento di Facile. La chiave è `pag_` seguito dal
nome del metodo, per esempio `pag_shopify_payments`. Vedi
[Il metodo di pagamento](ordini.md#il-metodo-di-pagamento).

## [STATO_ORDINI]

Usata dall'operazione stato degli ordini (990). Tutte le chiavi valgono `0`
se mancano.

| Chiave | Descrizione |
|---|---|
| `evaso` | `1` = gli ordini evasi in Facile si evadono anche su Shopify. |
| `annullato` | `1` = gli ordini annullati in Facile si annullano anche su Shopify, senza rimborso automatico. |
| `avvisa_cliente` | `1` = Shopify manda l'email al cliente. |

## [TAGLIECOL]

Solo nella versione taglie e colori, usata dai prodotti (984).

| Chiave | Predefinito | Descrizione |
|---|---|---|
| `opzione_taglia` | Taglia | Il nome dell'opzione taglia sul negozio. |
| `opzione_colore` | Colore | Il nome dell'opzione colore sul negozio. |

## [DEBUG]

Servono per le prove e per l'assistenza: in uso normale vanno lasciate
vuote o a `0`.

| Chiave | Predefinito | Descrizione |
|---|---|---|
| `codici` | vuoto | Elenco di codici articolo separati da virgole: prodotti e immagini lavorano solo su questi. |
| `limite` | 0 | Prodotti e immagini si fermano dopo questo numero di articoli; `0` = tutti. |
| `log_json` | 0 | `1` = ogni richiesta a Shopify e la sua risposta vengono salvate in file `.json` nella cartella `log`. Per le prove: i file contengono dati dei clienti. |

## Vedi anche

- [Connettore Shopify](index.md)
- [Esecuzione continua](ciclo.md)
- [E-commerce: avvio e registro di FacileToWeb](../index.md)
