---
title: Analisi e giacenza dei lotti
description: Le due analisi dei lotti — l'andamento economico di ciascun lotto e la giacenza residua.
modulo: Analisi Dati
maschera_id: IDD_ART_ANALISI_LOTTI
---

# Analisi e giacenza dei lotti

Chi compra a lotti — una partita di merce, uno stock, una campagna — vuole
sapere due cose: **quanto è rimasto** e **com'è andata**. Le due voci di questa
pagina rispondono all'una e all'altra, con la stessa maschera.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Analisi Dati ▸ Analisi Lotti
        - Menu ▸ Analisi Dati ▸ Giacenza Lotti
    - **Scorciatoia:** ++f2++ esporta in Excel, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

!!! note "Solo nella versione Evolution"

    Il menu **Analisi Dati** compare soltanto in Facile Evolution.

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Analisi Lotti** | L'andamento di ciascun lotto: quanto è entrato, quanto è uscito, a che prezzi. |
| **Giacenza Lotti** | Quanto resta di ciascun lotto. |

È la stessa maschera con due modi: cambia il titolo e cambia quello che la
griglia mostra.

## Prerequisiti

Prima di analizzare i lotti occorre:

- avere la **gestione dei lotti attiva**;
- avere caricato la merce indicando il lotto, dal
  [carico merci](../magazzino/carico-merci.md);
- avere un [listino](../listini-vendita/gestione-listini.md) da usare come
  riferimento per i valori.

## La maschera

![Analisi lotti](../../assets/img/analisi-dati/analisi-lotti.png)

In alto i filtri, sotto la griglia con un lotto per riga, e la barra dei comandi
con l'esportazione.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Carico Dal**, **Data Carico Al** | ● | Il periodo in cui i lotti sono stati caricati. | date |
| **Deposito** | | Restringe a un [deposito](../magazzino/depositi.md). Vuoto significa `TUTTI`. | codice |
| **Listino** | | Il listino con cui valorizzare. | codice |
| **Stato** | | Quali lotti mostrare. | `TUTTI`, `APERTI`, `CHIUSI` |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 Esporta** | ++f2++ | Esporta la griglia su un foglio Excel. |
| **Esci** | ++esc++ | Chiude la maschera. |
| Elenco valori | ++f10++ o ++space++ | Su **Deposito** e **Listino**, apre l'elenco. |

## Come si fa

### Vedere cosa resta di una partita

1. Apri **Menu ▸ Analisi Dati ▸ Giacenza Lotti**.
2. Indica il periodo di carico e metti **Stato** su `APERTI`: restano i lotti
   con merce ancora a magazzino.
3. Premi **F2 Esporta** se vuoi lavorarci in Excel.

### Capire com'è andato uno stock

1. Apri **Analisi Lotti**.
2. Indica il periodo di carico e il **Listino** con cui valorizzare.
3. Metti **Stato** su `CHIUSI` per esaminare le partite già esaurite.

### Trovare i lotti fermi

Metti **Stato** su `APERTI` e allarga il periodo di carico all'indietro: i lotti
vecchi ancora aperti sono quelli su cui la merce non gira. Per la scadenza vera
e propria c'è la
[Stampa Lotti in Scadenza](../anagrafiche/stampe-lotti-e-barcode.md).

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impossibile inizializzare il file excel!* | L'esportazione non è riuscita. | Chiudi qualche programma e riprova. |
| *(messaggio della libreria Excel)* | Errore in scrittura del foglio. | Controlla che il file non sia già aperto e che la cartella sia scrivibile. |

## Note

!!! note "Il menu dice «Giacenza», la finestra dice «Giacenze»"

    La voce di menu è al singolare, il titolo della finestra al plurale. È la
    stessa cosa.

!!! note "Lotti chiusi e lotti scaduti sono cose diverse"

    Qui `CHIUSI` vuol dire *esauriti*, non *scaduti*. La scadenza si guarda dalla
    [stampa dei lotti in scadenza](../anagrafiche/stampe-lotti-e-barcode.md).

!!! info "Che cosa esce dalle due voci"

    Non c'è una griglia a video: tutte e due producono **un foglio Excel**, e
    il programma chiede dove salvarlo. Cambiano le colonne, e sono il motivo
    per cui le voci sono due.

    **Giacenza Lotti** risponde a *quanto me n'è rimasto*:

    | Colonna | Contenuto |
    |---|---|
    | `DATA`, `N. CARICO` | Quando il lotto è entrato e con quale carico. |
    | `CODICE`, `DESCRIZIONE` | L'articolo. |
    | `FORNITORE` | Da chi è arrivato. |
    | `LOTTO` | Il numero di lotto. |
    | `INIZIO VEND.`, `SCADENZA` | Da quando si può vendere e quando scade. |
    | `U. MIS.` | L'unità di misura. |
    | `Q.TA CARICATA`, `Q.TA SCARICATA`, `ESISTENZA` | Entrato, uscito, rimasto. |
    | `REALE` | L'esistenza reale. |
    | `LISTINO`, `IMPORTO` | Il prezzo unitario e il valore della rimanenza. |

    **Analisi Lotti** risponde a *quanto ci ho guadagnato*:

    | Colonna | Contenuto |
    |---|---|
    | `DATA`, `N. CARICO`, `FORNITORE` | L'origine del lotto. |
    | `CODICE`, `DESCRIZIONE`, `LOTTO` | L'articolo e il lotto. |
    | `Q.TA CARICATA`, `PREZZO`, `VAL. CARICATO` | Quanto è entrato, a che prezzo, per quanto valore. |
    | `Q.TA SCARICATA`, `VAL SCARICATO` | Quanto è uscito e per quanto valore. |
    | `PROVV.` | Le provvigioni maturate su quel venduto. |
    | `VALORE GIACENZA` | Quanto vale quello che resta. |
    | `MARGINE` | Il margine del lotto. |
    | `MARGINE/Q.TA' VENDUTA` | Il margine per pezzo venduto. |
    | `MARGINE/VALORE VENDUTO` | Il margine in percentuale sul venduto. |

    In breve: **Giacenza** è una fotografia del magazzino lotto per lotto,
    **Analisi** è il conto economico dello stesso lotto.

!!! info "Le due voci ci sono solo con la gestione dei lotti attiva"

    L'interruttore è **Usa Gestione Lotti**, nella scheda della
    [ditta](../anagrafiche/ditte.md).

    Se è spento, il programma **toglie le voci dal menu all'avvio** — insieme
    alla stampa delle etichette dei lotti e a quella dei lotti in scadenza. Non
    si aprono e mostrano un risultato vuoto: **non ci sono proprio**. Se non le
    trovi, è lì che va guardato.

!!! info "A che cosa serve il campo Listino"

    A **valorizzare quello che resta**. Il numero indicato sceglie quale dei
    [listini di vendita](../listini-vendita/gestione-listini.md) usare, e per
    ogni lotto il programma prende il prezzo che l'articolo ha su quel listino:

    - in **Giacenza Lotti** finisce nella colonna `LISTINO`, e moltiplicato per
      l'esistenza dà l'`IMPORTO`;
    - in **Analisi Lotti** è la base del `VALORE GIACENZA`.

    Arriva già impostato con il **listino di vendita della ditta**: cambiandolo
    si cambia solo il metro con cui la rimanenza viene valutata, non i dati di
    carico e scarico.

    Se un articolo non ha prezzo su quel listino, il suo valore risulta **zero**
    e il foglio non lo segnala: una rimanenza che vale zero a fronte di
    un'esistenza diversa da zero è quasi sempre questo.

## Vedi anche

- [Stampa lotti in scadenza e spostamenti codici a barre](../anagrafiche/stampe-lotti-e-barcode.md)
- [Carico merci](../magazzino/carico-merci.md)
- [Venduto per…](venduto-per.md)
