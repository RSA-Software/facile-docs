---
title: Stampe dei movimenti di magazzino
description: Le diciotto stampe di magazzino — giornale, sintesi per reparto e categoria, valore del magazzino, sell-out, interrogazione articolo e adempimenti.
modulo: Magazzino
maschera_id: IDD_ST_MAGAZZINO
---

# Stampe dei movimenti di magazzino

Le voci in fondo al menu **Magazzino**: le stampe che leggono i movimenti senza
distinguere fra clienti e fornitori, più le interrogazioni e gli adempimenti di
settore.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Magazzino ▸ *(una delle voci elencate sotto)*
    - **Scorciatoia:** ++f2++ avvia la stampa, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | Cosa mostra |
|---|---|
| **Interrogazione Articolo** | La situazione di un articolo a video: esistenze, movimenti, prezzi. |
| **Giornale di Magazzino** | Il giornale dei movimenti in ordine cronologico. |
| **Stampa Vendite con Ricavo - Margine - Ricarico** | Il venduto con i tre indicatori di redditività. |
| **Stampa Percentuale Sell-Out** | La percentuale di sell-out. |
| **Stampa Percentuale Sell-Out Fornitore** | La stessa, per fornitore. La voce di menu è scritta *Stampa Precentuale Sell-Out Fornitore*, con un refuso. |
| **Sintesi Movimenti** | Il riepilogo dei movimenti del periodo. |
| **Sintesi Movimenti - Margini Ultimo Prezzo d' Acquisto** | La stessa sintesi, con i margini calcolati sull'ultimo costo. |
| **Sintesi Movimenti per Reparto** | I movimenti raggruppati per [reparto](reparti.md). |
| **Sintesi Movimenti per Categoria Merceologica** | Raggruppati per [categoria merceologica](categorie-merceologiche.md). |
| **Sintesi Movimenti per Giorno** | Raggruppati per giorno. |
| **Movimenti Magazzino per Articolo** | I movimenti di ciascun articolo. |
| **Movimenti Periodo** | I movimenti di un periodo. |
| **Venduto per Agenti/Cat. Merceologica** | Il venduto incrociato fra agente e categoria. |
| **Valore Magazzino** | Quanto vale la merce in giacenza. |
| **Stampa Registro Sostanze Zuccherine** | Il registro delle sostanze zuccherine. |
| **Modello HACCP Merci in Accettazione** | Il modulo HACCP per la merce in entrata. |
| **Esistenze da Lettore Formula 734** | Acquisisce le esistenze rilevate con il lettore Formula 734. |

## Prerequisiti

Prima di usare queste stampe occorre avere movimentato il magazzino con
[carichi](carico-merci.md),
[documenti di vendita](../vendite/documento-di-vendita.md) o
[movimenti diretti](movimenti-magazzino.md).

## La maschera

![Stampe di magazzino](../../assets/img/magazzino/stampe-movimenti-magazzino.png)

La maggior parte apre la stessa finestra di selezione delle
[stampe magazzino clienti](stampe-magazzino-clienti.md), con un parametro
diverso; **Interrogazione Articolo**, **Valore Magazzino**, **Movimenti
Periodo** e i due adempimenti hanno una maschera propria.

!!! info "I campi di Valore Magazzino"

    Ha i filtri consueti — deposito, sezione, articolo, aliquota IVA,
    reparto, categoria merceologica, marchio, stagione, settore, gruppo,
    sottogruppo, mix, fornitore e le tre tabelle libere — e in più quattro
    campi suoi:

    | Campo | Cosa decide |
    |---|---|
    | **Metodo** | Come valorizzare le giacenze: vedi sotto. |
    | **Calcolo** | Se i valori escono **IVA esclusa** o **IVA inclusa**. |
    | **Data Stampa** | La data che compare sul modulo. |
    | **Ricalcolo Automatico** | Rifà i conteggi prima di stampare, invece di usare quelli già in archivio. |

!!! info "I campi di Movimenti Periodo"

    **Data Iniziale** e **Data Finale**, **Deposito**, **Reparto**,
    **Sezione**, più due scelte:

    - **Formato**: `TUTTI I MOVIMENTI` oppure `SOLO MOVIMENTI DI VENDITA`;
    - **Ordinamento**: per deposito e codice, per deposito e descrizione, o
      per deposito, reparto e descrizione.

### Interrogazione Articolo

Non è una stampa: è una **finestra di consultazione** con la griglia dei
movimenti dell'articolo.

| Campo | Descrizione |
|---|---|
| **Data Iniziale**, **Data Finale** | Il periodo da guardare. |
| **Articolo** | L'articolo da interrogare. Accanto compare la descrizione. |
| **Tipo Interrogazione** | Dove cercare i movimenti: `ARCHIVI LOCALI` o `SERVER REMOTO`. |

{: .campi }

`SERVER REMOTO` serve a chi ha più punti vendita collegati: permette di
vedere i movimenti di un'altra sede senza cambiare archivio.

### Registro Sostanze Zuccherine

| Campo | Descrizione |
|---|---|
| **REGISTRAZIONI — Dal**, **Al** | Il periodo da stampare. |
| **Num. Iniziale**, **Num. Finale** | L'intervallo dei numeri di registrazione. |
| **Progr. Carico**, **Progr. Scarico** | I due progressivi da cui il registro riparte. |
| **Pagina Iniziale**, **Rigo Iniziale** | Da quale pagina e da quale riga cominciare a stampare. |
| **Stampa Definitiva** | Fa la stampa buona invece della prova. |

{: .campi }

È un registro vidimato: **Pagina Iniziale** e **Rigo Iniziale** servono a
riprendere da dove la stampa precedente si era fermata, e i due progressivi a
far tornare i totali di carico e scarico con il registro già stampato.

### Esistenze da Lettore Formula 734

*Nessun campo.* Se i depositi sono più d'uno il programma chiede **quale**,
partendo da quello attivo; con un solo deposito non chiede niente. Poi legge
il terminale e carica le esistenze.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo da esaminare. | date |
| **Articolo** | | Restringe a un articolo. | codice |
| **Deposito** | | Restringe a un [deposito](depositi.md). | codice |
| **Reparto**, **Cat. Merc.** | | Restringono alla classificazione. | codici |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Prepara e mostra l'anteprima della stampa. |
| **Esci** | ++esc++ | Chiude senza stampare. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Sapere quanto vale il magazzino

1. Apri **Menu ▸ Magazzino ▸ Valore Magazzino**.
2. Indica la data a cui valutare e il deposito.
3. Premi **F2 - OK**.

### Controllare la storia di un articolo

1. Apri **Menu ▸ Magazzino ▸ Interrogazione Articolo**.
2. Indica l'articolo: la maschera mostra esistenze e movimenti a video.

### Vedere quali reparti rendono

1. Apri **Sintesi Movimenti per Reparto**, oppure **Sintesi Movimenti -
   Margini Ultimo Prezzo d' Acquisto** se vuoi i margini.
2. Indica il periodo e stampa.

## Controlli e messaggi

| Messaggio | Dove | Causa | Cosa fare |
|---|---|---|---|
| *Il Deposito è escluso dall'inventario. Impossibile continuare!* | Valore Magazzino | Il deposito indicato ha la casella **Escludi da Inventario** spuntata. | Scegli un altro deposito, o togli quella casella dalla scheda del [deposito](depositi.md) se l'esclusione non serve più. |
| *Selezionare almeno una Sezione!* — *Selezionare almeno un Deposito!* | Percentuale Sellout | Si è confermato senza aver spuntato niente nei due elenchi. | Spunta almeno una sezione e almeno un deposito. |
| *SMTP Server non impostato !* — *Mittente Email non impostato !* | Interrogazione Articolo | Si è chiesto l'invio per email senza che la posta sia configurata. | Configura il server di posta sulla [ditta](../anagrafiche/ditte.md), scheda *Server*. |

Per il resto queste stampe sono silenziose: se la selezione non trova
niente, esce un modulo vuoto.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca una delle date. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! note "Adempimenti di settore"

    **Registro Sostanze Zuccherine** e **Modello HACCP Merci in Accettazione**
    riguardano settori specifici — enologia e alimentare. **Esistenze da
    Lettore Formula 734** serve a chi usa quel terminale per l'inventario.

!!! info "Il criterio di valorizzazione lo scegli tu"

    **Valore Magazzino** non ha un criterio fisso: il campo **Metodo**
    offre otto modi di valorizzare la stessa giacenza.

    | Metodo | Valorizza a |
    |---|---|
    | `COSTO MEDIO PONDERATO` | Media dei costi di acquisto pesata sulle quantità. |
    | `METODO LIFO` | Ultimi entrati, primi usciti. |
    | `METODO FIFO` | Primi entrati, primi usciti. |
    | `ULTIMO PREZZO ACQUISTO` | L'ultimo costo pagato. |
    | `PRIMO`, `SECONDO`, `TERZO PREZZO LISTINO` | Il prezzo di vendita del listino indicato. |
    | `PREZZO MEDIO VENDITA` | La media dei prezzi a cui è stato venduto. |

    I primi quattro danno il valore **di costo**, quello che serve al
    bilancio; gli ultimi quattro danno il valore **a prezzi di vendita**,
    utile per capire quanto vale il magazzino sullo scaffale. Sono numeri
    diversi e non vanno confusi.

!!! info "Che cosa misura la percentuale di sell-out"

    Quanta parte della merce che avevi a disposizione è effettivamente
    uscita nel periodo.

    La stampa mette insieme, articolo per articolo, la **rimanenza
    iniziale**, quanto è stato **caricato** nel periodo e l'**esistenza
    attuale**: la percentuale esprime il venduto rispetto al disponibile.
    Un sell-out basso significa merce ferma; uno alto, merce che gira o che
    sta per finire.

    La stampa si può ordinare per esistenza, per quantità venduta, per
    valore o per utile, e limitare ai primi della classifica: è il modo per
    trovare in fretta i fermi o i più redditizi.

    Il **calcolo dei costi** — e quindi l'utile — segue il metodo scelto
    nel campo apposta: medio ponderato, FIFO, LIFO o ultimo prezzo
    d'acquisto.

!!! note "Movimenti Periodo e Sintesi Movimenti per Giorno"

    **Movimenti Periodo** elenca i **movimenti uno per uno** fra due date,
    con la possibilità di limitarsi ai soli movimenti di vendita. È il
    dettaglio: una riga per ogni movimento.

    **Sintesi Movimenti per Giorno** non elenca niente: **somma** i
    movimenti e li presenta **raggruppati per giornata**, per vedere
    l'andamento giorno per giorno. C'è anche la variante per **giorno della
    settimana**, che accorpa tutti i lunedì, tutti i martedì e così via:
    serve a capire quali giorni tirano.

## Vedi anche

- [Movimenti di magazzino](movimenti-magazzino.md)
- [Stampe magazzino clienti](stampe-magazzino-clienti.md)
- [Stampe articoli](../anagrafiche/stampe-articoli.md)
