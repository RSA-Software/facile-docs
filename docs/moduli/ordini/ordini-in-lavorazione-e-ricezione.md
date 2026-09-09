---
title: Ordini in lavorazione e in ricezione
description: Le due griglie che seguono l'ordine dopo l'inserimento — quelli dei clienti da evadere e quelli ai fornitori in attesa di arrivo — e la cancellazione degli ordini ricevuti.
modulo: Ordini
maschera_id: IDD_ORDINI_LAVORAZIONE
---

# Ordini in lavorazione e in ricezione

Un ordine registrato non è ancora finito: quello del cliente va evaso, quello
al fornitore va ricevuto. Due griglie seguono i due percorsi.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Ordini ▸ Ordini da Clienti ▸ Ordini in Lavorazione
        - Menu ▸ Ordini ▸ Ordini a Fornitori ▸ Ordini in Ricezione
        - Menu ▸ Ordini ▸ Ordini a Fornitori ▸ Cancellazione Ordini Ricevuti
    - **Scorciatoia:** ++f2++ apre la riga, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md); **Cancellazione Ordini Ricevuti** richiede in più che l'utente non abbia il **Blocco Cancellazioni Dati**

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Ordini in Lavorazione** | L'elenco degli ordini dei clienti ancora da evadere, con tutto quello che serve per portarli a documento: attribuzione di lotti o partite, emissione dei documenti, controllo dei prezzi, scomposizione. |
| **Ordini in Ricezione** | L'elenco degli ordini fatti ai fornitori in attesa di arrivo. La finestra si chiama *Ordini da Ricevere*. |
| **Cancellazione Ordini Ricevuti** | Toglie dall'archivio gli ordini a fornitore completamente evasi di un periodo che scegli tu. |

## Prerequisiti

Prima di usare queste griglie occorre avere gli ordini in archivio, inseriti
dalla [maschera dei documenti](../vendite/documento-di-vendita.md) o arrivati
dallo [scambio con l'esterno](scambio-ordini.md).

Per emettere i documenti dagli ordini in lavorazione, gli ordini devono essere
**confermati**: su un ordine non confermato i comandi si rifiutano di lavorare.

## La maschera

![Ordini in lavorazione](../../assets/img/ordini/ordini-in-lavorazione-e-ricezione.png)

Entrambe hanno la stessa forma: in alto i filtri, poi una barra di avanzamento
e sotto la griglia. Il titolo di **Ordini in Lavorazione** riporta la ditta e
l'anno di lavoro — *Ordini in Lavorazione - 00001 NOME DITTA - Anno :2026*.

## Campi

### Ordini in Lavorazione

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Cliente** | | Restringe agli ordini di un cliente. A fianco compare la ragione sociale. | codice |
| **Registro** | | Restringe a un registro di numerazione. | `TUTTI` o una voce dell'elenco |

{: .campi }

Le colonne della griglia sono **Sel.**, **Codice**, **Numero**, **Data**,
**Tipo**, **Stato**, **Cons.**, **Totale**, **Cod.Cli.**, **Cliente**,
**Destinazione**, **Agente**, **Trasportatore** e **anno**. La prima colonna è
la casella con cui si scelgono le righe su cui agire.

### Ordini in Ricezione

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Fornitore** | | Restringe agli ordini fatti a un fornitore. A fianco compare la ragione sociale. | codice |

{: .campi }

Le colonne sono **Codice**, **Anno**, **Numero**, **Data**, **Tipo**,
**Arrivo**, **Totale**, **Cod. For.** e **Fornitore**.

### Scomposizione Ordine per Fornitore

Si apre da **F6- Scomponi** sull'ordine scelto.

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Numero Riferimento** | ● | L'ordine da scomporre. | numero |
| **Registro** | | Il registro dell'ordine di partenza. | voce dell'elenco |
| **Reg. Ordini Generati** | ● | Il registro su cui numerare gli ordini che nascono dalla scomposizione. | voce dell'elenco |
| **Criterio Scomposizione** | ● | Come dividere l'ordine. | `FORNITORE` |

{: .campi }

## Pulsanti e comandi

### Ordini in Lavorazione

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2- Modifica** | ++f2++ | Apre l'ordine della riga corrente. |
| **Sel. Tutti** | | Spunta tutte le righe. |
| **Desel. Tutti** | | Toglie la spunta da tutte. |
| **F3- Lotti** *(o* **F3- Partite** *)* | ++f3++ | Attribuisce automaticamente lotti o partite agli ordini scelti. L'etichetta dipende da come è configurata la gestione. |
| **F4- Documenti** | ++f4++ | Emette i documenti di vendita dagli ordini scelti. |
| **F5- Prezzi** | ++f5++ | Apre il controllo dei prezzi dell'ordine. |
| **F6- Scomponi** | ++f6++ | Apre *Scomposizione Ordine per Fornitore*: divide un ordine in più ordini, uno per fornitore. Vale su **un solo** ordine per volta, e solo se è ancora in stato *salvato*. |
| **F7- Stampa** | ++f7++ | Stampa quello che si vede. |
| **Ricarica** | | Rilegge gli ordini dall'archivio. |

### Ordini in Ricezione

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Apri** | ++f2++ | Apre l'ordine della riga corrente. Fanno lo stesso il doppio clic e ++enter++ sulla griglia. |
| **F3 - Ricarica** | ++f3++ | Rilegge gli ordini dall'archivio. |
| **F4 - Stampa** | ++f4++ | Stampa l'ordine della riga. Se l'ordine è ancora in stato *salvato*, prima di stampare ne ricalcola i totali. |

## Come si fa

### Evadere gli ordini della giornata

1. Apri **Menu ▸ Ordini ▸ Ordini da Clienti ▸ Ordini in Lavorazione**.
2. Restringi per **Cliente** o per **Registro** se serve.
3. Spunta gli ordini da evadere, o premi **Sel. Tutti**.
4. Se la merce è a lotti o a partite, premi prima **F3** per attribuirli.
5. Premi **F4- Documenti**: Facile genera i documenti di vendita.

### Vedere cosa deve ancora arrivare da un fornitore

1. Apri **Menu ▸ Ordini ▸ Ordini a Fornitori ▸ Ordini in Ricezione**.
2. Indica il **Fornitore**.
3. La colonna **Arrivo** dice quando la merce è attesa.

### Ripulire gli ordini a fornitore già arrivati

1. **Fai una copia di sicurezza degli archivi.**
2. Apri **Menu ▸ Ordini ▸ Ordini a Fornitori ▸ Cancellazione Ordini
   Ricevuti**.
3. Indica **Data Iniziale** e **Data Finale**. All'apertura sono tutte e due
   quella di oggi: il periodo va allargato a mano.
4. Premi **F2 - OK**.
5. Leggi il messaggio, che dice **quanti** ordini sta per cancellare e in che
   periodo. Se il numero non è quello che ti aspettavi, rispondi **No** e
   ricontrolla le date.
6. Rispondi **Sì**. Alla fine Facile dice quanti documenti ha cancellato.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Devi selezionare un solo ordine!* | Il comando lavora su una riga sola e ne hai spuntate più d'una. | Lascia la spunta su una sola riga. |
| *Devi selezionare almeno un ordine!* | Nessuna riga è spuntata. | Spunta le righe su cui vuoi agire. |
| *Ordine non Trovato in Archivio!* | La riga della griglia non corrisponde più a un ordine. | Premi **Ricarica** e riprova. |
| *L'ordine non é stato ancora confermato!* | Si stanno emettendo documenti da un ordine non confermato. | Apri l'ordine e confermalo. |
| *Non possono essere elaborati ordini non confermati!* | Fra le righe scelte c'è un ordine non confermato. | Togli la spunta a quelle righe o conferma gli ordini. |
| *Non possono essere elaborati ordini confermati o parzialmente evasi!* | Il comando vale solo su ordini ancora intatti. | Scegli altre righe. |
| *Operazione non consentita su Ordine parzialmente evaso!* | L'ordine è già stato evaso in parte. | Lavora sul documento già emesso. |
| *Operazione non consentita per lo stato dell' Ordine!* | Lo stato dell'ordine non ammette il comando. | Guarda la colonna **Stato**. |
| *Non é possibile emettere documenti per questo tipo di ordine!* | L'ordine è di un genere che non genera documenti. | Nessuna azione: è così per costruzione. |
| *Quantità inferiori a zero escluse dal corpo del documento!* | L'ordine ha righe con quantità negativa. | Sono state saltate: controlla il documento generato. |
| *Documento non modificabile !* | Il documento generato è già chiuso. | Non si corregge da qui. |
| *Impossibile elaborare i documenti!* / *Impossibile elaborare il documento!* | L'elaborazione non è andata a buon fine. | Riprova; se insiste, segnala all'assistenza. |
| *Errore su cancellazione movimenti dell' ordine!<br>Segnalare il problema all' assistenza e annullare l' ordine!* | I movimenti di magazzino dell'ordine non si sono potuti togliere. | Annulla l'ordine e chiama l'assistenza: gli archivi restano disallineati. |
| *Vuoi calcolare l' Iva sulla Fattura Pro Forma ?* | Si sta generando una pro forma. | **Sì** per l'IVA in fattura, **No** per lasciarla fuori. |
| *Confermi la Scomposizione dell'Ordine?* | Conferma prima di dividere l'ordine. | **Sì** procede. |
| *Scomposizione Ordine Completata!* | La scomposizione è andata a buon fine. | Controlla gli ordini generati dalla [gestione documenti](../vendite/gestione-documenti.md). |
| *Verranno cancellati definitivamente … ordini ricevuti con data fra il … e il …, insieme alle loro righe. L' operazione non si può annullare. Vuoi continuare ?* | La conferma della cancellazione, con il numero dei documenti trovati. | Controlla il numero e il periodo. **Sì** cancella; la risposta preimpostata è **No**. |
| *Nessun ordine ricevuto con data fra il … e il …* | Nel periodo indicato non c'è niente da cancellare. | Allarga il periodo, o non c'era nulla da ripulire. |
| *Cancellati … documenti.* | La cancellazione è finita. | Nulla: è il resoconto. |
| *Cancellazione interrotta: … documenti su …* | Hai premuto **Annulla** sulla barra di avanzamento. | I documenti già cancellati non tornano: ripeti pure la procedura per togliere i rimanenti. |
| *Cancellazioni non abilitate per l' utente !* | L'utente ha il **Blocco Cancellazioni Dati**. | Serve un utente abilitato, o va tolto il blocco da [Archivi ▸ Utenti](../anagrafiche/utenti.md). |
| *La data è esterna all' esercizio corrente.* | Una delle due date non appartiene all'esercizio aperto. | Correggila: gli ordini degli altri esercizi stanno in archivi separati. |

## Note

!!! warning "La cancellazione è definitiva"

    **Cancellazione Ordini Ricevuti** toglie dall'archivio gli ordini a
    fornitore in stato *evaso* del periodo indicato, con le loro righe e senza
    possibilità di tornare indietro. La conferma dice **quanti** sono, ma non
    quali: stampa l'elenco da **Ordini in Ricezione** e fai una copia degli
    archivi prima di lanciarla.

!!! note "«Ricevuto» ed «evaso» sono lo stesso stato"

    Facile registra un unico stato per l'ordine consegnato per intero, e lo
    chiama con parole diverse a seconda del verso: **EVASO** su un ordine di un
    cliente, **RICEVUTO** su un ordine a un fornitore. Esiste anche lo stato
    corrispondente per la consegna **parziale**.

    È per questo che le due cancellazioni — *Ordini Evasi* e *Ordini Ricevuti* —
    si somigliano tanto: fanno la stessa cosa sui due tipi di documento.

!!! note "A cosa serve scomporre un ordine"

    Un cliente ordina venti articoli che arrivano da quattro fornitori diversi.
    **F6- Scomponi** trasforma quell'ordine unico in quattro ordini, uno per
    fornitore, così ciascuno si evade per conto suo. Funziona su un ordine per
    volta e solo finché l'ordine è ancora **salvato**: dopo la conferma o
    l'evasione parziale il comando si rifiuta.

!!! note "Il numero nella domanda è il controllo vero"

    Sia questa cancellazione sia quella degli [ordini
    evasi](../vendite/ordini-clienti.md) chiedono conferma una volta sola, ma
    la domanda dice quanti documenti sta per togliere e in che periodo, con il
    pulsante **No** già scelto. Se il numero è molto più grande di quello che
    ti aspetti, il periodo è sbagliato: rispondi **No**.

## Vedi anche

- [Gestione documenti](../vendite/gestione-documenti.md)
- [Inserimento e Modifica documenti](../vendite/documento-di-vendita.md)
- [Ordini clienti](../vendite/ordini-clienti.md)
- [Scambio degli ordini con l'esterno](scambio-ordini.md)
