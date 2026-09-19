---
title: Grafici pluriennali e report personalizzati
description: I due grafici che confrontano fino a dieci annate e la raccolta dei report su misura fatti dall'assistenza.
modulo: Analisi Dati
maschera_id: IDD_VEN_VENDUTO_PLURIENNALI
---

# Grafici pluriennali e report personalizzati

Due modi di guardare i dati che non producono un elenco: **il grafico**, per
vedere l'andamento di più anni a colpo d'occhio, e **i report personalizzati**,
cioè le stampe su misura preparate dall'assistenza per la tua azienda.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Analisi Dati ▸ Grafico Vendite Pluriennali
        - Menu ▸ Analisi Dati ▸ Grafico Ricavi Pluriennali
        - Menu ▸ Analisi Dati ▸ Report Personalizzati
    - **Scorciatoia:** ++f2++ avvia o stampa, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

!!! note "Solo nella versione Evolution"

    Il menu **Analisi Dati** compare soltanto in Facile Evolution.

---

## A cosa serve

| Voce di menu | Cosa mostra | Titolo della finestra |
|---|---|---|
| **Grafico Vendite Pluriennali** | L'andamento del **venduto** su più annate. | *Vendite Pluriennali* |
| **Grafico Ricavi Pluriennali** | L'andamento dei **ricavi** — quindi il margine, non il fatturato. Stessa maschera. | *Ricavi Pluriennali* |
| **Report Personalizzati** | La raccolta dei report su misura installati nella tua azienda, con l'anteprima e la stampa. | *Report Personalizzati* |

## Prerequisiti

Per i grafici occorre avere in archivio le annate da confrontare, e aver
aggiornato lo **storico dei movimenti** con
[Aggiungi Movimenti dell' Anno allo Storico](../utility/manutenzione-archivi.md):
è da lì che i dati pluriennali vengono letti.

Per i report personalizzati occorre che l'assistenza ne abbia installato almeno
uno: sono file `.rpt`, cioè report Crystal, preparati su richiesta.

## La maschera

![Vendite pluriennali](../../assets/img/analisi-dati/grafici-e-report.png)

**Vendite Pluriennali** è una finestrella con due filtri e dieci caselle, una
per anno. **Report Personalizzati** è invece un esploratore: a sinistra la
cartella dei report, al centro l'elenco dei file, e l'anteprima del report
scelto.

## Campi

### Vendite / Ricavi Pluriennali

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Deposito** | | Restringe a un [deposito](../magazzino/depositi.md). | codice |
| **Sezione** | | Restringe a una [sezione](../contabilita/sezioni.md). | codice |
| **Anno_01** … **Anno_10** | ● | Le annate da mettere nel grafico: se ne possono confrontare fino a dieci. | attivo/non attivo |

{: .campi }

## Pulsanti e comandi

### Vendite / Ricavi Pluriennali

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Costruisce il grafico. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |

### Report Personalizzati

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Stampa** | ++f2++ | Stampa il report scelto. |
| **Esci** | ++esc++ | Chiude la maschera. |

## Come si fa

### Confrontare il venduto degli ultimi anni

1. Apri **Menu ▸ Analisi Dati ▸ Grafico Vendite Pluriennali**.
2. Spunta le annate da confrontare.
3. Restringi al **Deposito** se hai più punti vendita e vuoi guardarne uno.
4. Premi **F2 - OK**.

### Vedere se il margine tiene

Apri **Grafico Ricavi Pluriennali** invece di quello delle vendite: il
fatturato può crescere mentre il ricavo cala, ed è quello il dato che conta.

### Usare un report fatto su misura

1. Apri **Menu ▸ Analisi Dati ▸ Report Personalizzati**.
2. Nell'albero a sinistra apri la cartella dei report; al centro compaiono i
   file `.rpt` disponibili.
3. Scegli il report: l'anteprima appare a fianco.
4. Premi **F2 - Stampa**.

## Controlli e messaggi

Queste due maschere **non hanno messaggi propri**: i controlli sono
silenziosi, con il solo segnale acustico.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Non è stata spuntata nessuna annata. | Spunta almeno un anno. |

## Note

!!! note "I grafici leggono lo storico, non i movimenti dell'anno"

    Se un'annata non compare o risulta vuota, quasi sempre non è stata portata
    nello storico. Si rimedia da
    [Manutenzione degli archivi](../utility/manutenzione-archivi.md).

!!! info "I report personalizzati stanno in una cartella a sé"

    Sono report Crystal (`.rpt`) e il programma li cerca in **`rptcustom`**,
    sotto la cartella di installazione. Non nella cartella dei report
    ordinari: è una cartella dedicata, apposta per non confondere i report su
    misura con quelli di serie.

    Dentro si possono fare **sottocartelle**: l'albero a sinistra le mostra, e
    serve a tenere in ordine i report per argomento.

    Se un report che avevi non compare, è un problema di installazione — il
    file non è in quella cartella — non del menu. Per averne di nuovi si passa
    dall'assistenza.

!!! info "Il grafico è una stampa, e si esporta come le altre"

    Non è un grafico interattivo: è un **modello di stampa** che esce
    nell'anteprima come qualsiasi altra stampa di Facile, con il suo
    andamento mese per mese e una riga per ciascuna annata scelta.

    Da lì valgono i comandi dell'anteprima: si stampa, si sfoglia, si
    ingrandisce e **si esporta** nei formati che l'anteprima offre — PDF, Excel
    e gli altri. Non serve nessun comando speciale di questa maschera.

!!! info "Le dieci caselle degli anni si riempiono da sole"

    Non sono dieci anni fissi: all'apertura il programma **guarda nello
    storico** partendo dall'anno di lavoro e andando indietro di dieci anni, e
    per ogni anno che ci trova dei movimenti accende una casella scrivendoci
    sopra l'anno.

    Quindi:

    - le caselle compaiono **in ordine dal più recente al più vecchio**;
    - un anno **senza movimenti nello storico non compare affatto** — non è
      una casella spenta, è una casella che non c'è;
    - arrivano **già spuntate le prime tre**, cioè gli ultimi tre anni
      disponibili; le altre si spuntano a mano;
    - oltre i dieci anni indietro non si va.

    Se manca un'annata che dovrebbe esserci, va portata nello storico da
    [Manutenzione degli archivi](../utility/manutenzione-archivi.md).

## Vedi anche

- [Analisi delle vendite](analisi-vendite.md)
- [Venduto per…](venduto-per.md)
- [Manutenzione degli archivi](../utility/manutenzione-archivi.md)
