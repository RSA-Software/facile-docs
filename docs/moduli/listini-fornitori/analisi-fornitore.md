---
title: Analisi fornitore
description: Il confronto fra il listino di un fornitore, l'ultimo prezzo pagato e il miglior listino disponibile, articolo per articolo.
modulo: Archivi ▸ Listini Fornitori
maschera_id: IDD_ART_ANALISI_FORNITORE
---

# Analisi fornitore

Prende un fornitore e mostra, per ogni articolo, quanto chiede lui, quanto si è
pagato l'ultima volta e chi lo fa al prezzo migliore — con lo scostamento in
percentuale. È la maschera che dice **dove si sta comprando male**.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Archivi ▸ Listini Fornitori ▸ Analisi Fornitore
    - **Scorciatoia:** ++f2++ esporta su Excel, ++f3++ cerca nella griglia
    - **Permessi richiesti:** nessun profilo predefinito; la voce di menu si abilita per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Con più fornitori per gli stessi articoli, la domanda ricorrente è se convenga
continuare a comprare da chi si compra. Questa maschera la risolve a colpo
d'occhio: si sceglie il fornitore e si guarda la colonna dello scostamento
rispetto al miglior listino. Dove il numero è alto, c'è margine per trattare o
per cambiare fornitore.

## Prerequisiti

Prima di usare questa maschera occorre avere caricato i
[listini dei fornitori](gestione-listini-fornitori.md): senza quelli il
confronto non ha termini.

## La maschera

![Analisi fornitore](../../assets/img/listini-fornitori/analisi-fornitore.png)

In alto la barra dei comandi e il campo **Fornitore**; sotto, la griglia del
confronto.

La griglia ha queste colonne:

| Colonna | Contenuto |
|---|---|
| **Codice**, **Barcode**, **Descrizione** | L'articolo. |
| **Esistenza** | Quanto ce n'è in magazzino. |
| **Ult. Prezzo Acq.** | L'ultimo prezzo effettivamente pagato. |
| **Ultimo Acq.** | La data dell'ultimo acquisto. |
| **Fornitore Ultimo Acquisto** | Da chi si è comprato l'ultima volta. |
| **Listino For. Sel.** | Il prezzo del fornitore scelto in alto. |
| **% Scostamento Ult. Prezzo / Listino For. Sel** | Di quanto il listino del fornitore scelto si discosta da quanto si è pagato. |
| **Fornitore Miglior Listino** | Chi fa il prezzo più basso su quell'articolo. |
| **Miglior Listino** | Quel prezzo. |
| **% Scostamento For. Sel. / Miglior Listino** | Quanto si perde comprando dal fornitore scelto invece che dal migliore. |

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Fornitore** | ● | Il fornitore da mettere a confronto con gli altri. | codice |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Esporta** | ++f2++ | Salva la griglia in un foglio Excel. |
| **F3 - Trova** | ++f3++ | Cerca un testo nella griglia. |

## Come si fa

### Capire se conviene cambiare fornitore

1. Apri **Menu ▸ Archivi ▸ Listini Fornitori ▸ Analisi Fornitore**.
2. Indica il **Fornitore** con cui lavori abitualmente.
3. Ordina la griglia sulla colonna **% Scostamento For. Sel. / Miglior
   Listino**.
4. Guarda le righe in cima: sono gli articoli su cui stai pagando di più.
5. Per portarti il risultato fuori da Facile, premi **F2 - Esporta**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impossibile inizializzare il file excel!* | Il programma non riesce a preparare il foglio Excel. | Segnala all'assistenza. |

## Note

!!! note "Il confronto vale quanto valgono i listini"

    Il *miglior listino* è calcolato sui listini fornitore caricati in Facile:
    se il listino di un fornitore è vecchio o incompleto, il confronto lo
    riflette. Aggiorna i listini prima di trarne conclusioni.

!!! info "Si parte dal listino del fornitore, non dall'anagrafica"

    L'elenco contiene **solo gli articoli che stanno nel listino del
    fornitore scelto**, e di quelli solo i codici che esistono anche in
    [anagrafica articoli](../anagrafiche/anagrafica-articoli.md).

    Un articolo che quel fornitore non tratta non compare, e non compare
    nemmeno una riga di listino che non si riesce ad agganciare a nessun
    articolo. Non è quindi il modo di sapere **cosa non ti ha quotato**: per
    quello serve il confronto fra listini.

!!! warning "Il confronto è sul prezzo netto, non su quello di listino"

    Facile confronta il **netto** — il prezzo di listino **già decurtato di
    tutti e sette gli sconti** che la riga porta — e non il prezzo lordo.

    È il confronto giusto, ed è anche il motivo per cui un fornitore con il
    listino più caro può risultare il migliore: conta quello che si paga
    davvero.

    Di conseguenza, **se gli sconti di una riga non sono aggiornati il
    confronto mente**, e mente in silenzio. Prima di decidere su questa
    schermata vale la pena controllare che i listini siano recenti.

!!! info "Su quali depositi è calcolata l'esistenza"

    Non su uno: su **tutti i depositi e tutte le sezioni che l'utente può
    vedere**, sommati insieme, per l'anno di lavoro.

    Vuol dire che due persone con permessi diversi vedono **numeri diversi**
    nella stessa colonna: chi è legato a un solo deposito vede l'esistenza
    di quello, chi non ha limitazioni vede il totale dell'azienda. Non è un
    errore, ma va saputo prima di confrontare due schermate.

    Restano fuori le righe per **taglia e colore**: nelle versioni che le
    gestiscono, l'esistenza di un articolo declinato per taglie qui risulta
    a zero.

## Vedi anche

- [Gestione listini fornitori](gestione-listini-fornitori.md)
- [Conferma e confronto dei listini](../listini-vendita/controllo-listini.md)
