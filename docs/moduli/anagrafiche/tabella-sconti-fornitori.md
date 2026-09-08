---
title: Tabella sconti fornitori
description: Le tabelle di sconto dei contratti con i fornitori, con il metodo di calcolo con cui si applicano.
modulo: Archivi
maschera_id: IDD_CTR_SCONTIFOR
---

# Tabella sconti fornitori

Le condizioni di sconto concordate con i fornitori, raccolte in tabelle
richiamabili dai contratti. Ogni tabella dice anche **con quale metodo** i suoi
sconti si combinano con gli altri.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Archivi ▸ Fornitori ▸ Gestione Contratti ▸ Tabella Sconti Fornitori ▸ Inserimento *(oppure* Modifica*)*
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca
    - **Permessi richiesti:** nessun profilo predefinito; **Inserimento** e **Modifica** si abilitano separatamente per ogni utente da [Archivi ▸ Utenti](utenti.md)

---

## A cosa serve

Un fornitore concede sconti diversi secondo il prodotto, il periodo o il volume
concordato. Invece di ripetere le percentuali su ogni riga di contratto, si
definisce qui una tabella con un nome e la si richiama dove serve.

Il **Metodo Calcolo** stabilisce il posto che la tabella occupa quando più
sconti concorrono sullo stesso acquisto.

## Prerequisiti

Prima di usare questa maschera occorre avere in archivio i
[fornitori](anagrafica-fornitori.md) a cui le tabelle si riferiscono.

## La maschera

![Tabella sconti fornitori](../../assets/img/anagrafiche/tabella-sconti-fornitori.png)

È una maschera a finestra unica, senza schede: la barra dei comandi e tre
campi. Il titolo in modifica è *Modifica Sconti Fornitore*.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice** | ● | Identificativo della tabella. In modifica non è modificabile. | numero |
| **Descrizione** | ● | Nome della tabella, come compare quando la si richiama sul contratto. | testo |
| **Metodo Calcolo** | ● | Come gli sconti di questa tabella si combinano con gli altri. | `NORMALE`, `PRIMARIO`, `SECONDARIO` |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra la tabella. In inserimento la maschera si svuota per la successiva. |
| **F3 - Prec.** | ++f3++ | Passa alla tabella precedente. |
| **F4 - Succ.** | ++f4++ | Passa alla tabella successiva. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco delle tabelle, con **Codice**, **Descrizione** e **Metodo**. |
| **F6 - Elimina** | ++f6++ | Cancella la tabella, previa conferma. |
| **Ricarica** | | Rilegge la tabella dall'archivio, abbandonando le modifiche non salvate. |
| **Consultazione** | ++f11++ | Apre la consultazione. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |

## Come si fa

### Registrare una tabella di sconti

1. Apri **Menu ▸ Archivi ▸ Fornitori ▸ Gestione Contratti ▸ Tabella Sconti
   Fornitori ▸ Inserimento**.
2. Digita **Codice** e **Descrizione**.
3. Scegli il **Metodo Calcolo**.
4. Premi **F2 - Salva**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca il **Codice** o la **Descrizione**. | Guarda dove si è posizionato il cursore: è il campo da compilare. |
| *Confermi la Cancellazione....* | Conferma richiesta da **F6 - Elimina**. | Rispondi **Sì** per eliminare la tabella. |

## Note

Non applicabile.

<!-- DA VERIFICARE: cosa distingue i tre metodi di calcolo NORMALE, PRIMARIO e SECONDARIO nell'applicazione degli sconti. -->

<!-- DA VERIFICARE: dove si inseriscono le percentuali vere e proprie della tabella: questa maschera contiene solo la testata. -->

<!-- DA VERIFICARE: dove la tabella viene richiamata sul contratto fornitore. -->

## Vedi anche

- [Anagrafica fornitori](anagrafica-fornitori.md)
- [Canali di vendita](../altre-tabelle/canali-di-vendita.md)
