---
title: Fatture elettroniche attive
description: L'invio massivo delle fatture elettroniche emesse e il cruscotto da cui se ne segue lo stato.
modulo: Vendite
maschera_id: IDD_VEN_FATTURE_INVIO, IDD_VEN_CRUSCOTTO_FATTURE_PA
---

# Fatture elettroniche attive

Le fatture emesse vanno trasmesse per via elettronica e il loro esito va
seguito. **Invio Massivo** le manda in blocco, il **Cruscotto** mostra a che
punto sono.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Vendite ▸ Fatture ▸ Invio Massivo Fatture Elettroniche
        - Menu ▸ Vendite ▸ Fatture ▸ Cruscotto Fatture Elettroniche
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md); serve anche **Abilita download Stati Fatture Attive** sull'utente

---

## A cosa serve

**Invio Massivo Fatture Elettroniche** prende le fatture emesse e non ancora
trasmesse e le manda tutte insieme, invece di una per volta dal documento.

**Cruscotto Fatture Elettroniche** è il quadro degli esiti: quali sono partite,
quali sono state accettate, quali scartate e vanno rifatte.

## Prerequisiti

Prima di usare queste maschere occorre:

- avere emesso le [fatture](documento-di-vendita.md) con il **Tipo Documento**
  giusto;
- avere i dati fiscali dei clienti completi, compreso il codice destinatario o
  la PEC;
- avere **credito** sul servizio di trasmissione;
- avere l'utente abilitato al download degli stati: è l'unica condizione per
  sincronizzare, da qualsiasi computer.

## La maschera

![Cruscotto fatture elettroniche](../../assets/img/vendite/fatture-elettroniche-attive.png)

Sono due finestre a griglia: l'elenco dei documenti con il loro stato, e i
comandi per mandarli e per aggiornare gli esiti.

Sono **due finestre diverse**, una per mandare e una per seguire.

**Invio Fatture Emesse** ha in alto i filtri, e sotto una griglia con le
fatture da mandare: si spuntano quelle che interessano e si preme *Invio*.

**Cruscotto Fatture Elettroniche** ha in alto i filtri e sotto **due griglie**: quella
grande con le fatture e le autofatture inviate — numero, data, **Tipo** (il tipo
documento della fattura elettronica: TD01 fattura, TD04 nota di credito, TD17
integrazione per servizi dall'estero…), **Intestatario**,
partita IVA, totale e stato; l'autofattura si riconosce dal registro nel numero,
e il suo intestatario è il fornitore quando è intestata a un fornitore —
e sotto, per la fattura selezionata, quella degli **esiti**: un'icona, la data,
l'ora, lo **Stato** e il **Messaggio**. Gli esiti cambiano scorrendo le righe
della griglia di sopra.

L'icona dello stato è una busta con un tondo colorato: il colore dice a che
punto è la fattura, il simbolo dentro il tondo dice quale esito è arrivato.
Azzurro vuol dire che la fattura è in viaggio, verde che è arrivata, giallo che
c'è da guardare, rosso che è stata respinta, grigio che è ancora in attesa o
che l'esito è solo informativo. Le stesse icone compaiono nella griglia degli
esiti, una per ogni notifica.

| Icona | Stato |
|:---:|---|
| ![](../../assets/img/vendite/stati-fe/lavorazione.png){ width="24" } | In lavorazione: non è ancora partita. |
| ![](../../assets/img/vendite/stati-fe/inviata-ftp.png){ width="24" } | Partita verso il servizio di trasmissione, nessuna risposta ancora. |
| ![](../../assets/img/vendite/stati-fe/fe-inviato.png){ width="24" } | Presa in carico dal servizio di trasmissione. |
| ![](../../assets/img/vendite/stati-fe/firmato.png){ width="24" } | Inviata allo SdI: il servizio di trasmissione ha preparato la fattura e l'ha inviata al Sistema di Interscambio. |
| ![](../../assets/img/vendite/stati-fe/conservazione.png){ width="24" } | Inviata in conservazione: la fattura è stata mandata in conservazione e non è ancora arrivato un esito dallo SdI. |
| ![](../../assets/img/vendite/stati-fe/fe-esito-committente.png){ width="24" } | Esito inviato dalla PA. |
| ![](../../assets/img/vendite/stati-fe/ricevuta-di-consegna.png){ width="24" } | Consegnata: è arrivata la ricevuta di consegna. |
| ![](../../assets/img/vendite/stati-fe/fe-accettata.png){ width="24" } | Accettata dalla PA (pubblica amministrazione). |
| ![](../../assets/img/vendite/stati-fe/notifica-decorrenza-termini.png){ width="24" } | Decorrenza termini: la PA non ha risposto entro 15 giorni. |
| ![](../../assets/img/vendite/stati-fe/impossibilita-di-recapito.png){ width="24" } | Trasmessa, ma con impossibilità di recapito. |
| ![](../../assets/img/vendite/stati-fe/notifica-di-mancata-consegna.png){ width="24" } | Mancata consegna: la fattura è nel cassetto fiscale del cliente. |
| ![](../../assets/img/vendite/stati-fe/fe-metadati.png){ width="24" } | Dati di trasmissione del file. |
| ![](../../assets/img/vendite/stati-fe/fe-scarto-esito.png){ width="24" } | L'esito della PA è stato scartato dallo SdI. |
| ![](../../assets/img/vendite/stati-fe/scartata.png){ width="24" } | Scartata dal servizio di trasmissione prima di partire: va corretta e rimandata. |
| ![](../../assets/img/vendite/stati-fe/notifica-di-scarto-sdi.png){ width="24" } | Scartata dal Sistema di Interscambio. |
| ![](../../assets/img/vendite/stati-fe/fe-rifiutata.png){ width="24" } | Rifiutata dalla PA (pubblica amministrazione). |

## Campi

### Invio Fatture Emesse

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | | Il periodo delle fatture da elencare. | date |
| **Cliente** | | Restringe a un cliente. | codice |
| **Visualizza documenti già inviati** | | Mostra anche quelle già trasmesse, che di norma spariscono dall'elenco. | attivo/non attivo |

### Cruscotto Fatture Elettroniche

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | | Il periodo. | date |
| **Tipo Doc.** | | Mostra solo le fatture, solo le autofatture o solo le integrazioni. Sono integrazioni i documenti con tipologia da TD16 a TD19 (reverse charge interno, acquisto di servizi dall'estero, acquisto di beni intracomunitari, acquisto di beni ex art. 17 c. 2); le autofatture sono quelle da TD20 in poi. Vale insieme a **Filtra**. | `TUTTE`, `FATTURE`, `AUTOFATTURE`, `INTEGRAZIONI` |
| **Filtra** | | Mostra solo i documenti in uno stato, con i nomi della legenda delle icone. **DA CONTROLLARE** raccoglie quelli su cui intervenire: scartati, rifiutati dal committente, non consegnati o con impossibilità di recapito. | `TUTTE`, `DA CONTROLLARE`, `INVIATA, NESSUNA RISPOSTA`, `PRESA IN CARICO DA DIGITHUB`, `SCARTATA DA DIGITHUB`, `FIRMATA E INVIATA ALLO SDI`, `SCARTATA DALLO SDI`, `CONSEGNATA`, `MANCATA CONSEGNA`, `IMPOSSIBILITÀ DI RECAPITO`, `ACCETTATA DAL COMMITTENTE`, `RIFIUTATA DAL COMMITTENTE`, `DECORRENZA TERMINI`, `IN CONSERVAZIONE` |

!!! tip "I due scarti non sono la stessa cosa"

    **SCARTATA DAL SERVIZIO DI TRASMISSIONE** è una fattura fermata dall'intermediario prima di
    partire; **SCARTATA DALLO SDI** una partita e respinta dal Sistema di
    Interscambio. Le prime si correggono e si rimandano subito; le seconde
    hanno un esito ufficiale da leggere.

## Pulsanti e comandi

### Invio Fatture Emesse

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **Selez. Tutti**, **Deselez. Tutti** | | Spunta o toglie la spunta a tutte le righe. |
| **F2 - Invio** | ++f2++ | Manda le fatture spuntate. |
| **F3 - Esporta** | ++f3++ | Salva il documento in XML. |
| **F4 - Modifica Doc.** | ++f4++ | Apre il documento selezionato. |
| **F5 - Modifica Cliente** | ++f5++ | Apre il cliente del documento, per correggerne i dati. |
| **F6 - Email** | ++f6++ | Manda la fattura per email. |
| **F7 - Trova** | ++f7++ | Cerca nella griglia. |

### Cruscotto Fatture Elettroniche

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Sincronizza** | ++f2++ | Scarica gli esiti nuovi e aggiorna lo stato delle fatture. Compare solo se sull'utente è acceso **Abilita download Stati Fatture Attive**; la stessa operazione parte anche da sola all'apertura (vedi le note). Durante il lavoro il pulsante diventa **Interrompi**. |
| **F3 - Credito Residuo** | ++f3++ | Calcola quante trasmissioni restano. |
| **F4 - Esporta** | ++f4++ | Esporta in XML. |
| **F5 - Trova** | ++f5++ | Cerca nella griglia. |
| **F6 - https://fatture.facilecloud.net** | ++f6++ | Apre il portale nel browser. Compare solo se il codice cliente per le fatture PA è impostato sulla ditta. |
| **F7 - Salva Esito** | ++f7++ | Salva il file dell'esito selezionato nella griglia degli esiti: propone la cartella `out` dell'utente e il nome originale del file. |
| **F8 - Visualizza Esito** | ++f8++ | Apre il file dell'esito selezionato con il programma predefinito per quel tipo di file; se Windows non ne ha uno, con il Blocco note. È lo stesso del doppio clic sulla riga. |
| doppio clic su una riga degli esiti | ++enter++ | Come **F8 - Visualizza Esito**. Per salvare il file c'è **F7 - Salva Esito**. |

**F7 - Salva Esito** e **F8 - Visualizza Esito** sono attivi solo quando nella
griglia degli esiti è selezionata una riga che ha il suo file: restano spenti se
la griglia è vuota o se l'esito non ha un allegato.

La finestra **Esiti Fatture Elettroniche** che si apre dal documento
(**Fatture Elettroniche** ▸ **Controlla Esiti**) ha gli stessi tre comandi:
**F2 - Sincronizza** (anche qui solo se sull'utente è acceso **Abilita download
Stati Fatture Attive**), **F7 - Salva Esito** e **F8 - Visualizza Esito**.

## Come si fa

### Trasmettere le fatture del giorno

1. Emetti e controlla le fatture dalla
   [gestione documenti](gestione-documenti.md).
2. Apri **Menu ▸ Vendite ▸ Fatture ▸ Invio Massivo Fatture Elettroniche**.
3. Avvia l'invio.
4. Il giorno dopo apri il **Cruscotto** e controlla gli esiti.

### Aggiornare gli esiti

1. Apri il **Cruscotto Fatture Elettroniche**: se l'utente è abilitato, la
   sincronizzazione parte da sola e mostra una barra di avanzamento.
2. Per ripeterla in qualunque momento premi **F2 - Sincronizza**.
3. Se vuoi fermarla premi **Interrompi**: i file già scaricati restano, e il
   resto viene ripreso alla sincronizzazione successiva.
4. Leggi il messaggio finale: dice quanti file sono stati sincronizzati ed
   eventuali problemi (vedi *Controlli e messaggi*).

Gli esiti di una sola fattura o autofattura si vedono anche dal
[documento](documento-di-vendita.md): **Fatture Elettroniche** ▸ **Controlla Esiti**.

### Rimandare una fattura già inviata

1. Dalla gestione documenti o da **Invio Fatture Emesse** avvia l'invio e
   rispondi **Sì** alla domanda *Vuoi inviare il documento ?*.
2. Se la fattura risulta già inviata, compare un avviso: leggilo con
   attenzione, perché un secondo invio dello stesso documento viene quasi
   sempre scartato come duplicato.
3. Premi **Annulla** per rinunciare, oppure **OK** per mandarla comunque.

    L'avviso compare solo quando mandi **una fattura alla volta**: se ne
    selezioni più di una in **Invio Fatture Emesse**, l'invio procede senza
    domande e senza avviso.

### Rimediare a una fattura scartata

1. Nel **Cruscotto** individua il documento scartato e leggi il motivo.
2. Correggi il documento o l'anagrafica del cliente.
3. Rimanda il documento, dalla gestione documenti con **F8 - Forza Invio**
   oppure con un nuovo invio massivo.

## Controlli e messaggi


### Invio Fatture Emesse

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Nessuna Fattura è stata selezionata per l'invio dell'Email!* | Nessuna riga spuntata. | Spuntare le fatture. |
| *Impossibile trovare il documento in archivio!* | Il documento della riga non c'è più. | Ricaricare l'elenco. |
| *Impossibile trovare il cliente in archivio!* | Il cliente è stato cancellato. | Sistemare l'anagrafica. |
| *Registro Fatture PA non impostato sulla Ditta!* — e le gemelle su causale contabile, sezione e note di credito | Mancano le impostazioni fiscali per le fatture PA, o quelle del documento non coincidono. | Rispondere **No** e sistemare [Ditte](../anagrafiche/ditte.md); continuare manda un documento che può essere scartato. |
| *La fattura risulta già consegnata: un nuovo invio sarà scartato come duplicato. Per correggerla emetti una nota di credito.* | La fattura ha già un esito vero dal Sistema di Interscambio (consegna, mancata consegna, impossibilità di recapito, esito del committente, decorrenza dei termini) o è già in conservazione, e si sta per mandarla di nuovo. L'avviso non blocca: ha i pulsanti **OK** e **Annulla**. | **Annulla**, e per correggere la fattura emettere una nota di credito. **OK** solo se sai perché serve un secondo invio. |
| *La fattura è già stata inviata e l'esito non è ancora arrivato: un nuovo invio sarà quasi certamente scartato come duplicato.* | La fattura è già stata mandata, ma la sincronizzazione non ha ancora portato l'esito. Anche questo avviso non blocca. | Premere **Annulla**, sincronizzare dal Cruscotto con **F2 - Sincronizza** e controllare l'esito; mandarla di nuovo solo se è stata scartata. |
| *… contiene un carattere non valido (…) alla posizione …<br><br>Vuoi continuare ?* | Generando il file della fattura: un campo contiene un carattere che il tracciato della fattura elettronica non ammette in quel punto. Il messaggio dice quale campo (per esempio *Il codice CUP*, *Il numero del documento di riferimento*, *Il numero REA*, *La descrizione della riga 3*), il valore, il codice del carattere e la sua posizione. Vedi la nota *Quali caratteri sono ammessi*, più sotto. | Rispondere **No**, correggere il campo indicato e rigenerare il file. Rispondendo **Sì** il file viene generato lo stesso, ma il Sistema di Interscambio lo scarterà. |
| *Il codice del buono Carta del Docente nella riga … e' lungo … caratteri: il massimo e' 35.<br><br>Vuoi continuare ?* | Il codice del buono, scritto nelle note della riga, supera la lunghezza che il tracciato ammette. | Rispondere **No** e correggere il codice del buono nelle note della riga. |
| *Il Sistema di Interscambio scarterebbe questa fattura:<br><br>- … (controllo …)<br><br>Vuoi continuare ?* | Generando il file della fattura: il programma rifà sul file i controlli che il Sistema di Interscambio farà alla ricezione, e almeno uno non è superato. Ogni riga dice cosa non va e il codice del controllo (per esempio *il totale della riga 3 (12,50) non corrisponde a prezzo, sconti e quantità (12,35) (controllo 00423)*). Se sono più di dieci si vedono i primi dieci. Vedi la nota *I controlli del Sistema di Interscambio*, più sotto. | Rispondere **No**, correggere il documento o l'anagrafica indicata e rigenerare il file. Rispondendo **Sì** il file viene salvato ma la fattura non viene inviata. |
| *Esportazione Conclusa!* | In tutte e due le maschere: l'XML è stato scritto. | — |

### Cruscotto Fatture Elettroniche

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Sincronizzazione completata: …* seguito dal numero di file | È il riepilogo di fine sincronizzazione, con il numero di file scaricati. Può essere anche 0 se non c'era niente di nuovo. All'apertura del cruscotto compare solo se c'è qualcosa da dire. | — |
| *Sincronizzati … file su …: connessione persa, i rimanenti saranno scaricati alla prossima sincronizzazione.* | La linea è caduta e le riprese automatiche non sono bastate. | Niente: quello che manca verrà scaricato alla prossima sincronizzazione. Se si ripete, controllare la connessione. |
| *Sincronizzazione interrotta: sincronizzati … file su …, i rimanenti saranno scaricati alla prossima sincronizzazione.* | Hai premuto **Interrompi**. | Niente: il lavoro fatto resta e il resto riprende alla prossima sincronizzazione. |
| *File non scaricati per un errore: …. Restano sull'FTP e saranno riprovati alla prossima sincronizzazione.* | Alcuni file non si sono potuti scaricare. | Niente: saranno riprovati; se il numero non cala, contattare l'assistenza. |
| *Stati dal web service non salvati: …. Il dettaglio è nel registro degli errori.* | Alcuni stati letti dal web service di Digithera non si sono potuti registrare: per esempio una notifica non riconosciuta, uno stato di consegna arrivato senza la sua notifica, oppure uno stato che l'archivio ha rifiutato per più sincronizzazioni di seguito. | Contattare l'assistenza, che legge il dettaglio nel registro degli errori. |
| *Stati dal web service: letti i primi …, i rimanenti alla prossima sincronizzazione.* | Gli stati in attesa erano molti: la sincronizzazione ne legge un certo numero per volta. | Ripetere la sincronizzazione (++f2++) finché il messaggio non compare più. |
| *Stati dal web service non letti: …. Saranno riletti alla prossima sincronizzazione.* | Gli stati che Digithera mette a disposizione tramite il web service non si sono potuti leggere (il motivo segue i due punti). | Niente: si rileggono alla sincronizzazione successiva; se il messaggio si ripete, contattare l'assistenza. |
| *Accesso all'FTP di Digithera rifiutato: controllare le credenziali.* | Il servizio non ha accettato la password del collegamento. | Controllare il collegamento nella scheda **Fatture Elettroniche** di [Ditte](../anagrafiche/ditte.md). |
| *Vuoi eseguire adesso il controllo degli esiti del …?* (oppure *Vuoi riprendere adesso…*) | Dopo una sincronizzazione, la prima volta in un anno su quel computer: il programma propone il controllo periodico delle notifiche. | **Esegui adesso** per farlo subito, **Più tardi** per farselo richiedere alla prossima sincronizzazione, **Non eseguire e non chiedere più** per saltarlo per quell'anno. Vedi la nota *La prima volta in un anno può volerci qualche minuto*. |
| *Controllo periodico degli esiti … completato: aggiornato lo stato di … fatture.* (oppure *… di 1 fattura.*) | Esito del controllo periodico che si fa una volta per ogni anno su ogni computer (vedi le note). Compare solo se ha aggiornato lo stato di qualche fattura. | — |
| *Controllo periodico degli esiti … sospeso: riprenderà alla prossima sincronizzazione.* | Il controllo è stato fermato prima della fine. | Niente: riprende da solo alla prossima sincronizzazione. |
| *Reinvio scartato come duplicato: al cliente è arrivata la versione del primo invio* | Nella griglia degli esiti, colonna **Messaggio**: la fattura è stata mandata una seconda volta e il Sistema di Interscambio ha scartato il secondo invio perché già consegnato. | Niente: la consegna del primo invio resta valida e lo stato della fattura non cambia. |
| *Credito Esaurito! E' necessario acquistare del credito per poter effettuare l' invio. Impossibile continuare.* | Con **F3 - Credito Residuo**: finite le trasmissioni disponibili. | Acquistare credito. |
| *Credito Acquistato …*, *Credito Utilizzato …*, *Credito Residuo …* | Con **F3 - Credito Residuo**: il riepilogo delle trasmissioni acquistate, usate e rimaste. | — |
| *Identificativo Nazione (ISO alpha-2) non impostato su ditta!* / *Il codice nazione impostato sulla ditta deve essere di due caratteri!* / *Partita iva non impostata sulla ditta!* / *Server Digithub non impostato su ditta!* | Con **F2 - Sincronizza**: sulla ditta manca, o è sbagliato, un dato che serve per collegarsi. | Compilarlo in [Ditte](../anagrafiche/ditte.md): nazione e partita IVA nei dati della ditta, il server nella scheda **Fatture Elettroniche**. |
| *Impossibile scrivere il file '…'.* | Con **F4 - Esporta**: il file XML non si è potuto scrivere nella cartella scelta (cartella protetta, disco pieno, percorso troppo lungo). L'esportazione si ferma. | Scegliere un'altra cartella e ripetere l'esportazione. |
| *Impossibile aprire il browser!* | Con **F6**: Windows non è riuscito ad aprire il portale nel browser predefinito. | Controllare che ci sia un browser predefinito e riprovare. |
| *Errore di comunicazione! Impossibile contattare l'Authorization Server. Attendere qualche minuto e riprovare.* | Rete o servizio non raggiungibile. | Attendere qualche minuto e riprovare. |
| *Partita Iva Ditta non impostata!* / *Codice Abilitazione Invio Fatture Elettroniche non impostato!* | Manca un dato sulla ditta. | Compilarlo in [Ditte](../anagrafiche/ditte.md). |
| *Autenticazione Fallita!* | Con **F6** il programma accede al servizio delle fatture elettroniche prima di aprire il portale, e il servizio ha rifiutato l'accesso. | Riprovare; se si ripete, contattare l'assistenza. |
| *Mancata risposta dal server!* | Con **F6** il servizio delle fatture elettroniche non ha risposto. | Controllare la connessione a Internet e riprovare. |
| *POST -> Response status code = …* | Con **F6** il servizio ha risposto con un errore; il numero è il codice dell'errore. | Riprovare; se si ripete, comunicare il numero all'assistenza. |

## Note

!!! note "I controlli del Sistema di Interscambio"

    Prima di inviare una fattura il programma rifà sul file gli stessi
    controlli che il Sistema di Interscambio applica quando la riceve, con le
    stesse tolleranze, così uno scarto si scopre subito e non il giorno dopo:

    - **struttura del file** (controllo 00200): campi obbligatori, lunghezze,
      caratteri e valori ammessi, secondo il tracciato ufficiale;
    - **aliquota e natura IVA** (00400, 00401, 00413, 00414, 00429, 00430,
      00445): la natura c'è solo con aliquota zero, e non è una di quelle
      generiche non più ammesse;
    - **riepilogo IVA** (00419, 00443, 00444): ogni aliquota e ogni natura
      usate nelle righe hanno il loro riepilogo;
    - **calcoli** (00421, 00422, 00423): il totale di ogni riga corrisponde a
      prezzo, sconti e quantità (tolleranza un centesimo), l'imponibile del
      riepilogo alla somma delle righe (tolleranza un euro), l'imposta
      all'imponibile per l'aliquota (tolleranza un centesimo);
    - **date** (00403, 00418): la data del documento non è successiva al
      giorno dell'invio, e una nota di credito non precede la fattura a cui
      si riferisce;
    - **ritenuta** (00411, 00415): se una riga o la cassa previdenziale è
      soggetta a ritenuta ci sono i dati della ritenuta;
    - **scissione dei pagamenti** (00420): non è ammessa con l'inversione
      contabile;
    - **codice destinatario e formato** (00427, 00428);
    - **autofatture e integrazioni** (da 00471 a 00476): chi emette e chi
      riceve sono quelli che il tipo di documento richiede.

    Restano al Sistema di Interscambio i controlli che usano le sue banche
    dati: esistenza di partite IVA e codici fiscali, codice destinatario
    attivo, dichiarazioni d'intento, fattura già ricevuta.

!!! note "Quali caratteri sono ammessi"

    Il tracciato della fattura elettronica non accetta gli stessi caratteri in
    tutti i campi, e il programma li controlla quando genera il file:

    - **testo libero** (denominazione, nome e cognome, indirizzo, comune,
      descrizione delle righe, causale, causale del trasporto, codice della
      commessa o convenzione, riferimenti di testo, banca): lettere, cifre,
      punteggiatura, lettere accentate e i simboli più comuni, compreso il
      grado (°);
    - **codici e numeri** (unità di misura, CUP, CIG, numero dell'ordine, del
      contratto, della convenzione e del DDT, numero REA, telefono e fax):
      solo lettere non accentate, cifre e punteggiatura. Un `N° 12` viene
      scritto nel file come `N. 12` senza segnalazioni; gli altri casi, come
      un'unità di misura `°C`, vengono segnalati e vanno corretti;
    - **codice dell'articolo**: qualsiasi carattere, fino a 35;
    - **ABI e CAB**: solo cifre.

    I caratteri che arrivano da un incolla da Word (virgolette curve, trattini
    lunghi, puntini di sospensione, simbolo dell'euro) non vengono segnalati:
    nel file sono sostituiti dal carattere semplice che corrisponde. Nel codice
    dell'articolo restano invece come sono. I pochi caratteri invisibili che
    un incolla può lasciare nel testo vengono tolti.

!!! note "Lo stato si vede anche nella gestione documenti"

    La colonna **Sync** della [gestione documenti](gestione-documenti.md) dice
    se il documento è stato preso in carico, e **F8 - Forza Invio** lo rimanda.
    Il cruscotto serve quando si vuole il quadro d'insieme.

!!! info "La sincronizzazione parte da sola, ma non da tutti"

    Quando apri il cruscotto, se sull'utente è acceso **Abilita download Stati
    Fatture Attive**, gli esiti vengono scaricati subito, con una barra di
    avanzamento e il pulsante **Interrompi**. Non compare nessun messaggio né se il
    collegamento non è impostato, né se non c'è niente da segnalare. Con **F2 -
    Sincronizza** si ripete a mano quando si vuole.

    Non esiste più un computer "unico" abilitato: basta il permesso
    sull'utente, e si può sincronizzare da qualsiasi postazione.

    I file degli esiti rimasti nella cartella dove li salvavano le versioni
    precedenti vengono portati in archivio dalla sincronizzazione; quelli
    che non sono esiti riconoscibili vengono spostati, senza messaggi, nella
    sottocartella **Non riconosciuti** della stessa cartella.

    La sincronizzazione automatica all'apertura si può disattivare per un
    utente su un computer: chiedere all'assistenza.

!!! note "Se la linea cade, il lavoro riprende"

    Se la connessione si interrompe durante lo scarico, il programma ritenta da
    solo qualche volta, con una breve pausa tra un tentativo e l'altro. Se non
    basta, si ferma e dice quanti file ha sincronizzato; i rimanenti vengono
    scaricati alla sincronizzazione successiva, senza rifare quelli già fatti.

!!! note "Come si decide lo stato di una fattura"

    Lo stato mostrato è quello dell'**ultimo invio**. Quando arrivano più esiti
    vale quello più significativo, in quest'ordine: scarto, esito del
    committente (accettata o rifiutata), decorrenza dei termini, consegna /
    mancata consegna / impossibilità di recapito, conservazione, invio allo SdI, presa
    in carico. Consegna, mancata consegna e impossibilità di recapito contano
    allo stesso modo: vale il più recente.

    Se una fattura viene mandata una seconda volta e il secondo invio è
    scartato come duplicato, **la consegna del primo invio non si cancella**:
    la fattura resta consegnata. La **conservazione** compare come stato solo
    quando non c'è un esito vero.

    Gli esiti si abbinano allo stesso modo sia alle fatture inviate via FTP sia
    a quelle inviate con il servizio API di Digithera, e anche alle autofatture.
    Oltre che dall'FTP, la sincronizzazione li legge anche dal web service di
    Digithera, da cui arrivano soprattutto quelli delle autofatture.

!!! info "La prima volta in un anno può volerci qualche minuto"

    Quando si entra per la prima volta in un anno, la sincronizzazione propone
    un controllo periodico delle notifiche: verifica che ogni notifica sia
    associata alla sua fattura e aggiorna lo stato delle fatture. Prima di
    cominciare chiede cosa fare:

    - **Esegui adesso**: parte il controllo (finestra *Esiti FAE -
      Controllo...*), che può durare alcuni minuti;
    - **Più tardi**: non fa niente e lo richiede alla prossima
      sincronizzazione;
    - **Non eseguire e non chiedere più**: per quell'anno il controllo non
      viene fatto e non viene più proposto su quel computer; lo stato delle
      fatture resta quello attuale.

    Si fa una volta per anno **su ogni computer** (per ogni utente di Windows
    che usa Facile): ripeterlo non cambia niente. Al termine ne dice il
    risultato, se ha aggiornato lo stato di qualche fattura; se lo interrompi,
    riprende dal punto in cui era arrivato.

!!! note "Cosa dicono le righe della griglia degli esiti"

    Ogni riga della griglia di sotto è un passaggio della fattura, dal più
    vecchio al più recente, con la data, l'ora e una frase che dice cosa è
    successo:

    | Nella colonna **Stato** | Cosa vuol dire |
    |---|---|
    | *Presa in carico dal servizio di trasmissione* | Il servizio ha ricevuto il file. |
    | *Elaborata dal servizio di trasmissione* | Il servizio ha controllato e preparato il file per il Sistema di Interscambio. |
    | *Inviata al Sistema di Interscambio* | Il file è in consegna allo SdI. |
    | *Ricevuta dal Sistema di Interscambio, in attesa dell'esito* | Lo SdI ha il file e lo sta controllando: l'esito arriva di solito in poche ore, al massimo in cinque giorni. |
    | *Scartata dal servizio di trasmissione: non è arrivata allo SdI* | Il file non è partito: il motivo è nella colonna **Messaggio**. |
    | *Consegnata al cliente* | È arrivata la ricevuta di consegna. |
    | *Non recapitata: è a disposizione del cliente nella sua area riservata dell'Agenzia delle Entrate* | La fattura è valida ed emessa, ma lo SdI non è riuscito a recapitarla: conviene avvisare il cliente. |
    | *Scartata dal Sistema di Interscambio: va corretta e inviata di nuovo* | La fattura non risulta emessa: il motivo è nella colonna **Messaggio**. |
    | *Trasmessa, ma lo SdI non è riuscito a recapitarla alla PA* | Vale come prova dell'invio: la fattura va fatta avere all'ente in altro modo. |
    | *Accettata dalla PA* / *Rifiutata dalla PA* | L'esito che l'ente ha dato alla fattura. |
    | *Termini decorsi: la PA non ha risposto entro 15 giorni* | L'ente non ha né accettato né rifiutato. |
    | *Inviata in conservazione* | La fattura è stata mandata in conservazione. |

    Quando non c'è altro da dire, nella colonna **Messaggio** compare fra
    parentesi una sigla (per esempio *(RC)* o *(IS_ACQUIRED)*): è il nome
    tecnico del passaggio, utile se chiami l'assistenza.

!!! tip "Il motivo dello scarto sta nella griglia di sotto"

    Selezionando la fattura nella griglia grande, quella in basso mostra la sua
    storia: una riga per esito, con **Stato** e **Messaggio**. Il motivo dello
    scarto è il testo della colonna **Messaggio** dell'ultimo esito.

    Se l'esito ha un allegato — la ricevuta ufficiale — il **doppio clic** sulla
    riga lo apre; per salvarlo c'è **F7 - Salva Esito**, che parte dalla cartella
    `out` dell'utente. Il file è un XML: si apre con il programma che Windows usa
    per quel tipo di file, di solito il browser.

## Vedi anche

- [Gestione documenti](gestione-documenti.md)
- [Documento di vendita](documento-di-vendita.md)
- [Fatture elettroniche passive](../contabilita/fatture-elettroniche-passive.md)
