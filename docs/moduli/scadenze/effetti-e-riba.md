---
title: Effetti e RI.BA.
description: Il portafoglio effetti, la stampa delle RI.BA., la contabilizzazione degli effetti, il flusso elettronico per la banca e la stampa degli assegni.
modulo: Scadenze
maschera_id: IDD_CON_SCADENZE_RIBA
---

# Effetti e RI.BA.

Le scadenze che si incassano per il tramite della banca — ricevute bancarie,
tratte, ricevute di vendita — si governano da qui: si stampa il portafoglio, si
producono le RI.BA., si contabilizzano e si genera il file da mandare
all'istituto.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Portafoglio Effetti
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa RI.BA.
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Contabilizza Effetti
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Generazione File Flusso RI.BA.
        - Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Stampa Effetti Passivi
        - Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Stampa Assegni
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Stampa Portafoglio Effetti** | Gli effetti attivi in portafoglio. |
| **Stampa RI.BA.** | Stampa le ricevute bancarie da presentare. |
| **Contabilizza Effetti** | Genera le registrazioni contabili degli effetti presentati. |
| **Generazione File Flusso RI.BA.** | Produce il file elettronico da mandare alla banca. |
| **Stampa Effetti Passivi** | Gli effetti dal lato fornitori. |
| **Stampa Assegni** | Stampa gli assegni per pagare i fornitori. |

## Prerequisiti

Prima di usare queste maschere occorre:

- avere le scadenze con un [tipo di pagamento](../contabilita/tipi-di-pagamento.md)
  che prevede l'effetto;
- avere sui clienti le coordinate bancarie e la
  [banca](../contabilita/banche.md) di appoggio;
- **aver controllato le scadenze** dalla
  [gestione scadenze](gestione-scadenze.md): quello che si presenta alla banca
  non si corregge facilmente.

## La maschera

![Stampa RI.BA.](../../assets/img/scadenze/effetti-e-riba.png)

Sono finestre di selezione con più intervalli di date — emissione, scadenza,
data documento — e i pulsanti **F2 - OK** ed **Esci**.

## Campi

### Stampa Portafoglio Effetti ed Effetti Passivi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo. | date |
| **Fornitore** | | Restringe a un soggetto. Nello scadenziario clienti l'etichetta è **Cliente**. | codice |
| **Tipo Pagam.** | | Quale genere di effetto includere. | `TUTTI`, `RI.BA.`, `RI.VE.`, `TRATTA`, `ASSEGNO` |

{: .campi }

### Stampa RI.BA.

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Emissione Dal**, **Al** | | Periodo di emissione del documento. | date |
| **Scadenza Dal**, **Al** | | Periodo di scadenza. | date |
| **Data Doc. Dal**, **Al** | | Periodo della data documento. | date |
| **Scadenza Iniziale**, **Scadenza Finale** | | Intervallo dei numeri di scadenza. | numeri |
| **Banca Incasso** | | La [banca](../contabilita/banche.md) a cui si presentano. | codice |
| **Cliente** | | Restringe a un cliente. | codice |
| **Formato Stampa** | | L'impaginazione delle ricevute. | voce dell'elenco |

{: .campi }

### Contabilizza Effetti

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Emissione Dal**, **Al** | | Periodo di emissione. | date |
| **Scadenza Dal**, **Al** | | Periodo di scadenza. | date |
| **Data Doc. Dal**, **Al** | | Periodo della data documento. | date |
| **Da Numero Scad.**, **A Numero Scad.** | | Intervallo dei numeri di scadenza. | numeri |
| **Tipo Effetti** | ● | Quale genere di effetto contabilizzare. | `RI.BA.`, `RI.VE.`, e gli altri dell'elenco |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia la stampa o l'elaborazione. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |

## Come si fa

### Presentare le RI.BA. alla banca

1. Controlla le scadenze del periodo dalla
   [gestione scadenze](gestione-scadenze.md).
2. Apri **Stampa Portafoglio Effetti** e verifica cosa c'è da presentare.
3. Apri **Stampa RI.BA.**, indica il periodo di **Scadenza** e la **Banca
   Incasso**, e stampa.
4. Apri **Generazione File Flusso RI.BA.** per il file elettronico da mandare
   all'istituto.
5. Chiudi il giro con **Contabilizza Effetti**, che genera le scritture.

### Pagare i fornitori con assegno

1. Registra la [distinta di pagamento](distinte-incasso-pagamento.md).
2. Apri **Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Stampa Assegni**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Un campo non è valido, o la **Causale Contabile** non va bene. | Guarda dove si è posizionato il cursore. |
| *Il file del Flusso  "RIBA.TXT" è stato generato nella cartella OUT sotto la cartella di installazione del programma.* | Il flusso è stato scritto. | Prendi il file e mandalo alla banca. |
| *Vuoi marcare come incassate le scadenze contabilizzate ?* | **Contabilizza Effetti**, prima di partire. | **Sì** segna anche l'incasso, **No** scrive solo la registrazione e lascia le scadenze aperte. |

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! warning "L'ordine conta"

    Stampa e file di flusso vanno prodotti **prima** della contabilizzazione:
    contabilizzare per primo cambia lo stato degli effetti e la selezione
    successiva potrebbe non trovarli più.

!!! info "«Formato Stampa» ha due sole voci"

    | Voce | Cosa stampa |
    |---|---|
    | `MODULO` | Le RI.BA. sui **moduli prestampati**, una per foglio, con i campi nelle posizioni del modulo. |
    | `TABULATO` | Il **brogliaccio**: l'elenco delle RI.BA. su carta normale, per controllo. |

    Sono due modelli di stampa distinti, fissi: non c'è un elenco di moduli
    prestampati fra cui scegliere. Se il modulo in uso ha posizioni diverse, il
    modello va adattato dall'assistenza.

    Accanto c'è **Includi RI.BA. Stampate**: senza, la stampa salta quelle già
    fatte, così si ristampa solo il nuovo.

!!! info "Dove finisce il file di flusso e com'è fatto"

    Nella cartella **`out`** dell'installazione, con il nome fisso
    **`riba.txt`**. Il nome non cambia: **una generazione sovrascrive la
    precedente**, quindi conviene spostare il file appena esce.

    Il tracciato è quello **CBI** delle ricevute bancarie: righe di lunghezza
    fissa, una testata `IB`, per ogni effetto i record `14`, `20`, `30`, `50`,
    `51` e `70`, e una coda `EF`. È il formato che le banche italiane
    accettano per il portafoglio RI.BA.

    Vengono prese solo le scadenze di **clienti** con tipo di pagamento
    **RI.BA.**

!!! info "Che registrazioni fa «Contabilizza Effetti»"

    Una **registrazione di [prima
    nota](../contabilita/registrazione-prima-nota.md) per ogni effetto**, con la
    **Causale Contabile** indicata nella maschera: è lì che si decidono i conti,
    non nella procedura.

    La causale deve essere **di solo giornale** — registro 1 — **in relazione
    con i clienti**, **non IVA** e **non di beni da rivendere**: se non lo è, il
    programma non parte e riporta il cursore sul campo.

    Dei conti della causale, quello del **mastro clienti** viene sostituito con
    il conto del cliente dell'effetto; gli altri restano come stanno sulla
    causale. È così che l'effetto esce dal conto del cliente e entra sul conto
    degli effetti attivi, o su quello che la causale prevede.

    La data delle registrazioni si sceglie: quella indicata a mano, quella di
    emissione del documento o quella di scadenza dell'effetto.

    Alla partenza il programma chiede *«Vuoi marcare come incassate le scadenze
    contabilizzate ?»*. Rispondendo **No** le scadenze restano aperte e si
    chiuderanno all'incasso vero; rispondendo **Sì** vengono chiuse subito, con
    la data della registrazione.

### Generazione del file di flusso

| Campo | Descrizione |
|---|---|
| **Emissione Dal**, **Al** | Il periodo di emissione dei documenti. |
| **Scadenza Dal**, **Al** | Il periodo di scadenza. |
| **Data Doc. Dal**, **Al** | Il periodo di data documento. |
| **Da Num. Scadenza**, **A Num. Scadenza** | L'intervallo dei numeri di scadenza. |
| **Cliente** | Restringe a un cliente. |
| **Banca Ditta** | La [banca dell'azienda](../contabilita/banche-ditta.md) che presenta le RI.BA. |
| **Codice SIA Ditta** | Il codice SIA assegnato dalla banca. Arriva dalla ditta. |
| **Codice ABI Banca Gateway** | L'ABI della banca che riceve il flusso. |

{: .campi }

### Contabilizza Effetti

| Campo | Descrizione |
|---|---|
| **Emissione Dal**, **Al** — **Scadenza Dal**, **Al** — **Data Doc. Dal**, **Al** | I tre periodi con cui scegliere gli effetti. |
| **Da Numero Scad.**, **A Numero Scad.** | L'intervallo dei numeri. |
| **Tipo Effetti** | Che effetti contabilizzare. |
| **Includi gia' Contabilizzate** | Riprende anche quelle già fatte. |
| **Causale Contabile** | La [causale](../contabilita/causali-contabili.md) con cui registrare. |
| **Data Contabilizzazione** | Che data dare alle registrazioni: **Data Diversa** — e allora si scrive nel campo **Data** accanto —, **Data Emissione** o **Data Scadenza**. |

{: .campi }

**Tipo Effetti** vale `RI.BA.`, `RI.VE.` o `TRATTA`.

## Vedi anche

- [Gestione scadenze](gestione-scadenze.md)
- [Distinte di incasso e di pagamento](distinte-incasso-pagamento.md)
- [Banche](../contabilita/banche.md)
- [Tipi di pagamento](../contabilita/tipi-di-pagamento.md)
