---
title: Stampe magazzino clienti
description: Le tredici stampe che leggono i movimenti dal lato del cliente — schede, sintesi, analisi vendite e raffronti con i listini.
modulo: Magazzino
maschera_id: IDD_ST_MAGAZZINO
---

# Stampe magazzino clienti

Il sottomenu **Stampe Magazzino Clienti** guarda i movimenti dal lato di chi
compra: cosa ha preso ciascun cliente, quanto, quando e a che condizioni.
Quasi tutte aprono **la stessa maschera di selezione**, con un parametro
diverso.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Magazzino ▸ Stampe Magazzino Clienti ▸ *(una delle voci)*
    - **Scorciatoia:** ++f2++ avvia la stampa, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | Cosa mostra |
|---|---|
| **Scheda Movimenti Cliente** | Tutti i movimenti di un cliente, riga per riga. |
| **Scheda Movimenti Cliente - Sostituzioni** | Le sole sostituzioni. |
| **Stampa Movimenti Cliente - Omaggi e Sconti Merce** | Omaggi e sconti merce concessi. |
| **Sintesi Movimenti Cliente** | Il riepilogo per cliente, senza il dettaglio. |
| **Sintesi Movimenti Cliente per Articolo** | Quanto ogni cliente ha preso di ogni articolo. |
| **Sintesi Movimenti per Articolo con Dettaglio Promozioni** | Come sopra, distinguendo il venduto in promozione. |
| **Sintesi Mensile Movimenti** | Il riepilogo mese per mese. |
| **Analisi Vendite** | L'analisi del venduto. |
| **Raffronto Vendite con Prezzi Listino** | Confronta i prezzi praticati con quelli di listino: dice dove si è venduto sotto. |
| **Sintesi Movimenti per Giorno Settimana** | Come il venduto si distribuisce nella settimana. |
| **Riepilogo Totali Movimenti Clienti** | I totali per cliente. |
| **Confronto Vendite - Sostituzioni** | Il confronto fra vendite e sostituzioni. |
| **Stampa Giornale Vendita Prodotti Fiscali** | Il giornale delle vendite dei prodotti soggetti ad accisa. |

## Prerequisiti

Prima di usare queste stampe occorre avere movimentato il magazzino, con i
[documenti di vendita](../vendite/documento-di-vendita.md), gli
[scontrini](../vendite/scontrini.md) o i
[movimenti diretti](movimenti-magazzino.md).

## La maschera

![Stampe magazzino clienti](../../assets/img/magazzino/stampe-magazzino-clienti.png)

È una finestra di selezione: il periodo, i filtri su cliente, articolo,
deposito e classificazioni, e i pulsanti **F2 - OK** ed **Esci**. Il titolo
della finestra dice quale stampa si è aperta.

!!! info "I campi della maschera"

    È una maschera sola per tutte queste stampe: cambia il **titolo della
    finestra**, che dice quale stai facendo, e qualche campo si spegne dove
    non serve.

    **Periodo e ambito**: **Data Iniziale**, **Data Finale**, **Sezione**,
    **Deposito**, **Causale**, **Operatore**.

    **Che movimenti prendere**: **Tipo Movim.** — `CARICHI`, `SCARICHI`,
    `VENDITE`, `RESI`, `VENDITE+RESI` — e, dove l'installazione lo
    prevede, **Tipo Vendita** per distinguere normale, trasfert, conto
    servizi e delivery.

    **Chi**: **Cliente**, **Destinazione**, **Agente**, **Gruppo**.

    **Che merce**: **Articolo**, **Lotto**, **Cod. Iva**, **Gruppo Mix**,
    **Reparto**, **Cat. Merceol.**, **Marchio**, **Stagione**,
    **Fornitore**, **Gruppo**, **Sottogruppo** e le tre tabelle libere.

    Lasciare un filtro a zero significa «tutti».

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo da esaminare. | date |
| **Cliente** | | Restringe a un cliente. | codice |
| **Articolo** | | Restringe a un articolo. | codice |
| **Deposito** | | Restringe a un [deposito](depositi.md). | codice |
| **Agente** | | Restringe a un [agente](../anagrafiche/anagrafica-agenti.md). | codice |

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

### Vedere cosa ha comprato un cliente

1. Apri **Menu ▸ Magazzino ▸ Stampe Magazzino Clienti ▸ Scheda Movimenti
   Cliente**.
2. Indica il **Cliente** e il periodo.
3. Premi **F2 - OK**.

### Trovare le vendite sotto listino

1. Apri **Stampe Magazzino Clienti ▸ Raffronto Vendite con Prezzi Listino**.
2. Indica il periodo e premi **F2 - OK**.
3. Le righe in cui il prezzo praticato è sotto quello di listino sono quelle da
   guardare.

### Capire quanto pesa la promozione

1. Apri **Sintesi Movimenti per Articolo con Dettaglio Promozioni**.
2. Indica il periodo della promozione.
3. Confronta le colonne del venduto in promozione con quelle fuori promozione.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Selezionare almeno una Sezione!* | Si è confermato senza aver spuntato nessuna sezione. | Spunta le sezioni da includere. |
| *Vuoi Stampare Margine, Ricarico e Costo ?* | Chiesto prima di stampare, dove la stampa li sa calcolare. | **Sì** aggiunge le colonne economiche; **No** lascia le sole quantità e i valori di vendita. |
| *Vuoi il raggruppamento per Marchio ?* | Chiesto su alcune sintesi. | **Sì** raggruppa per marchio invece che per l'ordinamento consueto. |
| *Vuoi raggruppare i depositi ?* | Chiesto quando la selezione tocca più depositi. | **Sì** somma i depositi in un totale unico; **No** li tiene separati; **Annulla** ferma la stampa. |

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca una delle date. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! note "Il titolo della finestra dice quale stampa è"

    Poiché la maschera di selezione è la stessa, l'unico modo per accorgersi di
    aver aperto la stampa sbagliata è leggere il titolo in alto.

!!! info "Che cosa fa Analisi Vendite in più delle sintesi"

    Le **sintesi** sommano quello che è stato movimentato: quantità e
    valore, raggruppati per cliente, per articolo, per reparto, per mese.

    **Analisi Vendite** aggiunge il **conto economico**: prima di stampare
    chiede con quale criterio valorizzare il costo — medio ponderato,
    FIFO, LIFO, ultimo prezzo d'acquisto — e accanto al venduto mette il
    **costo**, il **margine** e il **ricarico**.

    È la stampa da usare per rispondere a «quanto ci ho guadagnato», non a
    «quanto ho venduto».

!!! note "Che cosa sono le sostituzioni"

    Sulla riga di un documento di vendita c'è una casella
    **Sostituzione**: si spunta quando quella riga non è una vendita nuova
    ma merce data **in sostituzione** di altra — un prodotto difettoso
    cambiato, una consegna rifatta.

    La stampa *Scheda Movimenti Cliente - Sostituzioni* è la stessa scheda
    movimenti del cliente, limitata alle sole righe con quella spunta:
    serve a vedere quanto di quello che è uscito verso un cliente non era
    merce venduta.

    La stampa gemella **Omaggi e Sconti Merce** lavora in modo diverso: non
    guarda una casella ma i numeri, e prende le righe con **sconto al cento
    per cento** o **prezzo a zero**.

## Vedi anche

- [Stampe magazzino fornitori](stampe-magazzino-fornitori.md)
- [Stampe dei movimenti di magazzino](stampe-movimenti-magazzino.md)
- [Riepiloghi e statistiche di vendita](../vendite/riepiloghi-e-statistiche.md)
