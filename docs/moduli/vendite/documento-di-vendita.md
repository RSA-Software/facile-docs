---
title: Documento di vendita
description: La maschera con cui si compilano fatture, DDT, bolle, buoni di consegna, ricevute fiscali, autofatture e ordini — testata, corpo, piede e totali.
modulo: Vendite
maschera_id: IDD_VEN_FATTURE
---

# Documento di vendita

Tutte le voci **Inserimento** e **Modifica** del menu Vendite aprono **la stessa
maschera**: cambia il tipo di documento che si sta compilando, non il modo di
compilarlo. Fattura, documento di trasporto, bolla, buono di consegna, ricevuta
fiscale, autofattura e ordine si scrivono qui.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Vendite ▸ *(un tipo di documento)* ▸ Inserimento *(oppure* Modifica*)*, o **F2 - Nuovo** dalla [gestione documenti](gestione-documenti.md)
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca, ++f7++ stampa, ++f8++ corpo, ++f9++ email
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

È il documento di vendita in tutte le sue forme. Si indica a chi va, cosa
contiene e a quali condizioni; il programma calcola gli importi, scarica il
magazzino e — a seconda del tipo — prepara le scadenze e la fattura
elettronica.

## Prerequisiti

Prima di usare questa maschera occorre:

- avere in archivio i [clienti](../anagrafiche/anagrafica-clienti.md) con le
  loro condizioni;
- avere gli [articoli](../anagrafiche/anagrafica-articoli.md) con i
  [listini](../listini-vendita/gestione-listini.md) valorizzati;
- avere le [aliquote IVA](../contabilita/aliquote-iva.md), i
  [tipi di pagamento](../contabilita/tipi-di-pagamento.md) e le
  [causali contabili](../contabilita/causali-contabili.md);
- avere impostato registri e numeratori nella
  [ditta](../anagrafiche/ditte.md).

## La maschera

![Documento di vendita](../../assets/img/vendite/documento-di-vendita.png)

La finestra è organizzata in tre parti, che si raggiungono dai pulsanti in
basso:

1. la **testata** — chi, che tipo di documento, a quali condizioni;
2. il **corpo** (**F8 - Corpo**) — le righe di merce;
3. il **piede** e i **totali** — spese, sconti finali, riepilogo IVA.

## Campi

### Testata

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Intestatario** | ● | Il [cliente](../anagrafiche/anagrafica-clienti.md) a cui il documento è intestato. Un elenco a fianco sceglie se è un cliente o un fornitore. | codice |
| **Destinatario** | | La destinazione della merce, se diversa dall'intestatario. | codice |
| **Tipo Documento** | ● | Il tipo ai fini della fattura elettronica. | `TD01 - FATTURA`, `TD04 - NOTA CREDITO`, `TD02 - FATTURA ACCONTO`, `TD05 - NOTA DI DEBITO`, `TD06 - PARCELLA`, `TD24 - FATTURA DIFFERITA…` e gli altri codici TD previsti |
| **Operatore** | | Chi sta emettendo il documento. | codice |
| **Gruppo** | | Il gruppo del cliente. | codice |
| **Pagamento** | ● | Il [tipo di pagamento](../contabilita/tipi-di-pagamento.md): da qui nascono le scadenze. Proposto dal cliente. | codice |
| **Data Diversa** | | Una data da cui far decorrere le scadenze, diversa da quella del documento. | data |
| **Banca** | | La [banca](../contabilita/banche.md) di appoggio. | codice |
| **Agente** | | L'[agente](../anagrafiche/anagrafica-agenti.md) su cui matura la provvigione. Proposto dal cliente. | codice |
| **Cau. Magazzino** | | La [causale di magazzino](../magazzino/causali-magazzino.md) con cui la merce viene movimentata. | codice |
| **Tipo Vendita** | | Il genere di vendita: decide quale delle quattro percentuali di provvigione si applica. | `N` normale, `T` trasferta, `C` e `D` centro servizi |
| **Cau. Contabile** | | La [causale](../contabilita/causali-contabili.md) con cui il documento sarà contabilizzato. | codice |
| **Registro** | ● | Il registro IVA e il numeratore da usare. | voce dell'elenco |
| **Num. Fattura**, **Data Fattura** | | Numero e data del documento. | numero e data |
| **Num. Ordine**, **Data Ordine** | | Il riferimento all'ordine del cliente. | numero e data |
| **Num. Documento**, **Data Fattura** | | Il riferimento al documento da cui questo deriva. | numero e data |
| **% Sconto** | | Lo sconto generale del documento. | percentuale |
| **Sezione** | | La [sezione](../contabilita/sezioni.md) contabile. | codice |
| **Commessa** | | La [commessa](../contabilita/commesse.md) a cui imputare. | codice |
| **Cen. Costo/Ricavo** | | Il [centro di costo o ricavo](../contabilita/centri-di-costo.md). | codice |
| **Addebito Bolli** | | Se addebitare il bollo al cliente. | `NO`, `SI` |
| **Add. Spese** | | Se addebitare le spese al cliente. | `NO`, `SI` |
| **Ric. Fiscale** | | Se il documento va raggruppato nella fatturazione differita. L'etichetta cambia con il tipo di documento: sui DDT, sulle bolle e sui DDT da terzi diventa **Raggruppa**, sui buoni di consegna **Pagato**, e su ricevute fiscali e autofatture sparisce del tutto. | `NO`, `SI` |
| **Consegna** | | La data di consegna. Compare **solo sugli ordini**, clienti e fornitori. | data |
| **Totale Documento** | | Il totale. Lo calcola il programma. | Sola lettura |

{: .campi }

### Corpo

Il corpo si apre con **F8 - Corpo** ed è la griglia delle righe:

| Colonna | Contenuto |
|---|---|
| **Codice** | Il codice dell'articolo. |
| **Col.**, **Tag.** | Colore e taglia, nella versione Taglie e Colori. |
| **Descrizione** | La descrizione, proposta dall'articolo e correggibile. |
| **Mis.** | L'[unità di misura](../magazzino/unita-di-misura.md). |
| **Quantità** | Quanto se ne vende. |
| **Q.tà Evasa** | Quanto è già stato consegnato, sugli ordini. |
| **Esistenza**, **Disponibilità** | Quanto ce n'è e quanto è libero da impegni. |
| **Data Ord. For.**, **Data Consegna** | Le date dell'ordine al fornitore e della consegna. |
| **Colli**, **Prel.** | I colli e la quantità prelevata. |
| **Prezzo Unit.** | Il prezzo, proposto dal listino del cliente. |
| **Sconto**, **Sc.Merce** | Lo sconto in percentuale e lo sconto merce. |
| **Importo** | Il totale della riga. |
| **C.Iva** | L'[aliquota IVA](../contabilita/aliquote-iva.md) della riga. |
| **Ordinare** | Segna la riga da ordinare al fornitore. |
| **Dep** | Il [deposito](../magazzino/depositi.md) da cui scaricare. |

### Piede

Si apre con il pulsante **Piede** e raccoglie i dati del trasporto e le note.
Su ricevute fiscali e autofatture quel pulsante non c'è: al suo posto
compare **Allegati**.

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Porto** | | A carico di chi è il trasporto. | *(vuoto)*, `FRANCO`, `ASSEGNATO`, `FRANCO DEPOSITO`, `EX WORKS`, `FRANCO CON ADDEBITO IN FATTURA` |
| **Trasp. a Cura** | | Chi cura il trasporto. | `VETTORE`, `MITTENTE`, `DESTINATARIO` |
| **Inizio Trasporto** | | Data e ora di partenza della merce. | data e ora |
| **Aspetto Merci** | | L'[aspetto esteriore dei beni](../altre-tabelle/note-aspetto-trasporto.md). | codice |
| **Colli** | | Quanti colli. | numero |
| **Peso** | | Il peso e la sua unità. | numero, `Gr.` `Hg.` `Kg.` `Q.` `T.` |
| **Caus. Trasporto** | | La causale del trasporto. | codice |
| **Esc. Invio 730** | | Tiene il documento fuori dall'invio al Sistema Tessera Sanitaria. | attivo/non attivo |
| **Tipo Invio 730** | | Che genere di comunicazione mandare. | `INS`, `VAR`, `RIMB`, `CANC` |
| **Trasportatore** | | Il [trasportatore](../anagrafiche/trasportatori.md) incaricato. | codice |
| **Gestione Merce in Transito** | | Segna la merce come in transito. | attivo/non attivo |
| **Vettori**, **Residenza**, **Ritiro Merci** | | Due righe per il primo e il secondo vettore, con la loro residenza e data e ora del ritiro. | codici, testo, data e ora |
| **Scad. Effetti** | | Le date delle scadenze, in chiaro sul documento. | testo |
| **Annotazioni** | | Una riga di note. | testo |
| **VARIE** | | Quattro righe libere che finiscono sul documento stampato. | testo |

{: .campi }

### Totali

Si apre con il pulsante **Totali**. È il riepilogo economico del documento:
quasi tutto lo calcola il programma, e si scrivono a mano solo le voci del
piede.

| Campo | Si scrive | Descrizione |
|---|:---:|---|
| **Tot. Merce**, **%Sconto**, **Netto Merce** | | Il totale delle righe, lo sconto generale e quello che resta. |
| **Trasp. Imballo** | ● | Spese di trasporto e imballo da addebitare. |
| **Varie** | ● | Altre spese. |
| **Inc. Effetti** | ● | Spese di incasso degli effetti. |
| **C.Iva**, **Rip. Spese**, **Imponibile**, **% Iva o Art. Esenzione**, **Tot. Iva** | | Il castelletto IVA, fino a quattro aliquote per documento. |
| **Esente**, **Non Soggetto**, **Non. Imponibile** | | I tre totali fuori campo IVA. |
| **Imponibile**, **Totale IVA** | | I due totali generali. |
| **Spese (Art. 15 )** | ● | Le spese escluse dalla base imponibile. |
| **Bolli Effetti** | ● | I bolli sugli effetti. |
| **Abbuoni** | ● | L'abbuono concesso. |
| **Acconto** | ● | L'acconto già versato, da scalare. |
| **Omaggi** | | Il valore degli omaggi. |
| **Ritenuta Acconto** | | La ritenuta d'acconto. |
| **Cassa Previd. Prof.** | | Il contributo alla cassa di previdenza. |
| **Enasarco** | | Il contributo Enasarco. |
| **Tot. Quantità** | | La somma delle quantità. |
| **T O T A L E** | | Il totale del documento. |
| **Totale Cauzioni**, **Totale Resi** | | I due totali delle versioni che li gestiscono. |
| **Detrazioni Fiscali** | ● | L'importo che dà diritto a detrazione. |
| **Totale da Pagare** | | Quello che il cliente deve. |
| **Ricavo Lordo**, **%Ric.**, **%Mar.**, **Totale Provvigione** | | Margine e provvigione del documento. Non compaiono su richieste offerta, autofatture e ordini a fornitore. |
| **N. Pedane**, **Costo Pedane** | ● | Le pedane, dove sono gestite. |

{: .campi }

A documento emesso le voci che si scrivono a mano diventano di sola lettura e
il pulsante **F2 - OK** sparisce: resta solo **Esci**.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra il documento. |
| **F3 - Prec.** | ++f3++ | Passa al documento precedente. |
| **F4 - Succ.** | ++f4++ | Passa al documento successivo. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco dei documenti. |
| **F6 - Elimina** | ++f6++ | Cancella il documento, previa conferma. |
| **F7 - Stampa** | ++f7++ | Stampa il documento. |
| **F8 - Corpo** | ++f8++ | Passa alle righe di merce. |
| **F9 - Email** | ++f9++ | Manda il documento per posta al cliente. |
| **Piede**, **Totali** | | Passano al piede e al riepilogo dei totali. |
| **Lista** | | Torna all'elenco dei documenti. |
| **Anteprima** | | Mostra l'anteprima di stampa. |
| **Etichette** | | Stampa le etichette del documento. |
| **Allegati** | | Allega un file al documento. |
| **Tracc.** | | Apre un menu con **Etichette Logistiche** ed **Etichette Commerciali**. Compare solo con la gestione dei lotti attiva. |
| **Fatture Elettroniche** | | Apre la gestione della fattura elettronica del documento. Compare solo su fatture, fatture accompagnatorie e autofatture. |
| **Ricarica** | | Rilegge il documento, abbandonando le modifiche non salvate. |
| **Annulla**, **Chiudi** | ++esc++ | Abbandonano il documento. |

## Come si fa

### Emettere una fattura

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Inserimento**.
2. Indica l'**Intestatario**: il programma propone pagamento, banca, listino e
   sconti dalle condizioni del cliente.
3. Controlla **Tipo Documento** — per una fattura ordinaria `TD01 - FATTURA` —
   e il **Registro**.
4. Premi **F8 - Corpo** e scrivi le righe: **Codice** e **Quantità** bastano,
   il **Prezzo Unit.** arriva dal listino.
5. Vai su **Totali** e controlla il riepilogo IVA.
6. Premi **F2 - Salva**, poi **F7 - Stampa** o **F9 - Email**.

### Emettere una nota di credito

1. Apri **Fatture ▸ Inserimento** come sopra.
2. In **Tipo Documento** scegli `TD04 - NOTA CREDITO`.
3. In **Num. Documento** e **Data Fattura** indica gli estremi della fattura
   che stai stornando.
4. Compila il corpo con le righe da stornare.

### Emettere un documento di trasporto

1. Apri **Menu ▸ Vendite ▸ Doc. di Trasporto ▸ Inserimento**.
2. Compila testata e corpo come per la fattura.
3. Il documento resta poi disponibile per l'
   [emissione differita della fattura](emissione-fatture-da-documenti.md).

## Controlli e messaggi

È la maschera che parla di più di tutto il programma. I messaggi sono
raccolti qui per **momento in cui si incontrano**, non in ordine alfabetico:
quasi sempre quello che serve è capire *a che punto* il documento si è
fermato.

!!! tip "Le domande importanti hanno «No» già selezionato"

    Quasi tutte le domande di questa maschera — fido superato, cliente
    cessato, righe senza lotto, scadenzario da correggere — arrivano con la
    risposta **No** preimpostata. Premere Invio per abitudine **non**
    prosegue: annulla. È voluto, ed è la ragione per cui conviene leggerle
    invece di scacciarle.

### Quando si indica il cliente

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Il cliente selezionato risulta cessato !<br>Vuoi Continuare ?* | Il cliente ha una data di cessazione nella sua [anagrafica](../anagrafiche/anagrafica-clienti.md). | **Sì** intesta lo stesso il documento. Se il cliente è tornato attivo, la strada giusta è togliere la data di cessazione. |
| *Attenzione !<br>E' stato superato il Fido concesso al Cliente (Euro …) per l' importo di Euro …<br>Vuoi Continuare ?* | Il documento porta l'esposizione del cliente oltre il fido. | **Sì** prosegue lo stesso. La cifra fra parentesi è il fido, l'altra lo sconfinamento. |
| *Attenzione !<br>E' stato superato il Fido concesso al Cliente (Euro …) per l' importo di Euro …<br>Impossibile Continuare!* | Lo stesso caso, ma l'installazione è configurata per **non** consentire lo sconfinamento. | Non si prosegue: o si incassa qualcosa, o si alza il fido nell'anagrafica del cliente. |
| *Non e' stato inserito il destinatario !<br>Vuoi inserirlo ?* | Manca la destinazione della merce. | **Sì** apre la scelta del destinatario. |
| *Indicare il tipo di pagamento !* | Manca il [tipo di pagamento](../contabilita/tipi-di-pagamento.md). | Va indicato: da lì nascono le scadenze. |
| *Il tipo di pagamento non e' stato impostato.<br>Sara' richiesto al momento della fatturazione!* | Su un documento che diventerà fattura più avanti. | Non è un errore: il pagamento verrà chiesto all'emissione della fattura. |
| *Scadenza non indicata!<br>Vuoi Continuare ?* | Il pagamento prevede una scadenza che non è stata scritta. | **Sì** salva senza; la scadenza andrà poi messa a mano nello [scadenzario](../scadenze/gestione-scadenze.md). |

### Quando si scrivono le righe

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Attenzione!<br>Articolo Inesistente<br>Codice … Q.ta …* | Il codice digitato non è in [anagrafica](../anagrafiche/anagrafica-articoli.md). | Controllare il codice o creare l'articolo. |
| *Codice … non corrispondente ad alcun articolo in archivio!* | Lo stesso caso, leggendo da un lettore o da un file. | Come sopra. |
| *Riga N. …<br>Esistenza non sufficiente per effettuare la vendita!* | L'esistenza dei depositi che l'utente può vedere non copre la quantità. | Controllare la giacenza: può anche essere un carico non ancora registrato. |
| *L'articolo selezionato ha superato la Scorta Max impostata!* | La riga porta l'articolo oltre la scorta massima. | È un avviso: si prosegue. |
| *Non sono ammesse quantità con decimali!* | L'articolo si vende a pezzi interi. | Correggere la quantità. |
| *Non sono ammesse quantita' con decimali nella gestione delle Matricole!<br>Articolo …* | L'articolo è gestito a matricola: ogni pezzo è un pezzo. | Come sopra. |
| *Attenzione!<br>Gestione Lotti attiva per l'articolo selezionato.<br>Vuoi Forzare?* | L'articolo vuole il [lotto](../analisi-dati/analisi-lotti.md) e non è stato indicato. | **No** torna sulla riga per indicarlo; **Sì** vende senza lotto, e la tracciabilità si perde. |
| *Lotto Mancante!<br>Vuoi Continuare ?* | Come sopra, in fase di controllo del documento. | Come sopra. |
| *Non c'è giacenza sufficiente per il lotto indicato!* | Il lotto scelto non ha abbastanza merce. | Scegliere un altro lotto o dividere la riga. |
| *GTIN Mancante!<br>Vuoi Continuare ?* | L'articolo non ha il codice a barre, richiesto da questo tipo di documento. | Conviene aggiungerlo in anagrafica. |
| *Attenzione!<br>Listino di vendita non impostato.<br>Saranno utilizzati i prezzi di acquisto.* | Il documento non ha un listino. | I prezzi proposti saranno quelli di acquisto: è quasi sempre da correggere. |
| *Impostare l'Aliquota Iva Predefinita prima di Continuare!* | Manca l'[aliquota](../contabilita/aliquote-iva.md) predefinita nelle impostazioni della ditta. | Va impostata una volta per tutte. |
| *Il tipo di documento selezionato non puo' contenere articoli fiscali!* | Si sta mettendo un articolo fiscale — tabacchi, valori bollati — in un documento che non li ammette. | Serve il tipo di documento giusto. |

### Quando il cliente è una pubblica amministrazione

Questa famiglia di messaggi nasce tutta dallo stesso controllo: la ditta ha
**un registro, una causale e una sezione dedicati** alle fatture e alle note
di credito verso la PA, e il documento deve usare quelli.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Il Cliente e' una pubblica amministrazione!<br>Vuoi utilizzare il registro e la causale per le Fatture PA ?* | Il cliente è marcato come PA. | **Sì** cambia registro e causale da sé: è la risposta giusta quasi sempre. |
| *Il Destinatario e' una pubblica amministrazione!<br>Vuoi utilizzare il registro e la causale per le Fatture PA ?* | Come sopra, quando è il destinatario a essere una PA. | Come sopra. |
| *Registro Documento non coincide con Registro Fatture PA impostato sulla Ditta!<br>Vuoi continuare ?* | Il documento usa un registro diverso da quello dedicato. | **No** e si corregge il registro: proseguire porta a una fattura che l'invio rifiuterà. |
| *Causale Contabile Documento non coincide con Causale Contabile Fatture PA impostata sulla Ditta!<br>Vuoi continuare ?* | Come sopra, per la causale. | Come sopra. |
| *Sezione Documento non coincide con Sezione Causale Contabile Fatture PA impostata sulla Ditta!<br>Vuoi continuare ?* | Come sopra, per la sezione. | Come sopra. |
| *Registro Fatture PA non impostato su Ditta!* | Nelle impostazioni della [ditta](../anagrafiche/ditte.md) manca il registro dedicato. | Va impostato prima di emettere fatture alla PA. |
| *Causale Contabile Fatture PA non impostata su Ditta o non valida!* | Manca la causale dedicata. | Come sopra. |
| *Sezione Fatture PA non impostata sulla Causale Contabile Fatture PA o non valida!* | La causale dedicata non ha la sezione. | Come sopra. |
| *Il documento risulta gia' inviato alla PA!<br>Vuoi continuare ?* | Si sta modificando un documento già trasmesso. | **No**. Quello che è stato inviato si corregge con una nota di credito, non riscrivendolo. |
| *Il documento non contiene righe di dettaglio dei beni/servizi!* | La fattura elettronica non ha righe. | Va compilato il corpo. |
| *Codice abilitazione per l' invio e il controllo esiti delle Fatture PA non impostato.<br>Contattare la R.S.A. … per ottenere ed impostare il codice.* | Manca il codice di abilitazione al servizio di invio. | È R.S.A. a fornirlo. |
| *Impostare codice fiscale sulla ditta!* / *Partita iva non impostata sulla ditta!* | Mancano i dati della ditta emittente. | Si completano nella scheda della ditta. |
| *Identificativo Nazione (ISO alpha-2) non impostato su ditta!* / *Il codice nazione impostato sulla ditta deve essere di due caratteri!* | Il codice nazione della ditta manca o è scritto male. | Deve essere di due lettere, per esempio `IT`. |

Le stesse identiche righe esistono per le **note di credito**, con «Note
Credito PA» al posto di «Fatture PA».

### Quando si salva, si stampa o si invia

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *IL documento e' ancora bloccato!<br>Vuoi sbloccarlo ?* | Il documento è bloccato — di solito perché aperto altrove, o lasciato aperto da una sessione caduta. | **Sì** lo sblocca, ma solo per gli utenti che ne hanno il permesso. |
| *Per poter eseguire la stampa il documento deve essere sbloccato!* | Come sopra, al momento della stampa. | Va sbloccato prima. |
| *Per il documento risultano gia' incassi per … Euro.<br>Se continui con l' operazione e non ristampi il documento, devi correggere manualmente lo scadenzario.<br>Vuoi Continuare ?* | Si sta modificando un documento su cui sono già stati registrati incassi (o pagamenti, per l'autofattura). | Leggerlo bene: proseguendo **senza ristampare**, lo scadenzario resta con i vecchi importi e va sistemato a mano. |
| *Confermi la stampa della fattura ?* | Conferma prima di stampare. | È il momento in cui il documento **diventa emesso**: magazzino, scadenze e provvigioni si muovono adesso. |
| *Vuoi Stampare il Documento?* | Proposta di stampa dopo il salvataggio. | **No** lascia il documento salvato ma non emesso. |
| *Vuoi Contabilizzare il documento ?* | Proposta di [contabilizzazione](contabilizzazione-documenti.md). | **Sì** genera la registrazione di prima nota. |
| *Impossibile trovare il documento in archivio!* | Il documento non c'è più: qualcuno l'ha eliminato. | Ricaricare l'elenco. |
| *Il record richiesto non è presente in archivio.* | Un codice richiamato dal documento non esiste più. | Controllare i codici della testata. |
| *Record di un archivio relazionato non trovato!* | Manca una tabella collegata — pagamento, banca, aliquota. | Va ripristinata la voce mancante. |
| *SMTP Server non impostato !* | Si è premuto **F9 - Email** senza il server di posta configurato. | Si imposta nella scheda della [ditta](../anagrafiche/ditte.md). |
| *Mittente Email non impostato !* | Manca l'indirizzo del mittente. | Si imposta sull'[utente](../anagrafiche/utenti.md) o sulla postazione. |
| *Errore CrystalReport …* | Il modello di stampa non si apre o non trova i dati. | Riportare all'assistenza il testo completo: contiene il nome del report e il codice dell'errore. |

!!! warning "Il messaggio sugli incassi già registrati è il più costoso da ignorare"

    *Per il documento risultano gia' incassi per … Euro* significa che il
    documento che si sta cambiando ha già una vita nello scadenzario.
    Rispondendo **Sì** e non ristampando il documento, gli importi in
    scadenza restano quelli di prima: il cliente risulterà debitore della
    cifra sbagliata, e la differenza salterà fuori al primo sollecito.

### Le righe che arrivano da fuori

Quando il corpo del documento non si scrive ma si **importa** — da un foglio
Excel, da un file del fornitore, da un carico merci, da uno scontrino — i
controlli sono altri.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Colonna CODICE non trovata nel documento !* | Il foglio Excel non ha la colonna del codice. | È obbligatoria: il foglio va sistemato. |
| *Colonna PREZZO non trovata nel documento !<br>Continuando nell'importazione saranno inseriti i prezzi del listino associato al documento.<br>Vuoi continuare?* | Manca la colonna del prezzo. | **Sì** prende i prezzi dal listino: va bene se i prezzi sono i propri, non se erano quelli del fornitore. |
| *Nessuna tra le Colonne QUANTITA o COLLI e' stata trovata nel documento !* | Manca la quantità. | Serve almeno una delle due colonne. |
| *Nessun codice articolo presente per la riga n. …<br>La riga sara' scartata e dovra' essere inserita manualmente!* | Una riga del file non ha codice. | La riga **non entra**: va aggiunta a mano. |
| *Non e' possibile accoppiare l'articolo della riga n. …<br>La riga sara' scartata e dovra' essere inserita manualmente!* | Il codice della riga non si aggancia a nessun articolo. | Come sopra. |
| *Impossibile aprire il file excel!* / *Impossibile accedere al foglio!* | Il file è aperto altrove o non è leggibile. | Chiuderlo in Excel e riprovare. |
| *In archivio non e' stato trovato nessun documento col numero e data corrispondenti al carico merci!<br>Impossibile continuare.* | Si sta generando un'autofattura da un carico che non ha documento. | Il carico va completato prima. |
| *In archivio sono stati trovati piu' documenti con stesso numero e data!<br>Impossibile continuare.* | Due documenti hanno lo stesso numero e la stessa data. | Vanno distinti prima di procedere. |
| *Il fornitore del carico non coincide con l' intestatario dell' Autofattura !* | L'autofattura è intestata a un soggetto diverso dal fornitore del carico. | Si corregge l'intestatario. |
| *La data del carico non coincide con la data dell' Autofattura !<br>Vuoi adeguare la data dell' Autofattura ?* | Le due date non coincidono. | **Sì** allinea la data. |
| *Data Documento non coincide con data scontrino!* / *La data dello scontrino non coincide con la data della Fattura !<br>Vuoi adeguare la data della Fattura ?* | Si sta emettendo una fattura da uno [scontrino](scontrini.md) di un altro giorno. | **Sì** allinea. |
| *Al carico sono gia' associati documenti fiscali!<br>Vuoi Continuare ?* | Il carico ha già generato un documento. | **No**, a meno di sapere perché lo si sta rifacendo. |

### Quello che il programma non dice

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio. | Guarda dove si è posizionato il cursore: è il campo da compilare. |

!!! note "I messaggi che non trovi qui"

    Restano fuori quelli delle lavorazioni che hanno una pagina propria — la
    [fattura elettronica](fatture-elettroniche-attive.md), gli
    [scontrini](scontrini.md), i [documenti accompagnatori](documenti-accompagnatori-semplificati.md),
    le [casse e bilance](../casse-bilance/casse.md) — e quelli delle
    installazioni con gestioni particolari, come i tabacchi o l'ortofrutta.

## Note

!!! note "Una maschera per tutti i documenti"

    Fatture, DDT, bolle, buoni di consegna, ricevute fiscali, autofatture e
    ordini si compilano tutti qui: cambia il registro e cambiano alcuni campi,
    ma il modo di lavorare è lo stesso. I **preventivi** fanno eccezione e
    hanno la [loro maschera](preventivi.md).

!!! warning "Il magazzino si scarica alla stampa, non al salvataggio"

    **F2 - Salva** registra il documento e basta: la merce non si muove, le
    scadenze non nascono, le provvigioni non maturano. Il documento resta una
    bozza, in stato *salvato*.

    Tutto succede quando il documento viene **emesso**, cioè con **F7 -
    Stampa** (o con l'emissione in blocco). In quel momento, e una volta sola,
    il programma:

    - **scarica il magazzino** delle righe;
    - genera le **scadenze** secondo il tipo di pagamento;
    - calcola e registra le **provvigioni** dell'agente.

    **Annullare** il documento fa il percorso inverso: la merce torna in
    magazzino e scadenze e provvigioni vengono tolte.

    È il motivo per cui una bozza non si vede nelle giacenze e non compare nello
    scadenzario: finché non è stampata, per il resto del programma non esiste.

!!! note "Cosa cambia nella testata secondo il tipo di documento"

    I campi sono sempre gli stessi: quello che cambia sono **le etichette** e,
    in pochi casi, la sparizione di un campo.

    Le due coppie in basso si rinominano così:

    | Documento | Primo numero e data | Numero e data di riferimento |
    |---|---|---|
    | Fattura | Num. Fattura / Data Fattura | Numero Scontrino / Data Scontrino |
    | Fattura pro forma | Numero Doc. / Data Doc. | Doc. Riferimento / Data Doc. Rif. |
    | Documento di trasporto | Num. D.D.T. / Data D.D.T. | Num. Fattura / Data Fattura |
    | Bolla | Num. Bolla / Data Bolla | Num. Fattura / Data Fattura |
    | Buono di consegna | Num. Buono / Data Buono | Num. Fattura / Data Fattura |
    | Ricevuta fiscale | Num. Ricevuta / Data Ricevuta | Num. Doc. Rif. / Data Doc. Rif. |
    | Autofattura | Num. Autofat. / Data Autofat. | Num. Doc. Rif. / Data Doc. Rif. |
    | Ordine cliente e ordine ricorrente | Num. Ordine / Data Ordine | Num. Doc. Rif. / Data Doc. Rif. |
    | Ordine a fornitore | Num. Ordine / Data Ordine | Num. Doc. Rif. / Data Doc. Rif. |
    | Richiesta di offerta | Num. Richiesta / Data Rich. | V/S Offerta / Data Offerta |
    | Reso da cliente | Num. Reso / Data Reso | Numero Nota Cre. / Data Nota Cre. |
    | Anomalia | Num. Anomalia / Data Anomalia | Doc. Riferimento / Data Doc. Rif. |

    E questi campi spariscono:

    - **Consegna** c'è **solo sugli ordini**, clienti e fornitori;
    - **Ric. Fiscale / Raggruppa** non c'è su ricevute fiscali, autofatture,
      richieste di offerta e anomalie;
    - **Registro** sparisce se la [ditta](../anagrafiche/ditte.md) è impostata a
      registro unico;
    - sulle **anomalie** spariscono anche **Tipo Documento**, **Cau.
      Magazzino** e **Add. Spese**, e **Cau. Contabile** diventa *Oggetto*.


!!! note "Che cosa stampa il pulsante Tracc."

    Le **etichette di tracciabilità** delle righe del documento: aperto il
    pulsante si sceglie fra **Etichette Logistiche** ed **Etichette
    Commerciali**, e il programma usa il modello di etichetta impostato nella
    ditta.

    Vengono stampate solo le righe complete: quelle con la **gestione lotti**
    attiva sull'articolo e con **lotto**, **GTIN** e **data di scadenza**
    compilati. Una riga a cui manca uno dei tre non produce etichetta.

    Il pulsante c'è solo se nella ditta è attiva la gestione dei lotti.

## Vedi anche

- [Gestione documenti](gestione-documenti.md)
- [Preventivi](preventivi.md)
- [Emissione fatture da documenti](emissione-fatture-da-documenti.md)
- [Contabilizzazione dei documenti](contabilizzazione-documenti.md)
