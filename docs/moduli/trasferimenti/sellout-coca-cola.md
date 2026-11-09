---
title: Sellout Coca Cola
description: Come FacileToWeb prepara ogni giorno il file Excel del venduto Coca Cola, dal primo del mese a ieri, e lo invia in SFTP al server indicato dal fornitore.
modulo: Trasferimenti
---

# Sellout Coca Cola

Il sellout Coca Cola è il file con cui il grossista comunica a Coca Cola che
cosa ha venduto, a chi e quando. Lo prepara **FacileToWeb**, senza finestre:
ogni volta che parte scrive il file Excel del mese in corso, dal primo del
mese a ieri, e se nella configurazione c'è un server lo invia in **SFTP**.
Pianificato una volta al giorno, il file sul server è sempre aggiornato alla
sera prima.

!!! info "In sintesi"

    - **Programma:** [FacileToWeb](../ecommerce/index.md), operazione **992**
    - **Periodo:** dal primo del mese a ieri; il primo del mese, il mese precedente completo
    - **File:** `COCACOLA_AAAAMM.xls`, uno al mese, riscritto ad ogni giro
    - **Invio:** SFTP (oppure FTP); senza server il file resta solo sul PC
    - **Licenza:** nessun modulo aggiuntivo

---

## Come funziona

Ad ogni giro FacileToWeb:

1. calcola il periodo: dal **primo del mese di ieri a ieri**. Il primo del
   mese esce così il mese precedente completo, e il primo gennaio il dicembre
   dell'anno prima, letto dal suo esercizio;
2. raccoglie i movimenti di magazzino dei **clienti** in quel periodo, sugli
   articoli dei **marchi** indicati nella configurazione;
3. scrive il file Excel nella cartella locale, sostituendo quello del giro
   precedente;
4. se è indicato un server, lo invia, sovrascrivendo il file con lo stesso
   nome.

Il file si chiama `COCACOLA_` seguito da anno e mese del periodo: per
esempio `COCACOLA_202611.xls` per novembre 2026. Se nel periodo non c'è
nessuna vendita, il file contiene solo le intestazioni e viene inviato lo
stesso.

### Quali movimenti entrano

Entrano solo i movimenti con una [causale di magazzino](../magazzino/causali-magazzino.md)
che tocca il venduto o i resi dei clienti. La quantità nel file è quella del
movimento, con il segno che le dà la causale:

| La causale mette | Segno | Esempio |
|---|---|---|
| **+** su *Venduta* (quantità) o su *Venduto* (valore) | Come nel movimento | Un DDT o una fattura di vendita: 10 pezzi escono come `10` |
| **−** su *Venduta* o su *Venduto* | Rovesciato | Una nota di credito che toglie dal venduto: 10 pezzi escono come `-10` |
| **+** su *Resa da Clienti* | Rovesciato | Un reso del cliente: 10 pezzi rientrati escono come `-10` |
| **−** su *Resa da Clienti* | Come nel movimento | L'annullamento di un reso: esce come `10`, e compensa il `-10` del reso |

In pratica nel file **le vendite sono positive e i resi negativi**, in
qualunque modo il reso sia registrato in Facile: con una causale di reso,
con una nota di credito, o con la causale di vendita e la quantità negativa
(come capita al banco), che esce negativa così com'è. Se una causale mette
sia **+** su *Venduta* sia **+** su *Resa da Clienti*, vale il reso.

I movimenti con causali che non toccano questi contatori (carichi,
trasferimenti, rettifiche) non entrano. Gli articoli devono avere il
[marchio](../magazzino/marchi.md) indicato in anagrafica: un articolo senza
marchio, o con un marchio diverso, resta fuori.

## Il tracciato

Un foglio Excel con una riga di intestazione e una riga per movimento. Le
prime venti colonne sono quelle del file che il grossista mandava a mano, con
le intestazioni scritte **esattamente come nell'originale**, refusi compresi:
chi riceve il file può leggere le colonne per nome. Le ultime due, l'agente,
sono state aggiunte su richiesta.

| # | Intestazione | Contenuto |
|---|---|---|
| 1 | Codice Cilente di consegna | `C` e il codice del cliente su cinque cifre (`C01690`); se il movimento ha una [destinazione diversa](../anagrafiche/destinazioni-diverse.md), `D` e il codice della destinazione (`D00740`). |
| 2 | Nome cliente di consegna | La ragione sociale della destinazione, o del cliente. |
| 3 | Indirizzo | L'indirizzo della destinazione, o del cliente. |
| 4 | CAP di consegna | Il CAP della destinazione, o del cliente. |
| 5 | Città di consegna | La città della destinazione, o del cliente. |
| 6 | P.Iva | Il codice fiscale o la partita IVA della destinazione; se manca, la partita IVA del cliente. |
| 7 | Sotto-canale di vendita di consegna | Il codice del [canale di vendita](../altre-tabelle/canali-di-vendita.md) del cliente: la destinazione non ha un canale proprio. Vuota se il cliente non ne ha. |
| 8 | Codice Prodotto Coca-Cola | Vuota. |
| 9 | Codice prodotto grossista | Il codice dell'articolo in Facile. |
| 10 | Descrizione Prod. Coca Cola | Vuota. |
| 11 | Descrizione Prod. Grossista | La descrizione dell'articolo. |
| 12 | Unità di misura | Il codice dell'[unità di misura](../magazzino/unita-di-misura.md) del movimento. |
| 13 | Q.ta | La quantità del movimento, con tre decimali e con il segno descritto sopra. |
| 14 | Data consegna | La data del movimento. |
| 15 | N° doc cosegna o N° fattura | Il numero della fattura con il registro (`18592/A`); se la merce non è ancora fatturata, il numero del documento di consegna (`1/CV`). Vuota per le vendite al banco con scontrino, che non hanno né l'uno né l'altro. |
| 16 | Codice Cilente di fatturazione | `C` e il codice del cliente su cinque cifre. |
| 17 | Nome cliente di fatturazione | La ragione sociale del cliente. |
| 18 | CAP di fatturazione | Il CAP del cliente. |
| 19 | Città di consegna | La città del cliente. L'intestazione è la stessa della colonna 5, come nel file originale. |
| 20 | Sotto-canale di vendita di fatturazione | Il codice del canale di vendita del cliente. |
| 21 | Codice agente | Il codice dell'[agente](../anagrafiche/anagrafica-agenti.md) del movimento; vuota se non c'è. |
| 22 | Nome agente | Il nome dell'agente. |

Un codice cliente di sei cifre o più esce per intero dopo la `C`
(`C254574`).

## Il file di configurazione

L'installazione di Facile non porta il file: si parte da questo modello.

[:material-download: Scarica cocacola.ini](../../assets/modelli/cocacola.ini){ .md-button download="cocacola.ini" }

Le sezioni `[LOGIN]` e `[COMMAND]` sono quelle comuni a tutte le operazioni di
FacileToWeb, descritte in
[E-commerce](../ecommerce/index.md#il-file-di-configurazione). Le altre:

| Sezione | Chiave | Predefinito | Descrizione |
|---|---|---|---|
| `[OPTIONS]` | `marchi` | — | Uno o più codici marchio, separati da virgola, punto e virgola o spazio. **Obbligatorio**: senza marchi l'esportazione non parte. |
| `[OPTIONS]` | `path` | la cartella `out` di Facile | La cartella in cui scrivere il file. |
| `[OPTIONS]` | `mese` | vuoto | Un mese da esportare per intero, nella forma `AAAAMM` (per esempio `202608`). Serve per rimandare un mese passato o per una prova; per il lavoro di ogni giorno va lasciato vuoto. |
| `[FTP]` | `server` | vuoto | L'indirizzo del server. **Se è vuoto il file non viene inviato** e resta solo nella cartella locale. |
| `[FTP]` | `protocol` | `sftp` | `sftp`, oppure `ftp` per un server FTP normale. |
| `[FTP]` | `port` | 22 in SFTP, 21 in FTP | La porta del server. |
| `[FTP]` | `user`, `password` | — | L'utente e la password del server. Obbligatori quando c'è il server. |
| `[FTP]` | `directory` | vuoto | La cartella del server in cui mettere il file; vuota, quella in cui il server fa entrare. |
| `[FTP]` | `fingerprint` | vuoto | Solo SFTP: l'impronta della chiave del server, che chi gestisce il server può comunicare. Se è indicata, il collegamento a un server con un'impronta diversa viene rifiutato. |
| `[FTP]` | `passive` | 1 | Solo FTP: la modalità passiva. |
| `[FTP]` | `log` | 0 | Con `1` salva nella cartella `log` il dialogo con il server (`sftplog…` o `ftplog…`), per l'assistenza. |

!!! warning "Il file contiene due password"

    Oltre a quella dell'utente di Facile, nel file c'è la password del server
    del fornitore. Tienilo in una cartella a cui accede solo chi deve.

Il contenuto del modello:

```ini
--8<-- "docs/assets/modelli/cocacola.ini"
```

## Metterlo in funzione

1. Scarica il modello `cocacola.ini` e salvalo nella cartella `cfg` di
   Facile. Compila `[LOGIN]` e i marchi in `[OPTIONS]`, e lascia **vuoto**
   `server` nella sezione `[FTP]`.
2. Lancialo a mano, dalla cartella di Facile:
   `FacileToWeb.exe -inicocacola.ini -ditta1`.
3. Apri il file nella cartella `out` e fallo controllare a chi lo riceve.
4. Compila la sezione `[FTP]` con i dati del server e rilancia: nel registro devono comparire le
   righe di connessione e `Fine Upload …`.
5. Pianificalo una volta al giorno, di notte o al mattino presto, come
   descritto in
   [Avviarlo a orari fissi](../ecommerce/index.md#avviarlo-a-orari-fissi).
   Il file sul server viene così sostituito ogni giorno con quello aggiornato.

## Controlli e messaggi

L'esportazione non mostra finestre: tutto quello che succede è nel registro
`operation_992_AAAAMMGG.txt`, nella cartella `log`.

| Riga del registro | Causa | Cosa fare |
|---|---|---|
| `Nessun marchio indicato nella configurazione: impostare marchi= nella sezione [OPTIONS]` | Nella configurazione manca `marchi`, oppure è vuoto. | Indica i codici dei marchi da esportare. |
| `Codice marchio non valido nella configurazione: …` | In `marchi` c'è qualcosa che non è un codice numerico. | Correggi l'elenco: solo numeri, separati da virgola. |
| `Mese non valido nella configurazione: … (formato AAAAMM)` | `mese` non è nella forma anno e mese, sei cifre. | Scrivilo come `202608`, oppure lascialo vuoto. |
| `Nessuna vendita nel periodo: il file contiene solo le intestazioni` | Nel periodo non ci sono vendite né resi degli articoli dei marchi indicati. Il file viene scritto e inviato lo stesso. | Normale nei primi giorni del mese. Se dura, controlla i marchi degli articoli e le causali dei documenti. |
| `Impossibile salvare il file …` | La cartella non esiste o il file è aperto in Excel. | Controlla `path` e chiudi il file. |
| `Server FTP non impostato: il file resta solo in locale` | La sezione `[FTP]` non ha `server`. | Normale durante le prove; per l'invio indica il server. |
| `Utente o password del server FTP non impostati: il file non e' stato inviato` | C'è il server ma mancano `user` o `password`. | Indica utente e password del server. |
| `Protocollo non riconosciuto nella configurazione: … (sftp oppure ftp)` | `protocol` non è né `sftp` né `ftp`. | Correggi il valore. |
| `L'impronta del server SFTP (…) non corrisponde a quella indicata nella configurazione (…)` | Il server ha una chiave diversa da quella attesa: è cambiato, oppure non è il server giusto. | Verifica l'impronta con chi gestisce il server prima di aggiornare `fingerprint`. |

Gli errori di collegamento e di invio (server irraggiungibile, utente o
password rifiutati, cartella inesistente) finiscono nel registro con il
testo restituito dal server, e anche in un file `sftperr…` (o `ftperr…`)
nella cartella `log`. Il file locale resta comunque scritto: al giro dopo
viene inviato di nuovo, aggiornato.

## Vedi anche

- [E-commerce](../ecommerce/index.md): come si avvia FacileToWeb e il registro delle operazioni
- [Marchi](../magazzino/marchi.md)
- [Causali di magazzino](../magazzino/causali-magazzino.md)
- [Destinazioni diverse](../anagrafiche/destinazioni-diverse.md)
- [Esportazione documenti per tracciato](esportazione-documenti.md): gli altri sellout
