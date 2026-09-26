---
title: Gestione scadenze
description: L'elenco delle scadenze aperte di clienti e fornitori, da cui si cercano, si aprono e se ne creano di nuove.
modulo: Scadenze
maschera_id: IDD_CON_GEST_SCADENZE
---

# Gestione scadenze

L'elenco di quello che si deve incassare e di quello che si deve pagare. La
stessa maschera serve i due scadenziari: cambia il titolo — *Gestione Scadenze
Clienti* o *Gestione Scadenze Fornitori* — e cambia l'archivio.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Gestione Scadenze
        - Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Gestione Scadenze
    - **Scorciatoia:** ++f2++ modifica, ++f3++ nuova
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Le scadenze nascono da sole quando si emette un documento con un
[tipo di pagamento](../contabilita/tipi-di-pagamento.md) che prevede le rate,
o quando si registra una fattura in
[prima nota](../contabilita/registrazione-prima-nota.md). Qui si vedono tutte
insieme, si cerca quella che serve e la si corregge; e si può aggiungerne una a
mano, per quello che non nasce da un documento.

È il punto di partenza del lavoro sulle scadenze: da qui si capisce chi è in
ritardo, e da lì si passa ai [solleciti](stampe-scadenze.md), alle
[distinte](distinte-incasso-pagamento.md) e agli
[effetti](effetti-e-riba.md).

## Prerequisiti

Prima di usare questa maschera occorre:

- avere in archivio i [clienti](../anagrafiche/anagrafica-clienti.md) e i
  [fornitori](../anagrafiche/anagrafica-fornitori.md);
- avere i [tipi di pagamento](../contabilita/tipi-di-pagamento.md) impostati,
  perché sono loro a generare le rate;
- avere emesso i documenti o registrato la prima nota da cui le scadenze
  nascono.

## La maschera

![Gestione scadenze](../../assets/img/scadenze/gestione-scadenze.png)

In alto la barra dei comandi e i filtri, sotto la griglia delle scadenze
trovate e in fondo il **TOTALE**.

La griglia ha queste colonne:

| Colonna | Contenuto |
|---|---|
| **Codice** | Numero della scadenza. |
| **Data** | Data di scadenza. |
| **Numero Doc.**, **Data Doc.** | Gli estremi del documento da cui nasce. |
| **Sez.** | La [sezione](../contabilita/sezioni.md) contabile. |
| **Descrizione** | La descrizione della scadenza. |
| **Importo** | Quanto c'è da incassare o da pagare. |
| **Cliente** | Il nominativo. Nello scadenziario fornitori è il fornitore. |
| **Destinazione** | La destinazione merce, quando c'è. |
| **Agente** | L'[agente](../anagrafiche/anagrafica-agenti.md) del documento. |

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | | Il periodo delle scadenze da mostrare. | date |
| **Stato** | | Se mostrare tutto o solo l'aperto. | `TUTTE`, `NON PAGATE`, `PAGATE` |
| **Sezione** | | Restringe a una [sezione](../contabilita/sezioni.md) contabile. | codice |
| **Cliente** | | Restringe a un nominativo. | codice |
| **Destinazione** | | Restringe a una destinazione merce. | codice |
| **Agente** | | Restringe a un [agente](../anagrafiche/anagrafica-agenti.md). | codice |
| **TOTALE** | | La somma delle scadenze trovate. Solo lettura. | — |

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Modifica** | ++f2++ | Apre in modifica la scadenza selezionata. |
| **F3 - Nuova** | ++f3++ | Crea una scadenza a mano. |
| **Trova** | | Cerca un testo nella griglia. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Vedere chi è in ritardo

1. Apri **Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Gestione Scadenze**.
2. Metti **Data Finale** a ieri e **Stato** su `NON PAGATE`.
3. Il **TOTALE** in fondo è lo scaduto.

### Correggere una scadenza sbagliata

1. Trova la riga e premi **F2 - Modifica**.
2. Correggi data o importo e salva.

### Vedere lo scaduto di un agente

1. Apri lo scadenziario clienti e indica l'**Agente**.
2. Metti **Stato** su `NON PAGATE` e **Data Finale** a oggi.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo, o **Fornitore Giro** e **Data Giro** non sono compilati tutti e due. | Guarda dove si è posizionato il cursore. |
| *Il cliente selezionato risulta cessato !<br><br>Vuoi Continuare ?* | Il cliente indicato è segnato come cessato. | **Sì** registra lo stesso. La risposta preimpostata è **No**. |
| *Causale Contabile Incassi non Impostata o non Valida.* — *Causale Contabile Pagamenti non Impostata o non Valida.* | Nella [ditta](../anagrafiche/ditte.md) manca la causale con cui registrare incassi o pagamenti. | Impostala: senza, **F7 - Incassa** non funziona. |
| *Il registro fiscale della causale di contabile per l'incasso deve essere il N° 1.* | La causale è su un registro IVA invece che sul giornale. | Correggi la [causale contabile](../contabilita/causali-contabili.md). |
| *La Causale non è in relazione con i Clienti.* — *La Causale non è in relazione con i Fornitori.* | La causale è collegata al soggetto sbagliato. | Come sopra. |
| *La causale non deve essere una causale Iva.* | La causale movimenta l'IVA. | L'incasso non è un'operazione IVA: serve una causale di solo giornale. |
| *La causale non deve trattare beni destinati alla rivendita.* | La causale ha il segno dei beni da rivendere. | Come sopra. |
| *Il codice del Fornitore per il giro non è valido o disponibile.* | Il fornitore indicato in **Fornitore Giro** non esiste. | Controlla il codice. |

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Un campo del filtro non è valido. | Guarda dove si è posizionato il cursore. |

## Note

!!! warning "Le scadenze aggiunte a mano non hanno un documento dietro"

    **F3 - Nuova** crea una scadenza scollegata da qualsiasi documento: non la
    ritroverai nel
    [controllo scadenze ↔ schede contabili](manutenzione-scadenze.md), che
    confronta scadenze e registrazioni. Usala solo quando serve davvero.

!!! info "I campi della singola scadenza"

    Aprendo una riga si apre la scheda — *Modifica Scadenze Clienti* o
    *Modifica Scadenze Fornitori*, *Inserimento…* se è nuova — con questi
    campi:

    | Campo | Descrizione |
    |---|---|
    | **Numero** | Il numero della scadenza. Lo assegna il programma e in modifica non si tocca. |
    | **Descrizione** | Un testo libero. |
    | **Cliente** / **Fornitore** | Il soggetto. L'etichetta cambia con lo scadenziario. |
    | **Destinazione** | La destinazione, con tre righe di indirizzo sotto. |
    | **Agente** | L'[agente](../anagrafiche/anagrafica-agenti.md). |
    | **N. Documento**, **Data**, **Protocollo**, **Importo** | Gli estremi del documento da cui la scadenza nasce e il suo totale. |
    | **Pagamento** e **Tipo** | Il [tipo di pagamento](../contabilita/tipi-di-pagamento.md) e la sua natura — rimessa, RI.BA., RID, tratta. |
    | **Banca Appog.** | La [banca](../contabilita/banche.md) su cui l'effetto è appoggiato. |
    | **Data Scadenza** | Quando scade. |
    | **Rata … di …** | Quale rata è, sul totale delle rate. |
    | *(elenco accanto alla rata)* | `ACCONTO` o `SALDO`. |
    | **Importo** | L'importo della rata. |
    | **Emessa il** | La data di emissione. |
    | **Sezione** | La [sezione](../contabilita/sezioni.md) contabile. |
    | **Insoluto** | Segna l'effetto tornato indietro. |
    | **Data Originale** | La scadenza di partenza, quando è stata spostata. |
    | **Fornitore Giro** e **Data Giro** | Il fornitore a cui l'effetto è stato girato e quando. Vanno compilati tutti e due o nessuno dei due. |

    In alto a destra due scritte si accendono quando serve: **I N C A S S A T
    A** quando la scadenza risulta pagata e **CONTABILIZZATA** quando ne è nata
    la registrazione di prima nota.

!!! info "Come una scadenza diventa pagata"

    Da qui, una per volta, con il pulsante della scheda: **F7 - Incassa** sui
    clienti, **F7 - Paga** sui fornitori. Non serve salvare: il pulsante fa
    tutto.

    Premendolo su una scadenza aperta il programma chiede **la data** — la
    finestrella si chiama *Incasso Scadenza* o *Pagamento Scadenza* — e poi:

    1. segna la scadenza come **pagata**, con quella data;
    2. **scrive la registrazione di prima nota** dell'incasso o del pagamento;
    3. accende le scritte **I N C A S S A T A** e **CONTABILIZZATA** sulla
       scheda.

    La causale con cui registra la prende dalla [ditta](../anagrafiche/ditte.md):
    la **causale pagamenti** per i fornitori, la **causale incassi** per i
    clienti — o la **causale effetti**, se il tipo di pagamento della scadenza è
    una RI.BA., un RID o una tratta.

    Il conto del cliente o del fornitore viene sostituito nella causale al posto
    del conto generico, così la registrazione va sul soggetto giusto.

!!! warning "Togliere il pagato non toglie la registrazione"

    Lo stesso **F7** premuto su una scadenza già pagata la **riapre**: toglie il
    segno di pagata e azzera la data.

    **La registrazione di prima nota però resta.** Va cancellata a mano dalla
    [gestione prima nota](../contabilita/gestione-prima-nota.md), altrimenti
    l'incasso risulta due volte quando la scadenza viene chiusa di nuovo.

    E se si richiude la scadenza, la registrazione viene rifatta.

!!! note "Anche le distinte e gli effetti chiudono le scadenze"

    **F7** è la strada per la singola scadenza. Per chiuderne molte insieme ci
    sono le [distinte di incasso e pagamento](distinte-incasso-pagamento.md) e
    la gestione degli [effetti](effetti-e-riba.md), che lavorano su un elenco.

## Vedi anche

- [Distinte di incasso e di pagamento](distinte-incasso-pagamento.md)
- [Stampe delle scadenze](stampe-scadenze.md)
- [Effetti e RI.BA.](effetti-e-riba.md)
- [Tipi di pagamento](../contabilita/tipi-di-pagamento.md)
