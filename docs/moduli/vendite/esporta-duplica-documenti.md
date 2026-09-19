---
title: Esportazione, duplicazione e ricezione dei documenti
description: Come si esporta un documento, se ne crea una copia e si ricevono i documenti dai palmari o dal server FTP.
modulo: Vendite
maschera_id: IDD_VEN_DUPLICA_DOC
---

# Esportazione, duplicazione e ricezione dei documenti

Tre gruppi di voci che si ripetono su quasi tutti i tipi di documento:
**Esporta** manda il documento fuori da Facile, **Duplica** ne fa una copia,
**Ricezione** porta dentro i documenti compilati altrove.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Vendite ▸ *(un tipo di documento)* ▸ Esporta
        - Menu ▸ Vendite ▸ *(un tipo di documento)* ▸ Duplica
        - Menu ▸ Vendite ▸ Fatture ▸ Ricezione Fatture da Palmare *(oppure* dal Server FTP*)*
        - Menu ▸ Vendite ▸ Doc. di Trasporto ▸ Riezione D.D.T. da Palmare *(oppure* Ricezione D.D.T. dal Server FTP*)*
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

**Duplica** è la scorciatoia più usata: si riparte da un documento già fatto
invece di ricompilarlo. La copia è un documento nuovo, con numero proprio, che
si può poi correggere.

**Esporta** produce il file del documento per chi lo deve ricevere in forma
elettronica.

**Ricezione da Palmare** e **Ricezione dal Server FTP** portano in archivio i
documenti compilati fuori sede — dall'agente in giro o dal furgone — e li
rendono documenti di Facile a tutti gli effetti.

## Prerequisiti

Per la duplicazione serve solo il documento di partenza. Per la ricezione
occorre che i palmari o il server FTP siano configurati.

## La maschera

![Duplica documento](../../assets/img/vendite/esporta-duplica-documenti.png)

**Duplica** è una finestrella con il documento di partenza, quello di arrivo e
il deposito. **Esporta** è una finestrella con il documento da esportare e il
formato. Le **Ricezioni** non hanno una maschera propria: fanno una domanda e
poi lavorano da sole.

Il titolo della finestra dice sempre su quale documento si sta lavorando —
*Duplicazione Fatture*, *Esporta Ordine Cliente*, e così via.

## Campi

### Duplica

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Numero Riferimento** | ● | Anno, numero e registro del documento da copiare. | anno, numero, lettera |
| **Nuovo Numero** | ● | Anno, numero e registro da dare alla copia. **Lo scegli tu**: il programma non propone il primo libero. | anno, numero, lettera |
| **Deposito Nuovo Doc.** | | Il [deposito](../magazzino/depositi.md) su cui mettere la copia. Lasciato a zero si legge `DEPOSITO DOCUMENTO ORIGINALE` e la copia resta sul deposito di partenza. | codice |
| **Rimuovi Documento di Riferimento** | | **Cancella l'originale** dopo aver creato la copia, previa conferma. | attivo/non attivo |

{: .campi }

I due campi **Registro** spariscono se la [ditta](../anagrafiche/ditte.md) è
impostata a registro unico.

### Esporta

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Registro** | ● | Il registro del documento. Arriva già impostato su quello della ditta per quel tipo di documento. | da `A` a `Z` |
| **Numero** | ● | Il numero del documento da esportare. | numero |
| **Formato** | ● | Il tracciato con cui scrivere il file. | vedi sotto |
| **Nazione** | | Sigla del paese del destinatario. Serve alla fattura elettronica. | sigla |
| **Cod. Fiscale** | | Codice fiscale o partita IVA del destinatario. | testo |
| **Destinatario** | | Il codice destinatario. Per la fattura verso la Pubblica Amministrazione dev'essere di **6 caratteri**. | testo |
| **PEC** | | L'indirizzo PEC del destinatario. | indirizzo |

{: .campi }

Le voci dell'elenco **Formato** cambiano secondo il documento:

| Documento | Formati offerti |
|---|---|
| Fattura | `FACILE`, `EXCEL`, `XML-PA SDI`, `XML-PR SDI`, `CHEF EXPRESS DESADV` |
| Autofattura / integrazione | `FACILE`, `EXCEL`, `XML-PA SDI`, `XML-PR SDI` |
| Documento di trasporto | `FACILE`, `EXCEL`, `CHEF EXPRESS DESADV` |
| Bolla, buono, ordine cliente, ordine a fornitore, richiesta offerta, pro forma | `FACILE`, `EXCEL` |

Sulle fatture il formato arriva già scelto: `XML-PA SDI` se il cliente o la
destinazione portano un codice IPA, `XML-PR SDI` negli altri casi.

### Ricezione

Non ci sono campi. Il programma chiede *«Vuoi Collegarti al server FTP ?»*:

- rispondendo **Sì**, fa tutto da solo (vedi le note);
- rispondendo **No**, apre una finestra per scegliere a mano il file da
  caricare — un `.rsa` o uno `.zip` — partendo dalla cartella `in` dell'utente.
## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Crea la copia, oppure avvia l'esportazione o la ricezione. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |

## Come si fa

### Rifare un documento simile a uno già emesso

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Duplica**.
2. In **Numero Riferimento** indica la fattura da copiare.
3. Scegli il **Registro** su cui creare la copia.
4. Premi **F2 - OK**, poi apri la copia dalla
   [gestione documenti](gestione-documenti.md) e correggila.

### Trasformare un documento in un altro tipo

Il tipo di arrivo **non si sceglie nella finestra**: lo decide la voce di menu
da cui si entra, e le voci che cambiano tipo sono due sole.

1. Per fare una fattura da una pro forma, apri
   **Menu ▸ Vendite ▸ Fatture Pro Forma ▸ Emissione Fattura da Pro Forma**.
2. Per fare un ordine da una richiesta di offerta, apri
   **Menu ▸ Ordini ▸ Richieste Offerta ▸ Genera Ordine a Fornitore**.

In tutti gli altri casi **Duplica** fa una copia dello **stesso tipo** del
documento di partenza.

### Ricevere i documenti degli agenti

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Ricezione Fatture dal Server FTP** —
   oppure **da Palmare** se il dispositivo è collegato al computer.
2. Alla domanda *«Vuoi Collegarti al server FTP ?»* rispondi **Sì**.
3. Aspetta: il programma passa in rassegna tutti gli agenti, uno per uno, e la
   finestra di avanzamento dice a chi è arrivato.
4. Controlla i documenti arrivati dalla
   [gestione documenti](gestione-documenti.md) prima di stamparli.

### Caricare a mano un file che l'agente ha mandato per posta

1. Apri la stessa voce **Ricezione ... dal Server FTP**.
2. Alla domanda sul collegamento rispondi **No**.
3. Scegli il file `.rsa` o `.zip` che ti è arrivato.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Il documento non è ancora stato emesso !<br>Confermi L' esportazione ?* | Si sta esportando un documento ancora in stato *salvato*. | **Sì** esporta lo stesso. Conviene però emetterlo prima: quello che esce non è ancora definitivo. |
| *Il documento risulta annullato!<br>Confermi L' esportazione ?* | Si sta esportando un documento annullato. | **Sì** esporta lo stesso, ma quasi sempre non è quello che si vuole. |
| *Funzione Esportazione Documento non impostata!* | Per questa installazione non è configurato alcun formato di esportazione. | Chiedi all'assistenza quale tracciato attivare. |
| *Il documento richiesto non esiste in archivio!* | Il **Numero Riferimento** non corrisponde a nessun documento. | Controlla anno, numero e registro. |
| *Il documento indicato è già presente in archivio!* | Il **Nuovo Numero** è già di un altro documento. | Scegli un numero libero. |
| *Duplicazione Documento Conclusa regolarmente!* | La copia è stata creata. | Nessuna azione. |
| *Confermi la rimozione del documento di riferimento ?* | Era attiva **Rimuovi Documento di Riferimento**. | **Sì** cancella l'originale. La risposta preimpostata è **No**. |
| *Emissione Fattura da Pro Forma Conclusa regolarmente!* | La fattura è stata generata dalla pro forma. | Nessuna azione. |
| *La stampa della Fattura comporterà una doppia<br>movimentazione degli articoli e un raddoppio delle scadenze.<br><br>Assicurarsi di annullare la Fattura Pro Forma!* | La ditta è impostata perché anche le pro forma movimentino il magazzino. | **Annulla la pro forma** prima di stampare la fattura, altrimenti merce e scadenze risultano il doppio. |
| *Ordine a Fornitore generato regolarmente!* | L'ordine è stato generato dalla richiesta di offerta. | Nessuna azione. |
| *Livello Importazioni non Valido!* | Il livello di importazione configurato per la ditta è fuori dai valori previsti. | Chiedi all'assistenza di sistemarlo: senza, la ricezione non parte. |
| *Impossibile Caricare RAPI.DLL !<br><br>Controllare presenza installazione ActiveSync.* | La ricezione **da palmare** non trova ActiveSync sul computer. | Installa ActiveSync, o usa la ricezione dal server FTP. |
| *(nessun messaggio, solo un segnale acustico)* | Manca il **Numero Riferimento**, il **Nuovo Numero** o uno dei due anni. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! note "La copia è un documento nuovo"

    **Duplica** non modifica l'originale: crea un documento con il numero e il
    registro che gli hai indicato. È il modo più rapido per emettere un
    documento simile a uno già fatto.

    Si può copiare anche **da un anno all'altro**: i due campi dell'anno sono
    indipendenti e arrivano tutti e due sull'anno di lavoro.

!!! warning "«Rimuovi Documento di Riferimento» cancella l'originale"

    Non lo archivia e non lo annulla: **lo elimina**. Il programma chiede
    conferma, e la risposta preimpostata è **No**.

    Serve quando si rifà un documento sbagliato, non quando se ne vuole uno
    simile: in quel caso la casella va lasciata spenta.

!!! note "Dove finisce il file dell'esportazione"

    **Esporta** scrive nella cartella `out` del programma, creandola se non
    c'è. Il **formato** dipende da come è configurata l'installazione: il
    tracciato documenti di Facile, un foglio Excel, un file XML, o uno dei
    tracciati concordati con il destinatario. Se non ne è stato impostato
    nessuno, il programma lo dice.

    Per i tracciati delle centrali e dei grandi fornitori la strada è un'altra:
    [Trasferimenti ▸ Esportazione per tracciato](../trasferimenti/esportazione-documenti.md).

!!! note "La duplicazione copia tutto il documento"

    Non solo la testata: **Duplica** ricopia anche **tutte le righe del corpo**
    nell'ordine in cui stanno, e le integrazioni collegate al documento. Quello
    che cambia è il numero, il registro e la data; il resto arriva identico e si
    corregge dopo.

!!! note "«Riezione D.D.T. da Palmare» è scritto così davvero"

    Il refuso è nella voce di menu del programma, in tutte le versioni: si legge
    *Riezione* invece di *Ricezione*. Non è un errore di questo manuale.

!!! info "Come funziona la ricezione dal server FTP"

    I parametri del collegamento stanno nella scheda della
    [ditta](../anagrafiche/ditte.md): indirizzo del server, utente, password,
    modo passivo e registrazione del log. Se il collegamento non è abilitato, la
    voce di menu non chiede niente e passa diritta alla scelta del file a mano.

    Quando invece è abilitato, il programma scorre **tutti gli
    [agenti](../anagrafiche/anagrafica-agenti.md) in archivio** e per ciascuno:

    1. si collega al server;
    2. entra nella cartella dell'agente, che porta il suo codice — `age00007`
       per l'agente 7 — e la crea se non c'è;
    3. scarica il file dei documenti della ditta, `dof00001.rsa` per la ditta 1,
       o in mancanza il corrispondente `.zip`;
    4. **cancella il file dal server** e lo carica in archivio.

    L'agente che sulla sua scheda ha spuntato **Escludi da ricezione ordini**
    viene saltato.

    Il file scaricato resta nella cartella `in` dell'installazione: è la copia
    di quello che è stato caricato, utile se qualcosa va storto.

!!! info "Come funziona la ricezione da palmare"

    Il palmare dev'essere un dispositivo **Windows Mobile** collegato al
    computer con **ActiveSync**: il programma usa quel collegamento per prendere
    il file `dof00001.rsa` — il numero è quello della ditta — dalla memoria del
    palmare e portarlo nella cartella `in`, poi lo carica.

    Se ActiveSync non è installato arriva il messaggio su `RAPI.DLL` e non
    succede altro. È una strada legata a dispositivi ormai vecchi: sui palmari
    di oggi si usa il server FTP.

## Vedi anche

- [Gestione documenti](gestione-documenti.md)
- [Documento di vendita](documento-di-vendita.md)
