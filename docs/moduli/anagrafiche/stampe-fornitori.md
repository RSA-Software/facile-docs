---
title: Stampe fornitori
description: Le quattro stampe dell'archivio fornitori — elenco, schede contabili, saldi ed elenco IVA.
modulo: Archivi
maschera_id: IDD_FOR_FORNITORI_ST
---

# Stampe fornitori

Le quattro voci di stampa che pendono da **Archivi ▸ Fornitori**: l'elenco
anagrafico e le tre stampe contabili.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Archivi ▸ Fornitori ▸ Stampa *(oppure* Stampa Schede*,* Stampa Saldi*,* Stampa Elenco IVA*)*
    - **Scorciatoia:** ++f2++ avvia la stampa, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](utenti.md)

---

## A cosa serve

| Voce di menu | Cosa stampa |
|---|---|
| **Stampa** | L'elenco dei fornitori, in quattro formati. |
| **Stampa Schede** | La scheda contabile del fornitore in un periodo, con il saldo progressivo. |
| **Stampa Saldi** | I saldi dei fornitori a una data. |
| **Stampa Elenco IVA** | L'elenco IVA fornitori. |

## Prerequisiti

Prima di usare queste maschere occorre avere in archivio i
[fornitori](anagrafica-fornitori.md). Per le stampe contabili servono anche le
registrazioni del periodo.

## La maschera

![Stampa fornitori](../../assets/img/anagrafiche/stampe-fornitori.png)

Struttura identica a quella delle [stampe clienti](stampe-clienti.md): in alto
l'intervallo, al centro i filtri, in basso le opzioni e i pulsanti **F2 - OK**
ed **Esci**.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Da Fornitore**, **A Fornitore** | | Primo e ultimo codice da stampare. Lasciandoli vuoti si stampano tutti. | codici |
| **Filtro** | | Restringe per descrizione. | testo |
| **Banca** | | Solo i fornitori appoggiati a quella [banca](../contabilita/banche.md). | codice |
| **Vettore** | | Solo i fornitori serviti da quel [trasportatore](trasportatori.md). | codice |
| **Pagamento** | | Solo i fornitori con quel [tipo di pagamento](../contabilita/tipi-di-pagamento.md). | codice |
| **Cat. Economica** | | Solo i fornitori di quella [categoria economica](categorie-economiche.md). | codice |
| **Filtra Tipo** | | Che genere di fornitore includere, secondo il campo **Tipo** della sua scheda. | `TUTTI`, `GENERICI`, `BENI`, `SERVIZI` |
| **Ordinamento** | | Come ordinare la stampa. | `CODICE`, `ALFABETICO` |
| **Formato** | ● | L'impaginazione della stampa. | `SINTETICA`, `DETTAGLIATA`, `ETICHETTE`, `RICHIESTA DATI FISCALI` |

Le stampe contabili — **Stampa Schede** e **Stampa Saldi** — aggiungono
**Data Iniziale**, **Data Finale** e **Sezione**, e usano gli stessi filtri
delle corrispondenti [stampe clienti](stampe-clienti.md).

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Prepara e mostra l'anteprima della stampa. |
| **Esci** | ++esc++ | Chiude senza stampare. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Stampare l'elenco dei fornitori di servizi

1. Apri **Menu ▸ Archivi ▸ Fornitori ▸ Stampa**.
2. Lascia vuoti **Da Fornitore** e **A Fornitore**.
3. Nell'elenco accanto a **Ordinamento** scegli `SERVIZI`.
4. Scegli **Formato** `SINTETICA` e premi **F2 - OK**.

### Chiedere i dati fiscali mancanti

1. Apri **Menu ▸ Archivi ▸ Fornitori ▸ Stampa**.
2. Scegli **Formato** `RICHIESTA DATI FISCALI`.
3. Premi **F2 - OK**.

### Stampare la scheda contabile di un fornitore

1. Apri **Menu ▸ Archivi ▸ Fornitori ▸ Stampa Schede**.
2. Metti lo stesso codice in **Da Fornitore** e **A Fornitore**.
3. Indica **Data Iniziale** e **Data Finale**.
4. Premi **F2 - OK**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impossibile creare il File!* | Il programma non riesce a scrivere il file di appoggio della stampa. | Verifica che la cartella di lavoro sia scrivibile; se il problema resta, segnala all'assistenza. |

## Note

!!! note "Le stesse stampe sono anche nel menu Contabilità"

    **Stampa Schede Fornitori** e **Elenco IVA Fornitori**, sotto
    **Menu ▸ Contabilità** e **Menu ▸ Contabilità ▸ Stampe Contabili**, aprono
    le stesse maschere descritte qui.

!!! note "Dove un fornitore diventa «di beni» o «di servizi»"

    Nella sua scheda, **Generale**, nel campo **Tipo**: `GENERICO`, `BENI`
    o `SERVIZI`. Non c'è nessun automatismo che lo deduca da quello che
    compri — lo decidi tu registrando il fornitore.

    È lo stesso campo su cui lavora il filtro **Filtra Tipo**, che trovi
    anche nella finestra di ricerca dei fornitori.

!!! note "Quali stampe sono davvero le stesse dei clienti"

    **Stampa Schede** è letteralmente la **stessa finestra** di quella dei
    clienti: cambia solo a quale dei due archivi si riferisce.

    **Stampa Saldi** invece è una finestra a sé, uguale a quella dei
    clienti **meno tre filtri** che sui fornitori non avrebbero senso:
    **agente**, **zona** e **gruppo**. Tutto il resto — periodo, sezioni,
    banca, categoria economica, pagamento, vettore, ordinamento — c'è
    uguale.

## Vedi anche

- [Anagrafica fornitori](anagrafica-fornitori.md)
- [Stampe clienti](stampe-clienti.md)
