---
title: Assistenza
description: Il sottomenu protetto da password — variazione dei codici in tutto l'archivio, rimozioni di massa e correzioni che l'assistenza esegue sui dati.
modulo: Utility
maschera_id: IDD_ART_ARTICOLI_VARIA
---

# Assistenza

Il sottomenu **Assistenza** contiene le procedure che intervengono sugli
archivi in modo massivo: cambiano un codice ovunque compaia, rimuovono
movimenti, azzerano campi. Tutte chiedono una **password** che ha l'assistenza
R.S.A., e non a caso.

!!! danger "Queste procedure vanno usate con l'assistenza"

    Non esiste annullamento. Prima di ciascuna, il programma stesso avvisa:
    *«Prima di utilizzare la procedura assicurarsi che nessun altro utente stia
    utilizzando il programma. Per la vostra sicurezza si consiglia di fare una
    copia dei dati prima di continuare. Prima di procedere è necessario
    effettuare un accesso ai dati di tutti gli anni di gestione presenti negli
    archivi e concludere con successo la funzione Aggiorna Catalogo Dati.»*

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Utility ▸ Assistenza ▸ *(una delle voci)*
    - **Scorciatoia:** ++f2++ conferma, ++esc++ esce
    - **Permessi richiesti:** oltre all'abilitazione della voce di menu da [Archivi ▸ Utenti](../anagrafiche/utenti.md), ogni voce chiede la **password dell'assistenza** nella finestra *Richiesta Password*

---

## A cosa serve

### Variazione dei codici

Cambiano un codice **ovunque compaia negli archivi**: anagrafiche, movimenti,
documenti, storico. È l'unico modo corretto di rinumerare qualcosa che è già
stato usato.

| Voce di menu | Cosa varia | Titolo della finestra |
|---|---|---|
| **Variazione Codici Cat. Merceologiche** | Le [categorie merceologiche](../magazzino/categorie-merceologiche.md). | *Variazione Cat. Merceologiche* |
| **Variazione Codici Iva** | Le [aliquote IVA](../contabilita/aliquote-iva.md). | *Variazione Codici IVA* |
| **Variazione Codici Reparti** | I [reparti](../magazzino/reparti.md). | *Variazione Reparti* |
| **Variazione Codici Stagione** | Le [stagioni](../magazzino/stagioni.md). | *Variazione Stagioni* |
| **Variazione Codici Marchi** | I [marchi](../magazzino/marchi.md). | *Variazione Marchi* |
| **Variazione Codici Deposito** | I [depositi](../magazzino/depositi.md). | *Variazione Deposito* |
| **Variazione Codici Articoli** | Il codice di un [articolo](../anagrafiche/anagrafica-articoli.md). | *Variazione Codice Articolo* |
| **Variazione Codici Cat. Economica Clienti** | Le [categorie economiche](../anagrafiche/categorie-economiche.md). | *Varia Categoria Economica Clienti* |
| **Variazione Codici Causali Magazzino** | Le [causali di magazzino](../magazzino/causali-magazzino.md). | *Varia Categoria Economica Clienti* |
| **Variazione Codici Operatori** | Gli [operatori](../altre-tabelle/operatori.md). | *Varia Categoria Economica Clienti* |
| **Variazione Codici Agenti** | Gli [agenti](../anagrafiche/anagrafica-agenti.md). | *Varia Categoria Economica Clienti* |
| **Variazione Codici Commesse** | Le [commesse](../contabilita/commesse.md). | *Varia Categoria Economica Clienti* |
| **Variazione Registro Scontrini** | Il registro degli [scontrini](../vendite/scontrini.md). | *Varia Registro Scontrini* |
| **Variazione Registro Carichi** | Il registro dei [carichi](../magazzino/carico-merci.md). | *Varia Registro Scontrini* |
| **Varia Conto** | Un [conto](../contabilita/conti.md) del piano dei conti. | *Variazione Conto* |
| **Variazione Sottoconti** | I [sottoconti](../contabilita/sottoconti.md). **Solo Studio:** nelle altre versioni la voce non compare. | — |
| **Spostamento Codici Clienti** | Sposta i codici dei [clienti](../anagrafiche/anagrafica-clienti.md). | — |

### Correzioni sugli articoli

| Voce di menu | A cosa serve |
|---|---|
| **Azzera Listino** | Azzera un [listino](../listini-vendita/gestione-listini.md) intero. |
| **Inversione Modalità IVA** | Converte l'archivio da IVA esclusa a IVA inclusa o viceversa. |
| **Articoli IVA Inclusa** / **Articoli IVA Esclusa** | Impostano il modo in cui i prezzi degli articoli sono intesi. |
| **Aggiorna Gruppi da Tabella** / **Aggiorna Sottogruppi da Tabella** | Riallineano gruppi e sottogruppi degli articoli alla tabella. |
| **Associa Settori->Gruppi** | Associa i settori ai gruppi. |
| **Tronca Descrizioni Articoli a 30 Car** | Accorcia le descrizioni a trenta caratteri, per gli apparecchi che non ne accettano di più. |
| **Azzeramento Commissione Articoli** | Azzera la commissione sugli articoli. |
| **Abilita Trasferimento Articoli** | Rimette il segno «da mandare» sugli articoli, per rifare un invio a [casse e bilance](../casse-bilance/casse.md). |

### Rimozioni e riporti

| Voce di menu | A cosa serve |
|---|---|
| **Cancellazione Buoni Sconto Scaduti** | Toglie dall'archivio i buoni sconto scaduti. |
| **Cancellazione Movimenti di Vendita** | Rimuove i movimenti di vendita. |
| **Rimozione Movimento Prima Nota** | Rimuove un intervallo di registrazioni di [prima nota](../contabilita/gestione-prima-nota.md). La finestra si chiama *Rimozione Movimento di Prima Nota*. |
| **Rimozione Movimenti di Magazzino** | Rimuove un intervallo di [movimenti di magazzino](../magazzino/movimenti-magazzino.md). |
| **Riporto Saldi Contabili da Scadenziario** | Ricostruisce i saldi contabili partendo dallo [scadenziario](../scadenze/gestione-scadenze.md). |
| **Abilita NoSync** | Disattiva la sincronizzazione. |

## Prerequisiti

Prima di ogni procedura di questo menu occorre:

- **la password dell'assistenza**;
- **una copia di sicurezza degli archivi**;
- che **nessun altro utente stia usando il programma**;
- aver aperto **tutti gli anni di gestione** presenti negli archivi e aver
  eseguito con successo
  [Aggiorna Catalogo Dati](manutenzione-archivi.md) su ciascuno.

L'ultimo punto è quello che viene dimenticato più spesso, ed è quello che fa
fallire le variazioni di codice a metà strada.

## La maschera

![Variazione codici IVA](../../assets/img/utility/assistenza.png)

Prima si apre **Richiesta Password**, con un campo **Password** e i pulsanti
**F2 - OK** ed **Esci**. Superata quella, compare l'avviso di cautela e poi la
maschera vera, che nella grande maggioranza dei casi ha due soli campi: il
codice attuale e quello nuovo.

## Campi

### Variazione dei codici degli articoli

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Deposito** | | Restringe a un deposito. | codice |
| **Articolo** | | Restringe a un articolo. | codice |
| **Cod. Iva**, **Reparto**, **Cat. Merc.**, **Fornitore**, **Stagione**, **Gruppo**, **Marchio**, **Sottogruppo** | | I filtri con cui scegliere quali articoli toccare. | codici |
| **Nuovo Codice** | ● | Il codice da attribuire. | codice |

{: .campi }

### Le variazioni a due campi

| Maschera | Campi |
|---|---|
| *Variazione Codice Articolo* | **Articolo**, **Nuovo Codice** |
| *Varia Categoria Economica Clienti* | **Da Cat. Economica**, **A Cat. Economica** |
| *Varia Registro Scontrini* | **Da Registro**, **A Registro** |
| *Variazione Conto* | **Da Conto**, **A Conto** |

### Rimozione Movimento di Prima Nota

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Da Numero**, **A Numero** | ● | L'intervallo di registrazioni. | numeri |
| **Da Data**, **A Data** | ● | Il periodo. | date |

{: .campi }

### Rimozione Movimenti di Magazzino

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Da Num. Movimento**, **A Num. Movimento** | ● | L'intervallo di movimenti. | numeri |
| **Da Data**, **A Data** | ● | Il periodo. | date |
| **Causale Magazzino** | | Restringe a una causale. | codice |
| **Deposito** | | Restringe a un deposito. | codice |

{: .campi }

### Riporto Saldi Contabili da Scadenziario

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data** | ● | La data delle registrazioni generate. | data |
| **Riporta** | ● | Da quale scadenziario partire. | `CLIENTI`, `FORNITORI` |
| **Causale Cont.** | ● | La [causale contabile](../contabilita/causali-contabili.md) da usare. | codice |
| **Bil. Apertura** | | Il conto di bilancio di apertura. | codice |

{: .campi }

### Azzera Listino

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Listino** | ● | Il listino da azzerare. | codice |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Conferma la password, o avvia la procedura. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco valori | ++f10++ o ++space++ | Sui campi con il codice, apre l'elenco. |

## Come si fa

### Cambiare un codice già usato

1. Chiama l'assistenza e concorda l'intervento.
2. **Fai una copia di sicurezza degli archivi** e fai uscire tutti dal
   programma.
3. Apri ogni anno di gestione con
   [Scegli Esercizio](esercizi-e-chiusure.md) ed esegui su ciascuno
   **Aggiorna Catalogo Dati**.
4. Apri la voce di variazione che serve e inserisci la password.
5. Indica il codice attuale e il **Nuovo Codice**.
6. Alla domanda *Confermi la Variazione?* rispondi **Sì**.
7. A fine lavoro Facile mostra un riepilogo di quello che ha toccato.

### Rimuovere un blocco di movimenti sbagliati

1. Stampa prima l'elenco di quello che stai per togliere — il
   [giornale di magazzino](../magazzino/stampe-movimenti-magazzino.md) o il
   [libro giornale](../contabilita/stampe-contabili.md).
2. Fai la copia di sicurezza.
3. Apri **Rimozione Movimenti di Magazzino** o **Rimozione Movimento Prima
   Nota**, inserisci la password e indica l'intervallo.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Password non Valida!* | La password inserita non è corretta. | Chiedila all'assistenza: non è una password d'utente. |
| *Attenzione!<br>Prima di utilizzare la procedura assicurarsi che nessun altro utente stia utilizzando il programma. …* | L'avviso di cautela che precede quasi tutte le procedure. | Leggilo: elenca i tre prerequisiti veri. |
| *Confermi la Variazione?* | Conferma prima di cambiare i codici. | **Sì** procede. La risposta preimpostata è **No**. |

A fine lavoro ogni variazione dice quanto ha toccato. Il testo cambia con la
procedura:

| Messaggio | Da dove arriva |
|---|---|
| *Variazione conclusa regolarmente!<br><br>N records modificati* | Le variazioni semplici: IVA, categorie merceologiche, stagioni, marchi, reparti. |
| *Variazione deposito conclusa regolarmente!<br><br>Sono stati aggiornati N records* | **Variazione Codici Deposito**. |
| *Variazione codice conclusa con successo : N records modificati* | **Variazione Codici Articoli**. |

Il numero è la somma delle righe riscritte in **tutti** gli archivi toccati,
non degli articoli: su una variazione di deposito o di codice articolo è
normale che sia molto alto.

Le altre risposte della variazione del codice articolo:

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impossibile trovare l' articolo !* | Il codice vecchio non esiste. | Controlla il codice. |
| *I due codici indicati sono identici!<br><br>Impossibile continuare.* | Vecchio e nuovo codice coincidono. | Correggi il codice nuovo. |
| *Il codice del nuovo articolo è già presente in archivio !<br><br>Vuoi unificare gli articoli ?* | Il codice di destinazione esiste già. | **Sì** fonde i due articoli in uno: movimenti, listini e giacenze del vecchio passano al nuovo e il vecchio sparisce. È irreversibile. La risposta preimpostata è **No**. |

## Note

!!! note "Perché serve aprire tutti gli anni"

    Una variazione di codice deve raggiungere anche gli archivi degli anni
    passati. Se un anno non è stato aperto e catalogato, la procedura non lo
    vede: il codice resta cambiato in un anno e vecchio in un altro, e le
    statistiche pluriennali smettono di quadrare.

!!! note "Molte finestre riusano lo stesso titolo"

    Cinque voci diverse — categorie economiche, causali di magazzino, operatori,
    agenti, commesse — aprono una finestra intitolata *Varia Categoria Economica
    Clienti*, perché è la stessa maschera parametrizzata. Il titolo non è
    aggiornato, ma i campi lavorano sul dato giusto.

!!! info "Quanto lavoro fa ciascuna variazione"

    Non sono tutte uguali, e il tempo che ci mettono lo dice.

    **IVA, categorie merceologiche, stagioni, marchi, reparti** cambiano un solo
    campo nell'anagrafica articoli, con una sola operazione. Durano un attimo:
    quei codici stanno solo lì.

    **Deposito** tocca **diciannove archivi**: righe dei documenti, movimenti di
    magazzino e storico, promozioni, distinte, contatori degli articoli,
    ubicazioni, inventario elettronico, produzione, scorte, testate dei carichi,
    scarti, matricole, risorse, manutenzioni, movimenti fiscali, contratti
    clienti e causali di magazzino.

    **Codice articolo** è la più pesante: tocca una **cinquantina di archivi**
    dell'anno in corso — tutto quello che nomina un articolo, dalle righe dei
    documenti ai listini, dai codici a barre alle distinte base, dagli allegati
    ai lotti — e poi ripete il giro sugli archivi **degli ultimi dieci anni**.
    Su un archivio grande può durare a lungo, ed è il motivo per cui va lanciata
    con tutti fuori dal programma.

    Di ogni variazione di codice articolo resta **traccia in archivio**: il
    programma registra codice vecchio, codice nuovo e data.

!!! info "Che cos'è «Abilita NoSync»"

    È un interruttore che **sospende i controlli di coerenza fra archivi**.

    Normalmente, quando il programma legge un documento che cita un cliente
    cancellato, un articolo che non c'è più o una causale sparita, si ferma con
    un errore e non lo fa aprire. Con NoSync acceso non si ferma: al posto della
    descrizione mancante scrive `*** NOT FOUND ***` e va avanti.

    Serve a **entrare in un archivio rotto per ripararlo**: senza, certe
    maschere non si aprirebbero nemmeno e non ci sarebbe modo di correggere il
    dato che manca.

    Due cose da sapere:

    - è un **interruttore**: la stessa voce lo accende e lo spegne, e il
      programma risponde *Flag NoSync Abilitato !* o *Flag NoSync Disabilitato
      !*. Quando è acceso, accanto alla voce di menu compare il segno di spunta;
    - **vale solo per la sessione**: chiudendo Facile torna spento, e vale solo
      sulla postazione che lo ha acceso.

    Lavorare con NoSync acceso è pericoloso: i controlli che impediscono di
    salvare dati incoerenti sono spenti. Si accende per la riparazione e si
    spegne subito dopo.

!!! warning "«Inversione Modalità IVA» e «Articoli IVA Inclusa/Esclusa» fanno cose opposte"

    Si somigliano nel nome e vanno tenute ben distinte.

    **Articoli IVA Inclusa** e **Articoli IVA Esclusa** cambiano solo il
    **segno**: mettono quel flag su tutti gli articoli e sulla ditta, e **non
    toccano un prezzo**. Un articolo da 100 resta da 100: cambia solo che adesso
    quel 100 si legge come lordo invece che come netto. Serve quando
    l'impostazione è stata sbagliata in partenza e i prezzi caricati erano già
    giusti.

    **Inversione Modalità IVA** fa la **conversione vera**: gira il flag della
    ditta e poi ricalcola, aliquota per aliquota, **tutti i prezzi** — i listini
    di ogni articolo, l'ultimo e il penultimo prezzo di acquisto, e i prezzi, i
    costi, le spese e i prezzi fornitore di **tutti i movimenti di magazzino**.
    Un listino da 100 con IVA al 22% diventa 122, o viceversa.

    Sbagliare fra le due è uno degli errori più costosi: la prima lascia i
    prezzi e cambia il significato, la seconda lascia il significato e cambia i
    prezzi. Prima di lanciarle, **la copia di sicurezza non è un consiglio**.

## Vedi anche

- [Manutenzione degli archivi](manutenzione-archivi.md)
- [Esercizi, ditte e chiusure contabili](esercizi-e-chiusure.md)
- [Movimenti di magazzino](../magazzino/movimenti-magazzino.md)
- [Gestione prima nota](../contabilita/gestione-prima-nota.md)
