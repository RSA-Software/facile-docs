---
title: Documenti accompagnatori semplificati
description: I DAS che accompagnano i prodotti soggetti ad accisa, con la stampa della distinta.
modulo: Vendite
maschera_id: IDD_VEN_DAS
---

# Documenti accompagnatori semplificati

I DAS accompagnano i prodotti soggetti ad accisa — vino, alcolici, prodotti
energetici — quando viaggiano. Si compilano qui e se ne stampa la distinta.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Vendite ▸ Documenti Accompagnatori Semplificati ▸ Inserimento *(oppure* Modifica*,* Stampa Distinta *o* Duplica*)*
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

È un adempimento di chi movimenta prodotti sottoposti ad accisa: il documento
accompagna la merce e la distinta riepiloga quelli emessi.

Serve solo a chi tratta quei prodotti; per tutti gli altri il sottomenu si
lascia stare.

## Prerequisiti

Prima di usare questa maschera occorre avere in archivio i
[clienti](../anagrafiche/anagrafica-clienti.md) e gli
[articoli](../anagrafiche/anagrafica-articoli.md) soggetti ad accisa, con i
dati che il documento richiede.

## La maschera

![Documento accompagnatorio semplificato](../../assets/img/vendite/documenti-accompagnatori-semplificati.png)

La finestra si chiama **Inserimento DAS**. In alto i dati del documento e
del suo riferimento, al centro cliente e destinatario, sotto i dati del
trasporto, e in fondo la griglia delle righe — una per prodotto.

Le righe non si scrivono nella griglia: si apre la finestra **Modifica
Riga**, che è dove stanno i dati fiscali del prodotto.

## Campi

### Il documento

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Registro** | ● | Il registro su cui il DAS è numerato. | da `A` a `Z` |
| **Numero Progres.** | ● | Il numero del documento. | numero |
| **Data** | ● | La data del DAS. | data |
| **Tipo** | ● | Che cosa rappresenta il documento. | `PRESENTAZIONE STANDARD`, `REINTRODUZIONE IN DEPOSITO`, `DAS NON SCORTA MERCE` |
| **Doc. Riferimento** | | Il documento di vendita a cui il DAS si appoggia. | `DOC. DI TRASPORTO`, `FATTURA`, `BOLLA ACCOMP.` |
| **Registro**, **Numero Doc.**, **Del** | | Registro, numero e data del documento di riferimento. | |
| **Cliente** | ● | Il destinatario della fattura. | codice |
| **Destinatario** | | Dove va la merce, se diverso dal cliente. | codice |

{: .campi }

### Il trasporto

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Tipo Invio** | | Se la merce parte subito o dopo. | `NON DIFFERITO`, `DIFFERITO` |
| **Resp.le Trasporto** | | Chi risponde del trasporto. | `SPEDITORE`, `DESTINATARIO`, `PROPRIETARIO DEI PRODOTTI`, `ALTRO` |
| **Tipo Trasporto** | | Il mezzo. La voce `ALTRO:` lascia scrivere la descrizione. | |
| **Unità Trasporto** | | Come viaggia la merce. | `CONTAINER`, `VEICOLO`, `RIMORCHIO` |
| **Vettore** | | Chi trasporta. | codice |
| **Autista**, **Mezzo di Trasp.**, **Firma** | | I dati di chi guida e del mezzo. | testo |
| **Inizio Trasporto** | | Quando la merce parte. | data e ora |
| **Durata Presunta** | | Quanto dura il viaggio. | **da 1 a 18** |
| **Stampato** | | Segnala che il documento è già stato stampato. | |

{: .campi }

### La riga (finestra *Modifica Riga*)

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice** | ● | Il prodotto energetico. | codice |
| **Codice NC** | | La nomenclatura combinata, proposta dal prodotto. | |
| **Registro** | | Il registro di carico e scarico del prodotto. | codice |
| **Causale** | ● | La causale di movimentazione: **deve essere di scarico**. | codice |
| **Pos. Fiscale** | | La posizione fiscale del prodotto. | codice |
| **Stoccaggio** | | Come il prodotto è stoccato. | `S - SFUSO`, `C - CONDIZIONATO` |
| **Num. Doc.** | | Il documento della riga. | |
| **Densità** e **Quantità (Lt)** | ● | Due coppie: a **temperatura ambiente** e a **15°**. | numero |
| **Kilogrammi** | | Il peso corrispondente. | numero |

{: .campi }

Non applicabile.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra il documento. |
| **F3 - Prec.**, **F4 - Succ.** | ++f3++, ++f4++ | Passano al documento precedente o successivo. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco dei documenti. |
| **F6 - Elimina** | ++f6++ | Cancella il documento, previa conferma. |
| **F7 - Stampa** | ++f7++ | Stampa il documento. |

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Salva il documento. |
| **F3 - Prec.**, **F4 - Succ.** | ++f3++, ++f4++ | Scorre i documenti già emessi. |
| **F5 - Cerca** | ++f5++ | Apre *Cerca DAS*, che cerca per **Num. Doc.**, **Data** o **Intestatario**. |
| **F6 - Elimina** | ++f6++ | Cancella il documento. |
| **F7 - Stampa** | ++f7++ | Stampa il DAS. |
| **F8 - Annulla** | ++f8++ | Ricarica il documento scartando le modifiche. |
| **F9 - Esporta** | ++f9++ | Esporta il documento. |

!!! note "In Inserimento c'è solo Salva"

    Aprendo da **Inserimento** la barra ha il solo **F2 - Salva**: gli altri
    comandi compaiono entrando da **Modifica**, che è la stessa maschera aperta
    su un documento esistente.

## Come si fa

### Emettere un DAS

1. Apri **Menu ▸ Vendite ▸ Documenti Accompagnatori Semplificati ▸
   Inserimento**.
2. Compila il documento con il destinatario e la merce.
3. Premi **F2 - Salva** e stampa il documento che accompagnerà la merce.

### Stampare la distinta dei documenti emessi

1. Apri **Menu ▸ Vendite ▸ Documenti Accompagnatori Semplificati ▸ Stampa
   Distinta**.
2. Indica il periodo e stampa.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Nessuna riga valida per la compilazione del DAS !* | Nessuna riga ha i dati fiscali completi. | Aprire le righe e completarle. |
| *la durata presunta del trasporto deve essere tra 1 e 18!* | **Durata Presunta** fuori intervallo. | Indicare un valore da 1 a 18. |
| *Valore Densita' a temperatura ambiente non indicato !* | Manca la densità sulla riga. | Aprire la riga e compilarla. |
| *Codice Registro Non Valido !* / *Codice Causale Movimentazione Non Valido !* / *Codice Posizione Fiscale Non Valido !* | Un codice fiscale della riga non esiste in archivio. | Correggerlo nella riga o nel prodotto energetico. |
| *La causale deve essere di Scarico !* | La causale indicata non è di scarico. | Il DAS accompagna merce in uscita: serve una causale di scarico. |
| *Vuoi stampare il Documento di Accompagnamento Semplificato (DAS) ?* | Chiesto dopo il salvataggio. | Rispondere **Sì** per stampare subito. |

!!! warning "In esportazione i controlli sono tutti domande"

    Esportando, ogni dato mancante apre una richiesta *« … assente. Vuoi
    Continuare? »* — tipo destinazione del cliente, codice fiscale, tipo
    speditore e codice identificativo della ditta, codice del cliente,
    vettore o sua partita IVA, indirizzo, CAP e città di cliente e
    destinatario. **Rispondere Sì a tutte produce un file incompleto**:
    conviene annullare e sistemare il dato.

Non applicabile.

## Note

!!! note "Riguarda solo i prodotti soggetti ad accisa"

    Se l'azienda non tratta alcolici o prodotti energetici, questo sottomenu
    non serve.

!!! info "I dati non vengono dall'anagrafica articoli"

    La riga del DAS si compila dall'archivio dei **prodotti energetici**, non
    dagli articoli: digitando il codice, il programma propone descrizione,
    **Codice NC**, **Registro** e **Pos. Fiscale** presi da lì.

    Si impostano da **Menu ▸ Archivi ▸ Prodotti Energetici ▸ Inserimento** (o
    *Modifica*); c'è anche **Importa (TA13)** per caricarli da file.
    Senza quei dati la riga resta incompleta e il DAS non si può emettere.

!!! note "Non c'è rapporto con il Registro Sostanze Zuccherine"

    Sono due cose separate, anche se vivono nello stesso mondo degli
    adempimenti. Il DAS è un **documento di trasporto** e sta nel suo archivio;
    la **Stampa Registro Sostanze Zuccherine** (*Menu ▸ Magazzino*) è un
    **registro di magazzino** costruito dai movimenti, e dei DAS non sa nulla.

    Emettere un DAS non scrive sul registro, e stampare il registro non
    guarda i DAS.

## Vedi anche

- [Documento di vendita](documento-di-vendita.md)
- [Anagrafica articoli](../anagrafiche/anagrafica-articoli.md)
