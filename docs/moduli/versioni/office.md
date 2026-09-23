---
title: Office
description: "Il ramo di menu per chi vende e assiste software: licenze, canoni di assistenza, fatturazione mensile e crediti per la fattura elettronica."
modulo: Office
maschera_id: IDD_OFF_LICENZE
---

# Office

Il menu **Office** serve a chi **vende e assiste programmi**: tiene il registro
delle licenze installate presso i clienti, le scadenze dell'assistenza e la
fatturazione dei canoni.

!!! warning "Se non trovi il menu, la tua versione non lo prevede"

    Come gli altri rami delle [versioni specifiche](index.md), all'avvio il
    programma toglie dalla barra l'intero menu quando la versione non è quella.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Office ▸ *(una delle sei voci)*
    - **Scorciatoia:** ++f2++ salva o avvia, ++f5++ cerca, ++esc++ esce

---

## Inserimento e Modifica Licenze

La scheda di una licenza installata.

### Che cosa è stato installato

| Campo | Descrizione |
|---|---|
| **Codice** | Il numero della licenza in archivio. |
| **Software** | Quale programma: `FACILE`, `FACILE LIGHT`, `RISTOFACILE`, `HOTEL`, `DENTAL`, `FACILE CRM` e gli altri dell'elenco. |
| **Anno** | L'anno della versione. |
| **N. Serie** | Il numero di serie consegnato al cliente. |
| **Build** | La build minima. |
| **Data** | La data della licenza. |
| **Versione** | La versione per esteso. |

{: .campi }

### Chi la usa e chi l'ha venduta

| Campo | Descrizione |
|---|---|
| **Cliente** | Chi usa il programma. |
| **Rivenditore** | Chi gliel'ha venduto, quando non è una vendita diretta. |
| **Agente** | L'[agente](../anagrafiche/anagrafica-agenti.md) che segue il cliente. |
| **Zona** | La [zona](../anagrafiche/zone.md). |

{: .campi }

### L'assistenza

| Campo | Descrizione |
|---|---|
| **Scadenza Assist.** | Quando scade il contratto di assistenza. |
| **Rinnovo Assist.** | `NO`, `SI`, `CHIAMARE` o `CESSATA`. |
| **Max Attivabile** | Fino a quale anno e build il cliente può aggiornarsi con questa licenza. |
| **Fatturazione** | `RIVENDITORE` o `DIRETTA`: a chi si fattura il canone. |
| **Periodicità** | `ANNUALE`, `SEMESTRALE`, `QUADRIMESTRALE`, `TRIMESTRALE`, `BIMESTRALE` o `MENSILE`. |

{: .campi }

!!! tip "«Chiamare» è una lista di lavoro"

    Il valore `CHIAMARE` di **Rinnovo Assist.** non è un forse: è il modo di
    segnare i clienti da ricontattare prima della scadenza. Si ritrovano tutti
    insieme filtrando la [stampa dei canoni](#stampa-canoni-assistenza) su
    quel valore.

### Quante licenze, e di che livello

Un quadro di conteggi su quattro colonne, una per **livello di licenza**:
**L** per `LIGHT`, **S** per `SMALL`, **P** per `PROFESSIONAL`, **E** per
`EVOLUTION`.

| Riga | Che cosa conta |
|---|---|
| **Principali** | Le licenze principali acquistate. |
| **Aggiuntive** | Le postazioni aggiuntive acquistate. |
| **Concesse** | Quante ne sono state concesse in tutto. |
| **Attivate** | Quante risultano attivate. |
| **Da Attivare** | Quante restano da attivare. |

{: .campi }

A parte, **Mobile** e **WEB** contano i dispositivi mobili e gli accessi web.

!!! note "«Concesse» non scende mai sotto la somma"

    Salvando, Facile controlla che le **Concesse** non siano meno di
    **Principali + Aggiuntive**, e se lo sono le alza da sé. Non è un errore da
    correggere: è il programma che impedisce di concedere meno di quanto il
    cliente ha comprato.

### Dove è installata e come si comporta

| Campo | Descrizione |
|---|---|
| **Configurazione** | Tre righe libere per descrivere l'installazione. |
| **Luogo Install.** | Dove si trova. |
| **Responsabile** | Il referente presso il cliente. |
| **Sottodominio**, **Indirizzo Api** | I riferimenti per la parte web. |
| **Stato Licenza** | `UTILIZZO NORMALE`, `DISATTIVAZIONE` o `BLOCCO`. |
| **Blocca Attivazione OnLine** | Impedisce che la licenza si attivi da sé via Internet. |
| **Blocca Accesso Web** | Chiude l'accesso web. |

{: .campi }

!!! danger "«Blocco» ferma il programma dal cliente"

    **Stato Licenza** non è una nota interna: è quello che il programma del
    cliente legge quando si attiva. Portarlo su `BLOCCO` o `DISATTIVAZIONE`, o
    spuntare i due blocchi, ha effetto **sull'installazione del cliente**.
    Sono leve da usare con la stessa cautela di una revoca.

!!! tip "La modifica parte dall'ultima licenza inserita"

    **Modifica Licenze** apre la scheda della licenza **inserita per ultima**,
    non un elenco. Per arrivare a un'altra si usa ++f5++.

## Stampa Canoni Assistenza

L'elenco dei canoni da incassare.

| Campo | Descrizione |
|---|---|
| **Mese** | Il mese di scadenza, o `TUTTI`. |
| **Software** | Un programma solo, o `TUTTI`. |
| **Anno** | L'anno. |
| **Cliente**, **Rivenditore**, **Agente**, **Zona** | I soliti filtri. |
| **Rinnovo** | `TUTTE`, `NO`, `SI`, `CHIAMARE` o `CESSATA` — le stesse voci della scheda della licenza. |

{: .campi }


## Emissione Fatture

Emette in una volta le fatture dei canoni del mese.

| Campo | Descrizione |
|---|---|
| **Mese** | Il mese da fatturare. |
| **Accorpa Fatture Stesso Cliente** | Un cliente con più licenze riceve **una fattura sola** invece di una per licenza. |
| **Registro Emissione Fatture** | La lettera del registro su cui emettere. |
| **Cliente**, **Rivenditore** | Restringono l'emissione. |

{: .campi }

Sotto, la griglia elenca quello che verrà fatturato. ++f2++ chiede conferma —
*Confermi l' emissione delle Fatture ?*, con **No** preimpostato — e alla fine
dice quante ne ha fatte: *E' stata emessa 1 Fattura!* oppure *Sono state emesse
N Fatture*.

**Se la ditta non è configurata** per la fattura alla pubblica amministrazione,
l'emissione avvisa e si ferma:

| Messaggio | Che cosa manca |
|---|---|
| *Registro Fatture PA non impostato su Ditta!* | Il registro dedicato, nelle impostazioni della [ditta](../anagrafiche/ditte.md). |
| *Causale Contabile Fatture PA non impostata su Ditta o non valida!* | La [causale contabile](../contabilita/causali-contabili.md) dedicata. |
| *Sezione Fatture PA non impostata sulla Causale Contabile Fatture PA o non valida!* | La [sezione](../contabilita/sezioni.md) sulla causale. |

## Situazione Crediti Fatture FE

Una stampa senza domande: elenca **i clienti che hanno comprato crediti per la
fattura elettronica**, ordinati per percentuale di utilizzo, dal più consumato
al meno. Chi è vicino a esaurirli sta in cima.

## Acquisizione Consumi FE da Digithera

Legge da Digithera quante fatture elettroniche ha consumato ciascun cliente e
riporta il dato in Facile. Riguarda **solo i clienti che hanno crediti
acquistati e una partita IVA**.

La domanda iniziale ha **tre risposte**, e vale la pena leggerla bene:

> *Vuoi adeguare i consumi di Facile con quelli di Digithera?*

| Risposta | Che cosa fa |
|---|---|
| **Sì** | Allinea: scrive il consumo letto da Digithera **e aggiorna i crediti utilizzati** del cliente. |
| **No** | Registra soltanto la lettura di Digithera, **lasciando come sta** il conteggio dei crediti utilizzati. Serve a confrontare senza toccare niente. |
| **Annulla** | Non fa nulla. |

La risposta preimpostata è **No**.

!!! tip "Prima si guarda, poi si allinea"

    Rispondere **No** la prima volta e stampare la
    [situazione crediti](#situazione-crediti-fatture-fe) permette di vedere dove
    i due conteggi divergono **prima** di sovrascriverli. Con **Sì** il dato
    vecchio di Facile è perso.

## Vedi anche

- [Versioni specifiche](index.md)
- [Gestione Licenza](../utility/gestione-licenza.md) — il lato del cliente
