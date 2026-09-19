---
title: Provvigioni agenti e capi area
description: Le tredici voci che registrano, ricalcolano, controllano e stampano le provvigioni degli agenti e dei capi area.
modulo: Vendite
maschera_id: IDD_PROVVIGIONI
---

# Provvigioni agenti e capi area

Il sottomenu **Provvigioni Agenti - Capi Area** raccoglie tutto quello che
riguarda il compenso della rete di vendita: la registrazione delle singole
provvigioni, le attribuzioni automatiche, i ricalcoli, i controlli e le stampe.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Vendite ▸ Provvigioni Agenti - Capi Area ▸ *(una delle voci)*
    - **Scorciatoia:** ++f2++ salva o avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Inserimento**, **Modifica** | Registrano a mano una provvigione su un documento. |
| **Attribuzione Automatica Provvigioni  Mancanti** | Riempie **solo le righe rimaste a zero**, prendendo la percentuale dal listino dell'articolo. |
| **Attribuzione  Provvigioni per Cliente** | **Riscrive tutte** le righe con le quattro percentuali che indichi tu, eventualmente per un solo cliente o un solo listino. |
| **Ricalcolo Provvigioni** | Rifà i conti sui documenti già emessi. |
| **Calcolo Maturato Agenti / Capi Area** | Calcola quanto è maturato a ciascuno. |
| **Stampa Distinta Provvigioni Agenti** | La distinta analitica, documento per documento. |
| **Stampa Totali Provvigioni Agenti** | I soli totali per agente. |
| **Stampa Distinta Provvigioni Capi Area** | La distinta dei [capi area](../anagrafiche/capi-area.md). |
| **Stampa Totali Provvigioni Capi Area** | I totali per capo area. |
| **Stampa Controllo Provvigioni Anomale** | Le righe con una provvigione **sotto l'1%**, da verificare. |
| **Incentivi Personale** | Registra le campagne incentivi sugli articoli. **Solo Griffe.** |

## Prerequisiti

Prima di usare queste maschere occorre:

- avere gli [agenti](../anagrafiche/anagrafica-agenti.md) con la loro tabella
  delle provvigioni, e i [capi area](../anagrafiche/capi-area.md);
- avere i clienti collegati al proprio agente, anche con
  [Associazione gruppi e giri](../anagrafiche/associazioni.md);
- avere le percentuali sui listini, impostate in anagrafica articoli o con
  [Varia Provvigioni](../listini-vendita/variazioni-di-massa.md);
- avere emesso i documenti su cui la provvigione matura.

## La maschera

![Provvigioni](../../assets/img/vendite/provvigioni-agenti.png)

**Inserimento** e **Modifica** aprono la scheda della singola provvigione. Le
stampe aprono finestre di selezione con periodo e filtri.

## Campi

### Inserimento e Modifica

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Agente** | ● | L'[agente](../anagrafiche/anagrafica-agenti.md) a cui la provvigione spetta. | codice |
| **Capo Area** | | Il [capo area](../anagrafiche/capi-area.md) dell'agente. | codice |
| **Cliente** | ● | Il cliente del documento. | codice |
| **Data Doc.**, **Num. Doc.** | ● | Gli estremi del documento su cui la provvigione matura. | data e numero |
| *(elenco del tipo documento)* | ● | Che tipo di documento è. | `FATTURA`, `BOLLA`, `D.D.T.`, `BUONO CON.`, `FATTURA PRO FORMA`, `SCONTRINO` |
| **Registro** | | Il registro del documento. | voce dell'elenco |

{: .campi }

### Stampa Distinta Provvigioni

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Agente** | | Restringe a un agente. | codice |
| **Data Saldo Iniziale**, **Data Saldo Finale** | | Il periodo dei saldi. | date |
| **Saldati** | | Se includere le provvigioni già pagate. | `TUTTI`, `SI`, `NO` |
| **Data Doc. Iniziale**, **Data Doc. Finale** | | Il periodo dei documenti. | date |
| **Registro** | | Restringe a un registro. | `TUTTI`, oppure un registro |

{: .campi }

### Attribuzione Provvigioni per Cliente

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Da Data**, **A Data** | ● | Il periodo dei documenti su cui intervenire. | date |
| **Cliente** | | Limita a un solo cliente. Vuoto vale per tutti. | codice |
| **Listino** | | Limita ai documenti fatti su un listino. Vuoto vale per tutti. | codice |
| **Provvig. Normale** | | La percentuale da scrivere sui documenti di vendita normale (`N`). | percentuale |
| **Provvig. Trasfert** | | Quella dei documenti di trasferta (`T`). | percentuale |
| **Provvig. C.S. Vendita** | | Quella dei documenti a centro servizi (`C`). | percentuale |
| **Provvig. C.S. Trasfert** | | Quella dell'ultimo tipo di vendita (`D`). | percentuale |

{: .campi }

**Attribuzione Automatica Provvigioni Mancanti** chiede invece soltanto il
periodo: le percentuali le prende dal listino, non dall'operatore.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** o **F2 - OK** | ++f2++ | Registra, oppure avvia la stampa o l'elaborazione. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Liquidare le provvigioni del trimestre

1. Fai girare **Attribuzione Automatica Provvigioni  Mancanti**, così nessun
   documento resta scoperto.
2. Stampa **Controllo Provvigioni Anomale** e verifica le righe che escono.
3. Apri **Calcolo Maturato Agenti / Capi Area** e calcola il periodo: è il
   passaggio che segna quali provvigioni sono **saldate** e quanto è
   effettivamente maturato.
4. Stampa la **Distinta Provvigioni Agenti** per il dettaglio e i **Totali
   Provvigioni Agenti** per il riepilogo da liquidare. In **Saldati** scegli
   `SI` per liquidare solo quello che il cliente ha già pagato.

### Correggere la provvigione di un documento

1. Apri **Menu ▸ Vendite ▸ Provvigioni Agenti - Capi Area ▸ Modifica**.
2. Ritrova il documento con **Data Doc.** e **Num. Doc.**.
3. Correggi e premi **F2 - Salva**.

### Rifare i conti dopo aver cambiato le percentuali

1. Cambia le percentuali con
   [Varia Provvigioni](../listini-vendita/variazioni-di-massa.md).
2. Fai girare **Ricalcolo Provvigioni** sul periodo interessato.
3. Ristampa la distinta e confrontala con la precedente.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! warning "Il ricalcolo sovrascrive quello che è stato corretto a mano"

    **Ricalcolo Provvigioni** rifà i conti su tutti i documenti del periodo:
    le provvigioni corrette a mano tornano al valore calcolato. Se ci sono
    accordi particolari, ricalcola su un periodo stretto e ricontrolla.

!!! info "«Anomala» vuol dire sotto l'1%"

    Non c'è nessun criterio statistico dietro: la stampa elenca le **righe di
    documento la cui percentuale di provvigione è inferiore a 1**, zero
    compreso. È il modo per trovare quello che è sfuggito all'attribuzione.

    Il controllo guarda solo i documenti su cui la provvigione matura —
    fatture, bolle, DDT, buoni di consegna, fatture accompagnatorie e ricevute
    fiscali — e **solo le righe con un codice articolo**: le righe di sola
    descrizione non compaiono. Restano fuori anche le righe di sostituzione e
    gli articoli che calcolano le competenze su listino nelle vendite non
    normali.

    Si può restringere a un solo agente; lasciando il campo vuoto si legge
    `TUTTI`.

!!! warning "Le due attribuzioni non fanno la stessa cosa"

    | | **Automatica Provvigioni Mancanti** | **Provvigioni per Cliente** |
    |---|---|---|
    | Quali righe tocca | **solo quelle a zero** | **tutte** quelle del periodo |
    | Da dove prende la percentuale | dal **listino dell'articolo** | dalle **quattro percentuali che scrivi tu** |
    | Cosa si può filtrare | il periodo | periodo, **cliente** e **listino** |

    La prima è quella da usare di routine: rattoppa i buchi e non tocca niente
    di quello che è già stato deciso. La seconda è un'azione di forza —
    **sovrascrive anche le provvigioni corrette a mano**, esattamente come il
    ricalcolo — e serve quando con un cliente si è concordata una percentuale
    diversa da quella dei listini.

    Tutte e due saltano le righe senza deposito, e tutte e due chiedono
    conferma con *«Confermi l' Attribuzione delle Provvigioni ?»*.

    Le quattro percentuali corrispondono ai quattro **tipi di vendita** che il
    documento può avere — `N`, `T`, `C`, `D` — e non alle aliquote o ai
    listini.

!!! info "«Saldata» non si mette a mano: la decide il Calcolo Maturato"

    Il segno di saldato è sulla singola provvigione, e a muoverlo è **Calcolo
    Maturato Agenti / Capi Area**. Per ogni documento somma le
    [scadenze](../scadenze/gestione-scadenze.md) già pagate e:

    - se l'incassato **copre l'intero documento**, la provvigione diventa
      **saldata**; altrimenti torna non saldata;
    - scrive come **data di saldo** la data dell'**ultimo incasso** registrato
      su quel documento — è quella su cui filtrano **Data Saldo Iniziale** e
      **Data Saldo Finale**;
    - calcola il **maturato**: se la scheda dell'agente ha **Calcola maturato al
      saldo**, matura tutto solo a documento interamente incassato; altrimenti
      matura **in proporzione** a quanto è stato incassato.

    Sugli **scontrini** il conto è immediato: la provvigione nasce già saldata,
    a meno che lo scontrino non sia stato pagato a credito.

    C'è anche un campo **Saldato** nella scheda della singola provvigione, e si
    può forzare a mano; ma il primo **Calcolo Maturato** lo riporta a quello che
    risulta dagli incassi.

!!! warning "«Incentivi Personale» registra le campagne, non le calcola"

    La finestra si intitola *Campagna incentivi* e serve a descriverne una:
    **Codice**, **Descrizione**, **Data Inizio**, **Data Fine** e **Deposito**
    in testa, e sotto l'elenco degli articoli, ciascuno con una **Soglia** e
    un'**Entità** in percentuale oppure in euro per pezzo.

    Quello che vi si scrive però **non viene letto da nessun'altra parte del
    programma**: non c'è un'elaborazione che confronti il venduto con la soglia,
    né una stampa che liquidi gli incentivi. È un archivio di consultazione, e
    il calcolo resta da fare fuori da Facile.

    La voce compare **solo nella versione Griffe**; nelle altre il programma la
    toglie dal menu all'avvio.

## Vedi anche

- [Anagrafica agenti](../anagrafiche/anagrafica-agenti.md)
- [Capi area](../anagrafiche/capi-area.md)
- [Variazioni di massa dei listini](../listini-vendita/variazioni-di-massa.md)
