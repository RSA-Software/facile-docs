---
title: Vendita al banco e POS
description: Le due schermate di vendita diretta — la vendita al banco da tastiera e il punto cassa touchscreen.
modulo: Vendite
maschera_id: IDD_VEN_VENDITE
---

# Vendita al banco e POS

Le due schermate con cui si vende al cliente che è davanti: **Vendita** si usa
da tastiera, **Pos Touchscreen** con lo schermo tattile. Non producono un
documento differito ma battono lo scontrino e scaricano il magazzino subito.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Vendite ▸ Vendita
        - Menu ▸ Vendite ▸ Pos Touchscreen
    - **Scorciatoia:** ++f2++ scarica, ++f3++ scontrino, ++f4++ documenti, ++f5++ preconto, ++f6++ dati, ++f9++ resi
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md); sull'utente pesano anche **Disabilita Stampe (POS)**, **Disabilita Rapporti e Azzeramenti Cassa (POS)** e **Disabilita Stampa Preconti**

---

## A cosa serve

È la cassa del negozio. Si passano gli articoli, si incassa e si chiude lo
scontrino; il magazzino si aggiorna nello stesso momento.

La differenza fra le due voci è l'interfaccia: **Vendita** è pensata per la
tastiera e il lettore di codici a barre, **Pos Touchscreen** per lo schermo
tattile con i tasti dei reparti e degli articoli.

**Vendita** però non è solo una cassa: quello che si è messo sul banco può
uscire come scontrino, come semplice scarico di magazzino oppure come
documento — fattura, DDT, ordine, preventivo. È la schermata da cui si lavora
in un negozio che vende sia al banco sia a clienti con partita IVA.

## Prerequisiti

Prima di usare queste schermate occorre:

- avere gli [articoli](../anagrafiche/anagrafica-articoli.md) con i
  [listini](../listini-vendita/gestione-listini.md) e i codici a barre;
- avere i [reparti](../magazzino/reparti.md) collegati al registratore di
  cassa;
- avere l'[operatore](../altre-tabelle/operatori.md) registrato e collegato
  all'[utente](../anagrafiche/utenti.md);
- avere il registratore di cassa configurato.

## La maschera

![Vendita al banco](../../assets/img/vendite/vendita-al-banco.png)

Sono due schermate a tutto schermo, costruite per essere usate senza mouse.

**Vendita** ha tre fasce:

- in alto la **testata**: il **Cliente** con la sua ragione sociale e il suo
  indirizzo, e a destra **Tipo** di vendita, **Lis.**, **%Sc.** e **Data**;
  sotto, il campo **Dep./Articolo** da cui si passano gli articoli, e la
  scritta **RESI ATTIVO** quando si sta lavorando in modalità reso;
- al centro la **griglia** di quello che si sta vendendo;
- in basso i totali — **Totale Q.tà**, **Tot. Imponibile**, **Totale IVA** e
  il **TOTALE** in grande — e, accanto, i **Punti Fidelity**: due riquadri,
  quelli maturati adesso e quelli che il cliente aveva già.

**Pos Touchscreen** è una tastiera a video:

- a sinistra in alto una griglia di **venti tasti articolo** (quattro colonne
  per cinque righe) con le frecce per scorrere le pagine;
- sotto, **dodici tasti reparto** (quattro per tre), anch'essi scorribili;
- in basso le **funzioni**: *Reso*, *Correz.*, *Solo Scarico*, *Prezzo
  Libero*, *Info Prezzo*, *Apre Casset.*, *Operat.*, *Doc.*, *Funzioni*,
  *Memo*, *Varianti*, *Stampa*, *Vincita*, *Annulla Scontr.*, *Storno*, *Pre
  Conto*, *Premio*, *Cliente*, *Cod. Fiscale*, *Lotteria* ed *Esci*;
- a destra il **display a due righe**, il **TOTALE** e la griglia dello
  scontrino in corso, con sotto il **tastierino numerico**.

Alcuni tasti cambiano nome secondo la configurazione: *Funzioni* può diventare
*Note*, *Stampa* può diventare *Agg.Cli.*, e così via.

## Campi

Nel **Pos Touchscreen** non ci sono campi: si preme e basta. In **Vendita**
la testata ne ha alcuni.

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Cliente** | | Il [cliente](../anagrafiche/anagrafica-clienti.md) a cui si sta vendendo. Accanto compaiono ragione sociale e indirizzo. Lasciandolo vuoto la vendita è anonima. | codice |
| **Tipo** | | Il tipo di vendita, che decide il listino e la provvigione. | `N` normale, `T` trasferta, `C` e `D` centro servizi |
| **Lis.** | | Il [listino](../listini-vendita/gestione-listini.md) da applicare. Proposto dal cliente. | codice |
| **%Sc.** | | Lo sconto generale. Proposto dal cliente. | percentuale |
| **Data** | | La data della vendita. | data |
| **Dep./Articolo** | | Il deposito e il codice dell'articolo da aggiungere. È il campo su cui si legge il codice a barre. | codici |
| **Totale Q.tà**, **Tot. Imponibile**, **Totale IVA**, **TOTALE** | | I totali di quello che è sul banco. | Sola lettura |
| **Punti Fidelity** | | A sinistra i punti che questa vendita fa maturare, a destra quelli già in saldo sulla tessera del cliente. | Sola lettura |

{: .campi }

## Pulsanti e comandi

Questi sono i comandi della schermata **Vendita**.

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Scarica** | ++f2++ | Scarica gli articoli dal magazzino **senza emettere niente**. |
| **F3 - Scontrino** | ++f3++ | Scarica gli articoli **e batte lo scontrino fiscale**. Resta spento se il registratore di cassa non è configurato. |
| **F4 - Documenti** | ++f4++ | Emette un documento con gli articoli sul banco: fattura, DDT, ordine, preventivo e gli altri. |
| **F5 - Preconto** | ++f5++ | Stampa il preconto, cioè il riepilogo non fiscale da mostrare al cliente prima di chiudere. |
| **F6 - Dati** | ++f6++ | Prende gli articoli da un **ordine**, da un **preventivo**, da un **DDT conto vendita** o da un lettore di codici a barre. |
| **F7 - Interroga Art.** | ++f7++ | Interrogazione dell'articolo. |
| **F8 - Contr.Ordine** | ++f8++ | Confronta quello che è sul banco con un ordine e segnala le differenze. |
| **F9 - Resi** | ++f9++ | Registra un reso. |
| **Cerca** | | Cerca un articolo. |
| **Info Taglia** | | Mostra la disponibilità per taglia e colore. |
| **Acq. Inventario** | | Acquisisce le letture per l'inventario. |
| **Buoni Regalo** | | Gestisce i buoni regalo. |
| **Esci** | | Chiude la schermata di vendita. |

## Come si fa

### Battere una vendita

1. Apri **Menu ▸ Vendite ▸ Vendita**.
2. Passa gli articoli con il lettore, o digitane il codice.
3. Se il cliente chiede il conto prima di pagare, premi **F5 - Preconto**.
4. Chiudi lo scontrino e incassa.

### Registrare un reso

1. Nella schermata di vendita premi **F9 - Resi**: in alto compare la scritta
   **RESI ATTIVO**.
2. Indica l'articolo reso e la quantità.

### Far maturare i punti al cliente

1. Prima di passare gli articoli, scrivi il codice del cliente nel campo
   **Cliente** in alto a sinistra — o cercalo con l'elenco.
2. Vendi normalmente: in basso a destra, accanto a **Punti Fidelity**, il
   primo riquadro conta i punti che la vendita sta facendo maturare e il
   secondo mostra quelli già sulla tessera.
3. Chiudi con **F3 - Scontrino**: i punti restano legati allo scontrino e al
   cliente.

Sul **Pos Touchscreen** lo stesso si fa con il tasto **Cliente**.

### Fatturare quello che è sul banco

1. Passa gli articoli come per una vendita normale.
2. Premi **F4 - Documenti** invece di **F3 - Scontrino**.
3. Scegli che documento emettere: fattura, fattura accompagnatoria, DDT,
   bolla, buono di consegna, ricevuta fiscale, ordine, preventivo, nota di
   credito o pro forma.
4. Il documento nasce già con le righe del banco e si completa come un
   [documento di vendita](documento-di-vendita.md) qualsiasi.

## Controlli e messaggi

Sono molti, e quasi tutti si capiscono meglio sapendo **in che momento**
arrivano. Qui sono raccolti per quello, non in ordine alfabetico.

### Quando si apre la schermata

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Attenzione!<br><br>Non e' stato impostato il listino di vendita.<br>Saranno riportati per la vendita i prezzi<br>di acquisto.* | La [ditta](../anagrafiche/ditte.md) non ha un listino di vendita. | Impostalo: altrimenti si vende al prezzo di acquisto. Il messaggio compare all'apertura della schermata. |
| *Attenzione!<br><br>Non e' stato impostato il listino di vendita per i trasfert.<br>Saranno riportati per la vendita i prezzi<br>di acquisto.* | Come sopra, per le vendite in trasferta. | Impostalo nella ditta. |
| *Impostazioni modello cassa o porta COM non valide!<br>Per impostare il modello di cassa e la porta COM andare su Utility->Impostazioni Postazione.<br>Vuoi entrare in modalita' DEMO ?* | La postazione non sa a quale registratore di cassa parlare. | **No** e si sistemano le [impostazioni della postazione](../utility/impostazioni-postazione.md). **Sì** apre la schermata in prova: si lavora, ma **non esce nessuno scontrino fiscale**. |
| *Matricola stampante fiscale non impostata!* / *Matricola stampante fiscale non valida!* | Manca o è sbagliata la matricola del registratore telematico. | Si imposta nelle impostazioni della postazione. |
| *Numero cassa non valido!* | La postazione non ha un numero di cassa. | Come sopra. |
| *Anno di esercizio diverso da anno emissione scontrini !<br>Vuoi Continuare ?* | Si sta lavorando su un esercizio diverso da quello in cui escono gli scontrini. | Quasi sempre è il segno che va aperto il nuovo esercizio. |
| *Anno corrente diverso da anno emissione scontrini!<br>Necessaria apertura nuovo esercizio.<br>Contattare l'assistenza tecnica.* | Lo stesso caso, ma qui il programma non lascia proseguire. | Va aperto il nuovo esercizio. |
| *Causale Vendita non impostata o non valida!* / *Causale Vendita Senza Documenti impostata o non valida!* | Mancano le [causali](../magazzino/causali-magazzino.md) con cui il banco scarica il magazzino. | Si impostano nella scheda della [ditta](../anagrafiche/ditte.md). |
| *Deposito attivo non impostato o non valido !* / *Selezionare il Deposito !* | Manca il [deposito](../magazzino/depositi.md) da cui scaricare. | Va indicato prima di vendere. |
| *Il codice dell' Operatore non è valido o disponibile.* | L'[operatore](../altre-tabelle/operatori.md) non esiste. | Va creato o corretto. |

!!! warning "La modalità DEMO non emette scontrini"

    Rispondere **Sì** alla domanda sulla modalità demo fa aprire la
    schermata anche senza cassa collegata: le righe si scrivono, i totali si
    calcolano, **ma il documento fiscale non viene emesso**. Va benissimo per
    provare o per far pratica; è un guaio se qualcuno ci lavora credendo di
    star battendo scontrini veri.

### Quando si battono le righe

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Attenzione!<br>Articolo Inesistente<br>Codice … Q.ta …* | Il codice letto o digitato non è in archivio. | Controllare il codice o creare l'articolo. |
| *Codice non trovato in archivio !<br>Vuoi effettuare un ricerca ?* | Come sopra. | **Sì** apre la ricerca articoli. |
| *Attenzione!<br>PLU non trovato in archivio (…)* | Il PLU letto dalla bilancia non corrisponde a nessun articolo. | Va allineata la [bilancia](../casse-bilance/bilance.md). |
| *Per questo Articolo non e' stato Impostato il Reparto Cassa!* | L'articolo non ha il reparto con cui la cassa lo registra. | Si imposta in [anagrafica articoli](../anagrafiche/anagrafica-articoli.md): senza, lo scontrino non si chiude. |
| *Per l' articolo regalo non e' stato Impostato il Reparto Cassa!* | Lo stesso, per l'articolo usato come omaggio. | Come sopra. |
| *Per l'articolo indicato non e' presente un prezzo di listino!<br>Vuoi inserirlo ugualmente?* | L'articolo non ha prezzo sul listino in uso. | **Sì** lo mette a zero: va corretto a mano. |
| *Attenzione !<br>L'articolo selezionato risulta escluso dal listino.* | L'articolo è escluso da quel listino. | Non si vende con quel listino. |
| *Attenzione Listino di Vendita non Impostato!<br>Per la Vendita si usera' l'Ultimo Prezzo di Acquisto!* | Manca il listino. | I prezzi proposti sono quelli di acquisto. |
| *Riga N. …<br>Esistenza non sufficiente per effettuare la vendita!* | Non c'è giacenza. | Controllare il magazzino: può essere un carico non registrato. |
| *L'Articolo selezionato ha raggiunto il Sottoscorta !* | L'articolo è sceso sotto la scorta minima. | È un avviso, la vendita prosegue. |
| *Non sono ammesse quantità con decimali!* | L'articolo si vende a pezzi interi. | Correggere la quantità. |
| *L'articolo … con la gestione dei seriali abilitata non puo' essere venduto con quantita' decimali!* | Come sopra, per gli articoli a matricola. | Come sopra. |
| *E' necessario inserire le matricole per chiudere lo scontrino!* | Righe a matricola senza matricola indicata. | Vanno inserite prima di chiudere. |
| *Attenzione !<br>Gestione Lotti attiva per l'articolo selezionato.<br>Vuoi Forzare ?* | L'articolo vuole il [lotto](../analisi-dati/analisi-lotti.md). | **No** torna a indicarlo; **Sì** vende senza, e la tracciabilità si perde. |
| *Per questo Articolo deve essere indicato il Lotto!* | Come sopra, senza possibilità di forzare. | Il lotto va indicato. |
| *Non c'è giacenza sufficiente per il lotto indicato!* | Il lotto non ha abbastanza merce. | Sceglierne un altro o dividere la riga. |
| *Riga … - Manca la taglia* / *Manca il colore* | Articolo per taglie e colori senza taglia o colore. | Vanno indicati. |
| *La Quantita' indicata e' pari a Zero !<br>Vuoi eliminare la riga ?* | Quantità a zero. | **Sì** toglie la riga. |
| *Raggiunto il numero massimo di sconti applicabili!<br>Lo sconto della promozioni non e' stato applicato!* | La riga ha già tutti gli sconti che può avere. | La [promozione](promozioni.md) **non entra**: se deve valere, va tolto uno degli sconti manuali. |
| *Attenzione!<br>Ci sono righe con prezzi pari a zero dovuti al cambio del listino applicato.<br>Controllare prima di emettere lo scontrino.* | Cambiando listino, alcune righe sono rimaste senza prezzo. | Vanno controllate una per una prima di chiudere. |
| *Attenzione!<br>Cliente con aliquota iva preimpostata.<br>Saranno ricalcolati i prezzi di vendita.* | Il cliente ha un'aliquota fissa. | I prezzi vengono rifatti su quell'aliquota. |

### Quando si sceglie il cliente

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Inserire il codice del cliente !* / *E' necessario selezionare un cliente!* | L'operazione richiede un cliente intestatario. | Va scelto. |
| *Il Codice del Cliente richiesto non è valido o disponibile.* | Il codice non esiste. | Controllare il codice. |
| *Attenzione !<br>E' stato superato il Fido concesso al Cliente.<br>Vuoi Continuare ?* | La vendita porta il cliente oltre il fido. | **Sì** prosegue lo stesso. |
| *Il cliente selezionato ha un credito di … Euro per un anticipo pagato in precedenza !* | Il cliente ha un [acconto](acconti.md) non ancora utilizzato. | Va scalato dal totale. |
| *Esiste in archivio un ordine in corso per il cliente !<br>Vuoi accorpare gli ordini ?* | C'è già un ordine aperto per quel cliente. | **Sì** unisce le righe in un solo ordine. |
| *Esiste in archivio un buono di consegna in corso per il cliente !<br>Vuoi accorpare i buoni ?* | Come sopra, per i buoni di consegna. | Come sopra. |
| *Attenzione!<br>L'ordine selezionato e' marcato come non frazionabile.* | L'ordine va consegnato tutto insieme. | Non si può evaderne una parte. |

**Quando lo scontrino deve portare i dati del cliente** — fattura
elettronica, lotteria, cliente estero — il programma li controlla tutti
prima di chiudere, e li elenca uno alla volta: *Ragione Sociale Cliente
assente!*, *Nome*, *Cognome*, *Indirizzo*, *Citta'*, *Cap … assente o non
valido!*, *Provincia*, *Codice Nazione* e *Codice ISO ALPHA 2 Nazione*,
*Partita IVA e Codice Fiscale Cliente entrambi assenti!*, *Il codice fiscale
del cliente deve essere di 11 o 16 caratteri!*. Tutti finiscono con
*Sistemare i dati del cliente e riprovare*: si correggono
[nell'anagrafica](../anagrafiche/anagrafica-clienti.md), non qui.

### Quando si chiude lo scontrino

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Confermi la chiusura dello scontrino ?<br>Scegliere SI per chiudere e scaricare gli articoli<br>Scegliere NO per chiudere senza scaricare gli articoli* | Conferma di chiusura. | **Leggerla**: la differenza fra Sì e No è se il magazzino si scarica. |
| *Attenzione!<br>Selezionando OK la vendita sara' chiusa ed inviata alla stampante fiscale.<br>Se devi rivedere qualcosa seleziona il tasto Annulla.* | Ultima conferma prima dell'invio alla cassa. | Da lì in avanti lo scontrino è emesso. |
| *Sono presenti righe con quantita' positive e negative.<br>Non e' possibile emettere lo scontrino!* | Vendite e resi nello stesso scontrino. | Vanno fatti due scontrini. |
| *In modalita' RT non e' possibile fare vendite e resi nello stesso scontrino!* | Come sopra, con il registratore telematico. | Come sopra. |
| *L'attivazione/disattivazione del reso puo' essere fatta solo con la griglia vuota!* | Si sta passando a reso con righe già battute. | Prima si svuota la griglia. |
| *Il buono fidelity deve essere utilizzato come prima forma di pagamento!<br>Tutte le forme di pagamento precedenti saranno eliminate e devono essere nuovamente applicate.* | Il buono fidelity è stato messo dopo altri pagamenti. | Si riparte dai pagamenti, mettendo il buono per primo. |
| *E' necessario impostare il tipo di buoni pasto ed il taglio prima di procedere con il pagamento!* | Buoni pasto senza tipo e taglio. | Vanno indicati. |
| *Il numero massimo accettabile di righe di pagamento con buoni pasto e' 5 !* | Più di cinque righe di buoni pasto. | Vanno raggruppate. |
| *Codice lotteria scontrini non valido!* | Il codice lotteria del cliente non è valido. | Va ricontrollato. |
| *Confermi l' annullamento dello scontrino ?* | Annullamento in corso. | La risposta preimpostata è **No**. |
| *Si e' verificato un problema nell'erogazione del resto.<br>Si prega di rendere manualmente Euro …* | La cassa automatica non è riuscita a erogare il resto. | **Il resto va dato a mano**: la cifra è quella indicata. |

!!! danger "«Chiudere senza scaricare gli articoli» non è la risposta di default da dare per abitudine"

    La domanda di chiusura offre due strade: **Sì** chiude e scarica il
    magazzino, **No** chiude e **non** lo scarica. Serve nei casi in cui la
    merce è già stata scaricata altrove — ma usata per sbaglio lascia il
    magazzino più pieno di quello che è, e l'errore si scopre solo
    all'inventario.

### Quando si emette un documento

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Attenzione!<br><br>Su una riga il segno "Gia' movimentato" aveva un valore non valido ed e' stato azzerato.<br>La riga scarichera' il magazzino.* / *Attenzione!<br><br>Su … righe il segno "Gia' movimentato" aveva un valore non valido ed e' stato azzerato.<br>Le righe scaricheranno il magazzino.* | Premendo **F4 - Documenti**, il programma controlla il segno che dice se una riga ha già scaricato il magazzino. Quel segno può essere solo acceso o spento: qui aveva un valore diverso, e il programma lo ha spento. | Niente: le righe scaricheranno il magazzino come quelle battute a mano, che è il comportamento normale. Il messaggio non dovrebbe comparire: se lo vedi, segnalalo all'assistenza. |

### Quando la cassa o la bilancia non rispondono

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Cassa OFF-LINE !* / *Cassa occupata !* | Il registratore non risponde o sta facendo altro. | Controllare cavo e stato della cassa. |
| *Driver Cassa non inizializzato !* / *Impossibile inizializzare il driver di comunicazione con la cassa !* | Il collegamento non si apre. | Verificare modello e porta nelle impostazioni della postazione. |
| *Comando non supportato dal modello della Cassa !* | Quel modello non sa fare quell'operazione. | Non tutte le casse fanno tutto. |
| *Non e' possibile inizializzare il driver di comunicazione con la stampante fiscale!<br>Controllare il display, potrebbe essere necessario un azzeramento fiscale.<br>Vuoi fare l'azzeramento fiscale?* | La stampante fiscale è bloccata in attesa della chiusura giornaliera. | Di norma **Sì**: è la chiusura di fine giornata non fatta. |
| *Il Cassetto puo' essere aperto solo a scontrino chiuso!* | Si è chiesto il cassetto a scontrino aperto. | Prima si chiude lo scontrino. |
| *Assenza di Comunicazione con la cassa automatica…<br>Vuoi riprovare?* | La cassa automatica non risponde. | **Sì** ritenta dopo aver controllato il collegamento. |
| *Errore di comunicazione con la bilancia!* / *Impossibile comunicare con la bilancia!* | La bilancia non risponde. | Controllare cavo e accensione. |
| *Bilancia non a livello!* | La bilancia non è in piano. | Va livellata, altrimenti pesa male. |
| *Peso Instabile!<br>Far stabilizzare il peso prima dell'acquisizione!* / *Peso non stabile o negativo!* | Il piatto si muove. | Attendere che si fermi. |
| *Sottopeso* / *Sovrappeso<br>Peso fuori dal range consentito!* | Il peso è fuori dai limiti della bilancia. | Il pezzo non è pesabile su quella bilancia. |
| *Posizionare sul piatto della bilancia l'articolo da pesare e ripetere l'operazione!* | Il piatto è vuoto. | Appoggiare l'articolo. |

### Quando si esce, si azzera, si abbandona

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Scontrino in corso...<br>Chiudere o annullare lo scontrino per uscire!* | Si sta uscendo con uno scontrino aperto. | Va chiuso o annullato. |
| *Per uscire devono essere abbandonate le vendite del cliente … !* | C'è una vendita in sospeso per un cliente. | Va chiusa o abbandonata. |
| *Vuoi Abbandonare la vendita ?* | Abbandono delle righe battute. | Con **Sì** si perde quello che è stato battuto. |
| *Confermi l'uscita ?* | Uscita dalla schermata. | — |
| *Confermi l'Azzeramento Fiscale?* | Chiusura fiscale di fine giornata. | È l'operazione che chiude il giorno sulla cassa. |
| *L'invio dei dati di vendita non e' andato a buon fine.<br>Si consiglia di ripetere la procedura<br>Vuoi interrompere l'Azzeramento Fiscale?* | I dati di vendita non sono arrivati in archivio. | **Sì**: meglio fermarsi e ripetere che chiudere il giorno con dati mancanti. |
| *Confermi l'Azzeramento Reparti?* / *Vuoi Azzerare i reparti ?* | Azzeramento dei totali per reparto. | — |
| *Confermi l'invio dei dati all' Agenzia delle Entrate?* | Invio del corrispettivo telematico. | — |
| *Cancello le vendite senza scontrino ?* | Pulizia delle vendite rimaste aperte. | **Sì** le elimina. |

### Due cose che il programma dice e non dovrebbe

| Messaggio | Che cos'è |
|---|---|
| *E' stato superato il numero massimo di clienti gestibili!<br>Aumentare MAX_VEN_SHEET* | Il banco tiene aperte **al massimo cinque vendite contemporanee**, una per cliente. Il limite è vero e va conosciuto; la seconda riga del messaggio è un promemoria per chi ha scritto il programma e non riguarda chi lo usa. |
| *Funzione in fase di realizzazione!* | Due tasti del Pos Touchscreen non fanno ancora niente. Non c'è nulla da sistemare: la funzione non esiste. |

## Note

!!! note "Cosa può fare l'operatore lo decide l'utente"

    Tre caselle della maschera [Utenti](../anagrafiche/utenti.md) intervengono
    qui: **Disabilita Stampe (POS)**, **Disabilita Rapporti e Azzeramenti Cassa
    (POS)** e **Disabilita Stampa Preconti**. Se un comando non risponde, è lì
    che va guardato.

!!! warning "Gli scontrini si consultano altrove"

    Da questa schermata si vende soltanto. Il riepilogo di quello che è stato
    battuto sta in [Scontrini](scontrini.md).

!!! note "Le due schermate scrivono negli stessi archivi"

    Tastiera o touchscreen, lo scontrino finisce nello stesso archivio e si
    ritrova nello stesso modo da [Scontrini](scontrini.md); il magazzino si
    scarica allo stesso modo e i punti fedeltà maturano allo stesso modo.

    Quello che cambia è **come si lavora** e **cosa si può fare**:

    | | **Vendita** | **Pos Touchscreen** |
    |---|---|---|
    | Come si passa un articolo | codice a barre o codice digitato | tasto a video, o codice a barre |
    | Emissione di documenti | sì, con **F4 - Documenti** | limitata, con il tasto *Doc.* |
    | Prelievo da ordini e preventivi | sì, con **F6 - Dati** | no |
    | Forme di pagamento | alla chiusura dello scontrino | tasti dedicati: contanti, elettronico, assegni, buoni pasto, credito, buoni multiuso |
    | Tasti reparto e articolo | no | sì, configurabili |

    In un negozio si usa il POS; in un magazzino o in un cash and carry, dove
    capita di dover emettere anche una fattura o un DDT, si usa **Vendita**.

!!! info "Il cliente si indica prima di battere"

    Per far maturare i punti, o semplicemente per sapere a chi si è venduto, il
    cliente va indicato **nel campo Cliente in testa alla schermata**, prima di
    chiudere lo scontrino; sul POS c'è il tasto **Cliente**.

    Indicandolo, il programma propone anche il suo **listino** e il suo
    **sconto**, e i due riquadri **Punti Fidelity** si accendono: a sinistra i
    punti che questa vendita sta maturando, a destra quelli che il cliente aveva
    già.

    Senza cliente la vendita è anonima: lo scontrino resta valido, ma non
    matura punti e non si ritrova per cliente.

!!! warning "«Scarica» e «Scontrino» non sono la stessa cosa"

    **F3 - Scontrino** scarica il magazzino **e** manda lo scontrino al
    registratore di cassa: è la vendita vera e propria.

    **F2 - Scarica** invece scarica il magazzino **e basta**, senza emettere
    niente. Serve per la merce che esce senza un documento — autoconsumo,
    campioni, rotture — e va usato sapendo che dal punto di vista fiscale non
    lascia traccia.

    Il comando si può togliere: con l'impostazione che blocca lo scarico senza
    documento, **F2 - Scarica** resta spento.

## Vedi anche

- [Scontrini](scontrini.md)
- [Promozioni](promozioni.md)
- [Anagrafica articoli](../anagrafiche/anagrafica-articoli.md)
