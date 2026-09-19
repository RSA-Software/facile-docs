---
title: Primo accesso
description: Come avviare Facile la prima volta, effettuare il login e selezionare l'azienda di lavoro.
---

# Primo accesso

Questa pagina racconta che cosa succede dal momento in cui si fa doppio clic
sull'icona di Facile a quando si è davanti al menu, pronti a lavorare.

!!! info "In sintesi"

    - **Si apre:** all'avvio del programma, e da Menu ▸ Utility ▸ Seleziona Archivio
    - **Scorciatoia:** ++f2++ entra, ++esc++ chiude il programma
    - **Tentativi:** tre, poi Facile si chiude da solo

---

## Prima di cominciare

L'installazione la fa l'assistenza R.S.A.: sistema il programma, gli archivi e
— se si lavora in rete — il server dei dati. All'utente resta da avere:

- una [licenza](../moduli/utility/gestione-licenza.md) attiva;
- un [utente](../moduli/anagrafiche/utenti.md) con il suo nome e la sua
  password;
- almeno una [ditta](../moduli/anagrafiche/ditte.md) negli archivi.

## La finestra di accesso

All'avvio compare una finestra con la chiave, il nome del prodotto — *Facile*,
*Facile Light*, *Facile Hotel*, *Facile CRM* secondo la versione installata — e
i campi per entrare.

| Campo | Descrizione |
|---|---|
| **Server** | Il nome del server dei dati. In una installazione nuova è proposto `FAIRCOMS`. |
| **Host** | Il computer su cui il server gira: `LOCALHOST` se è lo stesso, altrimenti il nome o l'indirizzo di rete. |
| **Archivio** | La cartella degli archivi sul server. In una installazione nuova è proposta `ARCHIVI`. |
| **Utente** | Il nome con cui si è registrati in Facile — è la **UserID** della scheda utente, non la descrizione. |
| **Password** | La password dell'utente. |
| **Crea struttura directory** | Riservata all'installazione: crea le cartelle di lavoro. Su archivi SQL l'etichetta diventa **Crea/Aggiorna Database**. |

{: .campi }

!!! note "I primi tre campi non sempre si vedono"

    **Server**, **Host** e **Archivio** riguardano il collegamento al server dei
    dati. Quando Facile lavora su archivi locali, o quando il collegamento è già
    stato fatto, quei campi **spariscono** e restano solo **Utente** e
    **Password**: non è un malfunzionamento, è la stessa finestra che si
    presenta più corta.

    Per lo stesso motivo la finestra può comparire **due volte**: la prima per
    entrare nel server dei dati, la seconda — senza i tre campi in alto — per
    riconoscere l'utente fra quelli registrati in Facile. Se la seconda non
    compare, vuol dire che il nome e la password del server sono andati bene
    anche per il programma.

### Tasti

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Entra. |
| **Esci** | ++esc++ | Chiude il programma senza entrare. |
| Campo successivo | ++enter++ oppure ++down++ | Passa al campo seguente. |
| Campo precedente | ++up++ | Torna al campo precedente. |

### Che cosa Facile si ricorda

Server, host e archivio vengono **registrati al primo accesso riuscito** e
riproposti le volte successive: normalmente si digitano una sola volta, il
giorno dell'installazione.

Il nome utente e la password **non si ricordano**: vanno scritti ogni volta.

!!! warning "Tre tentativi e il programma si chiude"

    Se il nome utente non esiste Facile dice *Nome Utente non Valido.*; se la
    password non corrisponde, *Password non Valida.* Dopo il terzo tentativo
    andato male il programma **si chiude**: bisogna riaprirlo.

    Se invece premendo ++f2++ **si sente solo un segnale acustico** e non
    compare nessun messaggio, manca un campo obbligatorio — server, archivio o
    utente: il cursore si posiziona su quello da riempire.

!!! note "Chi ha dimenticato la password"

    Le password degli utenti si cambiano dalla scheda
    [Utenti](../moduli/anagrafiche/utenti.md), che però è accessibile solo a chi
    amministra il programma. Se la password persa è proprio quella
    dell'amministratore, l'unica strada è l'[assistenza
    R.S.A.](../moduli/utility/assistenza.md), che dispone di una propria chiave
    di servizio: non è una password impostabile dal programma e non viene
    comunicata.

!!! tip "Durante la prova la password si vede"

    Nei primi dieci giorni di una installazione dimostrativa la password è
    mostrata in chiaro invece che a pallini. È voluto — serve a non restare
    fuori mentre si sta provando il programma — e smette da sé quando
    l'installazione diventa definitiva.

## Scegliere la ditta

Entrati, Facile deve sapere **su quale azienda** si lavora.

- Se in archivio c'è **una ditta sola**, la prende e non chiede niente.
- Se ce n'è **più d'una**, apre l'elenco delle ditte: si sceglie con un doppio
  clic o con ++enter++.

Fatta la scelta, il nome della ditta e l'anno finiscono **nella barra del
titolo**, in alto:

```
FACILE - 00001  MARIO ROSSI S.R.L. - Anno : 2026
```

Con gli archivi SQL la scritta comincia con `FACILE SQL`. È il modo più rapido
per accorgersi di stare lavorando sulla ditta o sull'anno sbagliato.

Per cambiare ditta senza uscire dal programma: **Menu ▸ Utility ▸ Cambio
Ditta**. Due risposte possibili al posto dell'elenco:

| Messaggio | Che cosa vuol dire |
|---|---|
| *Una sola ditta e' presente in archivio!* | Non c'è niente fra cui scegliere. |
| *Cambio ditta non permesso!* | Facile è stato avviato su una ditta fissa (vedi sotto): per cambiarla si chiude e si riapre. |

Per cambiare **anno** si usa invece Menu ▸ Utility ▸
[Esercizi](../moduli/utility/esercizi-e-chiusure.md).

## Che cosa cambia da un utente all'altro

Facile non mostra a tutti lo stesso menu: quello che si vede dipende dai
permessi dell'[utente](../moduli/anagrafiche/utenti.md) con cui si è entrati.
Le voci non concesse **non compaiono affatto** — non sono spente, non ci sono —
e i menu che restano vuoti spariscono insieme alle loro voci.

Chi non è amministratore, in più:

- non vede **Utenti**, **Nuovo Esercizio** e le voci di Facile Cloud;
- non può **personalizzare le barre degli strumenti**.

Le barre degli strumenti sono **per utente**: ognuno se le dispone come vuole e
le ritrova al prossimo accesso, senza disturbare i colleghi.

## Avviare Facile in un modo particolare

Chi installa può creare collegamenti che avviano Facile già indirizzato, senza
domande. Si aggiungono al collegamento uno o più di questi parametri:

| Parametro | Effetto |
|---|---|
| `/ditta<numero>` | Apre direttamente quella ditta e vieta il cambio ditta. Esempio: `/ditta3`. |
| `/server<nome>` `/host<nome>` `/arc<nome>` | Server, computer e archivio, senza chiederli. |
| `/usr<nome>` `/pwd<password>` | Nome utente e password. |
| `/ini<percorso>` | Usa un file di impostazioni diverso da quello predefinito. |
| `/x<n>` `/y<n>` `/w<n>` `/h<n>` | Posizione e dimensioni della finestra all'apertura. |

!!! danger "La password nel collegamento è in chiaro"

    `/pwd` scrive la password **leggibile** nelle proprietà del collegamento:
    chiunque si sieda a quel computer può vederla con un clic destro. Si usa
    solo su postazioni dedicate e fisicamente sicure — una cassa, un terminale
    di magazzino — mai su un computer condiviso.

Esistono altri parametri, riservati a lavorazioni specifiche e a singole
installazioni: li imposta l'assistenza e non vanno aggiunti a mano.

## Su Terminal Server

Quando Facile gira in sessione remota (Terminal Server, desktop remoto) le
impostazioni e le cartelle di lavoro sono **per utente Windows**, non per
computer: ciascuno ha le sue e non le vede quelle degli altri. Non c'è niente
da impostare, succede da sé.
