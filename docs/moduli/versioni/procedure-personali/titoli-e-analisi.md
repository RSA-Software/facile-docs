---
title: Titoli, sospesi e analisi
description: Cambiali, tratte e ricevute bancarie, sospesi e anticipazioni varie, le analisi dello studio e le procedure di fine anno.
modulo: Procedure Personali
maschera_id: IDD_STU_TITOLI
---

# Titoli, sospesi e analisi

Quello che sta intorno al conto del cliente: gli effetti ricevuti, le partite
sospese, le analisi e le due procedure di fine anno.

---

## Titoli

Cambiali, tratte e ricevute bancarie ricevute dai clienti.

| Campo | Descrizione |
|---|---|
| **Numero**, **Data** | Numero e data del titolo. |
| **Tipo** | **Cambiali**, **Tratte** o **Ric. Bancarie**. |
| **Scadenza** | Quando scade. |
| **Importo** | Il valore del titolo. |
| **Cliente** | Chi lo ha emesso. |
| **Banca** | La [banca](../../contabilita/banche.md) su cui è appoggiato. |
| **Versato il** | La data in cui è stato versato. |
| **Cod. Rinnovo** | Il titolo che lo sostituisce, quando viene rinnovato. |

{: .campi }

In alto a destra, accanto alla data, il programma scrive **lo stato** del
titolo: `SCADUTO`, `PAGATO`, `INSOLUTO`, `RINNOVATO`, `RESPINTO`. Non è un campo
da compilare — lo decide il programma da quello che è successo al titolo.

!!! tip "Il rinnovo si legge in due direzioni"

    Quando un titolo viene rinnovato, il vecchio passa a `RINNOVATO` e porta in
    **Cod. Rinnovo** il numero del nuovo. È il filo che permette di risalire
    alla catena dei rinnovi di un cliente, che è poi il modo più rapido di
    accorgersi che un credito si sta trascinando da troppo tempo.

### Elenco Titoli Scaduti

Senza domande: elenca i titoli **già scaduti** e non ancora sistemati. È il
controllo da fare periodicamente.

### Stampa dei titoli

| Campo | Descrizione |
|---|---|
| **Da Numero**, **A Numero** | L'intervallo dei numeri. |
| **Scadenza Dal**, **Al** | Il periodo di scadenza. |
| **Tipo** | `TUTTI`, `CAMBIALI`, `TRATTE` o `RI.BA.` |
| **Stato** | `TUTTI`, `ATTIVI`, `SCADUTI`, `PAGATI`, `INSOLUTI`, `RINNOVATI` o `RESPINTI`. |
| **Banca**, **Cliente** | Restringono a una banca o a un cliente. |

{: .campi }

## Sospesi e Anticipazioni Varie

Due voci che aprono **la stessa maschera**, tenendo però due elenchi distinti:
i **sospesi** e le **anticipazioni varie**.

| Campo | Descrizione |
|---|---|
| **Codice** | Il numero della partita. |
| **Data** | Quando è sorta. |
| **Importo** | Di quanto. |
| **Oggetto** | Cinque righe di testo libero per descriverla. |

{: .campi }

!!! note "Cinque righe di descrizione, e nessun cliente"

    La maschera non chiede a chi si riferisce la partita: c'è solo l'oggetto.
    Serve a tenere nota di somme in attesa di collocazione — un versamento da
    identificare, un'anticipazione da recuperare — e per questo la descrizione
    è generosa: cinque righe invece di una.

## Analisi Cassa e Banche

| Campo | Descrizione |
|---|---|
| **Data** | La data a cui fare l'analisi. |
| **Saldo Accantonamenti** | Il saldo degli accantonamenti da tenere fuori. |
| **Debito TFR Mese Prec.** | Il debito per trattamento di fine rapporto del mese precedente. |

{: .campi }

I due importi si scrivono a mano perché non stanno nella contabilità corrente:
servono a depurare la disponibilità di cassa e banca da quello che è già
impegnato, e quindi a leggere **quanto è davvero disponibile**.

## Analisi CO.ME.

Chiede soltanto il **Mese** — o `TUTTI` — e produce il riepilogo.

## Stampa Selettiva Clienti

L'elenco dei clienti, filtrato su più chiavi contemporaneamente. Ogni riga di
filtro accetta **fino a sette codici** e ha accanto una casella **Escludi**, che
rovescia il filtro: invece dei sette indicati, tutti tranne quelli.

| Filtro | Su che cosa |
|---|---|
| **Categoria** | Le [categorie economiche](../../anagrafiche/categorie-economiche.md). |
| **Responsabile** | I [responsabili](../studio-collaboratori.md). |
| **Tipo Cantab.** | I tipi di contabilità. L'etichetta è scritta così nel programma: è *Tipo Contab.* |

{: .campi }

!!! tip "«Escludi» è quello che rende utile la maschera"

    Chiedere «tutti i clienti tranne quelli in regime forfettario» è molto più
    frequente che elencare i sette regimi che interessano. La casella **Escludi**
    esiste per questo, e va letta insieme ai codici della sua riga.

## Raffronti

Chiede **1° Anno** e **2° Anno** e mette a confronto i due esercizi.

## Le procedure di fine anno

### Generazione Sottoconti Annuali

Crea i sottoconti dell'anno nuovo sotto i conti di **crediti**, **rettifiche** e
**ricavi**, copiando la struttura esistente.

| Campo | Descrizione |
|---|---|
| **Anno Iniziale**, **Anno Finale** | Gli anni per cui generare i sottoconti. |

{: .campi }

!!! warning "La generazione non chiede conferma"

    ++f2++ e parte. Indicare un intervallo di anni sbagliato crea sottoconti che
    poi vanno tolti con la voce seguente. L'unico controllo è che l'anno finale
    non sia precedente all'iniziale: fuori da questo, il programma esegue.

### Rimozione Sottoconti Annuali

La stessa maschera, in senso inverso. Qui la conferma c'è:

> *Confermi la Rimozione dei Sottoconti ?*

con **No** preimpostato.

!!! danger "Rimuove i sottoconti, non controlla se sono stati usati"

    Se su quei sottoconti ci sono già registrazioni, toglierli lascia le
    scritture senza il loro conto. La rimozione ha senso subito dopo una
    generazione sbagliata, non a esercizio avviato.

### Generazione Riporti Annuali Clienti

Senza domande: riporta sull'anno nuovo le posizioni dei clienti, mostrando
l'avanzamento (*Generazione Riporti Annuali Clienti…*, poi *Adeguamento Date
Riporti Clienti…*).

## Banche Ditta

Apre la maschera delle [banche della ditta](../../contabilita/banche-ditta.md)
nella variante di questo ramo.

## Vedi anche

- [Crediti e incassi](crediti-e-incassi.md)
- [Responsabili e Collaboratori](../studio-collaboratori.md)
