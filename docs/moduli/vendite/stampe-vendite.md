---
title: Stampe e strumenti di vendita
description: Liste di prelievo, distinte per i trasportatori, kg venduti, rapporto di cassa, analisi commessa e valorizzazione dei documenti trasfert.
modulo: Vendite
maschera_id: nessuna dialog propria
---

# Stampe e strumenti di vendita

Le voci sciolte in fondo al menu Vendite: quelle che servono a far uscire la
merce dal magazzino, a consegnarla e a controllare com'è andata la giornata.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Vendite ▸ Liste di Prelievo *(oppure* Stampa Distinta Carico Trasportatori*,* Stampa Distinta Trasportatori*,* Stampa Kg. Venduti*,* Stampa Rapporto Cassa *o* Analisi Commessa*)*
        - Menu ▸ Vendite ▸ Doc. di Trasporto ▸ Valorizza Doc. Trasfert e Concessionario
        - Menu ▸ Vendite ▸ Doc. di Trasporto ▸ Stampa Riepiloghi Competenze Doc. Trasfert e Conc.
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Liste di Prelievo** | La lista con cui il magazziniere va a prendere la merce a scaffale, **articolo per articolo**. |
| **Stampa Distinta Carico Trasportatori** | Che cosa va caricato su ciascun mezzo, riga per riga. |
| **Stampa Distinta Trasportatori** | L'elenco dei **documenti** da consegnare, per il giro del [trasportatore](../anagrafiche/trasportatori.md). |
| **Stampa Kg. Venduti** | I chili usciti nel periodo, per chi vende a peso. |
| **Stampa Rapporto Cassa** | Quanto è stato incassato in un giorno e con quali mezzi di pagamento. |
| **Analisi Commessa** | Tutti i documenti agganciati a una [commessa](../contabilita/commesse.md), con il totale e il margine. |
| **Valorizza Doc. Trasfert e Concessionario** | Attribuisce i valori ai documenti in trasfert e ai concessionari. |
| **Stampa Riepiloghi Competenze Doc. Trasfert e Conc.** | Le competenze maturate su quei documenti. |

## Prerequisiti

Prima di usare queste stampe occorre avere emesso i
[documenti](documento-di-vendita.md) del periodo; per le distinte, avere i
[trasportatori](../anagrafiche/trasportatori.md) in archivio e assegnati ai
documenti.

## La maschera

![Liste di prelievo](../../assets/img/vendite/stampe-vendite.png)

Cinque su sette sono semplici finestre di selezione: si mette il periodo, si
restringe con i filtri e si preme **F2 - OK**. Due invece sono finestre di
lavoro, con una griglia: **Liste di Prelievo** e **Analisi Commessa**.

Dove il filtro è un codice, lasciarlo a zero vuol dire *tutti*: il campo accanto
lo scrive a chiare lettere.

## Campi

### Liste di Prelievo

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Cliente** | | Restringe a un cliente solo. | codice |
| **Data Iniziale**, **Data Finale** | | Il periodo dei documenti. Lasciando vuota l'iniziale si prende tutto fino alla finale. | date |
| **Tipo Doc.** | | Quali documenti portare in griglia. | `TUTTI`, `FATTURE`, `ORDINI`, `DDT` |
| **Ubicazione** | | Stampa solo gli articoli in quella posizione di magazzino. Accetta i caratteri jolly `*` e `?`. | testo |

La griglia elenca un documento per riga: **Sel.**, tipo e numero, data, stato,
cliente, totale, totale da pagare, destinatario e operatore. Si spunta la colonna
**Sel.** per scegliere che cosa stampare.

### Stampa Distinta Carico Trasportatori

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo dei documenti. La finale non può precedere l'iniziale. | date |
| **Consegna** | | Restringe ai documenti con quella data di consegna. | data |
| **Trasportatore** | | Un vettore solo. | codice |
| **Reparto** | | Un reparto solo, guardando il reparto dell'articolo. | codice |
| **Agente** | | Un agente solo. | codice |

### Stampa Distinta Trasportatori

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo dei documenti. | date |
| **Trasportatore** | | Un vettore solo. | codice |
| **Agente** | | Un agente solo. | codice |
| **Tipo Vendite** | | Restringe a un tipo di vendita. | `TUTTE`, `NORMALI`, `TRASFERT`, `C.S. VENDITA`, `C.S. TRASFERT` |
| **Ordinamento** | | Come ordinare la stampa. | `NUM. DOCUMENTO + DATA`, `CLIENTE + DESTINAZIONE` |

### Stampa Kg. Venduti

La finestra si intitola *Stampa KG. Consegnati*, la voce di menu *Stampa Kg.
Venduti*: è la stessa cosa.

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo dei documenti. | date |
| **Fornitore** | | Solo gli articoli che hanno quel **fornitore abituale**: serve a sapere quanti chili di merce di un fornitore sono usciti. | codice |
| **Agente** | | Un agente solo. | codice |
| **Tipo Vendite** | | Restringe a un tipo di vendita. | `TUTTE`, `NORMALI`, `TRASFERT`, `C.S. VENDITA`, `C.S. TRASFERT` |

### Stampa Rapporto Cassa

In alto i tre filtri, sotto i totali, che il programma riempie da solo:

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data** | ● | Il giorno da esaminare. | data |
| **Registro** | | Il registro di cassa. | voce dell'elenco |
| **Operatore** | | Chi era alla cassa. | codice |

I totali in sola lettura sono due gruppi. Il primo conta i documenti:
**N. Scontrini** e **Totale Scontrini**, **N. Fatture** e **Totale Fatture**,
**N. Fat.+Scontr.** e **Totale Fat. + Scontr.**, con il **Totale**. Il secondo
divide l'incassato per mezzo di pagamento: **Contanti**, **Assegni**, **Carte
Credito**, **Bancomat**, **Buoni Pasto**, **A Credito**, e il **Totale**.

### Analisi Commessa

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Commessa** | ● | Quale commessa esaminare. | codice |
| **Data** | | La data della commessa. Non modificabile. | — |
| **Valore** | | Il valore della commessa, come sta nella sua scheda. Non modificabile. | — |
| **Totale** | | La somma dei netti dei documenti trovati. Non modificabile. | — |
| **Ricavo** | | **Totale meno costo**. Non modificabile, e **visibile solo agli amministratori**. | — |

Nella griglia, un documento per riga: tipo e numero, tipo documento, data, stato,
codice e ragione sociale del cliente o del fornitore.

### Riepilogo Competenze Doc. Trasfert e Concessionario

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Da Data**, **A Data** | ● | Il periodo dei documenti. | date |
| **Cliente** | | Un cliente solo. | codice |
| **Fornitore** | | Un fornitore solo. | codice |
| **Agente** | | Un agente solo. | codice |

### Valorizza Doc. Trasfert e Concessionario

Non ha una maschera propria: chiede solo il periodo, con la stessa finestrella
di scelta delle date usata altrove nel programma.

## Pulsanti e comandi

Sulle cinque finestre di sola selezione:

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia la stampa o l'elaborazione. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |

**Liste di Prelievo** ha una barra sua:

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Selez. Tutti** | ++f2++ | Spunta tutte le righe della griglia. |
| **F3 - Deselez. Tutti** | ++f3++ | Toglie tutte le spunte. |
| **F4 - Stampa** | ++f4++ | Stampa la lista di prelievo. |
| **F5 - Modifica Cliente** | ++f5++ | Apre la scheda del cliente del documento su cui sei. |
| **F7 - Trova** | ++f7++ | Cerca nella griglia. |

**Analisi Commessa** anche:

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Modifica** | ++f2++ | Apre il documento su cui sei. |
| **F3 - Aggiorna** | ++f3++ | Rilegge tutto, per vedere l'effetto di quello che è cambiato nel frattempo. |
| **F7 - Stampa** | ++f7++ | Apre un menu con tre stampe: *Consegne Raggruppate per Documento*, *Consegne Raggruppate per Cat. Merceologica*, *Consegne solo per Cat. Merceologica*. |

**Stampa Rapporto Cassa** ha il solo **F2 - Stampa**: i totali si vedono a
video appena si sceglie la data, e il pulsante serve a portarli su carta.

## Come si fa

### Preparare le consegne della giornata

1. Apri **Menu ▸ Vendite ▸ Liste di Prelievo**.
2. Indica il periodo e il **Tipo Doc.**: la griglia si riempie dei documenti da
   evadere.
3. Spunta quelli da preparare — o premi **F2 - Selez. Tutti** — e premi
   **F4 - Stampa**. La lista esce ordinata per articolo, non per documento: è
   fatta per girare il magazzino una volta sola.
4. Apri **Stampa Distinta Carico Trasportatori** e stampa cosa va su ciascun
   mezzo.
5. Apri **Stampa Distinta Trasportatori** per l'elenco delle consegne del giro,
   mettendo **Ordinamento** su `CLIENTE + DESTINAZIONE` se il giro si fa per
   indirizzo.

### Controllare la cassa a fine giornata

1. Apri **Menu ▸ Vendite ▸ Stampa Rapporto Cassa**.
2. Indica la data e stampa.
3. Confronta con il riepilogo degli [scontrini](scontrini.md).

### Valorizzare i documenti in trasfert

1. Apri **Menu ▸ Vendite ▸ Doc. di Trasporto ▸ Valorizza Doc. Trasfert e
   Concessionario**.
2. Indica il periodo e avvia.
3. Stampa poi i **Riepiloghi Competenze** per vedere quanto è maturato.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca una delle date, oppure la finale precede l'iniziale. | Guarda dove si è posizionato il cursore: è il campo da correggere. |
| *Impossibile trovare il cliente in archivio!* | In **Liste di Prelievo**, **F5 - Modifica Cliente** su una riga il cui cliente non c'è più. | Il documento è rimasto agganciato a un cliente cancellato. |
| *Impossibile trovare il documento in archivio!* | Il documento su cui sei è stato cancellato da un altro nel frattempo. | Aggiorna l'elenco. |
| *D.D.T. N. n Art. c Valorizzato a Zero !* | Nella valorizzazione, per quell'articolo non si è trovato nessun prezzo d'acquisto. | Controlla che l'articolo abbia un prezzo d'acquisto o un carico da cui prenderlo. Il documento viene valorizzato lo stesso, a zero. |
| *D.D.T. N. n Art. c Commissione uguale a Zero !* — *Fornitore : …* | La commissione del fornitore è a zero, e l'articolo dovrebbe averne una. | Controlla la commissione sulla scheda del fornitore indicato nel messaggio. |

## Note

!!! note "Il trasfert e i concessionari"

    Le due voci sui documenti trasfert riguardano chi vende tramite
    concessionari o agenti con merce in carico: la valorizzazione attribuisce i
    valori ai documenti, il riepiloghi competenze dice quanto spetta a
    ciascuno. Se non si lavora così, le due voci non servono.

!!! note "Le due distinte non sono la stessa stampa"

    Si somigliano nel nome e servono a due momenti diversi della giornata.

    | | Distinta **Carico** Trasportatori | Distinta Trasportatori |
    |---|---|---|
    | A che serve | Caricare il mezzo | Fare il giro |
    | Cosa elenca | Le **righe**: articolo per articolo | I **documenti**: uno per riga |
    | Quali documenti | Fatture, bolle, DDT, buoni, accompagnatorie — **e gli ordini clienti non ancora evasi** | Solo fatture, bolle e DDT verso clienti |
    | Filtri in più | Data di **consegna**, **reparto** | **Tipo vendite**, **ordinamento** |

    La differenza pratica è l'ultima riga della tabella: la distinta **di
    carico** vede anche gli ordini, quindi si può caricare il mezzo per un
    ordine che non è ancora diventato un documento; l'altra no.

    Su entrambe, un filtro lasciato a zero vuol dire *tutti*, e i documenti
    annullati non compaiono mai.

!!! note "Da dove nascono le liste di prelievo, e come si sceglie"

    La griglia raccoglie i documenti **verso clienti** e **non a credito** del
    periodo, di tre tipi soli: **fatture**, **ordini clienti** e **DDT**. Il
    campo **Tipo Doc.** restringe a uno dei tre.

    Si sceglie spuntando la colonna **Sel.**. In stampa finiscono solo le righe
    con **quantità ancora da consegnare**: quello che è già stato evaso non si
    va a riprendere.

!!! warning "Senza spunte, la lista di prelievo esce tutta"

    Se si preme **F4 - Stampa** senza aver spuntato niente, il programma non
    avvisa e non si ferma: stampa **tutto quello che c'è da prelevare**, di ogni
    documento in griglia. Non è un errore — può essere comodo — ma conviene
    saperlo prima di lanciare la stampa su un periodo lungo.

!!! note "Analisi Commessa e la scheda della commessa"

    Sono due cose diverse. La
    [scheda della commessa](../contabilita/commesse.md) in Archivi è
    l'anagrafica: come si chiama, quando è aperta, quanto vale.

    **Analisi Commessa** è il consuntivo: raccoglie tutto quello che si è
    agganciato a quella commessa — documenti di vendita, documenti d'acquisto e
    carichi merci — e lo mette in fila, con il **Totale** di quanto è passato e
    il **Ricavo**, cioè il margine.

    Raccoglie anche i documenti che **non** portano la commessa in testata ma ce
    l'hanno su una **singola riga**: sono i casi in cui a una commessa si è
    imputata solo una parte di un documento.

    Il **Ricavo** lo vede solo un amministratore: sugli altri utenti il campo
    non compare proprio.

!!! note "Che cosa vuol dire «valorizzare» un documento trasfert"

    Un documento in trasfert o a concessionario nasce senza prezzi: la merce
    parte, e solo dopo si sa quanto vale e quanto spetta a chi l'ha venduta.
    **Valorizza** è il passaggio che riempie quei numeri, sui documenti del
    periodo che sono in stato *salvato* o *emesso*.

    Riga per riga scrive:

    - il **prezzo d'acquisto** dell'articolo, che è il costo su cui la
      competenza viene calcolata. Non è un prezzo di listino: è il **costo medio
      dei carichi** da fornitore di quell'articolo, su quel deposito, dal primo
      del mese alla data del documento. Se in quel periodo non ci sono carichi,
      si ripiega sull'**ultimo prezzo d'acquisto** della scheda articolo;
    - il **prezzo di vendita**, preso dal listino trasfert del cliente o della
      destinazione;
    - la **commissione** che matura su quella riga;
    - di conseguenza sconti, totale sconto, peso e importo della riga.

    Alla fine ricalcola i totali del documento e lo riporta a *emesso*. Da quel
    momento i **Riepiloghi Competenze** hanno qualcosa da riepilogare.

    La commissione non si calcola in un modo solo: dipende da come è impostato
    l'articolo e da quale listino trasfert ha il cliente. Se un articolo resta
    senza prezzo, o la commissione viene zero, il programma lo dice documento per
    documento con i due messaggi *Valorizzato a Zero* e *Commissione uguale a
    Zero* — e prosegue.

!!! warning "Valorizza si può rilanciare, ma non è gratis"

    Rilanciando la valorizzazione sullo stesso periodo, i documenti già emessi
    vengono **annullati e riemessi** con i valori ricalcolati. È il modo giusto
    per rimediare a un listino sbagliato, ma va fatto sapendo che i documenti
    cambiano.

## Vedi anche

- [Documento di vendita](documento-di-vendita.md)
- [Trasportatori](../anagrafiche/trasportatori.md)
- [Commesse di contabilità analitica](../contabilita/commesse.md)
- [Scontrini](scontrini.md)
