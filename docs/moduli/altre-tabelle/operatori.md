---
title: Operatori
description: Le persone che operano alla cassa, con la tessera e la password con cui si identificano.
modulo: Archivi ▸ Altre Tabelle
maschera_id: IDD_TBC_OPERATORI
---

# Operatori

L'elenco di chi sta alla cassa. Ogni operatore ha una tessera e una password
con cui si riconosce, così gli scontrini e i movimenti restano attribuiti a chi
li ha fatti.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Archivi ▸ Altre Tabelle ▸ Operatori ▸ Inserimento *(oppure* Modifica*)*
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca
    - **Permessi richiesti:** nessun profilo predefinito; **Inserimento** e **Modifica** si abilitano separatamente per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

L'operatore non è la stessa cosa dell'[utente](../anagrafiche/utenti.md):
l'utente è chi entra in Facile con il proprio nome e i propri permessi,
l'operatore è chi materialmente batte alla cassa. In un negozio con un solo
computer e tre commessi ci sarà un utente e tre operatori.

L'operatore si collega poi all'utente nel campo **Operatore** della
[maschera Utenti](../anagrafiche/utenti.md).

## Prerequisiti

*Nessuno.*

## La maschera

![Operatori](../../assets/img/altre-tabelle/operatori.png)

È una maschera a finestra unica, senza schede: la barra dei comandi, quattro
campi e una casella.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice** | ● | Identificativo dell'operatore. In modifica non è modificabile. | numero |
| **Descrizione** | ● | Nome dell'operatore, come compare sugli scontrini e nelle stampe. | testo, fino a 30 caratteri |
| **Tessera** | | Il codice della tessera con cui l'operatore si identifica alla cassa. Quello che scrivi diventa maiuscolo. | testo, fino a 15 caratteri |
| **Password** | | Il codice che l'operatore digita per farsi riconoscere alla cassa touch. Si scrive coperto, a pallini, sia qui sia alla cassa. Distingue maiuscole e minuscole. | testo, fino a 16 caratteri |
| **Supervisore** | | Dà a questo operatore il permesso di usare i tasti riservati della cassa touch. | attivo/non attivo |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra l'operatore. In inserimento la maschera si svuota per il successivo. |
| **F3 - Prec.** | ++f3++ | Passa all'operatore precedente. |
| **F4 - Succ.** | ++f4++ | Passa all'operatore successivo. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco degli operatori. |
| **F6 - Elimina** | ++f6++ | Cancella l'operatore, previa conferma. |
| **Ricarica** | | Rilegge l'operatore dall'archivio, abbandonando le modifiche non salvate. |
| **Consultazione** | ++f11++ | Apre la consultazione. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |

## Come si fa

### Registrare un operatore di cassa

1. Apri **Menu ▸ Archivi ▸ Altre Tabelle ▸ Operatori ▸ Inserimento**.
2. Digita **Codice** e **Descrizione**.
3. Compila **Tessera** se l'operatore si identifica passando un badge.
4. Compila **Password** se lavora alla cassa touch: lì il codice gli viene
   chiesto, e senza password non entra.
5. Spunta **Supervisore** solo a chi deve poter usare i tasti riservati.
6. Premi **F2 - Salva**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca il **Codice** o la **Descrizione**. | Guarda dove si è posizionato il cursore: è il campo da compilare. |
| *Confermi la Cancellazione....* | Conferma richiesta da **F6 - Elimina**. | Rispondi **Sì** per eliminare l'operatore. |

## Note

!!! warning "Attenzione"

    L'operatore cancellato sparisce dall'elenco ma resta citato nei movimenti
    già registrati: non riciclare il suo codice per un'altra persona, o le
    statistiche di cassa risulteranno confuse.

!!! note "Quando viene chiesta la password"

    Soltanto alla **cassa touchscreen**, e in due momenti:

    - **all'apertura della cassa**, nella finestra dove si dice chi sta per
      lavorare: si indica l'operatore e si digita la sua password;
    - quando qualcuno preme un **tasto riservato** e l'operatore in turno non
      è un **Supervisore**. Allora si apre la finestra *Operatore
      Supervisore*, che chiede codice e password di chi autorizza. Se
      l'operatore in turno è già Supervisore non viene chiesto niente, e il
      permesso vale per tutto il resto della sessione.

    Se l'impostazione dei tasti riservati è disattivata sulla postazione, la
    seconda richiesta non compare mai.

    In tutte le altre maschere — documenti, vendita al banco, fatturazione —
    l'operatore si sceglie soltanto per codice o per tessera, **senza**
    password.

    La password sbagliata non produce nessun messaggio: solo un segnale
    acustico e il cursore che resta dov'è.

!!! note "La tessera: quale lettore"

    Nessuno in particolare. Il programma non dialoga con il lettore: la
    tessera si legge nello **stesso campo** dove si digita il codice
    dell'operatore. Prima prova a leggere quello che c'è scritto come numero
    di operatore e, se non lo trova, lo cerca fra le tessere.

    Va quindi bene qualunque lettore — badge a barre o banda magnetica — che
    si comporti come una tastiera e finisca con un invio. In **Tessera** si
    scrive **esattamente la stessa sequenza che il lettore trasmette**: fino a
    quindici caratteri, che il programma rende maiuscoli.

## Vedi anche

- [Utenti](../anagrafiche/utenti.md)
