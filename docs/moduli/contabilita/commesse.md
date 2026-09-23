---
title: Commesse di contabilità analitica
description: Le commesse di Facile: valore, budget, contratti, avanzamenti e costi, con il piano di fatturazione e il monitoraggio in Excel.
modulo: Archivi
maschera_id: IDD_TCN_COMMESSE
---

# Commesse di contabilità analitica

Da questa maschera si gestiscono le commesse: il lavoro venduto a un cliente,
con il suo valore, il budget previsto, i contratti che lo compongono, gli
avanzamenti fatturati e tutti i costi che vi si attribuiscono.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Archivi ▸ Commesse di Contabilità Analitica ▸ Inserimento *(oppure* Modifica*)*
    - **Scorciatoia:** nessuna; la maschera si apre dal menu
    - **Permessi richiesti:** nessun profilo predefinito; **Inserimento** e **Modifica** si abilitano separatamente per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

La commessa è il contenitore di un lavoro: da una parte quanto vale e quanto si
prevede di spendere, dall'altra quanto si è davvero speso e quanto si è
fatturato. È la maschera da cui si risponde alla domanda «questo lavoro sta
andando bene?».

Ci arrivano da soli, senza reinserirli, i costi registrati altrove: le
registrazioni di prima nota che portano il codice della commessa, gli ordini a
fornitore, i carichi di merce. Dal lato dei ricavi ci sono i contratti e gli
avanzamenti — i SAL — con quanto è già stato fatturato.

Esempio: una commessa da 100.000 euro con due contratti; man mano che si
emettono i SAL, la **% Fatturato** in testata dice a che punto si è, e le
schede dei costi dicono quanto è stato consumato del budget.

## Prerequisiti

Prima di aprire la prima commessa occorre l'[anagrafica del
cliente](../anagrafiche/anagrafica-clienti.md) per cui si lavora.

Servono inoltre, per le schede dei costi: i [centri di
costo](centri-di-costo.md), le [causali contabili](causali-contabili.md) su cui
la commessa sia stata resa richiedibile, e l'anagrafica dei
[fornitori](../anagrafiche/anagrafica-fornitori.md) per subappalti e ordini.

## La maschera

![Maschera Commesse di contabilità analitica](../../assets/img/contabilita/commesse.png)

La maschera è divisa in tre parti:

- in alto la **barra dei comandi**, con due pulsanti in più rispetto alle altre
  maschere;
- sotto la **testata**, sempre visibile, con i dati della commessa e i tre
  totali calcolati;
- al centro le **schede**.

Le schede sono queste:

| Scheda | Contenuto |
|---|---|
| **Budget** | Le voci di budget previsto, con **Codice**, **Descrizione**, **Importo** e **Previsione**. La somma alimenta il **Budget Previsto** in testata. |
| **Contratti** | I contratti che compongono la commessa: **Codice**, **Nome Contratto**, **Importo**, **Tipo Pag.** La somma degli importi è il **Valore** della commessa. |
| **Subappaltatori** | I subappalti affidati: **Codice**, **Fornitore**, **Importo**, **Data Contratto**, **Num. Contratto**, **Data Ord.**, **Num.- Ord.**, **Attività**. Si inseriscono e si correggono dalla finestra [Subappaltatore](subappaltatore.md). |
| **Milestone/SAL** | Gli avanzamenti da fatturare, per contratto: **Codice**, **N. SAL**, **Descrizione SAL**, **Importo Fat.**, **Importo Iva**, **Importo Rit.**, **Tot. Fattura**, **Fatture**, **Data Fattura**. |
| **Costi - Analitica** | Le registrazioni di prima nota di costo attribuite alla commessa. |
| **Ricavi - Analitica** | Le registrazioni di prima nota di ricavo attribuite alla commessa. |
| **Ordini a Fornitore** | Gli ordini emessi per la commessa: **Anno**, **Numero**, **Data**, **Fornitore**, **Centro di Costo**, **Importo**, **Stato**. In alto **Dal**, **Al** e **Centro di Costo** restringono l'elenco. |
| **Carichi** | I carichi di merce sulla commessa, con deposito, documento di trasporto e fattura. |
| **Costi - Centri di Costo** | I costi raggruppati per centro di costo: **Codice**, **Descrizione**, **Importo**. In alto **Data Doc. Dal** e **Data Doc. Al** restringono il periodo, **Totale Costi Diretti** somma quello che resta, e i pulsanti **Stampa** ed **Excel** portano fuori la stessa cosa. Doppio clic su una riga apre i movimenti che compongono quell'importo. |
| **Varianti** | Le varianti concordate: **Codice**, **Data**, **Descrizione**, **Importo**, **Giorni**. |
| **Claims** | Le riserve, con le stesse colonne delle varianti. |
| **Note** | Una nota libera, di lunghezza non prefissata. |
| **Allegati** | I file collegati alla commessa. |

Le schede *Contratti*, *Subappaltatori*, *Milestone/SAL*, *Varianti* e *Claims*
hanno i propri pulsanti **Nuovo**, **Modifica** ed **Elimina**; su
*Subappaltatori* c'è in più **SAL...**, e su *Costi - Centri di Costo* i due
pulsanti **Stampa** ed **Excel**. Le altre schede sono di sola consultazione:
raccolgono quello che è stato registrato altrove.

## Campi

### Testata

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| Codice | ● | Identificativo della commessa. | Numero |
| Data Apertura | ● | Data di apertura della commessa. | Data |
| Data Chiusura | | Data di chiusura. | Data |
| Data Consegna | | Data di consegna prevista o effettiva. | Data |
| Descrizione | ● | Nome della commessa, come compare nelle registrazioni e nelle stampe. | Testo |
| Cliente | | Cliente per cui si lavora. Accanto compare la ragione sociale. | Codice dall'archivio clienti |
| Valore | | **Sola lettura.** La somma degli importi dei contratti della scheda *Contratti*: non si scrive a mano. | Calcolato |
| Budget Previsto | | **Sola lettura.** La somma delle voci della scheda *Budget*. | Calcolato |
| % Fatturato | | **Sola lettura.** Quanto è stato fatturato rispetto al **Valore**. Vedi la nota qui sotto. | Calcolato |
| CIG | | Codice identificativo di gara, per i lavori pubblici. | Testo |
| CUP | | Codice unico di progetto. | Testo |
| Tecnico | | Il tecnico che segue la commessa. | Testo |
| Contatto Email | | Indirizzo di posta del referente. | Testo |

{: .campi }

!!! note "Come si calcola la % Fatturato"

    È la somma degli **Importo Fat.** degli avanzamenti, divisa per il
    **Valore** della commessa. Contano però solo gli avanzamenti legati a
    contratti con importo diverso da zero: un contratto a importo zero non
    entra nel valore, e per coerenza i suoi avanzamenti non entrano nel
    fatturato. Se il **Valore** è zero, la percentuale resta a zero.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra la commessa. |
| **F3 - Prec.** | ++f3++ | Passa alla commessa precedente. |
| **F4 - Succ.** | ++f4++ | Passa alla commessa successiva. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco delle commesse. |
| **F6 - Elimina** | ++f6++ | Cancella la commessa, previa conferma. |
| **Ricarica** | | Rilegge la commessa dall'archivio, abbandonando le modifiche non salvate. |
| **Piano Fatt.** | | Produce in Excel il piano di fatturazione della commessa. |
| **Monitoraggio** | | Produce in Excel il monitoraggio della commessa. |

I due pulsanti Excel sono spenti finché la commessa non è stata salvata, e
restano spenti per tutta la durata dell'elaborazione: mentre uno lavora, il
puntatore diventa una clessidra e quel pulsante non risponde. L'altro resta
disponibile.

Valgono inoltre:

| Comando | Scorciatoia | Effetto |
|---|---|---|
| Elenco valori | ++f10++, ++space++ o doppio clic su **Cliente** | Apre l'elenco dei clienti. |
| Consultazione | ++f11++ | Apre la finestra **Consultazione**. |
| Calcolatrice | ++f12++ | Apre la calcolatrice. |
| Campo successivo | ++enter++ | Sposta il cursore sul campo seguente. |
| Chiusura | ++esc++ | Chiude la maschera. |

## Come si fa

### Aprire una commessa

1. Apri **Menu ▸ Archivi ▸ Commesse di Contabilità Analitica ▸ Inserimento**.
2. Digita il **Codice**, la **Data Apertura** e la **Descrizione**: sono i tre
   dati che il programma pretende.
3. Indica il **Cliente** con ++f10++.
4. Se è un lavoro pubblico, compila **CIG** e **CUP**.
5. Premi **F2 - Salva**. Ora la commessa esiste e le schede si possono
   riempire.

### Stabilire il valore e il budget

1. Carica la commessa e apri la scheda *Contratti*.
2. Con **Nuovo** inserisci un contratto per volta, con il suo **Importo**: il
   campo **Valore** in testata si aggiorna da solo mentre lavori.
3. Passa alla scheda *Budget* e inserisci le voci di costo previste: la loro
   somma diventa il **Budget Previsto** in testata.
4. Premi **F2 - Salva**.

### Registrare un avanzamento

1. Carica la commessa e apri la scheda *Milestone/SAL*.
2. Premi **Nuovo** e compila il SAL, indicando il contratto a cui appartiene e
   l'**Importo Fat.**
3. Alla conferma, la **% Fatturato** in testata si aggiorna da sola.

### Vedere come sta andando la commessa

1. Carica la commessa.
2. Leggi in testata **Valore**, **Budget Previsto** e **% Fatturato**.
3. Apri le schede dei costi — *Costi - Analitica*, *Ordini a Fornitore*,
   *Carichi*, *Costi - Centri di Costo* — per vedere dove il budget si sta
   consumando.
4. Su *Costi - Analitica* e *Costi - Centri di Costo* restringi il periodo con
   **Data Doc. Dal** e **Data Doc. Al** se vuoi guardare un tratto di lavoro
   invece di tutta la commessa.
5. Premi **Monitoraggio** per averne il quadro in Excel.

### Risalire ai movimenti di un centro di costo

1. Carica la commessa e apri la scheda *Costi - Centri di Costo*.
2. Se ti serve un tratto di lavoro invece di tutta la commessa, restringi il
   periodo con **Data Doc. Dal** e **Data Doc. Al**.
3. Fai doppio clic sulla riga del centro di costo che vuoi esaminare, oppure
   selezionala e premi ++enter++.
4. Si apre **Movimenti del centro di costo**: il **Totale** in fondo coincide
   con l'importo della riga da cui sei partito.
5. Per vedere una registrazione per intero, fai doppio clic sul movimento: si
   apre la [prima nota](registrazione-prima-nota.md) già caricata.
6. Chiudi con **Chiudi** o con ++esc++. Se hai modificato qualcosa, l'elenco e
   la griglia sotto si sono già rifatti da soli.

### Produrre il piano di fatturazione

1. Carica la commessa: dev'essere già salvata, altrimenti il pulsante è spento.
2. Premi **Piano Fatt.**
3. Attendi che la clessidra sparisca: l'elaborazione produce il file Excel.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca il **Codice**, la **Data Apertura** o la **Descrizione**. | Guarda dove si è posizionato il cursore: è il campo da compilare. |
| *In archivio è già presente un record con lo stesso codice.* | Il codice digitato è già di un'altra commessa. | Cambia codice. |
| *Confermi la Cancellazione....* | Conferma richiesta da **F6 - Elimina**. | Rispondi **Sì** per eliminare la commessa. |
| *Non è possibile eliminare il record poiché utilizzato in alcuni record del database.* | La commessa compare su documenti, righe di documento, movimenti di magazzino o nello storico. | Non è eliminabile: lasciala in archivio. |
| *Il record è stato modificato da un altro nodo della rete.* | Un altro utente ha salvato la stessa commessa mentre la modificavi. | Premi **Ricarica**, verifica cosa è cambiato e rifai le tue modifiche. |
| *Il record è stato cancellato da un altro nodo della rete.* | Un altro utente ha eliminato la commessa mentre la modificavi. | La maschera si chiude: non c'è più nulla da salvare. |

## Note

!!! warning "Attenzione"

    **Valore**, **Budget Previsto** e **% Fatturato** non si scrivono: sono
    calcolati dalle schede *Contratti* e *Budget* e dagli avanzamenti. Per
    cambiare il valore della commessa si interviene sui contratti, non sulla
    testata.

    Le schede dei costi raccolgono quello che è stato registrato **altrove**
    indicando il codice della commessa: se un costo non compare, non è la
    commessa a essere sbagliata, è la registrazione che non le è stata
    attribuita.

    ++esc++ chiude la maschera senza chiedere conferma e senza salvare: le
    modifiche fatte dopo l'ultimo **F2 - Salva** vanno perse.

!!! info "Dove finiscono i due fogli Excel, e perché non c'è nessun messaggio"

    **Piano Fatt.** e **Monitoraggio** scrivono un foglio Excel nella
    cartella **`out` dell'utente**, e lo **aprono da soli** appena finito:
    per questo non compare nessun avviso di fine elaborazione — il
    risultato è il foglio che ti si apre davanti.

    Il nome porta il numero e il nome della commessa:

    - `piano_fatturazione_<numero>_<nome commessa>.xlsx`
    - `monitoraggio_<numero>_<nome commessa>.xlsx`

    I caratteri che Windows non accetta nei nomi di file vengono sostituiti
    con un trattino basso. Rilanciando l'elaborazione il foglio viene
    **riscritto**: se ci hai lavorato sopra, salvalo con un altro nome.

    Se il foglio non si riesce a scrivere — perché è aperto, di solito —
    compare l'errore della libreria Excel e non viene prodotto niente.

!!! info "Il pulsante SAL dei subappaltatori"

    Mettiti sulla riga del subappaltatore e premi **SAL...**: si apre
    [SAL Subappaltatore](sal-subappaltatore.md), l'elenco degli stati
    avanzamento lavori di **quel** subappalto, con i comandi **Nuovo**,
    **Modifica** ed **Elimina**.

    È lo stesso meccanismo degli avanzamenti della commessa, ma dalla parte
    di chi lavora per te: serve a sapere quanto del subappalto è stato
    eseguito e quanto resta, a fronte dell'importo pattuito.

    Senza una riga selezionata il pulsante non fa niente.

!!! abstract "Cosa va fra le Varianti e cosa fra i Claims"

    Una **variante** è concordata prima: nasce da una nuova esigenza del
    committente o da una miglioria, e per esistere ha bisogno di un
    accordo formale, l' ordine di modifica. Si gestisce prima o durante
    l' esecuzione dell' opera.

    Un **claim** - una riserva, una rivendicazione - è unilaterale e
    arriva dopo: lo apri tu a fronte di un imprevisto, di un ritardo o di
    un' inadempienza della controparte. Non c' è un accordo alle spalle ma
    una trattativa da fare, e spesso un contenzioso. Si formalizza a
    consuntivo o mentre l' evento critico è in corso.

    | | Varianti | Claims |
    |---|---|---|
    | **Natura** | concordata e preventiva | unilaterale e successiva all' evento |
    | **Approvazione** | accordo formale, ordine di modifica | trattativa o accertamento, spesso contenzioso |
    | **Causale tipica** | nuove esigenze del committente, migliorie | imprevisti, ritardi, inadempienze della controparte |
    | **Tempistica** | prima o durante l' esecuzione | a consuntivo, o durante l' evento critico |

    In due parole: la variante è un importo **pattuito**, il claim è un
    importo **preteso**. Il primo è acquisito, il secondo è ancora da
    ottenere.

!!! note "Varianti e Claims: per il programma sono la stessa cosa"

    Le due schede sono **la stessa maschera** aperta su due elenchi
    diversi: stesse colonne, stessi campi, stesso archivio. L'unica
    differenza è l'etichetta — registrando da *Varianti* la finestra si
    chiama *Inserimento Variante*, da *Claims* si chiama *Inserimento
    Claim* — e il fatto che ogni scheda mostra solo le proprie.

    Il programma non tratta le une diversamente dagli altri: la
    distinzione è **tua**, e serve a tenere in due elenchi distinti quello
    che va tenuto distinto.

    I conti invece restano separati: quando la commessa viene salvata, il
    programma calcola **due totali distinti** - importi e giorni delle
    Varianti da una parte, dei Claims dall’ altra. Nessuno dei due
    compare ancora in una maschera o in una stampa, ma il giorno che
    servissero la distinzione è già fatta, e un importo ancora in
    trattativa non risulterà acquisito.


!!! note "Il periodo dei costi va per data del documento"

    Le schede *Costi - Analitica*, *Ricavi - Analitica* e *Costi - Centri di
    Costo* hanno in alto due date, **Data Doc. Dal** e **Data Doc. Al**, che
    restringono il periodo.

    Il confronto è sulla **data del documento** — quella scritta sulla fattura
    del fornitore — non sulla data in cui la registrazione è stata scritta in
    prima nota. Le due quasi mai coincidono: una fattura di dicembre registrata
    a gennaio rientra in dicembre. La regola è la stessa su tutte e tre le
    schede, così i totali si possono confrontare fra loro.

    All'apertura le due date coprono tutto l'arco delle registrazioni presenti,
    quindi la scheda parte mostrando l'intera commessa. Cambiandone una, il
    totale e la griglia si rifanno appena lasci il campo, e la **Stampa** esce
    con lo stesso periodo che vedi a video: quello che c'è nella griglia è
    quello che finisce sul foglio.

!!! info "La finestra «Movimenti del centro di costo»"

    Su *Costi - Centri di Costo* la griglia mostra **un totale per centro di
    costo**, e basta. Il doppio clic su una riga — o ++enter++ con la riga
    selezionata — risponde alla domanda che segue sempre: *da quali
    registrazioni arriva questo importo?*

    La finestra occupa gran parte dello schermo, si centra da sola e non si
    ridimensiona. Il titolo riporta **centro di costo, commessa e periodo**,
    così si sa a cosa si riferisce quello che si sta guardando anche dopo
    averla spostata o averne aperte due di seguito.

    | Colonna | Cosa contiene |
    |---|---|
    | **Num. Movimento** | Il numero della registrazione di prima nota: è quello da citare all'assistenza. |
    | **Data** | La data di registrazione in prima nota. |
    | **Data Doc.** | La data scritta sul documento del fornitore. È questa che il periodo confronta. |
    | **Numero Doc.** | Il numero del documento del fornitore. |
    | **Cod. Fornitore** | Il codice del fornitore in [anagrafica](../anagrafiche/anagrafica-fornitori.md). Resta a zero sulle registrazioni senza controparte. |
    | **Descrizione Fornitore** | La ragione sociale come è stata registrata. |
    | **Importo** | Positivo o negativo secondo che la riga sia in **dare** o in **avere**. |

    Le righe con **importo negativo sono scritte in rosso**, per intero e non
    solo nella colonna dell'importo: sono storni e rettifiche, e in un elenco
    lungo devono saltare all'occhio senza doverli cercare.

    Il **Totale** in fondo somma quello che vedi e coincide con l'importo della
    riga da cui sei partito. Coincide **sempre**, perché la finestra usa il
    periodo con cui la griglia è stata riempita e non quello scritto nei campi:
    se hai cambiato una data senza uscire dal campo, i due numeri non si
    scollano comunque.

    Un doppio clic su un movimento apre la
    [registrazione di prima nota](registrazione-prima-nota.md) già caricata. Se
    la modifichi, al ritorno si rifanno **sia l'elenco sia la griglia dei centri
    di costo** sotto: nessuno dei due resta a mostrare un importo vecchio.

    Si chiude con **Chiudi** o con ++esc++.

    !!! warning "La riga «NON ATTRIBUITO» di norma si apre vuota"

        È la riga che raccoglie i costi a cui nessuno ha assegnato un centro di
        costo. Aprendola si ottiene quasi sempre un elenco vuoto, perché in
        pratica tutte le registrazioni di commessa il centro di costo ce
        l'hanno. Non è un difetto: è la conferma che non è rimasto fuori
        niente.

!!! info "I filtri di Ordini a Fornitore"

    La scheda elenca tutti gli ordini emessi per la commessa. Quando sono
    tanti, in alto ci sono tre filtri che lavorano insieme: **Dal**, **Al** e
    **Centro di Costo**.

    Le due date si applicano alla **data del documento** dell'ordine, quella
    che la griglia mostra nella colonna **Data** e su cui l'elenco è già
    ordinato. All'apertura coprono **dal primo all'ultimo ordine a fornitore
    presenti in archivio**, non solo quelli di questa commessa: così passando
    da una commessa all'altra il periodo resta quello che hai impostato e non
    si riazzera sotto le mani.

    La tendina **Centro di Costo** porta tutti i centri dell'anagrafica in
    ordine alfabetico, con **TUTTI** come prima voce. Finché è su **TUTTI** il
    centro di costo non entra nel filtro: scegliendone uno restano solo gli
    ordini che vi sono attribuiti.

    !!! warning "Gli ordini senza centro di costo escono dall'elenco"

        Scegliendo un centro specifico spariscono anche gli ordini a cui **non
        è stato attribuito alcun centro** — e non sono pochi: su un archivio
        reale erano 79 su 482. Non è un difetto, ma se i conti non tornano è
        la prima cosa da guardare: rimetti **TUTTI** e li ritrovi.

    Il pulsante **Stampa** non è toccato dai filtri: stampa l'ordine della riga
    selezionata, non l'elenco.

!!! tip "Excel, su Costi - Centri di Costo"

    Il pulsante **Excel** salva quello che hai davanti in un foglio di calcolo
    e lo apre subito. Il file finisce nella cartella `out` del programma e
    prende il nome dalla commessa, così le esportazioni di commesse diverse non
    si sovrascrivono.

    Il foglio riporta in testa **ditta**, **commessa** e il **periodo** con cui
    la griglia è stata riempita, poi le tre colonne come le vedi e in fondo il
    **Totale Costi Diretti**. Sono esportati **tutti** i centri di costo
    presenti a video, compresi quelli a zero: il foglio è la fotografia della
    scheda, non una selezione.

    Scrivere il periodo in testa non è un vezzo: un elenco di importi
    aggregati, riletto a distanza di giorni, senza le date non si sa a cosa si
    riferisca.

## Vedi anche

- [Subappaltatore](subappaltatore.md)
- [SAL Subappaltatore](sal-subappaltatore.md)
- [Centri di costo/ricavo](centri-di-costo.md)
- [Causali contabili](causali-contabili.md)
- [Anagrafica clienti](../anagrafiche/anagrafica-clienti.md)
