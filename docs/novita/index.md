---
title: Novità
description: "Cosa cambia in Facile versione per versione: funzioni nuove, miglioramenti e correzioni dalla 2026 B07 in avanti."
---

# Novità

--8<-- "includes/versione-facile.md"

Qui trovi, versione per versione, quello che cambia per chi usa Facile: le
funzioni nuove, i miglioramenti e le correzioni. Le voci che valgono solo per
una versione specifica del programma lo dicono in apertura, per esempio
**Solo Ortofrutta.** I nomi delle versioni sono spiegati nelle
[convenzioni](../introduzione/convenzioni.md).

Non sono elencate le modifiche interne, che non cambiano nulla a video, e
quelle dei prodotti che hanno un manuale proprio, come Hotel e RistoFacile.

## Versione 2026 B08.01

<!-- DA VERIFICARE: data di distribuzione della B08.01 -->

### Nuove funzioni

**[Scontrini delle bilance Zenith in cassa](../moduli/vendite/vendita-al-banco.md#passare-in-cassa-lo-scontrino-di-una-bilancia).**
Sul **Pos Touchscreen** si legge il codice a barre in fondo allo scontrino di
una bilancia Zenith e le sue righe entrano sul banco con il peso, i pezzi e i
prezzi della bilancia, come già succedeva per Bizerba, Macchi e Dibal. Lo
sconto fatto sulla bilancia entra come riga **SCONTO VAL.**, così il totale è
quello stampato dalla bilancia. Le righe che non si possono inserire vengono
elencate in un avviso, e uno scontrino già passato non si ripassa.

### Miglioramenti

- [Documento di vendita](../moduli/vendite/documento-di-vendita.md): la
  maschera lavora sempre sull'archivio attraverso il motore SQL, su tutte le
  installazioni, e in fondo al titolo compare **[SQL]**. È un'indicazione per
  l'assistenza. Lo stesso vale per i documenti aperti o eliminati dal CRM e
  per i [preventivi](../moduli/vendite/preventivi.md), che già lavoravano in
  SQL e ora lo dicono nel titolo.
- Documento di vendita: ++f1++ apre la guida anche dalle finestre che si
  aprono dal documento — corpo, riga, piede con le sue schede, totali,
  ricerca, integrazioni della fattura elettronica, riassortimento da vendite,
  scelta dello scontrino e del carico, etichette dei colli — ognuna alla sua
  sezione, che il manuale ora descrive con le schermate.
- Vendita al banco: il **TOTALE** in basso a destra si adatta al campo. Con lo
  schermo ingrandito o ad alta risoluzione restava piccolo e in alto; ora il
  numero riempie il campo, centrato, e si rimpicciolisce solo se un importo
  lungo non ci starebbe.
- [Vendita al banco](../moduli/vendite/vendita-al-banco.md): ++f1++ apre la
  guida anche dalle finestre che si aprono dal banco — riga, chiusura dello
  scontrino, scelta e dati del documento, controllo con un ordine, partite
  scadute, compleanno del cliente — e dal dettaglio di uno
  [scontrino](../moduli/vendite/scontrini.md#il-dettaglio-di-uno-scontrino).
  Il manuale le descrive ora con le schermate, e spiega passo per passo il
  reso a partire dallo scontrino.
- **Solo Ortofrutta.** ++f1++ apre la guida anche dalla riga della vendita al
  banco, e il manuale descrive ora le righe di questa versione — al banco e
  nel [documento di vendita](../moduli/vendite/documento-di-vendita.md#la-riga-del-documento)
  — e la voce **F7 - Dati ▸ File Listino Prezzi Excel** degli ordini clienti.
- **Solo Taglie e Colori.** Il manuale descrive ora la finestra della riga
  per taglie e colori del documento di vendita, le voci di **F7 - Dati** di
  questa versione e della variante Calzature, e le differenze della riga e
  della chiusura dello scontrino al banco.
- Documento di vendita, preventivi e righe: le etichette dei campi usano lo
  stesso carattere del resto della finestra, e non escono più tagliate.
  Lo stesso vale per la [vendita al banco](../moduli/vendite/vendita-al-banco.md)
  e le finestre che apre — riga, emissione dello scontrino, tipo e dati del
  documento, controllo dell'ordine, partite scadute — e per il dettaglio
  degli [scontrini](../moduli/vendite/scontrini.md).
- Clienti: lo stesso carattere uniforme arriva in tutte le finestre dei
  clienti — [anagrafica](../moduli/anagrafiche/anagrafica-clienti.md) con le
  sue schede e la ricerca, [stampe](../moduli/anagrafiche/stampe-clienti.md),
  [associazione gruppi e giri](../moduli/anagrafiche/associazioni.md),
  [gestione compleanni](../moduli/anagrafiche/gestione-compleanni.md),
  [gestori buoni pasto](../moduli/anagrafiche/gestori-buoni-pasto.md), filtro
  della [mailing list](../moduli/anagrafiche/mailing-list.md), tessere
  fidelity e prodotti dei clienti.
- Clienti: ++f1++ apre la guida anche da **Altri Dati Cliente**, dalla
  finestra **Tessera Fidelity**, dalla ricerca per parole, dai **Dati
  Trasmissione Agenzia Dogane** (versione Energy), dal filtro della mailing
  list e dall'elenco dei gestori di buoni pasto. Il manuale descrive ora i
  pulsanti della [scheda Fidelity](../moduli/anagrafiche/anagrafica-clienti.md#schede-di-consultazione).

### Correzioni

**In tutto il programma**

- Arrotondamenti: un importo che cade esattamente sul mezzo centesimo veniva
  a volte arrotondato per difetto. Per esempio 0,250 kg a 19,90 €/kg, cioè
  4,975, diventava 4,97 invece di 4,98, e lo scontrino della bilancia non
  tornava con quello della cassa. Ora il mezzo centesimo segue sempre la
  stessa regola, per eccesso (4,98), nella cassa come nei documenti.

**Listini e articoli**

- **Solo Taglie e Colori.** [Anagrafica articoli](../moduli/anagrafiche/anagrafica-articoli.md#schede-di-consultazione),
  scheda **Taglie**: aprendo la scheda le colonne erano così strette da non
  leggere le quantità, e si allargavano solo passando a un altro articolo con
  **F3 - Prec.** o **F4 - Succ.**, tranne la prima. Ora la griglia viene
  uguale all'apertura e a ogni cambio di articolo, e mostra solo le taglie
  del gruppo dell'articolo, senza le colonne vuote a destra.

**Vendite**

- [Vendita al banco](../moduli/vendite/vendita-al-banco.md#la-scelta-del-documento),
  **F4 - Documenti**: il foglio si svuotava solo dopo la chiusura del
  documento emesso e, per il DDT, del suo piede. Se nel frattempo si tornava
  sul banco per il cliente successivo, le righe appena emesse finivano anche
  nel documento seguente; e se si era passati a un altro foglio, a svuotarsi
  era quello. Ora il foglio si svuota appena il documento è emesso.
- Vendita al banco, **F8 - Contr.Ordine**: indicando un ordine già evaso
  compariva *Ordine annullato!*; ora il messaggio è *Ordine già evaso!*.
- **Solo Taglie e Colori.** Nella riga per taglie e colori del documento,
  il nome della terza tabella libera usciva tagliato (*Tipo Tomai* invece di
  *Tipo Tomaia*).
- Vendita al banco, **Buon Compleanno!**: con lo schermo ingrandito
  l'immagine di auguri copriva solo una parte della finestra; ora la riempie.
- Documento di vendita, corpo, **F7 - Dati ▸ Scontrino Facile**: uscendo con
  **Esci** compariva *SQL Error*; e se lo scontrino non esisteva, dopo il
  messaggio la fattura proseguiva con uno scontrino vuoto. Ora **Esci** chiude
  e basta, e il numero dello scontrino viene richiesto di nuovo.
- **Integrazioni Fatture**: **F2 - Aggiungi**, **F3 - Modifica** e **F6 -
  Elimina** rispondevano al rilascio del tasto invece che alla pressione.
- Integrazioni: con il tipo `RIF.TO AMMINISTRAZIONE` e la descrizione vuota
  l'integrazione veniva salvata lo stesso; ora il programma si ferma sulla
  descrizione. Sulle integrazioni di riga, cambiando tipo restavano le
  etichette di **ALTRI DATI GESTIONALI**, e venendo da `DOC. DI TRASPORTO`
  **Tipo Dato** e **Rif. Testo** restavano nascosti.
- Documento di vendita, **F5 - Cerca**: cercando per **Data** il documento
  proposto era il primo per numero fra quelli di quella data o successivi, non
  il primo per data; cercando per **Intestatario** su bolle e documenti di
  trasporto la scelta fra cliente e fornitore non contava.
- Riga del documento: **F3 - Integraz.** e **F3 - Acq. Peso** avevano la
  stessa scorciatoia e il tasto apriva sempre le integrazioni. La lettura del
  peso ora è **Maiusc+F3 - Acq. Peso**, e legge anche le bilance BIZERBA, come
  già faceva la vendita al banco; con una OMEGA CHECKOUT, che la riga non sa
  leggere, compare un avviso invece di una quantità zero.
- Autofattura da carico merci: la data adeguata a quella del carico non veniva
  registrata sugli archivi che lavorano in SQL.
- Documento di vendita, corpo, **F7 - Dati**: tolta la voce **Scontrino MTX
  F3.0**, che leggeva gli scontrini da un sistema di cassa non più in uso.

- [Documento di vendita](../moduli/vendite/documento-di-vendita.md): se il
  salvataggio non riesce, **F7 - Stampa** non stampa più. Prima, dopo un
  messaggio come *Il Record è stato modificato da un altro processo.*, il
  documento veniva stampato lo stesso ma restava solo salvato: il magazzino
  non si muoveva e le scadenze non nascevano. Ora il documento viene riletto
  com'è in archivio e la stampa si ripete con un nuovo ++f7++. Lo stesso vale
  per **Anteprima**, **F8 - Corpo**, **Totali** e **Piede**.
- Documento di vendita: in alcune installazioni certi errori di salvataggio
  non comparivano a video e il documento sembrava salvato. Ora il messaggio
  compare sempre.
- Documento di vendita: il programma controlla di scrivere proprio il
  documento aperto a video. Se si accorge che stava per scriverne un altro,
  si ferma con *Il Record è stato modificato da un altro processo.* invece di
  sovrascriverlo.
- **Vendite ▸ Doc. di Trasporto Consegne Terzi ▸ Modifica** apre l'ultimo
  documento registrato; prima proponeva un documento nuovo.
- Righe dei documenti: con Facile aperto per molte ore, o dopo l'emissione di
  molti documenti di seguito, le righe potevano non essere più registrate
  (il documento restava senza righe) oppure il salvataggio poteva non
  terminare. Ora l'ordine delle righe segue l'orologio e resta sempre valido.
- [Vendita al banco](../moduli/vendite/vendita-al-banco.md): i dati presi da
  un ordine, un preventivo o un DDT con **F6 - Dati** — numero e data del
  documento d'origine, pagamento, destinatario, agente — restano sul foglio
  su cui sono stati presi. Prima passavano al documento emesso da un altro
  foglio, cioè a un altro cliente.
- Vendita al banco: se sul foglio si cambia il cliente dopo aver richiamato un
  documento, i riferimenti a quel documento si tolgono e il programma avvisa.
- Vendita al banco: alla domanda *Vuoi accorpare gli ordini ?* (e *Vuoi
  accorpare i buoni ?*) la risposta proposta è ora **No**. Con **Sì**
  proposto, un ++enter++ di troppo aggiungeva le righe a un ordine già aperto.
- Vendita al banco: se l'emissione di un documento si interrompe dopo averne
  registrato la testata, il programma indica il numero del documento rimasto
  incompleto, da controllare prima di riemetterlo.
- Documento di vendita: se con **F3 - Prec.**, **F4 - Succ.** o **F5 -
  Cerca** il documento cercato non si poteva leggere (per esempio *Record di
  un archivio relazionato non trovato!*), a video restava il documento di
  prima ma il programma teneva in memoria quello cercato: salvando, il
  documento a video prendeva stato, totali e dati del piede dell'altro. Ora
  resta in memoria il documento a video. Lo stesso quando la preparazione di
  un documento nuovo si interrompe.
- Documento di vendita: se due postazioni modificano lo stesso documento,
  chi salva per secondo riceve di nuovo *Il record è stato modificato da un
  altro nodo della rete.* invece di sovrascrivere senza avviso le modifiche
  dell'altro.
- Documento di vendita, **Ricarica**: rileggeva il documento ma lasciava a
  video i campi modificati, che il salvataggio successivo registrava. Ora
  riporta davvero il documento com'è in archivio.
- Documento di vendita, **F8 - Corpo**: dopo i dati dello scontrino, i dati
  del carico o il cambio di listino, su un documento di un anno diverso da
  quello aperto la testata veniva riletta da quell'anno, cioè da un altro
  documento con lo stesso numero.
- Documento di vendita, **Shift+F1** (recupero dell'ordine): su un ordine
  nuovo non ancora salvato non fa più nulla. Con un numero scritto a mano,
  riscriveva l'ordine esistente con quel numero.
- Documento di vendita: l'importazione di un ordine da file non si blocca più
  se il numero proposto è già usato.
- Preventivi: se il salvataggio non riesce, **F8 - Corpo**, **Totali**,
  **Piede**, **Anteprima** e **F7 - Stampa** si fermano. Prima proseguivano,
  e con due postazioni sul numero nuovo le righe di una finivano nel
  preventivo dell'altra.
- Vendita al banco, accorpamento degli ordini: il messaggio dice quale ordine
  (numero e data), e vengono proposti solo ordini salvati e non ancora
  emessi. Prima l'ordine poteva essere uno qualsiasi degli ultimi 30 giorni,
  anche già emesso, che veniva riaperto.
- Vendita al banco, **F8 - Contr.Ordine** ▸ **F2 - Conferma Evasione**: non
  evadeva mai le quantità dell'ordine e poteva segnare come evaso un ordine
  diverso da quello controllato (di un altro cliente, o con il numero
  cambiato senza ricaricarlo). Ora evade l'ordine caricato in griglia.
- Pos Touchscreen, scontrini delle bilance Bizerba, Macchi e Dibal: indicando
  il cliente o la tessera dopo averli letti, le righe tornavano al prezzo di
  listino. Ora tengono il prezzo della bilancia.

**Casse e Bilance**

- [Bilance](../moduli/casse-bilance/bilance.md) Zenith, **Ricezione Scontrini
  da Bilance** e **da File**: le quantità venivano lette male, l'importo della
  riga veniva preso per il prezzo unitario, e gli articoli si cercavano solo
  per codice a barre. Ora le righe si riconoscono da bancone e PLU, e il
  movimento riporta il peso o i pezzi venduti e l'importo al netto degli
  sconti.

## Versione 2026 B08

In distribuzione dal 31 luglio 2026.

### Nuove funzioni

**Guida in linea.** Il tasto ++f1++ non apre più il vecchio file di guida: apre
nel browser la pagina di questo manuale dedicata alla maschera in cui ti
trovi. Funziona anche in maschere che prima non avevano guida, e non compare
più il messaggio *Impossibile aprire la Guida.*

**[Esportazione DDT - CENTRALE LATTE SALERNO](../moduli/trasferimenti/esportazione-ddt-centrale-latte-salerno.md).**
Il nuovo tracciato manda alla Centrale del Latte di Salerno i DDT trasfert del
periodo, con i punti vendita, gli articoli venduti e quelli resi. Il file
porta nel nome il codice concessionario e la data, quindi non sovrascrive
l'invio del giorno prima. Un DDT a cui manca un dato, per esempio un aggancio
o un codice fornitore, viene lasciato fuori per intero, con un messaggio che
dice cosa manca.

**[Commesse](../moduli/contabilita/commesse.md)**

- Nella scheda dei **Centri di Costo** il doppio clic su una riga apre
  l'elenco dei movimenti di prima nota che formano quell'importo, nello stesso
  periodo; da lì un altro doppio clic apre la registrazione. La stampa resta
  sul suo pulsante.
- Sempre nei **Centri di Costo**, il nuovo pulsante **Excel** esporta la
  scheda in un foglio con ditta, commessa e periodo in testa e il totale dei
  costi diretti in fondo.
- La scheda **Ordini a Fornitore** ha i filtri **Dal**, **Al** e **Centro di
  Costo**.
- Il totale dei **Claims** è separato da quello delle **Varianti**: prima
  venivano sommati insieme, contando come acquisito anche quello che è ancora
  in trattativa.

**[Banche](../moduli/contabilita/banche.md).** Al salvataggio l'**IBAN** viene
controllato con il calcolo previsto dallo standard. Se non torna, il programma
avvisa, ma si può salvare lo stesso: il controllo non deve impedire di
registrare una banca estera. Nella fattura elettronica un IBAN troppo corto
non sparisce più in silenzio: viene segnalato.

**[Rinumerazione protocolli](../moduli/contabilita/rinumerazione-protocolli.md).**
Prima di rinumerare il programma chiede conferma, e se uno dei registri scelti
è già stato stampato in bollato lo dice, con la data della stampa. In quel
caso chiede anche se azzerare le date dei bollati. Su entrambe le domande la
risposta proposta è **No**.

**[Fatture elettroniche passive](../moduli/contabilita/fatture-elettroniche-passive.md).**
L'importazione scrive, file per file, cosa è successo — importato, già
presente, scartato con il motivo, ignorato — in un diario nella cartella
`log` del programma. Il riepilogo finale rimanda a quel file.

**[Causali di magazzino](../moduli/magazzino/causali-magazzino.md).** Al
salvataggio il programma avvisa se le impostazioni si contraddicono, per
esempio un carico che sottrae dall'esistenza. Se cambi i contatori di una
causale già usata, ricorda di eseguire il ricalcolo dei movimenti di
magazzino. In entrambi i casi puoi salvare lo stesso.

**Ordini.** Le voci **Cancellazione Ordini Evasi** (ordini dei clienti) e
**Cancellazione Ordini Ricevuti** (ordini a fornitore) chiedono il periodo,
dicono quanti ordini verranno cancellati e chiedono conferma. Rispettano il
divieto di cancellazione impostato sull'utente.

**Inventario.** La voce **Esporta Dati Acquisiti in File Excel** non faceva
nulla: ora esporta.

**[Distribuzione automatica scorte e riordino](../moduli/anagrafiche/scorte-e-assortimento.md).**
La quantità da ordinare tiene conto di quanto è già impegnato dai clienti e
già ordinato ai fornitori, e la stampa degli articoli da ordinare elenca
esattamente le righe che finiranno negli ordini. Il fornitore abituale resta
in gara con gli altri: vince il prezzo più basso. **Ordini Selezione Depositi
da Cumulare** prima non inseriva nessuna riga, ora funziona. Il messaggio
finale dice quante righe erano già coperte da ordini aperti o erano senza
fornitore.

**Casse 3i.** Il programma legge dalla cassa il numero dello scontrino
fiscale, il numero gestionale, la matricola e il numero di azzeramento, e li
registra sullo scontrino. Prima restavano a zero.

**Conversione degli archivi c-tree.** Quando un archivio cambia tracciato, la
conversione ora parte anche sugli archivi di grandi dimensioni, che il server
divide in più parti. Prima di toccare qualsiasi cosa il programma chiede il
consenso in due passaggi, e annota tutto nel file `conversioni.txt` della
cartella `log`.

### Miglioramenti

- **[Cerca articoli](../moduli/anagrafiche/cerca-articoli.md)**: le
  descrizioni che vanno a capo si leggono per intero su due righe. L'elenco si
  apre nell'ordine scelto con **Preval. Ricerca Codice** anche sugli archivi
  PostgreSQL. La ricerca per codice si ferma sull'articolo scritto.
- **Campi obbligatori** in [Clienti](../moduli/anagrafiche/anagrafica-clienti.md)
  e [Articoli](../moduli/anagrafiche/anagrafica-articoli.md): quando ne manca
  uno, il programma dice quale — *Il campo … e' obbligatorio.* — invece di
  emettere solo un segnale acustico.
- **Elenchi**: le voci con la stessa descrizione escono sempre nello stesso
  ordine, per codice. Sugli archivi PostgreSQL, scorrendo elenchi lunghi, non
  capita più di vedere una voce due volte e di perderne un'altra.
- **Griglie nelle schede**: le griglie seguono la finestra quando la
  ingrandisci, e le colonne si ridistribuiscono. Vale fra le altre per
  Commesse, Movimenti del cliente, Destinazioni e Progressivi della ditta,
  Totali IVA.
- **Errori del database**: il messaggio dice da dove viene l'errore e ne
  riporta il codice, e ogni errore viene anche annotato, con data e ora, nel
  file `sqlerr.txt` della cartella `log`.
- **Campi data**: la data è centrata nel campo, in tutte le maschere.
- **Copia e incolla**: ++ctrl+c++ copia il testo selezionato nel campo. Prima,
  in molte maschere, metteva negli appunti il titolo della finestra.
- **[Gestione listini di vendita](../moduli/listini-vendita/gestione-listini.md)**:
  l'esportazione produce un foglio Excel formattato, e il caricamento
  dell'elenco è più veloce.
- **[Rubrica](../moduli/anagrafiche/rubrica.md)**: i pulsanti **Chiama** e
  **Chiudi** compaiono solo se è configurato un centralino, e ++space++ o
  ++f10++ su un numero di telefono non avviano più una chiamata.
- **[Clienti](../moduli/anagrafiche/anagrafica-clienti.md)**: la scheda si
  apre e scorre più in fretta sugli archivi PostgreSQL. Arrivati in fondo
  all'elenco, **Prec.** e **Succ.** chiudono la scheda come già facevano su
  c-tree.
- **Amministratori**: conta come amministratore chiunque abbia la casella
  nella propria scheda utente, non più solo l'utente ADMIN. Vale per le voci
  **Utenti** e **Nuovo Esercizio**, per la password nella scheda cliente e
  per i comandi riservati dei [dati dell'azienda](../moduli/anagrafiche/ditte.md).
- **Finestra di accesso**: non mostra più server e archivio quando la
  connessione è già aperta.
- **Terminali di pagamento Dojo**: un pagamento annullato sul terminale viene
  riconosciuto, e dopo due minuti senza esito la transazione viene annullata
  invece di lasciare il programma in attesa. Riaprendo le impostazioni, il
  terminale salvato risulta selezionato.
- **Bilance Zenith**: il PLU può arrivare fino a 9999.
- **[Promozioni](../moduli/vendite/promozioni.md)**: l'importazione da Excel
  legge anche i file `.xlsx`. Un articolo ripetuto nel foglio, o presente con
  due codici a barre diversi, non ferma più l'importazione: entra la prima
  riga, le altre vengono scartate. Anche gli articoli non trovati non
  interrompono più il lavoro con un messaggio per ciascuno. Alla fine un
  riepilogo dice quante righe sono entrate, e l'elenco delle righe scartate,
  con il motivo, si apre in un file di testo. Una percentuale scritta in una
  cella con formato percentuale vale quella che si vede: `20%` è uno sconto
  del venti per cento. Una riga senza offerta né sconto viene scartata:
  prima, in un foglio con entrambe le colonne, l'articolo entrava con uno
  sconto pari all'intero prezzo. Il manuale spiega come preparare il foglio e
  mette a disposizione un modello.

### Correzioni

**Contabilità**

- Contabilizzando le fatture, le scadenze non vengono più duplicate. Il
  difetto era comparso con la gestione delle scadenze sulle causali della
  B07.
- In prima nota, scegliendo la causale dall'elenco, la gestione delle
  scadenze si imposta secondo la causale.
- Sugli archivi PostgreSQL la cancellazione di un conto non azzera più i
  totali di un altro conto.
- La prima nota generata contabilizzando una fattura elettronica ha le
  scadenze attive, salvo che la causale le escluda.

**Vendite e magazzino**

- [Vendita al banco](../moduli/vendite/vendita-al-banco.md): lavorando con il
  secondo cliente o con uno dei successivi, i documenti emessi con **F4 -
  Documenti** potevano avere righe che non scaricavano il magazzino. Il difetto
  era comparso nella B07. Ora, se il segno di una riga ha un valore non valido,
  il programma lo azzera e lo dice.
- Evadendo un ordine (dalla fatturazione degli ordini, dagli ordini in
  lavorazione o dal banco) e recuperando un ordine da file, le righe non
  ereditano più dall'ordine il segno «già movimentato»: il documento che ne
  nasce scarica il magazzino come deve.
- [Fatturazione differita](../moduli/vendite/emissione-fatture-da-documenti.md)
  delle pro forma (**Fatture Pro Forma ▸ Emissione Fatture**): se la ditta non
  fa movimentare le pro forma, la fattura ora scarica il magazzino. Prima non
  lo scaricava né la pro forma né la fattura.
- [Fatturazione differita](../moduli/vendite/emissione-fatture-da-documenti.md)
  con il raggruppamento per articoli: due righe dello stesso articolo restano
  separate se una scarica il magazzino e l'altra no (per esempio una presa da
  un DDT conto vendita e una battuta a mano). Prima si fondevano, e la
  quantità dell'una scaricava il magazzino come l'altra.
- [Duplica](../moduli/vendite/esporta-duplica-documenti.md): la copia scarica
  il magazzino anche quando l'originale non lo faceva, per esempio duplicando
  una fattura nata da un DDT. La fattura da pro forma resta com'era.
- [Vendita al banco](../moduli/vendite/vendita-al-banco.md): le righe prese da
  un DDT conto vendita si possono emettere solo in fattura, fattura
  accompagnatoria, ricevuta fiscale o pro forma.
- Sugli archivi c-tree il salvataggio degli scontrini non viene più
  rifiutato.
- **Valorizza Doc. Trasfert e Concessionario**: il costo medio del mese entra
  finalmente nel calcolo.
- Gli ordini a fornitore generati dagli ordini dei clienti e con l'analisi
  prezzi danno un esito più chiaro.
- **Controllo merci in entrata**: gli stati *RESO RIPARAZIONE* e
  *SOSTITUZIONE* vengono salvati.
- Sei messaggi del [carico merci](../moduli/magazzino/carico-merci.md) avevano
  le lettere accentate storpiate.
- **Distinta di produzione**, comando Duplica: controlla tutte le righe e non
  solo la prima.
- Il divieto di cancellazione dell'utente ora vale anche per carichi merci,
  produzione, promozioni sellin e frontalini.

**Listini e articoli**

- [Gestione listini di vendita](../moduli/listini-vendita/gestione-listini.md),
  importazione da Excel: prezzi, sconti, minimo e scorta non perdono più i
  decimali (12,50 diventava 12).
- [Listini fornitori](../moduli/listini-fornitori/gestione-listini-fornitori.md):
  sugli archivi PostgreSQL, eliminando una riga dopo averne cambiato il codice
  non si cancella più la riga sbagliata. La seconda conferma della
  cancellazione massiva non è più invertita.
- **Conferma listini**: il secondo fornitore migliore non ricopia più il
  primo.
- Contratti con i fornitori: le percentuali di ribasso delle righe dalla 2
  alla 8 non prendono più il valore della prima.
- Le stampe degli articoli senza codici a barre, fuori assortimento e con
  variazioni attive, e diverse esportazioni in Excel, funzionano sugli archivi
  PostgreSQL.
- Marchio e stagione non si confondono più nel fatturato mensile per marchio,
  nell'analisi multidimensionale e nell'esportazione degli articoli.

**Archivi e utenti**

- Salvando un utente sugli archivi c-tree la password non si rovina più, e
  uscendo dal programma dopo il salvataggio non compare più un errore.
- Mailing list, panieri, ubicazioni, descrizioni in lingua e immagini della
  prima nota si salvano e si cancellano correttamente sugli archivi
  PostgreSQL.
- Cancellando un cliente mentre si scorre per numero di tessera non compare
  più un errore.
- Passando da un archivio c-tree a PostgreSQL, i record scartati
  dall'importazione di contratti e SAL delle commesse e degli abbinamenti con
  Shopify non fanno più comparire un messaggio a video per ciascuno: come per
  le altre tabelle, finiscono nel registro della tabella nella cartella `log`,
  che resta solo se qualcosa è stato scartato.

**Trasferimenti e altro**

- Esportazione **Customers Globe / Froneri**: il codice del canale di vendita
  del cliente veniva preso dal canale sbagliato.
- **Bilance BIZERBA**, ricezione dei totali delle vendite, e **Stampa
  Registro Sostanze Zuccherine** davano sempre errore: ora funzionano.
- **Attribuzione Automatica Provvigioni Mancanti** non faceva nulla sugli
  archivi PostgreSQL: ora funziona.
- **Solo Ortofrutta.** La chiusura vendita con stampa delle partite chiuse e
  le schede rimanenze non danno più errore.
- **Solo CRM.** La maschera **Tipi Prodotti** si apre di nuovo.

### Voci tolte dal menu

Sono sparite alcune voci che non facevano nulla:

- **Utility ▸ Assistenza ▸ Cancellazione Articoli Inesistenti**;
- **Archivi ▸ Contabilità ▸ Titoli** e **Utility ▸ Assistenza ▸ Variazione
  Sottoconti**, fuori dalla versione Studio.

### Testi a video

Sono stati corretti circa 250 refusi fra voci di menu, titoli, etichette e
messaggi. Fra i più visibili: *Riassortimento Punti Vendita da Vendite*,
*Cruscotto Finanziario*, *Ricezione D.D.T. da Palmare*, *Anagrafica Clienti -
FRONERI*, *Estratti Conto Scadenze*, *Stampa Portafoglio Effetti Attivi*, la
scheda *Alternativi* degli articoli, *Sfrido* nella produzione, *Imputazione*
nella contabilizzazione delle fatture. I puntini di sospensione e la parola
«file» sono ora scritti allo stesso modo in tutti i messaggi.

## Versione 2026 B07

In distribuzione dal 1° luglio 2026.

### Nuove funzioni

**[Commesse](../moduli/contabilita/commesse.md)** — la gestione è stata
ampliata in modo sostanziale:

- una commessa può avere **più contratti**, ciascuno con importo, tipo di
  pagamento (milestone o SAL) e termini di pagamento. Il contratto principale
  nasce da solo, e il valore della commessa è la somma dei contratti;
- il **piano di fatturazione** a milestone o a SAL non si compila più a mano:
  si collegano le fatture emesse già registrate in prima nota, e imponibile,
  IVA, ritenuta e totale si calcolano da quelle. Il pulsante **PDF** apre la
  fattura allegata;
- i **[subappaltatori](../moduli/contabilita/subappaltatore.md)** hanno i
  propri [SAL](../moduli/contabilita/sal-subappaltatore.md), collegati alle
  fatture passive del fornitore;
- il **budget per centro di costo**, e un **Gruppo** sui centri di costo
  (Fatture, Manodopera, Altro);
- le schede **Ordini a Fornitore** e **Carichi**, con il doppio clic che apre
  il documento;
- i campi **CUP**, **Tecnico**, **Contatto Email** e la **% Fatturato**;
- i pulsanti **Piano Fatt.** e **Monitoraggio** producono i fogli Excel del
  piano di fatturazione e del monitoraggio di costi e ricavi.

**[Conto vendita](../moduli/vendite/vendita-al-banco.md).** Dalla vendita si
richiamano i DDT del cliente emessi con una causale di trasporto esclusa dalla
fatturazione differita, e si fattura solo quanto è stato venduto. Le righe
riprese dal DDT non muovono di nuovo il magazzino, e sul DDT compare la
quantità già fatturata.

**[Causali contabili](../moduli/contabilita/causali-contabili.md).** La nuova
casella **Disabilita Gestione Scadenze** esclude la causale dallo
scadenzario: la prima nota non lo propone e l'importazione delle fatture
passive non genera scadenze. Lo scadenzario della prima nota viene ora
proposto anche per i clienti.

**[Invio massivo delle fatture elettroniche](../moduli/vendite/fatture-elettroniche-attive.md).**
Una nuova colonna mostra con un semaforo i termini di trasmissione allo SdI:
verde nei termini, giallo a tre giorni o meno dalla scadenza, rosso a termine
superato, azzurro per i documenti inviati in attesa di esito.

**Ricarico articoli.** La finestra ha il campo **Scorta Max**, accanto alla
scorta minima.

### Miglioramenti

- **Vendita al banco**: con l'arrotondamento ai 5 centesimi attivo, vale anche
  per gli incassi fatti dal preconto. Con **Chiudi Scontrino** del preconto
  attivo, la domanda di chiusura offre tre risposte: chiudere scaricando gli
  articoli, chiudere senza scaricarli, annullare.
- **Casse Custom** di terza generazione: la matricola fiscale si legge per
  intero.
- **Campi numerici**: ++ctrl+c++, ++ctrl+v++ e ++ctrl+x++ funzionano anche da
  tastiera.
- **Solo Studio.** Il confronto fra due esercizi legge i movimenti dall'anno
  richiesto, e non compare più il messaggio che lo limitava all'anno
  corrente.
- **Solo Ortofrutta.** Le stampe della scheda anomalie articoli, della
  chiusura vendita, del riepilogo partita e dei movimenti del cliente non si
  disturbano più se lanciate insieme da due postazioni.

### Correzioni

- **Fattura elettronica**: nel file XML le lettere accentate di ragioni
  sociali, indirizzi e descrizioni vengono convertite correttamente, e la
  provincia viene controllata (due lettere maiuscole).
- **Magazzino**: annullando o modificando il movimento di un articolo che ha
  un articolo associato, vengono stornate anche le quantità dell'associato.
- **Bollo automatico** sulle operazioni esenti: si applica solo a fatture,
  fatture accompagnatorie e ricevute fiscali.
- Caricando in fattura una **fattura elettronica XML**, il cliente
  identificato dal solo codice fiscale viene riconosciuto.
- **Allegati**: aprendo un allegato si vede sempre il file giusto, anche se
  nella cartella temporanea ce n'era già uno con lo stesso nome.
- **Gestione documenti**: rispondendo **No** all'avviso sul numero di record
  da estrarre non compare più un errore.
- Nelle caselle di spunta il testo non si scurisce e non si sovrappone più al
  passaggio del mouse.
