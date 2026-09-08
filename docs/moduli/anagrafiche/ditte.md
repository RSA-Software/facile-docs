---
title: Ditte
description: L'anagrafica delle aziende gestite da Facile e tutte le impostazioni che ne governano il funzionamento, dai progressivi alla fatturazione elettronica.
modulo: Archivi
maschera_id: IDD_DIT_DITTE
---

# Ditte

La scheda dell'azienda: i suoi dati fiscali, i progressivi dei documenti, i
parametri di magazzino e di contabilità, la modulistica, la fatturazione
elettronica. È la maschera che decide come si comporta il programma per quella
ditta. Da qui si passa anche da un'azienda all'altra.

!!! info "In sintesi"

    **Percorso:** Menu ▸ Archivi ▸ Ditte ▸ Inserimento *(oppure* Modifica *o* Cambio Ditta*)*
    **Scorciatoia:** ++f2++ salva, ++f5++ cerca
    **Permessi richiesti:** l'inserimento chiede una password di amministrazione; la voce di menu si abilita per ogni utente da [Archivi ▸ Utenti](utenti.md)

---

## A cosa serve

Facile può gestire più aziende nello stesso programma, ciascuna con i suoi
archivi e le sue impostazioni. Questa maschera è dove quelle impostazioni si
scrivono.

È anche la risposta a molte domande che nascono altrove nel manuale: quando una
scheda dice *«dipende dalle impostazioni della ditta»* — il deposito attivo,
l'aliquota IVA predefinita, il listino principale, i registri, le tre tabelle
di classificazione libere — l'impostazione si trova qui.

**Cambio Ditta** non modifica nulla: serve solo a spostarsi sull'azienda con cui
si vuole lavorare.

## Prerequisiti

Per creare una ditta nuova serve la password di amministrazione. Per lavorare
davvero con l'azienda appena creata occorrerà poi popolare le tabelle di base:
[aliquote IVA](../contabilita/aliquote-iva.md),
[depositi](../magazzino/depositi.md),
[causali](../magazzino/causali-magazzino.md) e il piano dei conti.

## La maschera

![Ditte](../../assets/img/anagrafiche/ditte.png)

In alto ci sono i tre campi che identificano l'azienda — **Codice**,
**Rag. Soc./ Cognome** e **Rag. Soc./ Nome** — e sotto una fila di schede, una
per famiglia di impostazioni:

| Scheda | Cosa contiene |
|---|---|
| **Generale** | Dati anagrafici e fiscali dell'azienda. |
| **Progressivi** | I numeratori dei documenti. |
| **Date Bollati** | Le date di stampa dei registri bollati. |
| **Parametri Magazzino** | Deposito attivo, causali di servizio, comportamento dei movimenti. |
| **Codici Articoli** | Come sono fatti i codici degli articoli e quali tabelle di classificazione sono in uso. |
| **Parametri Contabili** | Sottoconti di servizio e regole di registrazione. |
| **Modulistica** | Quali moduli di stampa usare per ciascun documento. |
| **Bolli - Spese** | Bolli e spese proposti nei documenti. |
| **Destinazioni** | Le destinazioni merce dell'azienda. |
| **Fidelity - Buoni Sconto** | Raccolta punti e buoni sconto. |
| **Fatture Elettroniche** | Trasmissione e conservazione delle fatture elettroniche. |
| **Comunicazioni** | Le comunicazioni periodiche verso l'Agenzia delle Entrate. |
| **Domicilio - Titolare** | Domicilio legale e dati del titolare. |
| **Rivendita Tabacchi** | Parametri della rivendita di generi di monopolio. |
| **E-Commerce** | Collegamento al negozio online. |
| **Parametri Ristorazione** | Parametri per la ristorazione. |
| **Parametri Hotel** | Parametri per la gestione alberghiera. |
| **CRM** | Parametri del modulo CRM. |

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice** | ● | Identificativo dell'azienda. Non è modificabile dopo l'inserimento. | numero |
| **Rag. Soc./ Cognome** | ● | Ragione sociale, oppure il cognome se l'azienda è una ditta individuale. | testo |
| **Rag. Soc./ Nome** | | Seconda riga della ragione sociale, oppure il nome. | testo |

{: .campi }

<!-- DA VERIFICARE: i campi delle diciotto schede, uno per uno. Sono molti e governano il comportamento dell'intero programma: vanno documentati in una passata dedicata, scheda per scheda. -->

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra le impostazioni. |
| **F3 - Prec.** | ++f3++ | Passa alla ditta precedente. |
| **F4 - Succ.** | ++f4++ | Passa alla ditta successiva. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco delle ditte, con **Codice**, **Descrizione** e **Anno**. |
| **F6 - Elimina** | ++f6++ | Cancella la ditta, previa conferma. |
| **Ricarica** | | Rilegge la ditta dall'archivio, abbandonando le modifiche non salvate. |
| **Consultazione** | ++f11++ | Apre la consultazione. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |

## Come si fa

### Passare a un'altra azienda

1. Apri **Menu ▸ Archivi ▸ Ditte ▸ Cambio Ditta**.
2. Scegli l'azienda dall'elenco.
3. Il programma chiude gli archivi, apre quelli della ditta scelta e ne scrive
   il nome nella barra del titolo. Se gli archivi vanno aggiornati alla
   versione corrente, lo chiede prima di procedere.

### Correggere un'impostazione della ditta

1. Apri **Menu ▸ Archivi ▸ Ditte ▸ Modifica**.
2. Scegli la scheda che contiene l'impostazione.
3. Correggila e premi **F2 - Salva**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Una sola ditta e' presente in archivio!* | Si è chiesto il cambio ditta ma l'azienda gestita è una sola. | Non c'è nulla da fare: si sta già lavorando sull'unica azienda. |
| *Cambio ditta non permesso!* | Il cambio ditta è stato bloccato per questa installazione. | Se serve, chiedi all'assistenza di abilitarlo. |

## Note

!!! warning "Attenzione"

    **Le impostazioni di questa maschera cambiano il comportamento del
    programma per tutti.** Un deposito attivo o un'aliquota IVA predefinita
    sbagliati si ripercuotono su documenti, importazioni e stampe. Modificale
    con la stessa cautela con cui si tocca un archivio.

    **Il cambio ditta chiude e riapre gli archivi.** Chiudi prima ogni
    maschera aperta e assicurati che nessuna registrazione sia a metà.

<!-- DA VERIFICARE: quale password protegge l'inserimento di una ditta nuova e chi la possiede. -->

<!-- DA VERIFICARE: se le schede Parametri Ristorazione, Parametri Hotel e CRM compaiano sempre o solo con i moduli corrispondenti attivi. -->

<!-- DA VERIFICARE: cosa succede alla ditta duplicata quando, dopo il cambio, il programma propone la copia degli archivi. -->

## Vedi anche

- [Utenti](utenti.md)
- [Depositi](../magazzino/depositi.md)
- [Aliquote IVA](../contabilita/aliquote-iva.md)
