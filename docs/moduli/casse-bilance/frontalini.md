---
title: Frontalini
description: La gestione e la stampa dei frontalini di scaffale — i cartellini con descrizione, prezzo e prezzo promozionale davanti alla merce.
modulo: Casse e Bilance
maschera_id: IDD_ART_FRONTALINI_ST
---

# Frontalini

Il frontalino è il cartellino che sta sul bordo dello scaffale, davanti alla
merce: descrizione, codice a barre, prezzo, e — quando c'è — il prezzo in
promozione con le date di validità. Ogni volta che un prezzo cambia il
frontalino va rifatto, e questa maschera serve a tenerne il conto.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Casse e Bilance ▸ Gestione e Stampa Frontalini
    - **Scorciatoia:** ++f2++ – ++f8++ i comandi della barra, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; la voce di menu si abilita per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

La finestra si chiama **Stampa Frontalini**, ma non è solo una stampa: è
l'elenco dei frontalini da rifare. Si riempie con gli articoli il cui prezzo è
cambiato in un periodo, si sfoltisce a mano, e si stampa quello che resta.

Il pulsante **F8 - Acquisisci** consente anche di riempirlo con i codici letti
da un terminalino: si gira il negozio segnando gli scaffali da aggiornare, e la
lista si compila da sé.

## Prerequisiti

Prima di stampare i frontalini occorre:

- avere gli [articoli](../anagrafiche/anagrafica-articoli.md) con descrizione e
  codice a barre;
- avere impostato il **tipo di stampante barcode** nei
  [parametri della ditta](../anagrafiche/ditte.md): senza quello la stampa non
  parte;
- avere almeno un **formato** di frontalino configurato.

## La maschera

![Stampa frontalini](../../assets/img/casse-bilance/frontalini.png)

In alto i filtri con cui si popola l'elenco — il periodo, la categoria, il
reparto — poi il formato e l'ordinamento; sotto la griglia dei frontalini, con
la casella di scelta sulla prima colonna. I comandi stanno nella barra in
testa.

Le colonne sono **Sel.**, **Codice**, **Descrizione**, **Barcode**,
**Prezzo**, **Prezzo Promo**, **Dal**, **Al**, **Cod. Bat.** e **Ultima
Stampa**. L'ultima dice quando quel frontalino è stato stampato l'ultima volta:
è il modo per accorgersi di quelli mai rifatti.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | | Il periodo in cui i prezzi sono cambiati. | date |
| **Cat. Merc.** | | Restringe a una [categoria merceologica](../magazzino/categorie-merceologiche.md). | codice |
| **Reparto** | | Restringe a un [reparto](../magazzino/reparti.md). | codice |
| **Formato** | ● | Il modello di frontalino da stampare. | voce dell'elenco |
| **Ordine** | | Come ordinare la stampa: conviene farla seguire il giro che si fa in negozio. | `NUMERO ACQUISIZIONE`, `DATA ACQUISIZIONE`, `CATEGORIA MERCEOLOGICA` |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Aggiungi** | ++f2++ | Aggiunge un articolo alla lista. |
| **F3 - Apri** | ++f3++ | Apre la riga corrente. |
| **F4 - Seleziona** | ++f4++ | Spunta le righe. |
| **F5 - Deselez. Tutti** | ++f5++ | Toglie la spunta da tutte. |
| **F6 - Elimina** | ++f6++ | Toglie dalla lista le righe **spuntate**, previa conferma. Non cancella gli articoli: solo le righe da stampare. |
| **F7 - Stampa** | ++f7++ | Stampa i frontalini spuntati. |
| **F8 - Acquisisci** | ++f8++ | Riempie la lista con i codici letti da un terminalino. |
| **Esci** | ++esc++ | Chiude la maschera. |

## Come si fa

### Rifare i frontalini dopo un cambio prezzi

1. Cambia i prezzi dai [listini](../listini-vendita/gestione-listini.md).
2. Apri **Menu ▸ Casse e Bilance ▸ Gestione e Stampa Frontalini**.
3. Metti in **Data Iniziale** e **Data Finale** il periodo del cambio.
4. Scegli il **Formato** e metti **Ordine** su `CATEGORIA MERCEOLOGICA`, così
   la stampa esce nell'ordine in cui girerai il negozio.
5. Controlla la griglia e togli con **F6 - Elimina** quello che non serve.
6. Spunta le righe da stampare e premi **F7 - Stampa**.
7. Alla domanda *Vuoi confermare le etichette ?* rispondi **Sì** se sono uscite
   bene: le righe risultano stampate e la colonna **Ultima Stampa** si
   aggiorna.

### Segnare gli scaffali da rifare con il terminalino

1. Gira il negozio leggendo i codici a barre degli scaffali da aggiornare.
2. Apri la maschera e premi **F8 - Acquisisci**.
3. Alla domanda *Vuoi eliminare le letture?* rispondi **Sì** per svuotare il
   terminalino.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Nessun formato di stampa disponibile!* | Non è configurato alcun modello di frontalino. | Chiedi all'assistenza di installarne uno. |
| *Nessuna riga selezionata per la stampa!* | Non hai spuntato nulla. | Spunta le righe, o usa **F4 - Seleziona**. |
| *Nessuna riga selezionata per la cancellazione!* | Hai premuto **F6 - Elimina** senza spuntare niente. | Spunta le righe da togliere. |
| *Frontalini selezionati : n* — *Confermi la cancellazione ?* | Hai premuto **F6 - Elimina**. | Il numero dice quante righe stai per togliere: se non torna, **No** e ricontrolla le spunte. La risposta preimpostata è **No**. |
| *Cancellazioni non abilitate per l' utente !* | L'utente ha il **Blocco Cancellazioni Dati**. | Solo chi può cancellare può usare **F6 - Elimina**. Il blocco si toglie da [Archivi ▸ Utenti](../anagrafiche/utenti.md). |
| *Tipo Stampante Barcode non Impostato.* / *Stampante Barcode non impostata !* | Manca la stampante nei parametri della ditta. | Impostala prima di stampare. |
| *Impossibile Inizializzare la Stampa !* | La stampante non risponde. | Controlla collegamento e driver. |
| *Vuoi confermare le etichette ?* | La stampa è finita. | **Sì** se sono uscite bene: le righe risultano stampate. **No** le lascia da rifare, **Annulla** ferma. |
| *Vuoi eliminare le letture?* | Dopo l'acquisizione dal terminalino. | **Sì** svuota il terminalino, **No** le lascia. |

## Note

!!! note "La conferma dopo la stampa non è una formalità"

    È la domanda *Vuoi confermare le etichette ?* a segnare i frontalini come
    stampati e ad aggiornare la colonna **Ultima Stampa**. Se la carta si
    inceppa, rispondi **No**: le righe restano in lista e si ristampano.

!!! info "Il formato del frontalino si imposta nella ditta"

    Il disegno del cartellino è un **modello di stampa**, scelto dal campo
    **Modulo Frontalini** nella scheda della [ditta](../anagrafiche/ditte.md).
    Quel numero punta al modello corrispondente fra quelli installati: il
    modello `4` è il file `frn00004.rpt` nella cartella dei report.

    Non c'è un elenco di formati standard fra cui scegliere dal programma: i
    modelli sono quelli che l'installazione ha, e per averne uno nuovo — un
    formato di cartellino diverso, un logo, un prezzo più grande — si passa
    dall'assistenza.

    La **stampante** invece è quella impostata come stampante dei frontalini in
    [Impostazione Stampanti](../utility/impostazioni-postazione.md): la stampa
    ci passa da sola e poi rimette a posto la stampante predefinita.

!!! info "Che cos'è il «Cod. Bat.»"

    È il **codice che finisce stampato sul cartellino**, e non è sempre il
    codice dell'articolo.

    Il programma lo riempie con il **codice a barre dell'articolo** — l'ultimo
    registrato, se ce n'è più d'uno — perché è quello che il cliente e il
    lettore devono trovare sullo scaffale. Se l'articolo non ha codici a barre,
    e si è acquisito il frontalino leggendo un codice diverso da quello
    dell'articolo, ci finisce il codice letto.

    Accanto viaggia la **quantità del codice a barre**: serve per i codici che
    valgono per una confezione e non per il pezzo singolo, così il prezzo sul
    cartellino resta quello giusto.

    In pratica: se su un cartellino compare un codice che non riconosci, è il
    codice a barre, non il codice interno.

!!! info "I terminalini che F8 - Acquisisci riconosce"

    Il pulsante apre un menu, e in fondo ci sono i terminali:

    | Voce | Terminale |
    |---|---|
    | **Terminale Formula 734** | Formula 734 |
    | **Terminale EIA Thunder - Solaris** | EIA Thunder / Solaris |
    | **Terminale TYSSO BCP8000** | Tysso BCP8000 |
    | **Terminale DENSO N661** | Denso N661 |
    | **Terminale Meteor 486** | Meteor ECO 486 |
    | **Terminale Unitech PT630D** | Unitech PT630D |
    | **Terminale Symbol PDT3011** | Symbol PDT3011 |

    Tre di questi lasciano il file in una posizione fissa, che vale la pena
    conoscere quando la lettura non arriva:

    | Terminale | File letto |
    |---|---|
    | Tysso BCP8000 | `in\letture.txt` |
    | Denso N661 | `in\dati.dat` |
    | Formula 734 | i file `in\term*.dat` |

    Lo stesso menu porta anche le voci che non riguardano i terminali —
    **Data Variazione Listino**, **Flag Variazione Listino**, **Flag Variazione
    Frontalini**, **Flag Variazione Articoli** e **Selezione Multipla
    Articoli** — con cui si sceglie che cosa mettere in elenco invece di
    leggerlo da un terminale.

!!! note "Solo l'Unitech manda anche il prezzo"

    Degli altri terminali arriva il **codice e basta**: il prezzo del cartellino
    lo prende Facile dal listino. Dall'Unitech PT630D arriva anche il prezzo
    letto, e viene usato quello — ma se è a zero, o se il listino indicato non è
    quello della ditta, il programma torna comunque a prendere il prezzo dal
    listino.

## Vedi anche

- [Casse](casse.md)
- [Bilance](bilance.md)
- [Stampe e manutenzione di casse e bilance](stampe-casse-bilance.md)
- [Gestione listini](../listini-vendita/gestione-listini.md)
