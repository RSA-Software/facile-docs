---
title: Manutenzione degli archivi
description: I ricalcoli che rimettono a posto saldi ed esistenze, lo storico dei movimenti, il catalogo dati, la rinumerazione degli scontrini e le importazioni di servizio.
modulo: Utility
maschera_id: IDD_MAG_RICALCOLO_MAG
---

# Manutenzione degli archivi

Quando i saldi contabili non tornano con le schede, o l'esistenza di un articolo
non corrisponde ai suoi movimenti, il rimedio non è correggere il numero: è
**rifare il calcolo**. Queste voci ricostruiscono i totali a partire dai
movimenti, che restano l'unica verità.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Utility ▸ Ricalcolo Saldi Contabili
        - Menu ▸ Utility ▸ Riporto Esistenze Magazzino Anno Precedente
        - Menu ▸ Utility ▸ Ricalcolo Movimenti di Magazzino
        - Menu ▸ Utility ▸ Valorizzazione Costi Movimenti
        - Menu ▸ Utility ▸ Aggiorna Catalogo Dati
        - Menu ▸ Utility ▸ Aggiungi Movimenti dell' Anno allo Storico
        - Menu ▸ Utility ▸ Rimuovi Movimenti dell' Anno dallo Storico
        - Menu ▸ Utility ▸ Rinumerazione Scontrini
        - Menu ▸ Utility ▸ Importa
        - Menu ▸ Utility ▸ Importa Foto
        - Menu ▸ Utility ▸ Installazione Software su PocketPC
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Ricalcolo Saldi Contabili** | Rifà i saldi dei conti a partire dai movimenti di [prima nota](../contabilita/registrazione-prima-nota.md). |
| **Riporto Esistenze Magazzino Anno Precedente** | Porta nell'anno in corso le esistenze finali dell'anno prima. La finestra si chiama *Riporto esistenze magazzino anno precedente*. |
| **Ricalcolo Movimenti di Magazzino** | Ricostruisce esistenze e progressivi a partire dai [movimenti](../magazzino/movimenti-magazzino.md). |
| **Valorizzazione Costi Movimenti** | Attribuisce ai movimenti il costo secondo il metodo scelto. |
| **Aggiorna Catalogo Dati** | Rifà il catalogo che permette di interrogare gli archivi come se fossero tabelle SQL. È il passo che alcune procedure di assistenza richiedono prima di poter partire. |
| **Aggiungi Movimenti dell' Anno allo Storico** | Porta i movimenti dell'anno nello storico, da cui pescano le statistiche pluriennali. |
| **Rimuovi Movimenti dell' Anno dallo Storico** | Li toglie. |
| **Rinumerazione Scontrini** | Rinumera un intervallo di [scontrini](../vendite/scontrini.md). |
| **Importa** | Carica gli archivi da **fogli Excel**, uno alla volta: clienti, fornitori, articoli, listini e altri diciotto. Serve nel primo popolamento di un'installazione nuova. |
| **Importa Foto** | Carica le fotografie degli articoli da una cartella. **Solo Calzature.** |
| **Installazione Software su PocketPC** | Installa il programma sul palmare collegato. |

## Prerequisiti

Prima di lanciare un ricalcolo occorre:

- **una copia di sicurezza degli archivi**;
- che **nessun altro stia usando il programma**: i ricalcoli riscrivono totali
  su tutto l'archivio;
- del tempo: su archivi grandi durano parecchio e non si interrompono a metà
  senza conseguenze.

Per l'installazione su palmare serve ActiveSync installato sulla postazione.

## La maschera

![Ricalcolo movimenti di magazzino](../../assets/img/utility/manutenzione-archivi.png)

Sono finestre di selezione piccole, con il periodo e il deposito. Alcune voci
non hanno maschera: chiedono conferma e lavorano mostrando l'avanzamento.

## Campi

### Ricalcolo Movimenti di Magazzino

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Deposito** | | Il [deposito](../magazzino/depositi.md) da ricalcolare. Vuoto significa tutti. | codice |
| **Da Data**, **A Data** | ● | Il periodo dei movimenti da rileggere. | date |

{: .campi }

### Valorizzazione Costi Movimenti

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo. | date |
| **Deposito** | | Restringe a un deposito. | codice |
| **Metodo** | ● | Come attribuire il costo. | `COSTO MEDIO PONDERATO`, `METODO LIFO`, `METODO FIFO`, `ULTIMO PREZZO ACQUISTO` |

{: .campi }

### Riporto esistenze magazzino anno precedente

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Deposito** | | Il deposito su cui riportare le esistenze. | codice |

{: .campi }

### Rinumerazione Scontrini

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Dal Numero**, **Al Numero** | ● | L'intervallo di scontrini da rinumerare. | numeri |
| **Nuovo Numero Iniziale** | ● | Il numero da cui ripartire. | numero |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia l'elaborazione. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco valori | ++f10++ o ++space++ | Sul **Deposito**, apre l'elenco. |

## Come si fa

### Rimettere a posto un'esistenza che non torna

1. Controlla prima **perché** non torna: il
   [giornale di magazzino](../magazzino/stampe-movimenti-magazzino.md)
   dell'articolo dice quali movimenti ci sono. Se manca un movimento, il
   ricalcolo non lo inventa.
2. **Fai una copia di sicurezza degli archivi.**
3. Apri **Menu ▸ Utility ▸ Ricalcolo Movimenti di Magazzino**.
4. Indica il **Deposito** e il periodo, e premi **F2 - OK**.

### Rimettere a posto un saldo contabile

1. Controlla la [scheda contabile](../contabilita/schede-contabili.md) del
   conto.
2. Fai la copia di sicurezza e lancia **Ricalcolo Saldi Contabili**.

### Valorizzare il magazzino con un metodo diverso

1. Apri **Valorizzazione Costi Movimenti**.
2. Indica il periodo e scegli il **Metodo**.
3. Premi **F2 - OK**: i movimenti del periodo prendono il costo secondo quel
   criterio, e con esso cambia il valore del magazzino.

### Alimentare le statistiche pluriennali

1. Apri **Aggiungi Movimenti dell' Anno allo Storico**.
2. Alla domanda rispondi **Sì**: la procedura prima toglie l'anno dallo storico
   e poi lo rimette, quindi si può rilanciare senza creare doppioni.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *La procedura permette l' acquisizione dei dati dell' anno allo storico dei movimenti.<br>Per essere eseguita puo' essere necessario parecchio tempo.<br>Vuoi Continuare ?* | Hai avviato l'aggiornamento dello storico. | **Sì** procede. La risposta preimpostata è **No**. |
| *La procedura permette la rimozioni dei dati dell' anno dallo storico dei movimenti.<br>Per essere eseguita puo' essere necessario parecchio tempo.<br>Vuoi Continuare ?* | Hai avviato la rimozione dallo storico. | **Sì** procede. |
| *Impossibile Caricare RAPI.DLL !<br>Controllare presenza installazione ActiveSync.* | Manca ActiveSync per parlare con il palmare. | Installalo sulla postazione. |

A questi si aggiungono i messaggi dei singoli ricalcoli:

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Con questa procedura vengono azzerati e ricalcolati tutti i saldi contabili.<br>Si raccomanda di fare una copia degli archivi prima di procedere e di lavorare con un  solo terminale collegato al programma per tutta la durata dell' operazione.<br><br> Scegliere Si per Continuare.* | Conferma richiesta dal **Ricalcolo Saldi Contabili**. | Fai davvero la copia. La risposta preimpostata è **No**. |
| *Errore su Movimento N. n* | Una registrazione di prima nota non si riesce a rileggere. | È un archivio danneggiato: chiama l'assistenza. |
| *Errore su Movimento N. n !<br><br>Correggere il movimento e ricalcolare i saldi.<br><br>Vuoi Continuare ?* | Una registrazione non si riesce a riscrivere. | Prendi nota del numero. **Sì** va avanti con le altre, **No** si ferma. In ogni caso quel movimento va sistemato e il ricalcolo rifatto. |
| *Vuoi effettuare il ricalcolo per deposito ?<br><br>Consigliata per archivi di grandi dimensioni.* | Il **Ricalcolo Movimenti di Magazzino** su più depositi. | **Sì** lavora un deposito per volta, più lento ma più leggero; **No** li fa tutti insieme. |
| *Ricalcolo Magazzino Concluso Regolarmente.* | Il ricalcolo del magazzino è finito. | Nessuna azione. |
| *Vuoi importare i clienti da un foglio EXCEL ?* e le domande analoghe | **Importa**: una domanda per ciascun archivio. | **Sì** apre la scelta del file, **No** passa all'archivio seguente. |
| *Formato file non compatibile!* | Il foglio Excel scelto non ha le colonne attese. | Controlla il tracciato con l'assistenza. |
| *Impossibile Creare la tabella* | Non si riesce a leggere il foglio. | Verifica che il file non sia aperto in Excel. |
| *Impossibile caricare le DLL di Imagekit!* | **Importa Foto** non trova i componenti per leggere le immagini. | Chiama l'assistenza: manca un pezzo dell'installazione. |

## Note

!!! warning "Un ricalcolo non si interrompe"

    Fermare a metà un ricalcolo lascia gli archivi in uno stato peggiore di
    quello di partenza. Lanciali quando c'è il tempo di aspettare, con gli altri
    utenti fuori dal programma.

!!! note "Il ricalcolo ricostruisce, non corregge"

    Rifà i totali **a partire dai movimenti**. Se il problema è un movimento
    sbagliato o mancante, il ricalcolo lo conferma invece di risolverlo: prima
    si sistema il movimento, poi si ricalcola.

!!! info "Che cosa fa «Aggiorna Catalogo Dati»"

    **Non tocca i dati.** Riscrive il file che descrive gli archivi al driver
    ODBC — il *catalogo* — cioè l'elenco delle tabelle e dei campi con cui
    Crystal e le stampe in modalità SQL riescono a interrogare gli archivi.

    Il file sta nella cartella del programma e si chiama `FDATI001.DB` per
    l'anno corrente della ditta 1, `F2025001.DB` per un anno passato: uno per
    ditta e per anno. È per questo che le procedure di assistenza chiedono di
    lanciarlo **su tutti gli anni** e non solo su quello corrente.

    Il programma lo rifà anche da sé quando si accorge che il catalogo è più
    vecchio del programma, e lo rifà sempre alla creazione di un
    [nuovo esercizio](esercizi-e-chiusure.md).

    Serve **solo con gli archivi c-tree**: su PostgreSQL la voce non fa niente,
    perché il catalogo lo tiene il server.

!!! info "Come «Importa Foto» trova le fotografie"

    È una funzione della **versione Calzature**: nelle altre la voce c'è nel
    menu ma non fa niente.

    Le immagini si mettono tutte in **una cartella sola**. La prima volta il
    programma la chiede con un selettore intitolato *Percorso Foto* e poi se la
    ricorda; in sessione remota usa la cartella `in` dell'utente.

    L'abbinamento è **per nome del file**, non per codice articolo. Il nome si
    compone di tre pezzi, tutti minuscoli e senza spazi:

    1. i **primi cinque caratteri del sottogruppo** dell'articolo;
    2. il **codice fornitore** dell'articolo **senza le ultime cinque cifre**;
    3. l'**ultimo carattere** del codice fornitore.

    Il tutto con estensione `.jpg`. Per lo stesso articolo si possono mettere
    fino a **quindici immagini**, aggiungendo al nome `_01`, `_02` e così via
    fino a `_14`.

    Vengono guardati solo gli articoli che hanno almeno un movimento nello
    storico. Di quello che è stato caricato resta il registro in `log\foto.txt`.

!!! warning "«Importa» non importa più da GESA"

    Il nome tradisce l'origine, ma il pezzo che leggeva gli archivi GESA **non
    è più nel programma**: resta nel sorgente disattivato e non viene nemmeno
    compilato.

    Quello che la voce fa davvero è una **catena di importazioni da fogli
    Excel**. Il programma chiede, uno dopo l'altro: clienti, punti fidelity,
    fornitori, scadenze, marchi, stagioni, reparti, categorie merceologiche,
    gruppi, sottogruppi, articoli, codici a barre, esistenze, codici IVA,
    listino, banchi, note degli articoli e ubicazioni.

    A ogni domanda si risponde **No** per saltare quell'archivio, oppure **Sì**
    e si sceglie il file `.xls`. È una sequenza lunga: per caricare un solo
    archivio bisogna rispondere No a tutti gli altri.

    **Ogni foglio deve avere il tracciato che il programma si aspetta**, ed è
    diverso per ciascun archivio: prima di usarla, fatti dare i tracciati
    dall'assistenza.

## Vedi anche

- [Esercizi, ditte e chiusure contabili](esercizi-e-chiusure.md)
- [Assistenza](assistenza.md)
- [Movimenti di magazzino](../magazzino/movimenti-magazzino.md)
- [Schede contabili](../contabilita/schede-contabili.md)
