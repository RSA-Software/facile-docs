---
title: E-commerce
description: Come Facile si collega ai negozi online con il programma FacileToWeb, come si configura con i file ini, come si avvia e dove si legge il registro delle operazioni.
modulo: E-commerce
---

# E-commerce

Facile e il negozio online si parlano attraverso **FacileToWeb**, un programma
che si installa insieme a Facile e lavora senza finestre: legge dall'archivio
articoli, giacenze e prezzi e li porta sul negozio, e porta in Facile gli
ordini che arrivano dal sito.

!!! info "In sintesi"

    - **Programma:** `FacileToWeb.exe`, nella cartella di Facile
    - **Configurazione:** un file `.ini` per ciascun lavoro, nella cartella `cfg`
    - **Registro:** un file per operazione e per giorno, nella cartella `log`
    - **Avvio:** a mano, dall'Utilità di pianificazione di Windows, oppure in
      esecuzione continua

---

## A cosa serve

Un negozio online ha bisogno ogni giorno degli stessi dati che stanno già in
Facile: quali articoli vendere, a che prezzo, quanti ce ne sono. Ricopiarli a
mano non è pensabile, e il negozio resterebbe indietro al primo carico di
merce. FacileToWeb fa questo lavoro al posto tuo, una volta configurato:

- **verso il negozio** manda gli articoli che hai preparato per il web, con
  descrizioni, fotografie, categorie, giacenze e prezzi;
- **verso Facile** porta gli ordini dei clienti del sito, che diventano
  ordini cliente come quelli inseriti a mano.

Ogni lavoro è una **operazione**, identificata da un numero: per esempio, con
Shopify, la 982 aggiorna le giacenze e la 980 importa gli ordini. Il numero
dell'operazione si scrive nel file di configurazione.

## Negozi collegati

| Negozio | Pagina |
|---|---|
| Shopify | [Connettore Shopify](shopify/index.md) |

FacileToWeb contiene anche i collegamenti con WooCommerce, PrestaShop,
Magento e nopCommerce, che questo manuale non descrive ancora.

## Prerequisiti

Prima di usare FacileToWeb occorre:

- che il computer su cui gira raggiunga l'archivio di Facile, come una
  normale postazione;
- un **utente di Facile** da dedicare a FacileToWeb, con la sua password;
- gli articoli preparati per il sito da
  [Impostazione Dati Web](../anagrafiche/impostazione-dati-web.md): almeno
  la casella **Includi WEB**, il nome e la descrizione per il sito, le
  categorie del catalogo e le fotografie.

## Come si avvia

FacileToWeb si lancia con due parametri:

```
FacileToWeb.exe -ini<nome del file> -ditta<codice della ditta>
```

per esempio:

```
FacileToWeb.exe -iniciclo_shopify.ini -ditta1
```

- **`-ini`** indica il file di configurazione, che deve stare nella cartella
  `cfg` di Facile. Il nome va scritto **attaccato** a `-ini`, senza spazi.
- **`-ditta`** indica la ditta su cui lavorare. Se manca, si lavora sulla
  ditta 1.

Il programma va avviato con la **cartella di Facile come cartella di
lavoro**: da lì ricava dove si trovano le cartelle `cfg` e `log`. Quando
Facile gira su un server remoto (Terminal Server), le cartelle `cfg` e `log`
sono quelle dell'utente, in `%LOCALAPPDATA%\Facile`.

Quando ha finito l'operazione, FacileToWeb si chiude da solo. Fa eccezione
l'[esecuzione continua](shopify/ciclo.md) di Shopify, che lavora a giri
finché non la si ferma.

### Avviarlo a orari fissi

Per far girare un'operazione da sola si usa l'**Utilità di pianificazione**
di Windows:

1. Apri l'Utilità di pianificazione e scegli **Crea attività**.
2. Nella scheda **Generale** scegli di eseguire l'attività anche quando
   l'utente non è connesso.
3. Nella scheda **Attivazione** imposta quando partire: per esempio ogni
   giorno con ripetizione ogni 15 minuti, oppure all'avvio del computer per
   l'esecuzione continua.
4. Nella scheda **Azioni** scegli **Avvia programma**, indica
   `FacileToWeb.exe` con il suo percorso completo, scrivi i parametri in
   **Aggiungi argomenti** e la cartella di Facile in **Inizio in**.
5. Conferma: l'operazione parte all'orario indicato e scrive il suo
   registro nella cartella `log`.

!!! warning "Prova a mano prima di pianificare"

    Se il file di configurazione è sbagliato, FacileToWeb lo dice con una
    finestra di messaggio (vedi *Controlli e messaggi* qui sotto). In
    un'attività pianificata che gira senza utente connesso quella finestra
    non la vede nessuno e il programma resta fermo ad aspettare. Lancia ogni
    configurazione nuova almeno una volta a mano, da una postazione.

## Il file di configurazione

Ogni file `.ini` descrive un lavoro. Due sezioni sono comuni a tutti i
negozi:

```ini
[LOGIN]
server            = FAIRCOMS
host              = 192.168.1.101
arc               = NOMEARCHIVIO
usr               = UTENTE
pwd               = password

[COMMAND]
operation         = 982
```

| Sezione | Chiave | Descrizione |
|---|---|---|
| `[LOGIN]` | `server`, `host` | Il server dell'archivio e il suo indirizzo, come nell'accesso a Facile. |
| `[LOGIN]` | `arc` | L'archivio su cui lavorare. |
| `[LOGIN]` | `usr`, `pwd` | L'utente di Facile e la sua password. |
| `[LOGIN]` | `port` | La porta del motore SQL dell'archivio; se manca, 6597. |
| `[LOGIN]` | `pg_port` | La porta di PostgreSQL; se manca, 5432. |
| `[COMMAND]` | `operation` | Il numero dell'operazione da eseguire. |
| `[COMMAND]` | `interval` | Usato da alcune operazioni, per esempio per decidere quanti giorni di ordini rileggere. |

Le altre sezioni dipendono dal negozio: per Shopify sono descritte nel
[file di configurazione del connettore](shopify/configurazione.md), da cui
si può scaricare un file di prova completo. L'installazione di Facile non
porta file di configurazione.

!!! warning "Il file contiene password"

    Nel file ci sono la password dell'utente di Facile e la chiave di
    accesso al negozio. Tienilo in una cartella a cui accede solo chi deve.

## Il registro delle operazioni

Ogni operazione scrive quello che fa in un file di testo nella cartella
`log`, che si chiama

```
operation_<numero dell'operazione>_<AAAAMMGG>.txt
```

per esempio `operation_982_20261010.txt`. Le operazioni dello stesso numero
nello stesso giorno si accodano nello stesso file. Ogni riga comincia con
data e ora.

Il registro si può aprire, con il Blocco note o con qualsiasi altro
programma, **anche mentre l'operazione è in corso**: è il modo più semplice
per vedere a che punto è. Non va modificato mentre il programma scrive.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impossibile recuperare la directory di lavoro.* | Windows non ha dato al programma la cartella da cui è stato avviato. | Avvia FacileToWeb indicando la cartella di Facile come cartella di lavoro (nell'Utilità di pianificazione, campo **Inizio in**). |
| *File INI non impostato su linea di comando.* | Manca il parametro `-ini`, oppure fra `-ini` e il nome del file c'è uno spazio. | Scrivi il nome del file attaccato al parametro: `-iniciclo_shopify.ini`. |
| *Operazione da eseguire non impostata nel file INI.* | Nel file manca `operation` nella sezione `[COMMAND]`, oppure il file non esiste nella cartella `cfg`. | Controlla il nome del file e la sua posizione, e che `[COMMAND]` contenga il numero dell'operazione. |

Gli altri problemi non compaiono a video ma nel registro. I più comuni
all'avvio:

| Riga del registro | Causa | Cosa fare |
|---|---|---|
| `Manca l' User ID : Inserire il parametro -usr` | Nella sezione `[LOGIN]` manca `usr`. | Indica l'utente di Facile. |
| `Manca la Password : Inserire il parametro -pwd` | Nella sezione `[LOGIN]` manca `pwd`. | Indica la password dell'utente. |
| `Manca il nome del server : Inserire i parametri -host e -server` | Nella sezione `[LOGIN]` mancano `server` e `host`. | Indica il server dell'archivio. |
| `Manca l' Archivio : Inserire il parametro -arc` | Nella sezione `[LOGIN]` manca `arc`. | Indica l'archivio. |
| `Apertura del database fallita...` | L'archivio non è raggiungibile, oppure utente o password sono sbagliati. | Prova ad accedere a Facile con gli stessi dati dalla stessa macchina. |
| `Operation Not Found!` | Il numero in `operation` non corrisponde a nessuna operazione. | Correggi il numero: per Shopify vedi l'[elenco delle operazioni](shopify/index.md#le-operazioni). |

## Vedi anche

- [Connettore Shopify](shopify/index.md)
- [Impostazione Dati Web](../anagrafiche/impostazione-dati-web.md)
- [Marchi](../magazzino/marchi.md): la colonna **Stock Ecommerce**
