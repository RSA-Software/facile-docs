---
title: Titoli
description: Cambiali, tratte e ricevute bancarie nella versione Studio di Facile, con scadenza, cliente e banca.
modulo: Archivi ▸ Contabilità
maschera_id: IDD_STU_TITOLI
---

# Titoli

**Solo Studio.** Da questa maschera si acquisiscono i titoli di credito —
cambiali, tratte e ricevute bancarie — con la loro scadenza, il cliente che li
ha emessi e la banca su cui sono appoggiati.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Archivi ▸ Contabilità ▸ Titoli ▸ Inserimento *(oppure* Modifica*)*
    - **Scorciatoia:** nessuna; la maschera si apre dal menu
    - **Versione:** **solo Studio.** Nelle altre versioni le voci restano nel menu ma non aprono nulla
    - **Permessi richiesti:** nessun profilo predefinito; **Inserimento** e **Modifica** si abilitano separatamente per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Il titolo è il pezzo di carta che il cliente consegna a garanzia o a
pagamento. Registrandolo qui si sa che cosa si ha in portafoglio, quando
scade, su quale banca è appoggiato e quando è stato versato.

Lo stesso menu contiene anche **Gestione Titoli Scaduti** e **Gestione Titoli
Attivi**, che sono le due viste da cui si lavora sul portafoglio.

!!! info "Solo nella versione Studio"

    Queste maschere esistono **solo nella versione Studio**. Nelle altre
    versioni il programma toglie all'avvio tutte e cinque le voci, e con esse
    il sottomenu **Titoli**, che resterebbe vuoto: se non lo trovi in
    **Archivi ▸ Contabilità**, è perché la tua versione non lo prevede.

## Prerequisiti

Prima di registrare un titolo occorrono l'[anagrafica del
cliente](../anagrafiche/anagrafica-clienti.md) che lo ha emesso e la
[banca](banche.md) su cui appoggiarlo.

## La maschera

![Maschera Titoli](../../assets/img/contabilita/titoli.png)

È una maschera a finestra unica, senza schede: la **barra dei comandi**, il
numero e la data del titolo, il riquadro **Tipo** con le tre scelte, e i dati
del titolo.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| Numero | | Numero del titolo. Lo assegna il programma e non si modifica. | Sola lettura |
| Data | ● | Data di acquisizione del titolo. | Data |
| **Tipo** | | Che titolo è. Si sceglie fra le tre voci del riquadro. | Cambiali, Tratte, Ric. Bancarie |
| Scadenza | ● | Data di scadenza del titolo. Non può essere anteriore alla **Data**. | Data |
| Importo | ● | Valore del titolo. Dev'essere maggiore di zero. | Importo |
| Cliente | ● | Cliente che ha emesso il titolo. Accanto compare la ragione sociale. | Codice dall'archivio clienti |
| Banca | | Banca su cui il titolo è appoggiato. Accanto compare la descrizione. | Codice dall'archivio banche |
| Versato il | | Data in cui il titolo è stato versato. Diventa obbligatoria se compili la **Banca**, e deve cadere nell'anno di lavoro. | Data |
| Cod. Rinnovo | | Numero del titolo che sostituisce questo, quando viene rinnovato. | Numero di un altro titolo |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra il titolo. |
| **F3 - Prec.** | ++f3++ | Passa al titolo precedente. |
| **F4 - Succ.** | ++f4++ | Passa al titolo successivo. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco dei titoli. |
| **F6 - Elimina** | ++f6++ | Cancella il titolo, previa conferma. |
| **Ricarica** | | Rilegge il titolo dall'archivio, abbandonando le modifiche non salvate. |

Valgono inoltre:

| Comando | Scorciatoia | Effetto |
|---|---|---|
| Elenco valori | ++f10++, ++space++ o doppio clic su **Cliente** e **Banca** | Apre l'elenco da cui scegliere. |
| Consultazione | ++f11++ | Apre la finestra **Consultazione**. |
| Calcolatrice | ++f12++ | Apre la calcolatrice. |
| Campo successivo | ++enter++ | Sposta il cursore sul campo seguente. |
| Chiusura | ++esc++ | Chiude la maschera. |

## Come si fa

### Acquisire un titolo

1. Apri **Menu ▸ Archivi ▸ Contabilità ▸ Titoli ▸ Inserimento**. Il **Numero**
   viene assegnato dal programma.
2. Indica la **Data** di acquisizione.
3. Scegli il **Tipo**: *Cambiali*, *Tratte* o *Ric. Bancarie*.
4. Compila **Scadenza** e **Importo**.
5. Indica il **Cliente** e la **Banca** con ++f10++.
6. Premi **F2 - Salva**.

### Registrare il versamento

1. Premi **F5 - Cerca** e carica il titolo.
2. Compila **Versato il** con la data del versamento.
3. Premi **F2 - Salva**.

### Registrare un rinnovo

1. Acquisisci il titolo nuovo con la procedura sopra e prendi nota del suo
   **Numero**.
2. Carica il titolo vecchio e scrivi quel numero in **Cod. Rinnovo**.
3. Premi **F2 - Salva**.

### Chiudere i titoli scaduti

1. Apri **Menu ▸ Archivi ▸ Contabilità ▸ Titoli ▸ Gestione Titoli Scaduti**.
2. Su ogni riga spunta **una sola** delle tre colonne, secondo com'è andata.
3. Premi **F2 - OK**.
4. Le righe spuntate vengono registrate con quell'esito e **spariscono dalla
   griglia**. In basso, in **Saldo**, resta il totale di quelle che hai
   lasciato in sospeso.

Si può ripetere più volte: la finestra si chiude da sé quando la griglia
rimane vuota. Le righe non spuntate restano come stanno e le ritrovi la volta
dopo.

!!! note "La finestra si chiama diversamente dal menu"

    La voce di menu dice **Titoli**, la didascalia della finestra dice
    **Acquisizione Titoli**. Sono la stessa cosa: qui si usa il nome del
    menu, che e' quello che cerchi quando vuoi aprirla.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Confermi la Cancellazione....* | Conferma richiesta da **F6 - Elimina**. | Rispondi **Sì** per eliminare il titolo. |
| *Il record è stato modificato da un altro nodo della rete.* | Un altro utente ha salvato lo stesso titolo mentre lo modificavi. | Premi **Ricarica**, verifica cosa è cambiato e rifai le tue modifiche. |
| *Il record è stato cancellato da un altro nodo della rete.* | Un altro utente ha eliminato il titolo mentre lo modificavi. | La maschera si chiude: non c'è più nulla da salvare. |

## Note

!!! info "Le altre due voci del menu: titoli scaduti e titoli attivi"

    Nello stesso menu ci sono altre due voci — **Gestione Titoli Scaduti** e
    **Gestione Titoli Attivi** — che aprono **la stessa finestra**, con un
    contenuto diverso: la prima mostra i soli titoli **scaduti**, la seconda
    mostra anche quelli **ancora in corso**.

    Tutte e due, prima di aprirsi, fanno una pulizia: i titoli scaduti che non
    sono stati presentati in banca vengono **tolti dal castelletto**, così la
    disponibilità residua torna a dire il vero.

    La finestra è una griglia con **Data**, **Numero**, **Importo**, **Tipo**,
    **Cliente** e **Banca**, e tre colonne da spuntare:

    | Colonna | Vuol dire |
    |---|---|
    | **Pag** | Il titolo è stato pagato. |
    | **Ins** | È tornato insoluto. |
    | **Rin** | È stato rinnovato. |

!!! warning "Attenzione"

    ++esc++ chiude la maschera senza chiedere conferma e senza salvare: le
    modifiche fatte dopo l'ultimo **F2 - Salva** vanno perse.

!!! note "Cosa il programma pretende prima di salvare"

    I controlli ci sono, ma sono silenziosi: niente messaggi, solo un segnale
    acustico e il cursore che si posiziona sul campo che manca.

    Sono, nell'ordine in cui vengono fatti:

    - la **Data** dev'essere compilata;
    - la **Data Scadenza** dev'essere compilata e **non anteriore** alla data
      del titolo;
    - l'**Importo** dev'essere maggiore di zero;
    - il **Cliente** dev'essere indicato.

    La **Banca** invece si può lasciare vuota: un titolo senza banca è un
    titolo in portafoglio, non ancora presentato. Ma **se la indichi**,
    diventa obbligatoria anche la **Data Versamento**, e quella data deve
    cadere nell'anno di lavoro: altrimenti arriva l'errore sull'esercizio.

    Il **Codice** non si tocca: lo assegna il programma.

## Vedi anche

- [Banche ditta](banche-ditta.md)
- [Anagrafica clienti](../anagrafiche/anagrafica-clienti.md)
