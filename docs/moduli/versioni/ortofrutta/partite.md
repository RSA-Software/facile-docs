---
title: Partite
description: Scheda e stampa del riepilogo di una partita, riepilogo di più partite, fogli di intestazione e passaggio delle partite aperte da un anno all'altro.
modulo: Ortofrutta
maschera_id: IDD_ORT_RIEPILOGO_PARTITA
---

# Partite

Cinque voci di menu che girano tutte intorno alla stessa cosa: sapere **come sta
andando una partita** e che cosa si deve al produttore.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Ortofrutta ▸ Scheda Riepilogo Partita *(e le voci seguenti)*
    - **Scorciatoia:** ++f2++ totali, ++f3++ stampa, ++f5++ email, ++esc++ esce
    - **Prerequisiti:** la partita deve esistere come [carico merci](../../magazzino/carico-merci.md)

---

## Scheda Riepilogo Partita

È la finestra centrale del modulo: una partita alla volta, riga per riga.

### I campi in alto

| Campo | Descrizione |
|---|---|
| **Fornitore** | Il produttore che ha conferito. Si sceglie col codice o con ++f10++. |
| **Partita** | Il numero della partita, cioè il numero del documento di carico. |
| **Movimenti** | `DEL GIORNO` mostra i movimenti della sola data indicata; `FINO AL GIORNO` tutto il venduto fino a quella data compresa. |
| **Data** | La data a cui riferire il conteggio. |
| **Formato** | `SINTETICO` una riga per articolo, `DETTAGLIATO` anche le singole vendite. |
| **Tipo Doc.** | Quali documenti considerare: `TUTTI`, `FATTURE`, `ORDINI` o `ALTRI`. |

{: .campi }

!!! tip "I tasti + e − cambiano il formato"

    Il **+** del tastierino passa a `DETTAGLIATO`, il **−** torna a `SINTETICO`:
    è più rapido che andare sulla casella.

### La griglia

Ogni riga è un articolo della partita, e racconta l'intero giro:

| Colonna | Che cosa dice |
|---|---|
| **Deposito**, **Codice**, **Descrizione**, **Misura** | Di quale articolo si tratta. |
| **Colli** e **Q.tà caricata**, **Prezzo di carico** | Quanto è entrato e a che valore. |
| **Imballaggio** | L'imballo con cui è arrivato. |
| **Giacenza** | Quanto ne resta. |
| **Colli** e **Q.tà venduta**, **Prezzo di vendita**, **Totale** | Quanto è uscito e quanto ha reso. |
| **Prezzo fornitore**, **Totale fornitore** | Quanto di quel ricavo spetta al produttore. |

La differenza fra **Totale** e **Totale fornitore** è quello che resta al
grossista.

Su una riga, ++enter++ o un doppio clic aprono il **dettaglio**: le singole
vendite che compongono quel totale, con documento e cliente.

### I comandi

| Pulsante | Tasto | Effetto |
|---|---|---|
| **F2 - Totali** | ++f2++ | Apre il conto della partita — spese, acconti e netto al produttore. Vedi sotto. |
| **F3 - Stampa** | ++f3++ | Stampa il riepilogo come è a video. |
| **F4 - Confronto** | ++f4++ | Produce la stampa **Situazione Partita**: le stesse righe della griglia, il caricato a fronte del venduto e della quota del produttore. |
| **F5 - Email** | ++f5++ | Fa la stessa stampa e **la spedisce per posta**, tipicamente al produttore. |
| **F6 - Partite Generate** | ++f6++ | Le partite nate da questa per lavorazione: una partita selezionata o confezionata ne genera altre. |
| **F7 - Partita Originale** | ++f7++ | Il percorso inverso: da dove viene questa partita. |

!!! note "Per l'email servono due impostazioni"

    Il mittente qui **non** è quello dell'utente ma quello della postazione. Se
    manca, Facile dice *Mittente Email non impostato !*; se non è configurato il
    server di posta della ditta, *SMTP Server non impostato !*. Si sistemano
    nelle [impostazioni della postazione](../../utility/impostazioni-postazione.md)
    e nella scheda della [ditta](../../anagrafiche/ditte.md).

### I totali della partita (F2)

È il conto della resa del conferimento.

A sinistra le spese da trattenere:

| Campo | Descrizione |
|---|---|
| **Trasporto Acquisto** | Il trasporto per portare la merce dal produttore. |
| **Trasporto Vendita** | Il trasporto per consegnarla ai clienti. |
| **Frigo - Ritorni** | Cella frigorifera e merce tornata indietro. |
| **Intermediari** | Quanto è andato ai mediatori. |
| **Provvigione** | La provvigione del grossista. |
| **Spese Imballaggi** | Il costo degli imballi. |
| **Spese Manodopera** | La manodopera di selezione e confezionamento. |

{: .campi }

Al centro **cinque acconti**, ciascuno con il suo importo e la sua data: gli
anticipi già dati al produttore mentre la partita si vendeva.

A destra il conto:

| Voce | Che cos'è |
|---|---|
| **Ricavo Merce** | Quanto ha reso il venduto. |
| **Note Credito** | Quanto è stato stornato. |
| **Costo Merce** | Il valore della merce conferita. |
| **Spese** | La somma delle spese di sinistra. |
| **Acconti** | La somma degli acconti. |
| **Ricavo Netto** | **Quello che resta da pagare al produttore.** |

In fondo **Fine Vendita**, la data in cui la partita si è esaurita, e la casella
**Controllo Effettuato**, da spuntare quando il conto è stato verificato.

## Stampa Riepilogo Partita

È **la stessa finestra**, aperta in sola stampa: gli stessi campi e la stessa
griglia, ma l'unico comando è **F2 - Stampa**. Si usa quando si vuole il foglio
e basta, senza rischiare di toccare i totali.

## Riepilogo Partite

Guarda **più partite insieme** invece di una sola.

| Campo | Descrizione |
|---|---|
| **Dal**, **Al** | Il periodo dei conferimenti. |
| **Da Partita**, **A Partita** | L'intervallo dei numeri. |
| **Fornitori** | Uno o più produttori; il pulsante **…** apre l'elenco da cui spuntarli. |
| **Formato** | Quale stampa produrre (vedi sotto). |

{: .campi }

| Formato | Che cosa dà |
|---|---|
| `STANDARD` | Il riepilogo di tutte le partite del periodo. |
| `STANDARD - PARTITE APERTE` | Lo stesso, ma solo per le partite non ancora chiuse. |
| `UTILE DA CONFERIMENTO DETTAGLIATO` | Quanto ha reso ogni conferimento, riga per riga. |
| `UTILE DA CONFERIMENTO RIEPILOGO` | Lo stesso, totalizzato. |
| `PARTITE APERTE` | L'elenco di quelle ancora da finire. |
| `PARTITE CHIUSE` | L'elenco di quelle esaurite. |

## Fogli Intestazione

Stampa i **fogli su cui si segna la vendita a mano** durante la giornata di
mercato, già intestati con i dati della partita.

| Campo | Obbl. | Descrizione |
|---|:---:|---|
| **Partita** | | Il numero della partita da intestare. |
| **Numero Copie** | ● | Quanti fogli stampare. |

{: .campi }

!!! note "Partita a zero: fogli non intestati"

    Lasciando **Partita** vuota il programma non stampa i fogli di una partita
    in particolare: prende la prima partita dell'anno solo per avere un
    riferimento e avverte il modello di stampa che non è una partita vera. Che
    cosa compaia sul foglio in quel caso lo decide il modello.

    Con **Numero Copie** a zero non succede niente: solo un segnale acustico.

## Esportazione e Importazione Partite Aperte

Servono a **portare nel nuovo esercizio la merce ancora invenduta**.

A fine anno, dall'esercizio vecchio, **Esportazione Partite Aperte** chiede
*Confermi l' esportazione delle partite aperte ?* e scrive il file
`partiteaperte.txt` nella cartella **out** del programma. Finito, dice
*Esportazione conclusa regolarmente !*.

Nel nuovo esercizio si mette quel file nella cartella **in** e si lancia
**Importazione Partite Aperte**, che chiede *Vuoi importare le partite aperte ?*
e ricrea le partite, ciascuna con il ricordo di quella da cui viene.

!!! warning "Si importa solo l'anno immediatamente precedente"

    Il file porta scritto l'anno da cui è uscito, e l'importazione lo accetta
    **solo se è l'anno prima di quello su cui si sta lavorando**. Se non lo è,
    Facile risponde *Anno File di Interscambio non Valido!* e non importa
    niente: non si può saltare un esercizio.

**I messaggi**

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impossibile aprire il file !* | La cartella **out** (o **in**) non esiste, o il file è aperto altrove. | Controllare la cartella e chiudere chi tiene aperto il file. |
| *File di Interscambio non Valido!* | Il file non è un file di interscambio di Facile. | Si è preso il file sbagliato. |
| *Versione File di Interscambio non Valida!* | Il file viene da una versione diversa del programma. | Esportare di nuovo con la versione in uso. |
| *Anno File di Interscambio non Valido!* | L'anno del file non è quello precedente. | Vedi l'avviso qui sopra. |
| *Formato Record Sconosciuto!* | Il file è danneggiato. | Rifare l'esportazione. |

## Vedi anche

- [Chiusura della vendita](chiusura-vendita.md)
- [Carico Merci](../../magazzino/carico-merci.md)
