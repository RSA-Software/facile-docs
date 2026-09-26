---
title: Mailing list
description: Come si costruiscono le liste di clienti a cui mandare email o SMS, e come si spediscono.
modulo: Archivi
maschera_id: IDD_CLI_MAILING
---

# Mailing list

Si prepara una lista di clienti, la si riempie scegliendoli a mano o a gruppi, e
da lì si manda a tutti un'email o un SMS. La stessa lista si può stampare,
esportare su Excel o usare per le etichette.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Archivi ▸ Clienti ▸ Mailing list
    - **Scorciatoia:** ++f2++ email, ++f3++ SMS, ++f4++ Excel, ++f5++ stampa elenco
    - **Permessi richiesti:** nessun profilo predefinito; la voce di menu si abilita per ogni utente da [Archivi ▸ Utenti](utenti.md)

---

## A cosa serve

Serve per le comunicazioni a molti: la lettera di Natale, l'avviso di chiusura,
la promozione del mese. Le liste restano in archivio, quindi una volta
costruita la lista «clienti bar della provincia» la si riusa.

## Prerequisiti

Prima di usare questa maschera occorre:

- avere in archivio i [clienti](anagrafica-clienti.md) con i recapiti
  compilati: senza email non si manda posta, senza cellulare non si mandano
  SMS;
- avere impostato l'indirizzo del mittente, altrimenti l'invio si ferma;
- per gli SMS, il servizio di invio configurato.

## La maschera

![Mailing list](../../assets/img/anagrafiche/mailing-list.png)

La finestra *Mailing list* si ridimensiona e ha un menu tutto suo — **Liste**,
**Clienti**, **Azioni** — invece della solita barra dei comandi. In alto il
campo **Lista**, sotto la griglia dei destinatari, in basso una barra di stato.

La griglia ha queste colonne:

| Colonna | Contenuto |
|---|---|
| **Sel** | La spunta che include la riga nell'invio. |
| **SMS** | Segna se al cliente si può mandare un SMS. |
| **Email** | Segna se al cliente si può mandare un'email. |
| **Cliente** | Ragione sociale. |
| **Telefono**, **Cellulare**, **Cellulare 2**, **Cellulare 3** | I recapiti telefonici. |
| **Indirizzo**, **Città**, **Cap**, **Prov.** | L'indirizzo postale, per le etichette. |
| **Codice** | Codice del cliente. |

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Lista** | ● | Quale lista si sta lavorando. | codice della lista |

## Pulsanti e comandi

### Menu Liste

| Comando | Effetto |
|---|---|
| **Inserimento** | Crea una lista nuova. |
| **Modifica** | Cambia i dati della lista. |
| **Stampa** | Stampa la lista. |
| **Duplica** | Crea una copia della lista, per partire da una esistente. |

### Menu Clienti

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **Aggiungi** | ++f8++ | Aggiunge un cliente alla lista. |
| **Aggiungi Gruppo** | ++f9++ | Aggiunge alla lista **un gruppo di clienti in blocco**: apre il filtro clienti, e tutti quelli che ne escono entrano nella lista. |
| **Visualizza** | | Apre l'[anagrafica](anagrafica-clienti.md) del cliente della riga. |
| **Elimina Riga** | | Toglie dalla lista la riga attiva. |
| **Elimina Selezionati** | | Toglie le righe spuntate. |
| **Elimina non Selezionati** | | Toglie le righe **non** spuntate, tenendo solo quelle scelte. |
| **Elimina Tutti** | | Svuota la lista. |

### Menu Azioni

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **Email** | ++f2++ | Manda l'email ai destinatari spuntati. |
| **Sms** | ++f3++ | Manda l'SMS ai destinatari spuntati. |
| **Esporta su Excel** | ++f4++ | Salva la lista in un foglio Excel. |
| **Stampa Elenco** | ++f5++ | Stampa l'elenco dei destinatari. |
| **Stampa Etichette** | | Stampa le etichette postali. |
| **Deseleziona Tutti** | ++f6++ | Toglie la spunta a tutte le righe. |
| **Seleziona Tutti** | ++f7++ | Spunta tutte le righe. |

## Come si fa

### Mandare un'email a un gruppo di clienti

1. Apri **Menu ▸ Archivi ▸ Clienti ▸ Mailing list**.
2. Da **Liste ▸ Inserimento** crea la lista e dalle un nome.
3. Con **Clienti ▸ Aggiungi Gruppo** — o ++f9++ — porta dentro i clienti che
   ti servono, oppure aggiungili uno a uno con ++f8++.
4. Guarda la colonna **Email**: chi non ce l'ha non riceverà nulla.
5. Premi ++f7++ per spuntare tutti, poi togli la spunta a chi vuoi escludere.
6. Premi ++f2++ per l'invio.

### Riusare una lista dell'anno prima

1. Apri la lista.
2. Usa **Liste ▸ Duplica** per farne una copia.
3. Sulla copia togli i clienti che non servono più con **Clienti ▸ Elimina
   Riga**, e aggiungi i nuovi.

### Stampare le etichette dei destinatari

1. Costruisci la lista e spunta i destinatari.
2. Usa **Azioni ▸ Stampa Etichette**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Indirizzo email del mittente non impostato!* / *Impossibile procedere* | Manca l'indirizzo da cui inviare. | Impostalo nei dati dell'[utente](utenti.md) o della [ditta](ditte.md) e riprova. |
| *Confermi l' eliminazione delle righe selezionate ?* | Si è scelto **Elimina Selezionati**. | **Sì** toglie dalla lista le righe spuntate. I clienti restano in archivio. |
| *Confermi l' eliminazione delle righe non selezionate ?* | Si è scelto **Elimina non Selezionati**. | **Sì** tiene solo le righe spuntate. |
| *Confermi l' eliminazione di tutte le righe ?* | Si è scelto **Elimina Tutti**. | **Sì** svuota la lista. |

## Note

!!! note "Eliminare non cancella il cliente"

    Le voci **Elimina** del menu **Clienti** tolgono i nominativi *dalla
    lista*: l'anagrafica del cliente non viene toccata.

!!! info "«Aggiungi Gruppo» vuol dire un gruppo di clienti"

    Non è il gruppo dell'anagrafica né un raggruppamento della mailing list:
    è **un blocco di clienti in una volta sola**, in contrapposizione ad
    **Aggiungi**, che ne porta dentro uno.

    Premendolo si apre il **filtro clienti**, lo stesso delle stampe: zona,
    agente, categoria, comune e così via. Confermando, tutti i clienti che
    rispondono al filtro vengono aggiunti alla lista.

    Il filtro sa guardare anche **quello che i clienti hanno comprato**:
    riempiendone la parte sugli articoli — codice, descrizione, gruppo,
    sottogruppo, categoria — entrano nella lista solo i clienti che hanno
    movimenti su quegli articoli. È il modo per scrivere, per esempio, a chi
    ha comprato una certa linea di prodotti.

    Prima di premerlo bisogna aver scelto una lista: senza, il comando non fa
    niente e non dice niente.

!!! info "Dove si scrive il testo del messaggio"

    Nella finestra che si apre **dopo** aver dato l'invio: *Invia Email*, con
    **Oggetto**, **Allegati** e un riquadro di scrittura formattata, oppure
    *Invio SMS*, con il solo testo.

    Qui il testo parte **vuoto**: la mailing list non ha un testo
    preconfezionato, a differenza degli
    [auguri di compleanno](gestione-compleanni.md), che partono da un file di
    modello.

    Il destinatario non si compila: lo mette il programma riga per riga,
    scorrendo le righe spuntate della lista.

!!! info "Da quale indirizzo parte l'email"

    Il programma prende il mittente in quest'ordine:

    1. l'indirizzo di posta scritto sulla scheda dell'**utente** che sta
       lavorando, se c'è;
    2. altrimenti l'utente del **server di posta della ditta**.

    Se l'utente ha anche server, password e porta suoi, l'invio parte
    **davvero** dal suo account, non da quello della ditta. È il modo per far
    sì che ogni operatore scriva con il proprio indirizzo.

    Se alla fine non risulta nessun indirizzo, l'invio si ferma prima di
    cominciare con *Indirizzo email del mittente non impostato!*.

    Sull'email vengono poi aggiunti da sé, se configurati sulla ditta,
    l'indirizzo a cui far tornare le risposte e un destinatario in copia
    nascosta per tenerne traccia.

!!! info "Il servizio SMS"

    Si configura sulla **ditta**, scheda *Server*: si sceglie il fornitore fra
    quelli previsti e si compilano account, password e mittente. Gli SMS non
    partono da Facile: li consegna quel fornitore, e vanno pagati a lui.

    Qui il comando di invio resta acceso anche se il fornitore non è stato
    scelto: te ne accorgi solo al momento di mandare, con *Sms Provider non
    valido*, e non parte niente.

!!! warning "Un SMS lungo sono più SMS"

    Prima di partire il programma conta quanti messaggi serviranno per il
    testo che hai scritto. Se ne serve più di uno chiede conferma dicendo
    quanti sono — e vanno moltiplicati per il numero dei destinatari.

## Vedi anche

- [Anagrafica clienti](anagrafica-clienti.md)
- [Gestione compleanni](gestione-compleanni.md)
- [Stampe clienti](stampe-clienti.md)
