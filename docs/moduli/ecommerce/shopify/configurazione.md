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

Questo file fa girare l'[esecuzione continua](ciclo.md) con le scelte più
comuni. Copialo, dagli un nome e completa le parti in maiuscolo.

```ini
[LOGIN]
server            = FAIRCOMS
host              = 192.168.1.101
arc               = ARCHIVIO
usr               = UTENTE
pwd               = PASSWORD

[COMMAND]
operation         = 979
interval          = 2

[CICLO]
pausa             = 300
exit              = 0
setup             = 0
abbina            = 0
ordini            = 1
prodotti          = 3600
giacenze          = 1
prezzi            = 1
ingrosso          = 0
stato_ordini      = 0
immagini          = 86400

[ECOMMERCE]
web_host          = NOMENEGOZIO.myshopify.com
api_version       = 2026-10
token             = TOKEN
;client_id        =
;client_secret    =
location_name     =
modalita          = B2C
listino_web       = 1
listino_uff       = 1
listino_ing       = 2
depositi_disp     = 1
deposito          = 1
registro          =
pagamento         = 1
cateco            = 0
cliente_generico  = 0
verifica_spariti  = 1
tipo_prodotto     = 1
sigle             = USB,LED

[ARTICOLI]
cod_spese_tra     = CODICE ARTICOLO SPESE
cod_buono_sco     = CODICE ARTICOLO SCONTO

[STATI]
paid              = 1
partially_paid    = 1
authorized        = 1
pending           = 0

[PAGAMENTI]
pag_manual        = 1
pag_shopify_payments = 1

[STATO_ORDINI]
evaso             = 0
annullato         = 0
avvisa_cliente    = 0

[TAGLIECOL]
opzione_taglia    = Taglia
opzione_colore    = Colore

[DEBUG]
codici            =
limite            = 0
log_json          = 0
```

<!-- DA VERIFICARE: se l'installazione di Facile porta nella cartella cfg i file di esempio del connettore (ciclo_shopify.ini e gli altri) -->

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
| `token` | — | tutte | Il token di accesso dell'app creata dall'amministrazione del negozio. Se c'è, vince su `client_id` e `client_secret`. |
| `client_id`, `client_secret` | — | tutte | Le credenziali dell'app creata dal Dev Dashboard di Shopify, in alternativa al token. |
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

!!! note "Cambiare tipo_prodotto o sigle"

    Quando cambi `tipo_prodotto` o `sigle`, al giro successivo l'operazione
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
