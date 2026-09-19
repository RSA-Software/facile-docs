---
title: I menu File e ?
description: Imposta stampante, barra degli strumenti, richiesta di assistenza remota, invio di email e SMS, uscita dal programma e informazioni sulla versione.
---

# I menu File e ?

Sono i due menu che non appartengono a nessun modulo: stanno in fondo alla
barra, dopo **Utility**, e ci sono sempre.

---

## Il menu File

| Voce | Che cosa fa |
|---|---|
| **Imposta stampante…** | Apre la finestra di Windows per scegliere la stampante e impostarne il formato. Vale per la sessione in corso. |
| **Toolbar ▸ Barra degli strumenti** | Mostra o nasconde la barra dei pulsanti. |
| **RSA Online Support** | Avvia il collegamento per l'assistenza remota. |
| **Email** | Apre la finestra per scrivere e spedire un messaggio di posta. |
| **SMS** | Apre la finestra per spedire un SMS. |
| **Esci** | Chiude Facile. |

### RSA Online Support

Serve a far entrare l'assistenza R.S.A. sul computer, quando al telefono non si
viene a capo. Facile chiede prima:

> *Confermi la richiesta del supporto ?*

La risposta preimpostata è **No**. Rispondendo **Sì** parte il programma di
assistenza remota installato insieme a Facile, che mostra un codice da dettare
al telefono: senza quel codice nessuno può collegarsi.

!!! note "Non è il menu Assistenza"

    **Menu ▸ Utility ▸ [Assistenza](../moduli/utility/assistenza.md)** è un'altra
    cosa: sono le procedure che l'assistenza esegue **sugli archivi**, protette
    da password. Questa voce apre solo il collegamento.

### Email

Una finestra di posta dentro Facile, per mandare un messaggio senza passare dal
programma di posta.

| Campo | Descrizione |
|---|---|
| **A**, **CC**, **BCC** | I destinatari. Il pulsante a sinistra di ciascuno apre la rubrica da cui sceglierli. |
| **Oggetto** | L'oggetto del messaggio. |
| **Allegati** | I file da allegare; il pulsante **Allega** apre la finestra di scelta. |
| *(corpo)* | Il testo, con la formattazione. |
| **Invia** | Spedisce. Sotto, una barra mostra l'avanzamento. |

Il **mittente** è l'indirizzo dell'utente collegato, preso dalla sua
[scheda](../moduli/anagrafiche/utenti.md). Se quell'utente ha anche i propri
parametri di posta, il messaggio parte dalla **sua** casella; altrimenti da
quella della [ditta](../moduli/anagrafiche/ditte.md).

!!! warning "Una copia nascosta può partire da sola"

    Se nelle impostazioni della ditta è indicato un indirizzo per le notifiche,
    quell'indirizzo viene messo **in copia nascosta su ogni messaggio**, già
    compilato nel campo **BCC**. È voluto — serve a tenere traccia di quello che
    esce — ma è bene saperlo prima di scrivere qualcosa di riservato.

**I messaggi**

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impostare server SMTP in configurazione Ditta !* | Non è configurato nessun server di posta. | Va impostato nelle impostazioni della ditta: i parametri li dà il gestore della casella. |
| *Impostare Email Mittente sull' utente !* | L'utente collegato non ha un indirizzo di posta. | Scriverlo nella sua scheda utente. |
| *Specificare indirizzo Destinatario !* | Manca il campo **A**. | Indicare almeno un destinatario. |
| *Specificare l'oggetto dell'email !* | Manca l'oggetto. | L'oggetto è obbligatorio. |
| *Raggiunto il numero massimo di files selezionabili!* | Si stanno allegando più di mille file. | Allegarne di meno, o zipparli. |

### SMS

| Campo | Descrizione |
|---|---|
| **A…** | Apre l'elenco da cui scegliere i destinatari; i numeri si possono anche scrivere a mano. |
| *(testo)* | Il messaggio. |
| **Invio Programmato — Data**, **Ora** | Quando farlo partire. Lasciandoli vuoti parte subito. |
| **Invia** | Spedisce. |

Mentre si scrive, **il titolo della finestra conta i caratteri**: *Invio SMS :
40 caratteri*. Superati i 160 diventa *Invio di 2 SMS : 173 caratteri* e si
sente un segnale acustico — da lì in poi ogni 160 caratteri è un messaggio in
più, e si paga in più.

!!! note "Alcuni caratteri contano doppio"

    I simboli `{ } [ ] \ | ~ ^ €` non stanno nell'alfabeto base degli SMS:
    sul telefono occupano **il posto di due caratteri**, e il conteggio ne
    tiene conto. Una parentesi graffa di troppo può far passare il messaggio
    da uno a due.

    I caratteri che un SMS non sa portare — le virgolette curve copiate da
    Word, per esempio — vengono contati, ma **arrivano storti**: meglio
    scrivere il testo qui dentro invece di incollarlo da un documento.

**I messaggi**

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Non è stato impostato nessun destinatario !* | Manca il campo **A**. | Indicare almeno un numero. |
| *Non è stato impostato nessun testo da inviare !* | Il messaggio è vuoto. | Scrivere il testo. |
| *Confermi l'invio dell' SMS ?* | Conferma prima di spedire. | La risposta preimpostata è **No**. |
| *Per inviare il testo inserito è necessario inviare più di un messaggio ! Confermi l'invio di N SMS ?* | Il testo supera i 160 caratteri. | Confermando si spediscono — e si pagano — N messaggi. |
| *Sms Provider non valido* | Nelle impostazioni della ditta non è indicato quale servizio SMS usare. | Va scelto fra quelli previsti; lo imposta l'assistenza insieme alle credenziali. |

!!! note "L'invio programmato vale solo per il futuro"

    Se la data e l'ora indicate sono già passate, il messaggio **parte subito**:
    non viene scartato e non viene segnalato niente.

## Il menu ?

| Voce | Che cosa fa |
|---|---|
| **Argomenti della Guida** | Apre questo manuale alla copertina. |
| **Informazioni su Facile…** | Mostra la versione del programma e i riferimenti di R.S.A. |

La finestra **Informazioni** riporta in alto la versione nella forma `FACILE
2026 B8` — l'anno e il numero di versione degli archivi — e sotto indirizzo,
telefono, sito e posta di R.S.A. È il primo dato che l'assistenza chiede quando
si telefona.

!!! tip "F1 apre la pagina giusta"

    Da dentro una maschera non serve passare da questo menu: ++f1++ apre
    direttamente la pagina del manuale che parla di quella maschera. **Argomenti
    della Guida** serve quando non si sa dove cercare.
