---
title: Fatture ricorrenti
description: Le schede dei contratti da cui Facile emette periodicamente le fatture, senza ricompilarle ogni volta.
modulo: Vendite
maschera_id: IDD_OFF_FATRIC
---

# Fatture ricorrenti

Chi fattura le stesse cose agli stessi clienti a scadenza fissa — canoni,
noleggi, assistenze — registra una scheda contratto e lascia che il programma
emetta le fatture quando è ora.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Vendite ▸ Fatture ▸ Fatture Ricorrenti ▸ Inserimento Schede Contratti *(oppure* Modifica Schede Contratti*,* Stampa Schede Contratti *o* Emissione Fatture*)*
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

La scheda contratto dice **a chi** fatturare e, riga per riga, **cosa** e in
**quale mese**. **Emissione Fatture** chiede il mese, mostra tutte le righe di
quel mese e genera le fatture di quelle che si confermano.

## Prerequisiti

Prima di usare questa maschera occorre avere in archivio i
[clienti](../anagrafiche/anagrafica-clienti.md), gli
[articoli](../anagrafiche/anagrafica-articoli.md) o le voci da fatturare, e gli
[agenti](../anagrafiche/anagrafica-agenti.md) se le provvigioni maturano.

## La maschera

![Fatture ricorrenti](../../assets/img/vendite/fatture-ricorrenti.png)

In alto gli estremi della scheda, poi i destinatari, poi la periodicità, e
sotto la griglia delle righe da fatturare.

Le colonne della griglia sono **Codice**, **Mese**, **Quantità**, **Importo**,
**%Sco.**, **Totale**, **Dep.**, **Cod. Articolo** e **Descrizione**. Un doppio
clic su una riga apre la finestrella con cui la si compila.

## Campi

### La scheda

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice** | ● | Identificativo della scheda contratto. | numero |
| **Data** | ● | Data della scheda. | data |
| **Cliente** | ● | Chi va fatturato. | codice |
| **Destinazione** | | La destinazione, se diversa. | codice |
| **Agente** | | L'[agente](../anagrafiche/anagrafica-agenti.md) su cui maturano le provvigioni. | codice |
| **Periodicità** | ● | Quanti mesi copre ogni fattura. Non decide *quando* si fattura: serve a scrivere il periodo sulla riga della fattura. | `ANNUALE`, `SEMESTRALE`, `QUADRIMESTRALE`, `TRIMESTRALE`, `BIMESTRALE`, `MENSILE` |
| **Tipo Fatturazione** | | Se il periodo indicato sulla fattura va avanti o indietro rispetto al mese di emissione. | `POSTICIPATA`, `ANTICIPATA`, `NESSUNA DATA` |
| **Blocca Fatturazione** | | Sospende il contratto: le sue righe compaiono ancora nell'emissione, ma in evidenza e **già deselezionate**. | attivo/non attivo |

{: .campi }

### La riga da fatturare

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Mese Fatturazione** | ● | In quale mese dell'anno questa riga va fatturata. | da `GENNAIO` a `DICEMBRE` |
| **Articolo da Fatturare** | ● | Deposito e codice dell'[articolo](../anagrafiche/anagrafica-articoli.md). Accanto compare la descrizione. | codici |
| *(riquadro grande senza etichetta)* | | Descrizione estesa da riportare sulla fattura al posto di quella dell'articolo. | testo, 512 caratteri |
| **Matricola** | | La matricola dell'apparecchio a cui il canone si riferisce. | testo |
| **Quantità** | | Quante unità fatturare. | numero |
| **Prezzo Unitario** | | Il prezzo da applicare. | importo |
| **% Sco. Rivenditore** | | Sconto sulla riga. | percentuale |

{: .campi }
## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra la scheda. |
| **F3 - Prec.**, **F4 - Succ.** | ++f3++, ++f4++ | Passano alla scheda precedente o successiva. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco delle schede. |
| **F6 - Elimina** | ++f6++ | Cancella la scheda, previa conferma. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Registrare un canone annuale

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Fatture Ricorrenti ▸ Inserimento Schede
   Contratti**.
2. Compila **Cliente** e **Data**.
3. Metti **Periodicità** su `ANNUALE`.
4. Aggiungi la riga da fatturare e indica in **Mese Fatturazione** il mese in
   cui il canone va emesso — per esempio `GENNAIO`.
5. Premi **F2 - Salva**.

### Registrare un canone trimestrale

Servono **quattro righe**, una per ciascun mese di emissione: `GENNAIO`,
`APRILE`, `LUGLIO`, `OTTOBRE`. La **Periodicità** `TRIMESTRALE` dice che
ognuna copre tre mesi, e il programma lo scriverà sulla fattura.

### Emettere le fatture del mese

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Fatture Ricorrenti ▸ Emissione Fatture**.
2. Il **Mese** arriva già impostato su quello corrente: cambialo se stai
   lavorando in ritardo o in anticipo.
3. Scegli il **Registro Emissione Fatture**.
4. Se lo stesso cliente ha più righe e ne vuoi una fattura sola, spunta
   **Accorpa Fatture Stesso Cliente**.
5. Controlla la griglia e **togli la spunta** alle righe che non vuoi
   fatturare.
6. Avvia l'emissione.
7. Controlla i documenti generati dalla
   [gestione fatture](gestione-documenti.md) prima di stamparli.

### Controllare i contratti attivi

Apri **Stampa Schede Contratti** e stampa l'elenco.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! warning "L'emissione genera documenti veri"

    **Emissione Fatture** crea fatture a tutti gli effetti, numerate sul
    registro. Controllale prima di stamparle e mandarle.

!!! warning "La scadenza la decide il Mese della riga, non la Periodicità"

    È il punto che si fraintende più spesso. Ogni **riga** del contratto porta
    un **Mese Fatturazione**, e l'emissione lavora su **un mese per volta**:
    mostra le righe di quel mese e basta.

    La **Periodicità** non fa scattare niente: dice solo **quanto periodo copre**
    ogni fattura, e serve al programma per scrivere sulla riga la frase
    *DAL gg/mm/aaaa AL gg/mm/aaaa*.

    Per un canone trimestrale non basta quindi mettere `TRIMESTRALE`: vanno
    inserite **quattro righe**, sui quattro mesi in cui si fattura. Con una riga
    sola la fattura uscirebbe una volta l'anno.

!!! note "Non esiste una data di ultima fatturazione che comanda"

    Ogni riga si annota **numero e data dell'ultima fattura emessa**, ma sono
    solo un promemoria: compaiono in due colonne della griglia e non impediscono
    niente.

    L'unica precauzione che il programma prende è questa: le righe **fatturate
    negli ultimi sette giorni** arrivano in griglia **sbarrate e già
    deselezionate**, così non si rifanno per sbaglio. Passati sette giorni
    tornano selezionabili: rilanciando l'emissione sullo stesso mese si
    otterrebbe una seconda fattura.

!!! note "L'emissione chiede un mese, non una data"

    La finestra *Fatturazione Mensile* ha un elenco **Mese** che parte dal mese
    corrente. Non c'è nessuna data di riferimento: il giorno in cui si lavora
    serve solo a datare le fatture che escono.

    Gli altri campi sono **Registro Emissione Fatture**, **Accorpa Fatture
    Stesso Cliente** e i due filtri **Cliente** e **Rivenditore**.

!!! note "Le righe di un altro anno non compaiono"

    Se una riga porta un anno diverso dall'anno di lavoro non viene elencata.
    Le righe senza anno valgono per tutti gli anni: è il caso normale di un
    canone che si ripete.

## Vedi anche

- [Documento di vendita](documento-di-vendita.md)
- [Gestione documenti](gestione-documenti.md)
