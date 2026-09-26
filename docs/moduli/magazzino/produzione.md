---
title: Produzione
description: La distinta base, il fabbisogno, l'avanzamento della produzione e il carico dei prodotti finiti.
modulo: Magazzino
maschera_id: IDD_MAG_PRODUZIONE
---

# Produzione

Chi trasforma la merce invece di rivenderla ha bisogno di dire **di cosa è
fatto** ogni prodotto, di sapere **cosa manca** per produrlo, e di caricare a
magazzino quello che esce dalla lavorazione scaricando quello che è entrato.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Magazzino ▸ Produzione ▸ *(una delle voci)*
    - **Scorciatoia:** ++f2++ salva o avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Distinta di Produzione** | La distinta base: dice di quali componenti è fatto un prodotto finito. |
| **Stampa Elenco Distinte di Produzione** | L'elenco delle distinte registrate. |
| **Fabbisogno di Produzione** | Data una quantità da produrre, calcola quanti componenti servono. |
| **Inizio Nuova Produzione** | Apre una **commessa di produzione**: impegna il materiale e resta aperta finché la lavorazione non è finita. |
| **Modifica Avanzamento Produzione** | Riapre una commessa già avviata per registrare gli scarichi man mano che si consumano i componenti, e per chiuderla. |
| **Aggiornamento Costi** | Rimette nelle distinte il costo dei componenti, preso dall'ultimo prezzo d'acquisto di ciascuno. |
| **Inserimento Carico da produzione** | Carica a magazzino il prodotto finito scaricando i componenti, tutto in un colpo solo: senza commessa. |
| **Modifica Carichi da Produzione** | Corregge un carico da produzione già fatto. |

## Prerequisiti

Prima di usare queste maschere occorre:

- avere in archivio sia i **componenti** sia i **prodotti finiti** come
  [articoli](../anagrafiche/anagrafica-articoli.md);
- avere le [causali di magazzino](causali-magazzino.md) della produzione, e
  averle indicate nei
  [parametri di magazzino della ditta](../anagrafiche/ditte.md): **Carico da
  Produzione**, **Scarico da Produzione**, **Scarico Sfrido di Produzione**,
  **Impegno di Produzione** e **Avvio Produzione**. Se ne manca una, la
  maschera lo dice e non si apre: *Inserimento Carico da produzione* ne vuole
  le prime tre, *Inizio Nuova Produzione* tutte e cinque;
- avere registrato le **distinte di produzione**: senza quelle il fabbisogno e
  il carico non hanno da cosa partire.

## La maschera

![Produzione](../../assets/img/magazzino/produzione.png)

Le voci del menu aprono maschere diverse fra loro.

**Distinta di Produzione** è una sola schermata: in alto l'articolo finito e la
quantità che la distinta descrive, sotto l'elenco dei componenti con quantità,
sfrido e costo, e in fondo a destra il **totale**, che è il costo del prodotto.

**Fabbisogno di Produzione** ha **due griglie**. In quella in alto si scrive
quanto si vuole produrre, articolo per articolo; quella in basso è il risultato:
i componenti che servono, con quello che c'è in magazzino e quello che manca.

**Inizio Nuova Produzione** apre la commessa: in alto i dati del lavoro — numero,
date, quantità, deposito, articolo da produrre — e sotto i movimenti di magazzino
che la commessa ha generato, ciascuno con la sua causale. Il **Costo Totale** in
alto si aggiorna man mano.

**Inserimento Carico da produzione** è la strada breve: articolo, quantità, data,
ed è il programma a comporre la griglia dei componenti dalla distinta.

## Campi

### Distinta di Produzione

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice Articolo** | ● | Il prodotto finito di cui si sta scrivendo la distinta. | codice |
| **Q.tà Prodotta** | ● | A quante unità di prodotto finito si riferiscono le quantità dei componenti. Con `100` si scrive la distinta di un lotto da cento pezzi. Deve essere maggiore di zero. | numero |

Nella griglia, una riga per componente:

| Colonna | Descrizione |
|---|---|
| **Codice**, **Descrizione** | Il componente. |
| **Cod. Art. Fornitore** | Il codice con cui lo chiama il fornitore. |
| **Mis.** | L'unità di misura del componente. |
| **Quantità** | Quanto ne serve per la quantità prodotta indicata sopra. |
| **Sfrido** | Quanto se ne perde nella lavorazione, in più rispetto alla quantità. Viene scaricato anche lui. |
| **Costo Unitario** | Il costo del componente. Lo si può scrivere a mano oppure farlo riempire da **F5 - Agg. Costi**. |

Il **TOTALE** in fondo è la somma di quantità per costo: il costo del prodotto
finito secondo questa distinta.

### Fabbisogno di Produzione

Nella griglia in alto si compila una sola colonna:

| Colonna | Descrizione |
|---|---|
| **Quantità** | Quanti pezzi di quel prodotto finito si vogliono produrre. Gli altri campi — codice, descrizione, misura — sono già lì, uno per ogni articolo che ha una distinta. |

La griglia in basso è il risultato del calcolo e non si tocca:

| Colonna | Descrizione |
|---|---|
| **Codice**, **Descrizione**, **Mis.** | Il componente. |
| **Quantità** | Quanto ne serve in tutto. |
| **Sfrido** | Lo sfrido che ne deriva. |
| **Esistenza** | Quanto ce n'è nel deposito. |
| **Fabbisogno** | **Quantità + Sfrido − Esistenza**: quanto manca. Se l'esistenza è negativa viene contata come zero. |
| **Livello** | A che profondità della distinta sta il componente: `0` è un componente diretto del finito, `1` un componente di un semilavorato, e così via. |

### Inizio Nuova Produzione

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice** | ● | Il numero della commessa. Proposto dal programma. | numero |
| **Data** | ● | La data di avvio. Proposta a oggi. | data |
| **Descrizione** | ● | Il nome della commessa. | testo |
| **Data Consegna** | | Quando il finito deve essere pronto. | data |
| **Quantità** | ● | Quanti pezzi si producono. Cambiandola, le quantità dei componenti si rifanno in proporzione. | numero |
| **Fine Produzione** | | La data di chiusura. La scrive il programma quando si preme **Fine**: finché è vuota la commessa è aperta. | — |
| **Costo Totale** | | La somma dei costi dei movimenti della commessa, esclusi l'avvio e il carico del finito. Non modificabile. | — |
| **Deposito** | ● | Il deposito su cui si lavora. | codice |
| **Sezione** | ● | La sezione del deposito. | codice |
| **Codice Articolo** | ● | Il prodotto finito da produrre. Deve avere una distinta, altrimenti la griglia resta vuota e il salvataggio non passa. | codice |

Nella griglia, prima del salvataggio, ci sono i componenti presi dalla distinta;
dopo, i movimenti di magazzino veri della commessa, con data, causale, anno e
numero di movimento. I componenti che hanno **a loro volta una distinta** sono
scritti in **grassetto**.

### Scarico Articolo Produzione

La finestra che si apre con **Aggiungi** su una commessa:

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Deposito** | ● | Da dove esce il materiale. | codice |
| **Codice Articolo** | ● | Il componente consumato. | codice |
| **Data** | ● | Quando. | data |
| **Quantità** | ● | Quanto. Con la gestione matricole attiva non sono ammessi decimali. | numero |
| **Lotto** | | Il lotto da cui si preleva, se l'articolo è a lotti. Un lotto chiuso non è utilizzabile. | codice |
| **Causale** | ● | *Scarico da Produzione* o *Scarico Sfrido di Produzione*. | due voci |

### Carico da Produzione

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data** | ● | La data dei movimenti. | data |
| **Codice Articolo** | ● | Il prodotto finito. Deve avere una distinta. | codice |
| **Quantità** | ● | Quanti pezzi si sono prodotti. Diversa da zero. | numero |
| **Lotto** | | Il lotto del finito, obbligatorio se l'articolo è a lotti. Se non esiste, il programma propone di crearlo. | codice |
| **Scadenza** | | La scadenza del lotto. | data |

La griglia sotto, intitolata *Articoli Componenti per Quantità Unitaria di
Prodotto*, si riempie da sola dalla distinta: accanto a **Q.ta** e **Sfrido**
unitari ci sono **Q.ta Mov** e **Sfrido Mov.**, cioè quello che verrà
effettivamente scaricato, con lotto, SSCC, GTIN e scadenza del componente
prelevato.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** o **F2 - OK** | ++f2++ | Registra, oppure avvia l'elaborazione. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |

Oltre a questi, ogni maschera ha i suoi.

**Distinta di Produzione**

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra la distinta. |
| **F5 - Agg. Costi** | ++f5++ | Riempie la colonna **Costo Unitario** di questa distinta con l'ultimo prezzo d'acquisto di ciascun componente. |
| **F6 - Elimina** | ++f6++ | Cancella la distinta. |
| **F7 - Stampa** | ++f7++ | Stampa la distinta. Chiede prima se stampare anche i costi. |
| **F8 - Duplica** | ++f8++ | Copia la distinta su un altro articolo, che si sceglie dall'elenco. |

**Fabbisogno di Produzione**

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F5 - Ordini** | ++f5++ | Riempie le quantità da produrre con quello che risulta ancora da consegnare dagli [ordini clienti](../vendite/ordini-clienti.md) di un periodo, che viene chiesto prima. Le quantità si **sommano** a quelle già scritte. |
| **F6 - Pulisci** | ++f6++ | Azzera tutte le quantità della griglia in alto, previa conferma. |
| **F2 - Stampa** | ++f2++ | Fa il calcolo e stampa il fabbisogno. |

**Inizio Nuova Produzione** e **Modifica Avanzamento**

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **Nuova** | | Comincia un'altra commessa. C'è solo entrando da *Inizio Nuova Produzione*. |
| **Aggiungi** | | Registra il consumo di un componente: apre *Scarico Articolo Produzione*. |
| **Modifica** | | Riapre la riga su cui si è posizionati. |
| **F7 - Stampa** | ++f7++ | Stampa la commessa con il suo andamento. |
| **Fine** | | Chiude la commessa e carica a magazzino il prodotto finito. |

**Carico da Produzione**

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Esegue il carico del finito e lo scarico dei componenti. |
| **F5 - Stampa** | ++f5++ | Stampa il carico. |
| **F9 - Fabbisogno** | ++f9++ | Mostra, per l'articolo indicato, quanto c'è in magazzino dei suoi componenti. |

## Come si fa

### Preparare la distinta di un prodotto

1. Apri **Menu ▸ Magazzino ▸ Produzione ▸ Distinta di Produzione**.
2. Indica il prodotto finito e i componenti con le quantità.
3. Salva.

### Sapere cosa comprare per produrre

1. Apri **Menu ▸ Magazzino ▸ Produzione ▸ Fabbisogno di Produzione**.
2. Indica il prodotto e la quantità da produrre.
3. Il calcolo dice quanti componenti servono; confrontalo con le esistenze.

### Caricare il prodotto finito, senza seguire la lavorazione

1. Apri **Menu ▸ Magazzino ▸ Produzione ▸ Inserimento Carico da produzione**.
2. Indica il prodotto e la quantità prodotta.
3. Salva: il finito entra a magazzino e i componenti escono, secondo la
   distinta.

### Seguire una lavorazione dall'inizio alla fine

1. Apri **Menu ▸ Magazzino ▸ Produzione ▸ Inizio Nuova Produzione**.
2. Compila descrizione, date, quantità, deposito, sezione e articolo da
   produrre: la griglia si riempie dalla distinta.
3. Salva: il materiale risulta **impegnato**.
4. Man mano che la lavorazione va avanti, riapri la commessa da **Modifica
   Avanzamento Produzione** e registra con **Aggiungi** i componenti consumati
   e gli sfridi.
5. Quando è finita, premi **Fine**: il programma chiede la data e, se
   l'articolo è a lotti, lotto e scadenza, poi carica il prodotto finito e
   scrive la data in **Fine Produzione**.

### Aggiornare i costi dopo un rincaro

1. Registra i [carichi](carico-merci.md) con i prezzi nuovi.
2. Apri **Menu ▸ Magazzino ▸ Produzione ▸ Aggiornamento Costi**: il costo dei
   prodotti finiti si ricalcola dai componenti.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio. | Guarda dove si è posizionato il cursore. |
| *Codice Articolo in corpo di distinta uguale a codice Articolo Master.* | Fra i componenti c'è il prodotto finito stesso. | Togli quella riga: una distinta non può contenere sé stessa. |
| *Non ci sono righe valide* | La distinta non ha nessun componente con quantità o sfrido diversi da zero. | Compila almeno una riga. |
| *Ci sono articoli in cui è stato indicato il costo pari a Zero.* — *Continuare?* | Qualche componente non ha costo. | **Sì** salva lo stesso: il costo del finito sarà sottostimato. Con **F5 - Agg. Costi** si riempiono i costi mancanti. |
| *L'Articolo Selezionato contiene già una Distinta di Produzione!* | Duplicando, l'articolo di destinazione ha già una distinta. | Scegline un altro, o cancella prima la sua distinta. |
| *L'Articolo Selezionato possiede un componente che è l'Articolo stesso!* | Duplicando, l'articolo di destinazione compare fra i componenti della distinta che si sta copiando. | Scegline un altro. |
| *Nessuna quantità di prodotto inserita !* | Nel fabbisogno non è stata scritta nessuna quantità da produrre. | Compila la colonna **Quantità** della griglia in alto. |
| *Confermi l'azzeramento di tutte le quantità ?* | Hai premuto **F6 - Pulisci**. | **Sì** svuota la colonna. La risposta preimpostata è **No**. |
| *Confermi l' aggiornamento dei costi delle distinte di produzione ?* | Hai lanciato **Aggiornamento Costi** dal menu. | **Sì** riscrive il costo di **tutti** i componenti di **tutte** le distinte. La risposta preimpostata è **No**. |
| *Distinta di produzione non caricata per l'articolo indicato.* | Il carico da produzione è stato chiesto per un articolo senza distinta. | Scrivi prima la distinta. |
| *Cancellazioni non abilitate per l' utente !* | L'utente ha il **Blocco Cancellazioni Dati**. | Serve un utente abilitato, o va tolto il blocco da [Archivi ▸ Utenti](../anagrafiche/utenti.md). |
| *Procedendo con la cancellazione sarà eliminato l'intero andamento della produzione!* — *Vuoi Continuare?* | Hai chiesto di cancellare una commessa. | **Sì** cancella la commessa e tutti i suoi movimenti. La risposta preimpostata è **No**. |
| *Ci sono righe con impegno materiale per la produzione!* — *Vuoi rimuoverle?* | Si sta chiudendo una commessa che ha ancora righe di impegno non trasformate in scarico. | **Sì** le toglie e prosegue. **No** interrompe la chiusura. |
| *Ci sono righe con impegno materiale per la produzione fatte in anni diversi dal corrente!* | Come sopra, ma le righe di impegno sono di un esercizio precedente. | Vanno tolte dall'esercizio in cui sono nate: rientra in quell'anno e ripeti. |
| *Il lotto selezionato è stato chiuso e non può essere utilizzato!* | Il lotto indicato è chiuso. | Scegline un altro. |
| *Gestione Lotti attiva per l'articolo selezionato.* — *Vuoi Forzare ?* | Si sta movimentando senza indicare il lotto un articolo che li gestisce. | **Sì** procede senza lotto, e la tracciabilità di quel movimento si perde. La risposta preimpostata è **No**. |
| *Il Lotto imputato non esiste : vuoi crearlo?* / *Lotto Inesistente!* — *Vuoi Crearlo ?* | Chiudendo la produzione o salvando il carico è stato scritto un lotto nuovo. | **Sì** lo crea al volo. |
| *Articolo non abilitato alla gestione dei lotti!* — *Vuoi abilitarlo ?* | È stato indicato un lotto per un articolo che non li gestisce. | **Sì** attiva la gestione lotti sull'articolo, da qui in avanti. |
| *Non sono ammesse quantità con decimali nella gestione delle matricole!* | L'articolo è a matricola e la quantità ha decimali. | Metti una quantità intera. |
| *Vuoi stampare le etichette ?* | Il carico da produzione è andato a buon fine. | **Sì** stampa le etichette del prodotto finito. |

## Note

!!! warning "Il carico da produzione muove il magazzino due volte"

    Un carico da produzione **carica** il prodotto finito e **scarica** i
    componenti secondo la distinta. Se la distinta è sbagliata, si sbagliano
    entrambi i movimenti.

!!! note "La distinta è a un livello, il fabbisogno li esplode tutti"

    Una distinta elenca i componenti **diretti** del prodotto: un livello solo.
    Ma niente vieta che un componente abbia a sua volta una distinta, e così i
    livelli si formano lo stesso.

    Chi li legge è il **Fabbisogno di Produzione**: parte dal finito, scende nei
    semilavorati e va avanti fino a **dieci livelli** di profondità, segnando in
    quale livello sta ogni componente. Poi fa due cose importanti:

    - di un semilavorato non chiede tutto il fabbisogno teorico ma solo quello
      che manca davvero: se ce n'è già in magazzino, si scende a cercare i
      componenti solo della parte da produrre;
    - se lo stesso articolo compare in più rami, le quantità vengono **sommate
      in una riga sola**.

    Nella maschera **Inizio Nuova Produzione**, invece, i componenti restano
    quelli diretti: quelli che hanno una distinta propria sono scritti in
    **grassetto**, così si vede subito che dietro c'è dell'altro.

    L'unico anello vietato è quello su sé stessi: un articolo non può essere
    componente di sé stesso, e il programma lo rifiuta.

!!! note "Due strade per caricare il finito, non due passi"

    **Inserimento Carico da produzione** e **Inizio Nuova Produzione** non sono
    in sequenza: sono due modi alternativi di fare la stessa cosa.

    | | Carico da produzione | Inizio Nuova Produzione |
    |---|---|---|
    | Quando si usa | La lavorazione è già finita e si registra il risultato. | La lavorazione dura, e si vuole seguirla. |
    | Quanto dura | Un colpo solo: carico del finito e scarico dei componenti insieme. | Resta aperta finché non si preme **Fine**. |
    | Che cosa scrive | Solo i movimenti di carico e scarico. | Prima l'avvio e l'**impegno** del materiale, poi gli scarichi veri man mano, infine il carico del finito. |
    | Quantità dei componenti | Sempre quelle della distinta. | Quelle della distinta come proposta, ma si registra **quanto si è consumato davvero**, riga per riga. |
    | Causali necessarie | Tre. | Cinque. |
    | Costo del finito | Quello della distinta. | Quello che risulta dai consumi effettivi, nel campo **Costo Totale**. |

    Chi produce a lotti brevi e regolari usa il carico; chi ha commesse che
    durano, e vuole sapere quanto è costata ciascuna, usa la produzione.

!!! warning "«Aggiornamento Costi» non calcola il costo del finito"

    Non fa un ricalcolo a cascata: per **ogni componente di ogni distinta** va a
    prendere l'**ultimo prezzo d'acquisto** registrato sull'articolo e lo scrive
    nel costo di quella riga. Il costo del prodotto finito è semplicemente il
    totale che ne risulta — quantità per costo, riga per riga.

    Due conseguenze:

    - un componente che è a sua volta un semilavorato prende l'ultimo prezzo
      d'**acquisto**, non il costo della sua distinta. Se non lo si compra mai,
      quel costo resta a zero;
    - la voce di menu lavora su **tutte** le distinte in una volta. Per
      aggiornare una sola distinta si usa **F5 - Agg. Costi** dentro la
      maschera.

## Vedi anche

- [Carico merci](carico-merci.md)
- [Movimenti di magazzino](movimenti-magazzino.md)
- [Anagrafica articoli](../anagrafiche/anagrafica-articoli.md)
