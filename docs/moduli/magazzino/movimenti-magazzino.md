---
title: Movimenti di magazzino
description: La registrazione diretta dei movimenti di magazzino, quando la merce si muove senza un documento di vendita o un carico.
modulo: Magazzino
maschera_id: IDD_MAG_MOVIMENTI
---

# Movimenti di magazzino

Non tutto quello che muove il magazzino passa da un documento: le rettifiche di
inventario, i trasferimenti fra depositi, i cali, gli autoconsumi si registrano
direttamente qui.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Magazzino ▸ Inserimento Movimenti *(oppure* Modifica Movimenti*)*
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca
    - **Permessi richiesti:** nessun profilo predefinito; **Inserimento Movimenti** e **Modifica Movimenti** si abilitano separatamente per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

È il movimento di magazzino nella sua forma pura: una causale, un deposito, un
articolo, una quantità. La [causale](causali-magazzino.md) decide se la merce
entra o esce e quali contatori dell'articolo si muovono.

Serve per le rettifiche dopo l'inventario, per spostare merce da un
[deposito](depositi.md) all'altro, per registrare rotture e cali, e per tutto
quello che non nasce da una vendita o da un acquisto.

## Prerequisiti

Prima di usare questa maschera occorre:

- avere le [causali di magazzino](causali-magazzino.md) impostate: sono loro a
  governare il movimento;
- avere i [depositi](depositi.md) e gli
  [articoli](../anagrafiche/anagrafica-articoli.md).

## La maschera

![Movimenti di magazzino](../../assets/img/magazzino/movimenti-magazzino.png)

In alto la testata del movimento, sotto le righe della merce.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Anno-Numero** | | Identificativo del movimento. Lo assegna il programma. | numero |
| **Data** | ● | Data del movimento. | data |
| **Num. e Data Doc.** | | Gli estremi del documento che giustifica il movimento. | numero e data |
| **Numero Fattura**, **Data Fattura** | | Gli estremi della fattura, quando c'è. | numero e data |
| **Gruppo** | | Il gruppo del soggetto. | codice |
| **Causale** | ● | La [causale di magazzino](causali-magazzino.md): decide entrata o uscita e i contatori aggiornati. | codice |
| **Cliente/Fornit.** | | Il soggetto del movimento. L'etichetta cambia secondo la causale. | codice |
| **Destinazione** | | La destinazione merce. | codice |
| **Agente** | | L'[agente](../anagrafiche/anagrafica-agenti.md) del movimento. | codice |
| **Deposito** | ● | Il [deposito](depositi.md) movimentato. | codice |
| **Operatore** | | Chi ha registrato il movimento. | codice |
| **Commessa** | | La [commessa](../contabilita/commesse.md) a cui imputare. | codice |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra il movimento e aggiorna le esistenze. |
| **F3 - Prec.**, **F4 - Succ.** | ++f3++, ++f4++ | Passano al movimento precedente o successivo. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco dei movimenti. |
| **F6 - Elimina** | ++f6++ | Cancella il movimento, previa conferma. |
| **F7 - Stampa** | ++f7++ | Stampa il movimento. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Trasferire merce fra due depositi

1. Apri **Menu ▸ Magazzino ▸ Inserimento Movimenti**.
2. Indica la **Causale** di scarico per trasferimento e il **Deposito** di
   partenza.
3. Inserisci le righe della merce e salva.
4. Ripeti con la causale di carico e il deposito di arrivo.

### Registrare una rottura

1. Apri **Inserimento Movimenti**.
2. Indica la **Causale** che scarica per rottura e il **Deposito**.
3. Inserisci l'articolo e la quantità, poi salva.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Se il movimento è di tipo SCARICO impostare ESISTENZA -* | La causale scelta è di scarico ma non toglie dall'esistenza. | Correggi la [causale di magazzino](causali-magazzino.md), o scegline un'altra. |
| *Se il movimento è di tipo CARICO impostare ESISTENZA +* | La causale scelta è di carico ma non aggiunge all'esistenza. | Come sopra. |
| *Data fuori dall'Esercizio Corrente ! Vuoi Continuare ?* | La data del movimento non cade nell'anno di lavoro. | **No** per correggerla. **Sì** registra lo stesso: il movimento finisce in un altro esercizio. |
| *Commessa obbligatoria!* | La causale pretende la commessa e il campo è vuoto. | Indica la commessa. |
| *Centro Cost/Ricavo obbligatorio!* | La causale pretende il centro di costo e il campo è vuoto. | Indica il centro. |
| *Non sono ammesse quantità con decimali nella gestione delle matricole!* | L'articolo è gestito a matricola e hai scritto una quantità con la virgola. | Le matricole si contano a pezzi interi. |
| *Impossibile Continuare ! Il movimento contiene articoli fiscali.* | Si sta salvando o cancellando un movimento che tocca articoli soggetti a registro fiscale. | Quei movimenti non si toccano da qui: si correggono dalla gestione dei registri fiscali. |

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! warning "La causale decide tutto"

    Una causale sbagliata muove i contatori nel verso sbagliato, e in Facile
    **non c'è un controllo di coerenza**: una causale di carico può sottrarre
    dall'esistenza, se è stata impostata così. Prima di usare una causale nuova,
    controlla come è fatta.

!!! info "Sì: un movimento solo può muovere due depositi"

    È il caso del **trasferimento fra depositi**, e si imposta sulla
    causale: la [causale di magazzino](causali-magazzino.md) ha un
    **deposito** e una **causale di contropartita**. Scegliendola, la
    maschera compila da sé i due campi **Al Deposito** e **Causale 2°
    Dep.**, che restano modificabili.

    Salvando, il programma scrive **due movimenti**: quello che hai davanti
    e il suo gemello sull'altro deposito, con la causale di contropartita e
    la nota *PROVIENE DAL DEPOSITO N*.

    Il gemello nasce **solo al primo salvataggio**, e solo se il secondo
    deposito esiste ed è diverso dal primo. Modificando dopo il movimento,
    il gemello **non viene aggiornato**: va corretto a mano.

!!! note "Il movimento non tocca la contabilità"

    Registrando un movimento non nasce nessuna scrittura di prima nota: il
    magazzino e la contabilità restano due cose separate.

    Se il movimento ha un riflesso contabile — un omaggio, un ammanco, un
    autoconsumo — la scrittura va fatta a parte in
    [prima nota](../contabilita/registrazione-prima-nota.md).

## Vedi anche

- [Causali magazzino](causali-magazzino.md)
- [Depositi](depositi.md)
- [Carico merci](carico-merci.md)
- [Stampe dei movimenti di magazzino](stampe-movimenti-magazzino.md)
