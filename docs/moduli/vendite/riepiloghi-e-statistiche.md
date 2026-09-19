---
title: Riepiloghi e statistiche di vendita
description: I riepiloghi dei documenti emessi e le statistiche del fatturato, mensili e per gruppo, reparto, aliquota, fornitore, marchio e categoria.
modulo: Vendite
maschera_id: IDD_FAT_RIEPILOGO
---

# Riepiloghi e statistiche di vendita

Due famiglie di stampe che leggono i documenti emessi: i **riepiloghi**, che
elencano i documenti di un periodo, e le **statistiche**, che sommano il
fatturato e lo spezzano per una classificazione.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Vendite ▸ *(un tipo di documento)* ▸ Riepilogo
        - Menu ▸ Vendite ▸ Fatture ▸ Statistiche *(oppure* Statistiche Mensili *o uno dei* Fatturato Mensile per…*)*
    - **Scorciatoia:** ++f2++ avvia la stampa, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

**Riepilogo** esiste su quasi tutti i tipi di documento — fatture, DDT, bolle,
buoni di consegna, ricevute fiscali, autofatture, pro forma, consegne terzi — e
apre sempre la stessa maschera: elenca i documenti del periodo con i loro
totali.

Sui documenti di trasporto il riepilogo si declina in tre voci — **Riepilogo
Documenti Emessi a Clienti**, **Riepilogo Documenti Emessi a Fornitori** e
**Riepilogo Documenti Emessi a Clienti e Fornitori** — e sulle autofatture in
due: **Riepilogo Autofatture** e **Riepilogo Integrazioni**.

Le **statistiche** sommano il fatturato, e sono di tre famiglie:

- **Statistiche** lavora su un **intervallo di numeri di documento** e li
  somma nel modo che si sceglie;
- **Statistiche Mensili** lavora su un **periodo** e dà il fatturato mese per
  mese;
- i sette **Fatturato Mensile per…** lavorano su **un mese solo** e lo
  spezzano per una classificazione degli articoli.

I sette tagli già pronti sono:

| Voce di menu | Come spezza il fatturato |
|---|---|
| **Fatturato Mensile per Gruppo** | Per gruppo di articoli. |
| **Fatturato Mensile per Sottogruppo** | Per sottogruppo. |
| **Fatturato Mensile per Reparto** | Per [reparto](../magazzino/reparti.md). |
| **Fatturato Mensile per Cod. Iva** | Per [aliquota IVA](../contabilita/aliquote-iva.md). |
| **Fatturato Mensile per Fornitore** | Per fornitore dell'articolo. |
| **Fatturato Mensile per Marchio** | Per [marchio](../magazzino/marchi.md). |
| **Fatturato Mensile per Cat. Merceologica** | Per [categoria merceologica](../magazzino/categorie-merceologiche.md). |

Le **Fatture Pro Forma** hanno le proprie **Statistiche** e **Statistiche
Mensili**.

## Prerequisiti

Prima di usare queste stampe occorre avere emesso i
[documenti](documento-di-vendita.md) del periodo.

## La maschera

![Riepilogo documenti](../../assets/img/vendite/riepiloghi-e-statistiche.png)

Sono finestre di selezione: il periodo, i filtri e i pulsanti **F2 - OK** ed
**Esci**.

## Campi

### Riepilogo

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo da riepilogare. | date |
| **Registro** | | Restringe a un registro. | voce dell'elenco |
| **Cliente** | | Restringe a un cliente. | codice |
| **Agente** | | Restringe a un [agente](../anagrafiche/anagrafica-agenti.md). | codice |

{: .campi }

### Statistiche

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Registro** | | Il registro dei documenti. | da `A` a `Z` |
| **Da Numero**, **A Numero** | ● | L'intervallo dei numeri di documento. | numeri |
| **Da Data**, **A Data** | ● | Il periodo. | date |
| **Agente** | | Restringe a un agente. | codice |
| **Raggruppamento** | | Come sommare il fatturato. Ogni scelta produce una stampa diversa. | `NESSUNO`, `CLIENTE`, `AGENTE`, `MENSILE` |

{: .campi }

### Statistiche Mensili

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Da Data**, **A Data** | ● | Il periodo. | date |
| **Cliente** | | Restringe a un cliente. | codice |
| **Agente** | | Restringe a un agente. | codice |
| **Zona** | | Restringe a una zona. | codice |
| **Escludi Resi e Note di Credito** | | Somma il solo venduto, senza sottrarre resi e note di credito. | attivo/non attivo |

{: .campi }

### Fatturato Mensile per…

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Mese** | ● | Il mese da stampare. Arriva già impostato sul mese corrente, con il nome accanto. | da `1` a `12` |
| **Cliente** | | Restringe a un cliente. | codice |
| **Agente** | | Restringe a un agente. | codice |
| **Fatture** | | Includi le fatture. | attivo/non attivo |
| **Fatture Pro Forma** | | Includi le pro forma. | attivo/non attivo |
| **D.D.T. Vendita Normale** | | Includi i DDT di vendita normale. | attivo/non attivo |
| **D.D.T. Vendita Trasfert** | | Includi i DDT di trasferta. | attivo/non attivo |
| **D.D.T. Vendita Trasfert C.S.** | | Includi i DDT di trasferta a centro servizi. | attivo/non attivo |

{: .campi }

Queste sette stampe lavorano su **un mese per volta** e sull'**anno di
lavoro**: non c'è un intervallo di date.
## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Prepara e mostra l'anteprima della stampa. |
| **Esci** | ++esc++ | Chiude senza stampare. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Controllare le fatture emesse nel mese

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Riepilogo**.
2. Indica il periodo e premi **F2 - OK**.

### Vedere come si è mosso il fatturato per categoria

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Fatturato Mensile per Cat.
   Merceologica**.
2. Indica il **Mese** e spunta i documenti da contare — almeno **Fatture**.
3. Premi **F2 - OK**: esce il fatturato di quel mese, spezzato per categoria.

### Confrontare i dodici mesi dell'anno

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Statistiche Mensili**.
2. Indica come periodo tutto l'anno.
3. Premi **F2 - OK**: esce una riga per mese.

Le voci **Fatturato Mensile per…** non servono a questo: danno un mese solo.

### Controllare i documenti di trasporto emessi a fornitori

1. Apri **Menu ▸ Vendite ▸ Doc. di Trasporto ▸ Riepilogo Documenti Emessi a
   Fornitori**.
2. Indica il periodo e stampa.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca una delle date. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! note "I riepiloghi non sono stampe fiscali"

    Servono al controllo interno: non numerano nulla e si rifanno quante volte
    si vuole. Le stampe che fanno fede sono i
    [registri IVA](../contabilita/registri-iva.md).

!!! info "Statistiche e Statistiche Mensili sono due stampe diverse"

    | | **Statistiche** | **Statistiche Mensili** |
    |---|---|---|
    | Cosa si indica | registro, **intervallo di numeri** e periodo | il solo periodo |
    | Filtri | agente | cliente, agente, **zona** |
    | Risultato | dipende dal **Raggruppamento** | sempre il fatturato **mese per mese** |

    **Statistiche** cambia stampa secondo il raggruppamento scelto: `NESSUNO` dà
    l'elenco dei documenti con i loro ricavi, `CLIENTE` e `AGENTE` li sommano per
    soggetto, `MENSILE` li somma per mese. È quest'ultima scelta che la avvicina
    alle *Statistiche Mensili*, senza però i filtri per cliente e per zona.

    Tutte e due contano solo i documenti **emessi o contabilizzati**: le bozze e
    gli annullati restano fuori.

!!! note "Le sette voci «Fatturato Mensile per…» sono una maschera sola"

    Aprono tutte la stessa finestra, con lo stesso **Mese**, gli stessi due
    filtri e le stesse cinque caselle dei documenti: cambia solo la stampa che
    ne esce, e il titolo della finestra, che diventa *Fatturato Mensile per
    Gruppo*, *… per Reparto*, e così via.

    Imparata una, sono imparate tutte.

!!! note "«Fatturato Mensile per Marchio» raggruppa davvero per marchio"

    Dentro al programma quella voce porta ancora un nome che parla di
    *stagione*: è un residuo di quando il campo si chiamava così. La finestra si
    intitola *Fatturato Mensile per Marchio*, la stampa si intitola
    *FATTURATO … PER MARCHIO* e il raggruppamento è sul
    [marchio](../magazzino/marchi.md) dell'articolo. Il nome sul menu è quello
    giusto.

## Vedi anche

- [Gestione documenti](gestione-documenti.md)
- [Documento di vendita](documento-di-vendita.md)
- [Stampe di magazzino clienti](../magazzino/stampe-magazzino-clienti.md)
