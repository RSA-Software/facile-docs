---
title: Flussi e riepiloghi
description: Generazione del flusso per l'Agenzia delle Dogane, riepiloghi delle accise e imposte di consumo, crediti e riaccrediti, ravvedimenti.
modulo: Energy
maschera_id: IDD_ENE_GEN_FLUSSI
---

# Flussi e riepiloghi

Quello che esce dal deposito e va all'**Agenzia delle Dogane**: il file dei
movimenti e i conteggi dei tributi.

---

## Flussi

Il **flusso** è il file che raccoglie i movimenti di un periodo e li porta
all'Agenzia.

| Campo | Descrizione |
|---|---|
| **Codice Flusso**, **Data** | Numero e data del flusso. |
| **Movimenti Dal**, **Al** | Il periodo dei movimenti da comprendere. |
| **N. Record** | Quanti record contiene; lo conta il programma. |
| **Sog. Obbligato** | Il soggetto obbligato che trasmette. |
| **Codice UA**, **Cod. Accisa** | Il codice dell'unità amministrativa e il codice accisa del deposito. |
| **Cod. Ufficio** | L'ufficio delle dogane destinatario. |
| **Anno**, **Numero**, **N. Sede** | I riferimenti con cui il flusso si identifica. |

Sotto, la griglia elenca i movimenti che il flusso conterrà.

### Generare il file

Premuto ++f2++, Facile chiede:

> *Vuoi generare il file ?*

Il file viene scritto nella cartella **out** del programma, con il nome
composto dal **codice UA**, dal mese e giorno e dal numero del flusso — per
esempio `AB120319.C01`. È quello da trasmettere.

!!! note "C'è anche la cancellazione di prova"

    Generando il flusso di una cancellazione, Facile chiede in più:

    *Vuoi generare il file per la cancellazione in ambiente di prova ?*

    con **No** preimpostato. Serve a provare la cancellazione sull'ambiente di
    test dell'Agenzia prima di mandarla su quello vero.

### I controlli prima di generare

Facile non genera un flusso che l'Agenzia rifiuterebbe: passa in rassegna i
movimenti e si ferma al primo dato mancante o incoerente, indicando **il numero
del movimento e la controparte**.

| Messaggio | Che cosa manca |
|---|---|
| *Dati Trasmissione Agenzia Dogane non trovati in archivio !* | Il cliente o il fornitore non ha la scheda con i dati per l'Agenzia. |
| *Dati Cliente non trovati in archivio !* / *Dati Fornitore non trovati in archivio !* | L'anagrafica richiamata dal movimento non esiste più. |
| *Mancano Cod. Fiscale e P.IVA !* | La controparte non ha né codice fiscale né partita IVA: non si può trasmettere. |
| *ID Ufficio Dogane non valido !* | L'ID dell'ufficio non ha la forma prevista — otto caratteri, gli ultimi sei numerici. |
| *Codice Accisa non valido !* | Il codice accisa della controparte non è valido. Il messaggio dice se si tratta del cliente o del fornitore. |
| *Tipo cliente non valido per prodotti in sospensione di imposta !* | A quel tipo di cliente non si può cedere merce in sospensione d'imposta. |
| *Targa non valida !* | La targa del mezzo non è nella forma attesa. |
| *Ufficio Dogana non trovato in archivio !* | L'ufficio indicato sul flusso non esiste in tabella. |
| *Impossibile aprire il file !* | La cartella **out** non esiste, o il file è già aperto. |

!!! tip "Gli errori si correggono nelle anagrafiche, non qui"

    Quasi tutti questi messaggi parlano di **dati mancanti sul cliente o sul
    fornitore**: si sistemano nella loro anagrafica, nella sezione dei dati per
    l'Agenzia delle Dogane, e poi si rigenera il flusso.


## Riepilogo Accise e Imposte di Consumo

Il conto dei tributi di un periodo.

| Campo | Descrizione |
|---|---|
| **Codice**, **Data** | Numero e data del riepilogo. |
| **Tipo Richiesta** | `I - INSERIMENTO` o `C - CANCELLAZIONE`. |
| **Sogg. Obblig.** | Il soggetto obbligato. |
| **Periodo**, **Anno** | Il [periodo di movimentazione d'imposta](tabelle.md) e l'anno. |
| **Tipo Tributo** | Il [tributo](tabelle.md) di cui si fa il conto. |
| **Tributo a Debito** | Quanto è dovuto. |
| **Crediti/Riaccrediti** | Quanto c'è a credito. |
| **Storni** | Gli storni del periodo. |
| **Totale Tributi** | Il saldo. |
| **Note** | Testo libero. |

## Riepilogo Crediti e Riaccrediti

Registra un credito riconosciuto da un provvedimento dell'Agenzia.

| Campo | Descrizione |
|---|---|
| **Codice**, **Data** | Numero e data. |
| **Tipo Richiesta** | `I - INSERIMENTO` o `C - CANCELLAZIONE`. |
| **Sogg. Obblig.**, **Periodo**, **Anno**, **Tipo Tributo** | Come sopra. |
| **Cod. Ufficio** | L'ufficio che ha emesso il provvedimento. |
| **Data Provvedimento**, **N. Provvedimento** | Gli estremi del provvedimento. |
| **Importo Complessivo** | L'importo riconosciuto. |
| **Importo Scontato** | La parte già utilizzata in compensazione. |
| **Note** | Testo libero. |

## Ravvedimenti

Il conto del **ravvedimento operoso**: quanto si deve pagare per mettersi in
regola su un tributo versato in ritardo.

| Campo | Descrizione |
|---|---|
| **Codice**, **Data** | Numero e data. |
| **Tipo Richiesta** | `I - INSERIMENTO` o `C - CANCELLAZIONE`. |
| **Sogg. Obblig.**, **Periodo**, **Anno**, **Tipo Tributo** | Come sopra. |
| **Tributo Dovuto** | L'imposta non versata. |
| **Sanzione Minima** | La sanzione piena prevista. |
| **% Riduzione** | La riduzione che spetta secondo quanto tempo è passato. |
| **Sanzione** | La sanzione ridotta da pagare. |
| **Tasso legale**, **Giorni**, **Importo Interessi** | Il conto degli interessi. |

!!! note "La percentuale di riduzione dipende dal ritardo"

    Quanto si riduce la sanzione lo stabilisce la norma in base ai giorni di
    ritardo, e cambia nel tempo: il campo è lasciato libero proprio perché la
    misura giusta va presa dalla disciplina in vigore al momento del
    versamento, non da una tabella fissata nel programma.

## Vedi anche

- [Movimenti](movimenti.md)
- [Le tabelle](tabelle.md)
