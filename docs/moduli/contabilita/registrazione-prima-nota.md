---
title: Registrazione di prima nota
description: La maschera con cui si registra un documento in contabilità — testata, righe IVA, righe contabili, ratei e risconti, imputazione analitica.
modulo: Contabilità
maschera_id: IDD_CON_PNOTA
---

# Registrazione di prima nota

La maschera con cui una fattura, un corrispettivo o un movimento di banca
entrano in contabilità. La causale scelta decide quasi tutto: quali campi
compaiono, su quale registro IVA finisce il documento e quali conti vengono
proposti.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Contabilità ▸ Inserimento *(oppure* Modifica*)*, o **F3 - Nuova** dalla [gestione prima nota](gestione-prima-nota.md)
    - **Scorciatoia:** ++f6++ elimina, ++f7++ allegati, ++f8++ causale, ++f9++ integrazioni
    - **Permessi richiesti:** nessun profilo predefinito; **Inserimento** e **Modifica** si abilitano separatamente per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

È il gesto contabile quotidiano: si sceglie la causale, si indica il
cliente o il fornitore, si spezza l'imponibile per aliquota IVA e si controlla
che dare e avere quadrino.

Il programma fa gran parte del lavoro: dalla causale ricava il registro IVA e i
conti da usare, dal cliente o dal fornitore ricava il sottoconto e le
condizioni di pagamento, dalle righe IVA calcola l'imposta.

## Prerequisiti

Prima di usare questa maschera occorre:

- avere le [causali contabili](causali-contabili.md) impostate, perché sono
  loro a governare la registrazione;
- avere il piano dei conti — [mastri](mastri.md), [conti](conti.md),
  [sottoconti](sottoconti.md);
- avere le [aliquote IVA](aliquote-iva.md) e i
  [tipi di pagamento](tipi-di-pagamento.md);
- avere in archivio il [cliente](../anagrafiche/anagrafica-clienti.md) o il
  [fornitore](../anagrafiche/anagrafica-fornitori.md) del documento.

## La maschera

![Inserimento prima nota](../../assets/img/contabilita/registrazione-prima-nota.png)

La finestra si chiama *Inserimento Prima Nota* — in modifica *Modifica Prima
Nota* — ed è divisa in quattro fasce, dall'alto in basso:

1. la **testata**: numero, causale, sezione, protocollo, date, cliente o
   fornitore, pagamento;
2. la **griglia IVA**: una riga per aliquota;
3. i **totali** del documento;
4. la **griglia contabile**: le righe in dare e avere, con in fondo **Totale
   Dare** e **Totale Avere**.

## Campi

### Testata

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Numero** | | Numero della registrazione. Lo assegna il programma. | numero |
| **Causale** | ● | La [causale contabile](causali-contabili.md): decide registro IVA, conti proposti e quali campi compaiono. | codice |
| **Sez.** | | La [sezione](sezioni.md) contabile. | codice |
| **Protocollo** | | Il numero di protocollo sul registro IVA. | numero |
| **Data** | ● | Data di registrazione. | data |
| **Numero Documento**, **Data Documento** | | Gli estremi del documento che si sta registrando. | numero e data |
| **Cliente** | ● | Il nominativo. L'etichetta diventa **Fornitore** o **Conto** secondo la causale. | codice |
| **Pagamento** | | Il [tipo di pagamento](tipi-di-pagamento.md), da cui nascono le scadenze. | codice |
| **Data Decorrenza Pagamento** | | Da quando decorrono le scadenze. | data |
| **Data Competenza** | | La data a cui il costo o il ricavo compete, se diversa da quella di registrazione. | data |
| **Registrazione da Verificare** | | Marca la registrazione come da ricontrollare: si ritrova nella colonna **Verif.** della [gestione prima nota](gestione-prima-nota.md). | attivo/non attivo |
| **Escludi da Spesometro** | | Tiene la registrazione fuori dalla [comunicazione delle operazioni IVA](comunicazioni-iva.md). | attivo/non attivo |

### Griglia IVA

| Colonna | Contenuto |
|---|---|
| **Cod. IVA** | L'[aliquota](aliquote-iva.md) della riga. |
| **Imponibile** | L'imponibile di quell'aliquota. |
| **Aliquota** | La percentuale, proposta dal codice IVA. |
| **Imposta** | L'imposta calcolata. |
| **% Inded.** | La quota di IVA indetraibile. |

### Totali

| Campo | Descrizione |
|---|---|
| **TOTALE DOCUMENTO** | Il totale che deve corrispondere a quello del documento in mano. |
| **TOTALE ARROTOND.** | L'eventuale arrotondamento. |
| **SQUADRATURA** | La differenza fra dare e avere: **deve essere zero**. |
| **IMPORTO VALUTA**, **DESC. VALUTA** | Importo e valuta, per i documenti in valuta estera. |

### Griglia contabile

| Colonna | Contenuto |
|---|---|
| **Conto**, **Sottoconto**, **Descrizione** | Il conto movimentato. |
| **Cau** | La causale della riga. |
| **N. Doc.** | Il numero del documento a cui la riga si riferisce. |
| **Importo**, **D/A** | L'importo e se va in dare o in avere. |
| **Comp.** | La data di competenza della riga. |
| **Ana.** | Segna la riga come oggetto di contabilità analitica. |
| **C.Cos/Ric** | Il [centro di costo o ricavo](centri-di-costo.md). |
| **Commessa** | La [commessa](commesse.md) a cui imputare. |

### Ratei e risconti

Dalla registrazione si aprono le **competenze**, con cui si spalma un costo o
un ricavo su più esercizi:

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Descrizione** | | Cosa si sta ripartendo. | testo |
| **Importo** | ● | L'importo da ripartire. | importo |
| **Inizio**, **Fine** | ● | Il periodo di competenza. | date |
| **Tipologia** | ● | Che genere di scrittura. | `RATEO ATTIVO`, `RATEO PASSIVO`, `RISCONTO ATTIVO`, `RISCONTO PASSIVO` |
| **Calcolo** | ● | Come ripartire. | `GIORNI`, `MESI` |

Sotto compare la ripartizione calcolata, **Anno** per **Importo**.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F6 - Elimina** | ++f6++ | Cancella la registrazione, previa conferma. |
| **F7 - Allegati** | ++f7++ | Allega il documento scansionato alla registrazione. |
| **F8 - Causale** | ++f8++ | Apre la [causale contabile](causali-contabili.md) in uso, per controllarne le impostazioni. |
| **F9 - Integr.** | ++f9++ | Apre le integrazioni, che cambiano secondo il registro della causale: vedi sotto. Sul libro giornale il comando è spento. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

!!! note "Tre comandi si vedono solo in modifica"

    **F6 - Elimina**, **F7 - Allegati** e **F9 - Integr.** compaiono nella
    barra **solo riaprendo una registrazione già fatta**. Mentre ne stai
    inserendo una nuova la barra ha il salvataggio e **F8 - Causale**, e
    basta: allegati e integrazioni si aggiungono dopo aver salvato.

## Come si fa

### Registrare una fattura di acquisto

1. Apri **Menu ▸ Contabilità ▸ Inserimento**.
2. Indica la **Causale** degli acquisti: da lì il programma sa su quale
   registro IVA mettere il documento.
3. Compila **Data**, **Numero Documento** e **Data Documento**.
4. Indica il **Fornitore**: il programma propone il suo sottoconto e il
   pagamento.
5. Nella griglia IVA scrivi una riga per ogni aliquota del documento, con
   **Imponibile** e **Cod. IVA**.
6. Controlla che **TOTALE DOCUMENTO** corrisponda alla fattura e che
   **SQUADRATURA** sia zero.
7. Salva. Se il programma chiede *«Vuoi Inserire adesso il pagamento?»*,
   rispondi **Sì** per generare subito la scadenza.

### Registrare un costo di competenza dell'anno prossimo

1. Registra il documento come sopra.
2. Sulla riga contabile del costo fai **clic sulla cella della colonna
   Comp.**: si apre la finestra delle competenze.
3. Imposta **Tipologia** `RISCONTO ATTIVO`, il periodo e il **Calcolo** a
   `GIORNI`.
4. Confermando, nella colonna **Comp.** compare `SI`.

### Imputare una registrazione a una commessa

1. Sulla riga contabile attiva **Ana.**.
2. Compila **C.Cos/Ric** e **Commessa**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Data esterna all' esercizio corrente !* / *Vuoi Continuare ?* | La data di registrazione cade fuori dall'esercizio aperto. | **No** e correggi la data, salvo che tu voglia davvero registrare fuori esercizio. |
| *Attenzione la data indicata ricade in un esercizio con chiusura effettuata!* / *Vuoi Continuare?* | L'esercizio di quella data è già stato chiuso. | **No**, salvo casi particolari: registrare in un esercizio chiuso ne altera i saldi. |
| *Il cliente selezionato risulta cessato !* / *Vuoi Continuare ?* | Il cliente è marcato come cessato. | Verifica di aver scelto il nominativo giusto. |
| *Attenzione!* / *I movimenti di apertura e di chiusura non possono essere modificati.* | Si è aperta una registrazione di apertura o chiusura dell'esercizio. | Non è modificabile: le scritture di apertura e chiusura si rifanno con le procedure di fine anno. |
| *Attenzione!* / *Il movimento contiene incassi/rettifiche e non può essere modificato.* | Alla registrazione sono già agganciati incassi o rettifiche. | Vanno tolti prima quelli, poi si può modificare. |
| *Attenzione!* / *Il movimento risulta esportato al consulente.* / *Prendere nota delle modifiche apportate* | La registrazione è già stata mandata al commercialista con l'[esportazione movimenti](esportazione-movimenti.md). | Annota la modifica: il consulente ha già la versione precedente. |
| *Vuoi Inserire adesso il pagamento?* | La causale prevede la scadenza e il pagamento non è ancora stato generato. | **Sì** genera subito la scadenza. |
| *Vuoi inserire allegati ?* | Il programma propone di allegare il documento. | **Sì** apre la scelta del file. |

## Note

!!! warning "Attenzione"

    **La squadratura deve essere zero.** Il campo **SQUADRATURA** è il
    controllo che dare e avere coincidano: una registrazione squadrata sporca
    il bilancio e si ritrova poi con
    [Squadrature Movimenti](statistiche-e-controlli.md).

    **La causale comanda.** Cambiarla dopo aver compilato la registrazione può
    cambiare registro IVA, conti e campi visibili. Sceglila per prima.

!!! info "La maschera cambia forma secondo la causale"

    Finché non hai scelto la **Causale** quasi tutto è bloccato: è lei a
    dire che registrazione stai facendo, e la maschera si adatta.

    Dipende da **tre cose** scritte sulla causale:

    **Se ha una relazione con cliente o fornitore.** In quel caso compaiono
    il campo del soggetto — con l'etichetta che diventa *Cliente* o
    *Fornitore* — le tre righe di descrizione, il **Pagamento** e la **Data
    pagamento**. Con una causale senza relazione quei campi **spariscono**,
    non si limitano a bloccarsi; e se ci avevi già scritto qualcosa,
    cambiando causale viene azzerato.

    **Se è una causale IVA.** Solo allora si possono scrivere il **Totale
    documento** e la **griglia dell'IVA**, e si può spuntare l'esclusione
    dallo spesometro. Con una causale non IVA la griglia resta bloccata.

    **Quale registro usa.** Il **Protocollo** si scrive su tutti i registri
    tranne il **libro giornale**, dove non esiste. La **Valuta** si sblocca
    solo sui due registri **CEE** e solo con una causale IVA. Nella griglia
    dell'IVA, la colonna dell'**imposta** si apre o resta bloccata secondo
    il registro e il tipo di aliquota della riga.

!!! info "Che cosa apre F9 - Integr."

    Non è una finestra sola: il comando apre **l'integrazione che serve a
    quel registro**.

    | Registro della causale | F9 apre |
    |---|---|
    | Corrispettivi | La finestra delle **operazioni speciali** dei corrispettivi. |
    | Acquisti, Acquisti CEE | Le **integrazioni per lo spesometro**. Confermando, la registrazione viene anche salvata. |
    | Fatture Emesse, Fatture in Sospensione | Un menu con due voci: **Cointestatari** e **Spesometro**. Se però la causale è una **nota di variazione**, il menu non compare e si va dritti allo spesometro. |
    | Libro giornale | Niente: il comando è spento. |

    Sono tutti dati che il documento non porta con sé ma che le
    comunicazioni fiscali pretendono: da qui si aggiungono senza uscire
    dalla registrazione.

!!! note "Le competenze si aprono dalla griglia, non dalla barra"

    Non c'è un pulsante: si fa **clic sulla cella della colonna Comp.**
    della riga contabile, e si apre la finestra dei ratei e risconti per
    quella riga.

    La riga dev'essere già compilata almeno con il mastro: su una riga vuota
    il clic non fa niente. A competenza impostata, nella colonna compare
    `SI`.

    Allo stesso modo si apre la **contabilità analitica**, dalla cella
    accanto.

!!! note "Il pulsante Fatture Elettroniche non c'è"

    Nelle versioni attuali quel comando **non compare** nella barra della
    registrazione. Le fatture ricevute si registrano partendo dalla loro
    maschera — [Fatture elettroniche
    passive](fatture-elettroniche-passive.md) — che porta i dati in prima
    nota, non il contrario.

## Vedi anche

- [Gestione prima nota](gestione-prima-nota.md)
- [Causali contabili](causali-contabili.md)
- [Fatture elettroniche passive](fatture-elettroniche-passive.md)
- [Stampe contabili](stampe-contabili.md)
