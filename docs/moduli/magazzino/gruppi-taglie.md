---
title: Gruppi taglie
description: "I gruppi di taglie di Facile: fino a cinquanta taglie per gruppo, con sigla, riferimento e nome per il sito."
modulo: Archivi ▸ Magazzino
maschera_id: IDD_TBM_TAGLIE
---

# Gruppi taglie

Da questa maschera si definiscono i gruppi di taglie: gli insiemi di misure con
cui si articola un modello. Ogni gruppo contiene fino a cinquanta taglie.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Archivi ▸ Magazzino ▸ Gruppi Taglie ▸ Inserimento *(oppure* Modifica*)*
    - **Scorciatoia:** nessuna; la maschera si apre dal menu
    - **Permessi richiesti:** nessun profilo predefinito; **Inserimento** e **Modifica** si abilitano separatamente per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Nel commercio di abbigliamento e calzature lo stesso articolo esiste in più
taglie, e la giacenza va tenuta taglia per taglia. Il gruppo taglie è l'elenco
delle misure che quell'articolo può avere.

Esempio: un gruppo *SCARPE UOMO* con le taglie da 39 a 46, e un gruppo
*MAGLIERIA* con S, M, L, XL. In anagrafica articoli si assegna il gruppo giusto
e da lì il magazzino tiene una giacenza per ciascuna taglia.

!!! note "Nota"

    Nella versione Taglie e Colori il gruppo taglie si assegna dal campo della
    scheda *Generale* dell'articolo che in quella versione si chiama
    **Gru. Taglie**.

## Prerequisiti

*Nessuno.*

## La maschera

![Maschera Gruppi taglie](../../assets/img/magazzino/gruppi-taglie.png)

È una maschera a finestra unica, senza schede: in alto la **barra dei
comandi**, poi codice e descrizione del gruppo, e sotto una griglia di
cinquanta righe numerate da **01** a **50**, disposte su cinque colonne da
dieci. Ogni riga ha tre caselle.

### L'elenco dei gruppi taglie

![Elenco dei gruppi taglie](../../assets/img/magazzino/gruppi-taglie-elenco.png)

Premendo **F5 - Cerca** si apre la finestra **Cerca Gruppi Taglie**: l'elenco
dei gruppi con le colonne **Codice** e **Descrizione**. Sotto l'elenco, nelle
fasce **Misure** e **Riferimenti**, compaiono le taglie del gruppo su cui ti
trovi, nell'ordine delle righe: servono a riconoscerlo, non si modificano da
qui.

Dalla barra dei comandi: **F2 - OK** sceglie il gruppo selezionato (vale anche
il doppio clic), **F3 - Nuovo** apre la maschera per aggiungere un gruppo,
**F4 - Modifica** apre il gruppo selezionato per correggerlo.

In alto ci sono due campi di ricerca:

- **Codice** — scrivi il codice e passa al campo successivo: l'elenco si
  posiziona su quel gruppo, o sul primo che lo segue;
- **Descrizione** — scrivi l'inizio della descrizione: l'elenco mostra solo i
  gruppi che cominciano così. Svuota il campo per tornare all'elenco completo.

### La finestra Seleziona Taglia

![Finestra Seleziona Taglia](../../assets/img/magazzino/gruppi-taglie-scelta.png)

Nelle maschere che chiedono una taglia — le righe dei documenti di vendita e
del carico merci, i movimenti di magazzino, l'inventario, i codici a barre, i
frontalini e le etichette — un doppio clic sulla casella della taglia apre la
finestra **Seleziona Taglia**. In alto riporta codice e descrizione del gruppo
taglie dell'articolo; sotto, una riga per ogni taglia del gruppo con le colonne
**Misura**, **Riferimento** e **Web**. Le righe lasciate vuote nel gruppo non
compaiono. Il modo di usarla è descritto in
[Scegliere una taglia](#scegliere-una-taglia).

### Il riepilogo taglie e colori

![Riepilogo taglie e colori](../../assets/img/magazzino/gruppi-taglie-riepilogo.png)

Quando vendi al banco un articolo gestito a taglie e colori senza indicare
taglia e colore, si apre la finestra **Seleziona Taglia e Colore**. Il suo
pulsante **F3 - Assortimento** apre il **Riepilogo Taglie e Colori** dell'articolo:
una tabella con un colore per riga e una taglia per colonna, che mostra la
giacenza attuale nel deposito della vendita.

- In testa a ogni colonna c'è la taglia, con la misura e sotto il riferimento.
- La colonna **Totale** somma la riga; l'ultima riga, **T O T A L I**, somma le
  colonne.
- Le righe del gruppo lasciate vuote, senza misura né riferimento, non
  compaiono come colonne; nelle righe dei colori le quantità a zero non si
  vedono.

Un doppio clic su una cella sceglie quel colore e quella taglia e li riporta
nella vendita. ++esc++ o **Esci** chiudono la finestra senza scegliere nulla.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| Codice | ● | Identificativo del gruppo. In modifica non è modificabile. | Numero |
| Descrizione | ● | Nome del gruppo, come compare in anagrafica articoli. | Fino a 30 caratteri |
| Mis. | | La taglia come si scrive: *39*, *M*, *XL*. È quella che compare sui documenti e sulle etichette. | Testo breve |
| Rifer. | | Riferimento interno della taglia, per allinearla a una codifica propria o del fornitore. | Testo breve |
| Web | | La taglia come deve comparire sul sito. | Testo breve |

Si compilano solo le righe che servono: un gruppo di otto taglie occupa le
prime otto righe e lascia vuote le altre quarantadue.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra il gruppo con tutte le sue taglie. |
| **F3 - Prec.** | ++f3++ | Passa al gruppo precedente. |
| **F4 - Succ.** | ++f4++ | Passa al gruppo successivo. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco dei gruppi taglie. |
| **F6 - Elimina** | ++f6++ | Cancella il gruppo, previa conferma. |
| **Ricarica** | | Rilegge il gruppo dall'archivio, abbandonando le modifiche non salvate. |

Valgono inoltre:

| Comando | Scorciatoia | Effetto |
|---|---|---|
| Consultazione | ++f11++ | Apre la finestra **Consultazione**. |
| Calcolatrice | ++f12++ | Apre la calcolatrice. |
| Campo successivo | ++enter++ | Sposta il cursore sulla casella seguente. |
| Chiusura | ++esc++ | Chiude la maschera. |

## Come si fa

### Creare un gruppo di taglie

1. Apri **Menu ▸ Archivi ▸ Magazzino ▸ Gruppi Taglie ▸ Inserimento**.
2. Digita il **Codice** e la **Descrizione** del gruppo.
3. Nella prima riga scrivi la prima taglia in **Mis.**, e prosegui riga per
   riga nell'ordine in cui vuoi vederle.
4. Compila **Web** se le taglie devono comparire sul sito con una scrittura
   diversa.
5. Premi **F2 - Salva**.

### Scegliere una taglia

1. Nella riga del documento, del carico o del movimento fai doppio clic sulla
   casella della taglia: si apre la finestra **Seleziona Taglia**, già
   posizionata sulla taglia della riga se ne ha una.
2. Spostati sulla taglia che ti serve con le frecce.
3. Premi **F2 - OK** o ++enter++, oppure fai doppio clic sulla riga: la
   finestra si chiude e la taglia passa nella riga di partenza.

Con ++esc++ o **Esci** la finestra si chiude e la riga resta com'era.

### Assegnare il gruppo a un articolo

1. Apri l'[anagrafica dell'articolo](../anagrafiche/anagrafica-articoli.md).
2. Nella scheda *Generale* indica il gruppo taglie.
3. Premi **F2 - Salva**. Da quel momento la giacenza dell'articolo si tiene
   taglia per taglia.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca il **Codice** o la **Descrizione**. | Guarda dove si è posizionato il cursore: è il campo da compilare. |
| *In archivio è già presente un record con lo stesso codice.* | Il codice digitato è già di un altro gruppo. | Cambia codice. |
| *Confermi la Cancellazione....* | Conferma richiesta da **F6 - Elimina**. | Rispondi **Sì** per eliminare il gruppo. |
| *Non è possibile eliminare il record poiché utilizzato in alcuni record del database.* | Il gruppo è assegnato a degli articoli o ha delle giacenze per taglia. | Non è eliminabile: lascialo in archivio. |
| *Il record è stato modificato da un altro nodo della rete.* | Un altro utente ha salvato lo stesso gruppo mentre lo modificavi. | Premi **Ricarica**, verifica cosa è cambiato e rifai le tue modifiche. |
| *Il record è stato cancellato da un altro nodo della rete.* | Un altro utente ha eliminato il gruppo mentre lo modificavi. | La maschera si chiude: non c'è più nulla da salvare. |

## Note

!!! warning "Attenzione"

    **L'ordine delle righe conta**: la giacenza di ogni taglia è legata alla
    posizione nella griglia, non a quello che c'è scritto. Cambiare una taglia
    su un gruppo già in uso sposta la giacenza da una misura all'altra.
    Su un gruppo già usato si aggiungono taglie in fondo; non si riordinano
    quelle esistenti.

    ++esc++ chiude la maschera senza chiedere conferma e senza salvare: le
    modifiche fatte dopo l'ultimo **F2 - Salva** vanno perse.

!!! info "Perché conta la posizione e non il testo"

    Tutto quello che il programma tiene per taglia — le **giacenze**, i
    **codici a barre**, i **prezzi per taglia**, gli allegati — è legato al
    **numero della riga** nel gruppo, non alla misura scritta.

    La terza riga del gruppo è «la taglia numero 3»: se domani scrivi un
    altro valore su quella riga, tutta la giacenza che era della vecchia
    misura diventa della nuova, senza che nessuno avverta.

!!! note "A che cosa serve Rifer."

    È un **secondo modo di chiamare la stessa taglia**, più corto o più
    comodo da digitare.

    Lo usa il programma quando bisogna **indicare una taglia scrivendola**:
    nell'inventario e nella gestione dei codici a barre si batte il
    riferimento e il programma risale alla taglia. Nelle stampe dei listini
    per taglia compare accanto alla misura.

    Non è legato a un fornitore: è un codice tuo, e conviene tenerlo breve
    e senza spazi, perché si digita spesso da terminale.

## Vedi anche

- [Anagrafica articoli](../anagrafiche/anagrafica-articoli.md)
- [Tabelle di classificazione](tabelle-di-classificazione.md)
