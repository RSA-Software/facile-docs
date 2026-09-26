---
title: Anomalie carichi e promozioni sellin
description: Le anomalie riscontrate sui carichi ai punti vendita e le promozioni concordate con il fornitore.
modulo: Magazzino
maschera_id: IDD_PRM_PROMO_SELLIN
---

# Anomalie carichi e promozioni sellin

Due sottomenu che riguardano il rapporto con il fornitore: le **anomalie** che
si trovano sulla merce in arrivo ai punti vendita, e le **promozioni sellin**,
cioè le condizioni promozionali che il fornitore concede a chi compra.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Magazzino ▸ Anomalie Carichi Merci ▸ Gestione *(oppure* Inserimento*,* Modifica*,* Riepilogo *o* Contabilizza*)*
        - Menu ▸ Magazzino ▸ Promozioni Sellin ▸ Inserimento *(oppure* Modifica*)*
    - **Scorciatoia:** ++f2++ salva o avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

**Anomalie Carichi Merci** registra quello che non torna sulla merce arrivata a
un punto vendita: quantità mancanti, merce danneggiata, prezzi diversi da
quelli concordati. È un documento a tutti gli effetti, che si può riepilogare e
contabilizzare.

**Promozioni Sellin** sono le promozioni **in acquisto**: lo sconto o il
contributo che il fornitore riconosce su un periodo. Da non confondere con le
[promozioni](../vendite/promozioni.md) del menu Vendite, che sono i prezzi
promozionali **in vendita**.

## Prerequisiti

Prima di usare queste maschere occorre avere i
[fornitori](../anagrafiche/anagrafica-fornitori.md), gli
[articoli](../anagrafiche/anagrafica-articoli.md) e — per le anomalie — i
[carichi](carico-merci.md) su cui l'anomalia è stata riscontrata.

## La maschera

![Anomalie carichi merci](../../assets/img/magazzino/anomalie-e-promozioni-sellin.png)

Le **Anomalie Carichi Merci** usano le stesse maschere dei documenti di
vendita: la [griglia di gestione](../vendite/gestione-documenti.md) con il
titolo *Anomalie Carichi Merce su Punti Vendita*, e la
[maschera del documento](../vendite/documento-di-vendita.md) per inserimento e
modifica. **Riepilogo** e **Contabilizza** sono quelli descritti in
[Riepiloghi](../vendite/riepiloghi-e-statistiche.md) e
[Contabilizzazione](../vendite/contabilizzazione-documenti.md).

Le **Promozioni Sellin** hanno una maschera propria, fatta come un documento:
in alto la testata — di chi è la promozione e per quanto vale — e sotto la
griglia degli articoli, uno per riga, con prezzo, sconti e prezzo netto
calcolato.

Ogni riga si apre in una finestra a parte, *Inserimento Riga Promozione
Sellin*, dove si indicano articolo, prezzo e le condizioni.

## Campi

Per le anomalie valgono i campi del
[documento di vendita](../vendite/documento-di-vendita.md).

### Promozioni Sellin — testata

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Registro** | ● | Il registro su cui la promozione è numerata. | `A` … `Z` |
| **Codice** | ● | Il numero della promozione dentro il registro. Proposto dal programma. | numero |
| **Descrizione** | ● | Il nome della promozione. | testo |
| **Dal**, **Al** | ● | Il periodo in cui la promozione vale **sugli acquisti**: è questo che Facile guarda quando propone il prezzo su un ordine a fornitore. La fine non può precedere l'inizio. | date |
| **Inizio Cessione**, **Fine Cessione** | | Il periodo di cessione concordato con il fornitore. È questo, e non l'altro, che il [controllo listini](../listini-vendita/controllo-listini.md) e l'analisi fornitore guardano per decidere se la promozione è in corso a una certa data. La fine non può precedere l'inizio. | date |
| **Fornitore** | ● | Il fornitore che concede la promozione. | codice |

### Promozioni Sellin — riga

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Articolo** | ● | L'articolo in promozione. | codice |
| **Prezzo** | | Il prezzo di acquisto concordato, al lordo degli sconti. | importo |
| **%Sco.1** … **%Sco.7** | | I sette sconti percentuali, applicati **a cascata**: ciascuno agisce su quello che resta dopo il precedente. | percentuali |
| **Sconto Merce** | | Lo sconto in merce, cioè i pezzi in omaggio. Non entra nel prezzo netto: viaggia a parte, come quantità. | quantità |
| **Sconto Valore** | | Uno sconto a importo fisso, sottratto dopo i sette percentuali. | importo |
| **Prezzo Netto** | | Calcolato dal programma: prezzo meno i sette sconti a cascata meno lo sconto valore. Non modificabile. | — |

!!! note "Lo sconto merce non abbassa il prezzo netto"

    Gli sconti percentuali e lo sconto valore riducono il prezzo; lo **sconto
    merce** no, perché non è uno sconto sul prezzo ma dei pezzi in più a parità
    di importo. Nel documento finisce nella sua colonna, accanto alla
    quantità.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco. |
| **F6 - Elimina** | ++f6++ | Cancella, previa conferma. |
| **Esci** | ++esc++ | Chiude senza salvare. |

Le **Promozioni Sellin**, oltre a questi, hanno:

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F7 - Aggiungi** | ++f7++ | Aggiunge una riga alla promozione. |
| **F8 - Stampa** | ++f8++ | Stampa la promozione, con il suo periodo e il fornitore. |
| **Excel** | | **Importa** articoli e condizioni da un foglio Excel. Non esporta. |
| **Trova** | | Cerca un testo in qualunque colonna della griglia. |

I comandi si accendono dopo il primo salvataggio della testata.

#### Il foglio Excel da importare

Il file è un `.xls` e l'intestazione sta sulla **prima riga**:

| Colonna | Obbl. | Contenuto |
|---|:---:|---|
| `CODICE` | ● | Il codice dell'articolo. |
| `PREZZO` | ● | Il prezzo di acquisto. |
| `DESCRIZIONE` | | La descrizione, a titolo di controllo. |
| `SCONTO1` … `SCONTO7` | | I sette sconti percentuali. |
| `SCONTOMER` | | Lo sconto merce. |
| `SCONTOVAL` | | Lo sconto a valore. |

## Come si fa

### Registrare un'anomalia su un carico

1. Apri **Menu ▸ Magazzino ▸ Anomalie Carichi Merci ▸ Inserimento**.
2. Indica il fornitore e il carico a cui l'anomalia si riferisce.
3. Inserisci le righe con quello che non torna.
4. Salva, e usa **Riepilogo** per il quadro del periodo.

### Registrare una promozione concordata con il fornitore

1. Apri **Menu ▸ Magazzino ▸ Promozioni Sellin ▸ Inserimento**.
2. Indica fornitore, articoli e condizioni concordate.
3. Salva.

## Controlli e messaggi

Per le **anomalie** valgono i messaggi del
[documento di vendita](../vendite/documento-di-vendita.md).

Per le **promozioni sellin**:

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca la descrizione, il fornitore o una data, oppure una data di fine precede la sua data di inizio. | Guarda dove si è posizionato il cursore: è il campo da correggere. |
| *Cancellazioni non abilitate per l' utente !* | L'utente ha il **Blocco Cancellazioni Dati**. | Serve un utente abilitato, o va tolto il blocco da [Archivi ▸ Utenti](../anagrafiche/utenti.md). |
| *Vuoi Cancellare tutte le righe della promozione ?* | Hai premuto **F6 - Elimina**. | **Sì** cancella testata e righe. La risposta preimpostata è **No**. |
| *L'articolo fa parte di un Gruppo Mix!* — *Vuoi inserire tutti gli altri articoli del gruppo ?* | L'articolo appena inserito appartiene a un gruppo mix. | **Sì** aggiunge in blocco gli altri articoli del gruppo. |
| *Vuoi importare gli articoli per la promozione sellin da un foglio Excel ?* | Hai premuto **Excel**. | **Sì** apre la scelta del file. |
| *Colonna CODICE non trovata nel documento !* | Il foglio non ha l'intestazione `CODICE` sulla prima riga. | Correggi l'intestazione. |
| *Colonna OFFERTA non trovata nel documento !* | Manca la colonna del prezzo. **Il messaggio nomina una colonna che non esiste:** quella cercata si chiama `PREZZO`. | Intitola la colonna `PREZZO`. |
| *Formato file non compatibile!* | Il file scelto non è un foglio Excel. | Scegli un `.xls`. |
| *File utilizzato da un' altra applicazione o formato file non compatibile!* | Il foglio è aperto in Excel. | Chiudilo e riprova. |

## Note

!!! note "Sellin e sell-out"

    Le **promozioni sellin** riguardano quello che si compra; le
    [promozioni](../vendite/promozioni.md) del menu Vendite quello che si
    vende. Il rapporto fra le due si misura con la **Stampa Percentuale
    Sell-Out**, vedi
    [Stampe dei movimenti di magazzino](stampe-movimenti-magazzino.md).

!!! info "L'anomalia è un documento, e il carico ne porta il numero"

    Verificando un carico, se quello che è arrivato non corrisponde a
    quello che era stato ordinato o bollettato, il programma **genera un
    documento di anomalie**, con una riga per ogni scostamento, e lo
    annuncia: *È stato generato un documento di Anomalie! Doc. N. …*.

    Il numero di quel documento viene **scritto sulla testata del carico**.
    È quello il collegamento: da un carico si risale alla sua anomalia con
    il comando **Anomalia**, che apre il documento; e la ricerca dei
    carichi permette di chiedere i soli carichi **verificati con anomalie**
    o i soli **verificati senza**.

    Un carico ha **una sola** anomalia: rifacendo la verifica il documento
    viene rigenerato.

!!! info "Contabilizzare non è un'elaborazione: apre la prima nota"

    Il comando **Contabilizza** prende i carichi che hai spuntato e apre la
    maschera di **registrazione di prima nota** già compilata con quello
    che sa: il fornitore, il numero e la data della fattura, gli imponibili
    e le imposte che risultano dai carichi.

    Da lì la registrazione si completa e si salva come qualunque altra: il
    programma non registra niente da solo, e finché non salvi non è stato
    scritto nulla.

    Si possono contabilizzare più carichi insieme **solo se hanno lo stesso
    numero e la stessa data di fattura**; altrimenti il programma si ferma
    con *Non si possono contabilizzare carichi con numeri fattura
    differenti.*

!!! note "Dove finiscono le promozioni sellin"

    Registrata, la promozione lavora da sola in quattro posti:

    - **sugli ordini a fornitore**: inserendo un articolo di quel fornitore,
      Facile prende prima le condizioni del
      [listino fornitore](../listini-fornitori/gestione-listini-fornitori.md)
      e poi, se c'è una sellin valida alla data del documento, ci scrive sopra
      le sue — prezzo, sette sconti, sconto merce e sconto valore. Vince la
      promozione, non il listino;
    - nel [controllo listini](../listini-vendita/controllo-listini.md), dove il
      prezzo netto della sellin concorre al **miglior prezzo d'acquisto** e può
      scalzare i due migliori di listino;
    - nell'[analisi fornitore](../listini-fornitori/analisi-fornitore.md) e nella
      **proposta di riordino**, con lo stesso
      criterio;
    - nella [scheda articolo](../anagrafiche/anagrafica-articoli.md), alla
      linguetta *Promo Sellin*, che elenca tutte le sellin di quell'articolo
      per fornitore.

    Attenzione al periodo: gli ordini guardano **Dal / Al**, il controllo
    listini e l'analisi fornitore guardano **Inizio / Fine Cessione**. Se le
    due coppie di date non coincidono, i due posti possono dare risposte
    diverse sullo stesso giorno.

## Vedi anche

- [Carico merci](carico-merci.md)
- [Promozioni](../vendite/promozioni.md)
- [Gestione documenti](../vendite/gestione-documenti.md)
