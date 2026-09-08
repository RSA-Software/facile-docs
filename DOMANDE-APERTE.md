# Domande aperte del manuale Facile

Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.
Aggiornato al 2026-09-08 — **408 domande** su 130 pagine.

Ogni voce corrisponde a un commento HTML dentro la pagina indicata: rispondendo
alla domanda, la correzione va fatta nella pagina e il marcatore va tolto.
Per rigenerare questo elenco:

    .venv/Scripts/python.exe tools/domande-aperte.py

## Convenzioni del manuale

`docs/introduzione/convenzioni.md`

- [ ] come si chiamano a video i livelli di licenza (Lite, Standard, Professional) e se il manuale debba dichiararlo esplicitamente.
- [ ] due voci di questa tabella. "Studio" — la descrizione del settore è provvisoria, va confermata. "Killin" — è il nome interno di una personalizzazione: va citato così nel manuale o sostituito?

## Canali di vendita

`docs/moduli/altre-tabelle/canali-di-vendita.md`

- [ ] la differenza pratica fra i quattro costi di "Cess. da Costo" (ULTIMO, MEDIO, NETTO, FINITO).
- [ ] dove il canale viene assegnato: sul cliente, sul contratto fornitore, o su entrambi.
- [ ] cosa cambia esattamente la casella "Totale" rispetto al solo "Ribalt. Sconti F.Ft.".

## Note, aspetto e causali di trasporto

`docs/moduli/altre-tabelle/note-aspetto-trasporto.md`

- [ ] se i documenti già emessi conservino la frase o rileggano la tabella al momento della ristampa.
- [ ] dove esattamente si richiamano le Note Particolari nei documenti.

## Operatori

`docs/moduli/altre-tabelle/operatori.md`

- [ ] se la password dell'operatore sia digitata in chiaro o coperta, e dove venga richiesta durante il lavoro alla cassa.
- [ ] quale lettore di tessere è previsto e in che formato va scritto il codice in "Tessera".

## Agganci trasferimento documenti

`docs/moduli/anagrafiche/agganci-trasferimento-documenti.md`

- [ ] quali trasferimenti di documenti usano questa tabella, e se l'aggancio avvenga sul Cod. Cliente o sul Codice Socio.
- [ ] dove le competenze al chilo vengono usate: se generino provvigioni o restino un dato di consultazione.

## Anagrafica agenti

`docs/moduli/anagrafiche/anagrafica-agenti.md`

- [ ] la corrispondenza fra le quindici percentuali della tabella provvigioni e i cinque modi di Calcolo Provvigione Da. Quale delle quindici viene usata in ciascun caso? Dal codice della maschera non si ricava: il calcolo avviene altrove.
- [ ] il campo Password e la casella Escludi da ricezione ordini riguardano il palmare degli agenti. È un modulo da documentare a parte?

## Anagrafica articoli

`docs/moduli/anagrafiche/anagrafica-articoli.md`

- [ ] quali chiavi ammette la sezione [CHECK] di articoli_check.ini.

## Anagrafica clienti

`docs/moduli/anagrafiche/anagrafica-clienti.md`

- [ ] l'elenco dei campi resi obbligatori è in un file di configurazione dell'installazione. Va documentato in una pagina per l'amministratore, o basta dire all'utente che l'elenco lo decide l'assistenza?
- [ ] dove si imposta l'intervallo di codici riservato ai clienti (quello che fa comparire il messaggio sulle autorizzazioni)? È un dato dell'azienda: qual è il percorso di menu da citare?
- [ ] il campo Livello nella scheda Generale. Esiste una funzione di servizio che lo allinea alla Cat. Economica, ma non è chiaro a cosa serva nell'uso quotidiano.

## Anagrafica fornitori

`docs/moduli/anagrafiche/anagrafica-fornitori.md`

- [ ] dove si imposta l'intervallo di codici riservato ai fornitori (quello che fa comparire il messaggio sulle autorizzazioni)? È un dato dell'azienda: qual è il percorso di menu da citare?
- [ ] il campo Nota Trasfert. Dal codice risulta che la nota viene riportata sui documenti in cui compaiono articoli del fornitore, ma non è chiaro in quali casi d'uso reali si compili.

## Associazione gruppi e giri

`docs/moduli/anagrafiche/associazioni.md`

- [ ] se compilando la Destinazione l'assegnazione valga solo per quella o sovrascriva anche il cliente.
- [ ] cosa succede lasciando vuoto un campo in salvataggio: se azzeri il valore che il cliente aveva o lo lasci com'è.
- [ ] a quale "Gruppo" si riferisca il campo omonimo: gruppo aziende, gruppo mailing o altro.

## Banchi conservatori e attrezzature in comodato

`docs/moduli/anagrafiche/banchi-conservatori.md`

- [ ] quando compare la richiesta di importazione da Excel: all'apertura della maschera o da un comando che non ho individuato.
- [ ] quali colonne del foglio Excel vengono lette oltre a MATRICOLA.
- [ ] se la Penale venga usata automaticamente in qualche documento o resti un dato di sola consultazione.
- [ ] cosa stampa esattamente F7 - Stampa: la scheda della singola attrezzatura o un elenco.

## Bollini

`docs/moduli/anagrafiche/bollini.md`

- [ ] che ruolo abbia la data indicata nell'azzeramento della campagna attuale — se sia la data di chiusura registrata sul cliente o un filtro sui movimenti.
- [ ] cosa distingue "campagna attuale" da "campagna precedente" negli archivi, e dove si stabilisce quando una campagna finisce.
- [ ] da quali documenti il ricalcolo rilegga i bollini: la finestra di avanzamento cita gli scontrini, ma non è detto siano gli unici.

## Capi area

`docs/moduli/anagrafiche/capi-area.md`

- [ ] dove si collega l'agente al suo capo area — se dall'anagrafica agenti o da questa maschera.
- [ ] se la partita IVA e il codice fiscale siano controllati come su clienti e fornitori.

## Codici catastali comuni

`docs/moduli/anagrafiche/codici-catastali-comuni.md`

- [ ] il campo Cod. Catastale non è obbligatorio, ma serve alla fatturazione elettronica. Vale la pena renderlo obbligatorio nel programma, o basta segnalarlo nel manuale?
- [ ] il Codice Ufficio Registro è diviso in due caselle affiancate senza etichette distinte. Che cosa va scritto in ciascuna?

## Ditte

`docs/moduli/anagrafiche/ditte.md`

- [ ] i campi delle schede Parametri Hotel e CRM, che nella copia in uso non sono state esaminate.
- [ ] quale password protegge l'inserimento di una ditta nuova e le Impostazioni Protette, e chi la possiede.
- [ ] cosa succede alla ditta duplicata quando, dopo il cambio, il programma propone la copia degli archivi.
- [ ] se i moduli di stampa della scheda Modulistica si scelgano da un elenco o si scrivano a mano.

## Gestione compleanni

`docs/moduli/anagrafiche/gestione-compleanni.md`

- [ ] come si compone il testo degli auguri: non ho individuato il punto in cui si scrive.
- [ ] se il programma tenga traccia degli auguri già mandati, per non ripeterli.
- [ ] a cosa servono le colonne mmdd, Cod_Cli, Cod_Fid e Data Nas. che compaiono in coda alla griglia.

## Gestori buoni pasto

`docs/moduli/anagrafiche/gestori-buoni-pasto.md`

- [ ] cosa succede alla cassa se il cliente presenta un buono di un taglio non previsto — viene rifiutato, o solo segnalato?
- [ ] la % Commissione entra automaticamente nella fattura di rimborso al gestore, o è solo un dato di riferimento?

## Impostazione dati web degli articoli

`docs/moduli/anagrafiche/impostazione-dati-web.md`

- [ ] come si sceglie la nazione a cui i testi web si riferiscono, e come si passa da una lingua all'altra.
- [ ] quante immagini si possono caricare per articolo e a cosa serve il Deposito indicato accanto a ciascuna.
- [ ] come si aggiungono e si tolgono gli articoli collegati.
- [ ] se i dati web debbano essere salvati esplicitamente o siano registrati mano a mano.

## Mailing list

`docs/moduli/anagrafiche/mailing-list.md`

- [ ] dove si configura il servizio di invio SMS e cosa succede se non è configurato.
- [ ] se l'indirizzo del mittente venga preso dai dati dell'utente o da quelli della ditta.
- [ ] come si compone il testo del messaggio da inviare: non ho individuato il punto in cui si scrive.
- [ ] cosa significa "Aggiungi Gruppo": se il gruppo aziende, il gruppo mailing o un altro raggruppamento.

## Manutenzione degli articoli

`docs/moduli/anagrafiche/manutenzione-articoli.md`

- [ ] cosa fa esattamente il pulsante "Classifica" dell'attribuzione tassonomie.

## Modifica articoli da griglia

`docs/moduli/anagrafiche/modifica-da-griglia.md`

- [ ] quali colonne sono modificabili e quali di sola lettura: dalle risorse risulta bloccata solo la colonna delle taglie.
- [ ] se "Esporta su Excel" produca un foglio reimportabile da "Importa da Excel".
- [ ] cosa succede alla colonna NPO quando si spunta: se venga anche registrata la data di non ordinabilità.

## Nazioni

`docs/moduli/anagrafiche/nazioni.md`

- [ ] il Codice UNICO. È il codice del paese per il modello Unico, ma andrebbe confermato a chi cura la modulistica fiscale.

## Rubrica

`docs/moduli/anagrafiche/rubrica.md`

- [ ] la casella Aggiornamento Automatico. Nel codice il commento che la descrive è troncato e il campo non risulta usato altrove: cosa fa esattamente, e ogni quanto?
- [ ] la voce di menu Importa. Da quale formato di file carica i contatti, e con quale corrispondenza di colonne?
- [ ] dove si inseriscono le categorie della rubrica. Sono una tabella generica: qual è il percorso di menu da citare nei prerequisiti?

## Scorte, assortimento e ubicazioni

`docs/moduli/anagrafiche/scorte-e-assortimento.md`

- [ ] che formato deve avere il file letto da "F3 - Importa" delle ubicazioni.
- [ ] con quale criterio si applicano i coefficienti stagionali quando la Copertura è 90 o 120 giorni.
- [ ] come si sceglie il deposito di partenza e quello di arrivo nella distribuzione automatica.

## Stampe agenti

`docs/moduli/anagrafiche/stampe-agenti.md`

- [ ] se la Stampa Giro Agente riporti le tre sequenze o solo quella del giro indicato.
- [ ] quale formato di etichette usa la stampa delle etichette dei giri.

## Stampe articoli

`docs/moduli/anagrafiche/stampe-articoli.md`

- [ ] quali campi (Formato, Data Riferimento, le tre caselle) compaiano su quali stampe: variano da una voce all'altra.
- [ ] cosa produce l'ordinamento CASUALE nelle stampe diverse da quelle dei banconi.
- [ ] su quale periodo si basa "Solo Articoli Modificati o Movimentati".
- [ ] se "Stampa Esistenza" nella versione Taglie e Colori apra una maschera diversa, e con quali campi.

## Stampe clienti

`docs/moduli/anagrafiche/stampe-clienti.md`

- [ ] quali formati della stampa elenco chiedono "Vuoi la stampa in ordine alfabetico ?" nonostante il campo Ordinamento sia già stato compilato.
- [ ] cosa contiene esattamente il formato SENZA ACQUISTI: su quale periodo è calcolata l'assenza di acquisti.
- [ ] a cosa serve il filtro "Dep. Codifica" e dove il deposito di codifica si imposta sul cliente.

## Stampe fornitori

`docs/moduli/anagrafiche/stampe-fornitori.md`

- [ ] come si chiama a video l'elenco senza etichetta con i valori TUTTI / GENERICI / BENI / SERVIZI, e dove il fornitore viene classificato in beni o servizi.
- [ ] se Stampa Schede e Stampa Saldi dei fornitori aprano davvero le stesse maschere delle corrispondenti stampe clienti.

## Stampa lotti in scadenza e spostamenti codici a barre

`docs/moduli/anagrafiche/stampe-lotti-e-barcode.md`

- [ ] quale impostazione attiva la gestione dei lotti, e cosa mostra la stampa se i lotti non sono gestiti.
- [ ] cosa si intende per "spostamento" di un codice a barre e da quale maschera si effettua.

## Tabella sconti fornitori

`docs/moduli/anagrafiche/tabella-sconti-fornitori.md`

- [ ] cosa distingue i tre metodi di calcolo NORMALE, PRIMARIO e SECONDARIO nell'applicazione degli sconti.
- [ ] dove si inseriscono le percentuali vere e proprie della tabella: questa maschera contiene solo la testata.
- [ ] dove la tabella viene richiamata sul contratto fornitore.

## Trasportatori

`docs/moduli/anagrafiche/trasportatori.md`

- [ ] il campo Naz. non ha l'elenco da cui scegliere, a differenza degli stessi campi in clienti e fornitori. È voluto?

## Utenti

`docs/moduli/anagrafiche/utenti.md`

- [ ] se il nuovo menu venga applicato subito o al successivo accesso dell'utente.
- [ ] cosa comportano esattamente i "Privilegi Amministratore" rispetto alle spunte dell'albero: se scavalchino i permessi o si sommino.
- [ ] che formato deve avere il file allegato con F7 Firma Email e dove viene usato.
- [ ] dove si impostano i loghi a cui fa riferimento il campo Logo.

## Analisi e giacenza dei lotti

`docs/moduli/analisi-dati/analisi-lotti.md`

- [ ] quali colonne mostra la griglia nei due modi, e cosa cambia fra Analisi e Giacenza.
- [ ] quale impostazione attiva la gestione dei lotti e cosa mostrano queste analisi se non è attiva.
- [ ] come viene usato il campo "Listino" nella valorizzazione.

## Analisi delle vendite

`docs/moduli/analisi-dati/analisi-vendite.md`

- [ ] quali dimensioni e quali misure sono disponibili nel cubo multidimensionale.
- [ ] cosa mostra esattamente "Analisi Scontrini" — se il dettaglio riga per riga o i totali per operatore.
- [ ] che differenza c'è fra i filtri di "Analisi Vendite Periodo" e quelli di "Venduto per Articolo".

## Grafici pluriennali e report personalizzati

`docs/moduli/analisi-dati/grafici-e-report.md`

- [ ] i messaggi di queste due maschere.
- [ ] in quale cartella vengono cercati i file .rpt dei report personalizzati.
- [ ] che aspetto ha il grafico prodotto e se sia esportabile o solo stampabile.
- [ ] come le dieci caselle Anno_01…Anno_10 si associano agli anni di gestione presenti in archivio.

## Venduto incrociato per cliente e per agente

`docs/moduli/analisi-dati/venduto-incrociato.md`

- [ ] i messaggi propri di queste analisi.
- [ ] perché la casella si chiama "Salto Pagina dopo ogni Cliente" anche nelle analisi raggruppate per agente.
- [ ] se la comparazione su due anni richieda che entrambe le annate siano nello storico dei movimenti.

## Venduto per…

`docs/moduli/analisi-dati/venduto-per.md`

- [ ] i messaggi propri di queste analisi.
- [ ] quali sono le voci dell'elenco "Tipo Vendita" oltre a TUTTE, e su quali analisi compare.
- [ ] come viene calcolato il turnover e su quale giacenza media.

## Bilance

`docs/moduli/casse-bilance/bilance.md`

- [ ] la differenza fra le due voci di invio delle bilance DIBAL, "- CS" e "- D900".
- [ ] in quale cartella ciascuna marca di bilance scrive e legge i file di scambio.
- [ ] se i tre modi della maschera Elga (invio, ricezione, ricezione da file) mostrino campi diversi.
- [ ] cosa distingue la "ricezione scontrini" dalla "ricezione totali vendite" nel risultato in Facile.

## Casse

`docs/moduli/casse-bilance/casse.md`

- [ ] quale famiglia usa quale cartella e quale tracciato di file.
- [ ] come si configura il collegamento fisico alle casse Ditron oltre alla scelta delle porte.
- [ ] cosa cambia fra i sei livelli di "PARZIALE" nella cancellazione promozioni.
- [ ] se l'invio dei clienti e dei saldi fidelity esista anche per le altre famiglie di casse.

## Frontalini

`docs/moduli/casse-bilance/frontalini.md`

- [ ] dove si configurano i formati dei frontalini e quali sono quelli standard.
- [ ] cosa contiene la colonna "Cod. Bat." e a cosa serve.
- [ ] quali terminalini sono supportati da "F8 - Acquisisci".

## Stampe e manutenzione di casse e bilance

`docs/moduli/casse-bilance/stampe-casse-bilance.md`

- [ ] i messaggi propri di queste stampe.
- [ ] dove si vedono gli scarti oltre che in stampa, e se si possano correggere senza reinserire il venduto a mano.
- [ ] quali campi dell'articolo attivano il flag variazioni, e se lo attivi anche una modifica non di prezzo.

## Aliquote IVA

`docs/moduli/contabilita/aliquote-iva.md`

- [ ] il campo "!% Imponibile Calcolo Rit. Acconto" ha un punto esclamativo iniziale nell'etichetta a video. È voluto o è un refuso da correggere nel programma?
- [ ] il campo Beni non Destinati Rivendita accetta un solo carattere. Quali valori sono previsti?

## Banche ditta

`docs/moduli/contabilita/banche-ditta.md`

- [ ] Saldo Attuale e Ultimo Movimento si aggiornano da soli con le registrazioni, o si scrivono a mano?
- [ ] le quattro righe dei tassi bastano sempre? Cosa succede quando si esauriscono.
- [ ] la casella Prestiti Gruppo Interno.

## Banche

`docs/moduli/contabilita/banche.md`

- [ ] la maschera non calcola né verifica il CIN a partire da ABI, CAB e numero di conto. È voluto, o va segnalato all'utente che il controllo è a suo carico?
- [ ] due etichette della maschera hanno un refuso — "Citta" senza accento e "Nun. Conto" invece di "Num. Conto". Vanno corrette nel programma o riportate così come sono anche nelle prossime versioni del manuale?

## Causali contabili

`docs/moduli/contabilita/causali-contabili.md`

- [ ] la griglia dello schema di registrazione. Le colonne sono Codice, Descrizione, Registro, Imputazione e D/A, ma non è chiaro come si compilano le righe né cosa contenga Imputazione. Serve una prova sulla maschera.
- [ ] la differenza fra le due caselle di IVA di cassa (D.L. 185/2008 e D.L. 83/2012) — quando si usa l'una e quando l'altra?
- [ ] l'etichetta "Richiesta Allegati su Registrazone" ha un refuso (manca la "i" di Registrazione). Va corretta nel programma?

## Centri di costo/ricavo

`docs/moduli/contabilita/centri-di-costo.md`

- [ ] il campo Gruppo. L'elenco viene riempito dal programma: quali valori contiene e a che cosa serve il raggruppamento?
- [ ] la maschera si chiama "Centri di Costo/Ricavo" ma non c'è un campo che distingua un centro di costo da uno di ricavo. La distinzione si fa altrove?

## Commesse di contabilità analitica

`docs/moduli/contabilita/commesse.md`

- [ ] dove finiscono i due file Excel di Piano Fatt. e Monitoraggio — cartella, nome del file, e se si aprono da soli. Dal codice non risulta alcun messaggio a fine elaborazione.
- [ ] il pulsante SAL... sulla scheda Subappaltatori apre una maschera a sé (avanzamenti del subappalto). Va documentata separatamente?
- [ ] la differenza operativa fra Varianti e Claims. Le due schede hanno le stesse colonne e la stessa maschera: cosa distingue le une dagli altri nell'uso.
- [ ] nella scheda Carichi una colonna si legge "Nnum. Fat." (refuso per "Num. Fat."). Va corretta nel programma?

## Comunicazioni IVA

`docs/moduli/contabilita/comunicazioni-iva.md`

- [ ] quali di questi adempimenti siano ancora in vigore e quali restino per gli anni pregressi.
- [ ] quali valori contiene l'elenco "Carica" oltre a 0 - NESSUNA e 1 - TEST.
- [ ] in quale cartella vengono prodotti i file da trasmettere.
- [ ] come le aggregazioni entrano nel calcolo della soglia e quale soglia sia.
- [ ] i campi della maschera Spesometro: il decodificatore non ne ha estratti.

## Conti per la riclassificazione

`docs/moduli/contabilita/conti-riclassificazione.md`

- [ ] le cinque caselle del codice vanno compilate tutte, o si lasciano a zero i livelli non usati? E come si costruisce un livello intermedio che raggruppa quelli sotto?
- [ ] se la griglia della finestra Riclassificazione Conti salvi a ogni cella confermata, come le altre griglie del programma.

## Integrazioni, operazioni speciali e cointestatari

`docs/moduli/contabilita/corrispettivi-speciali-cointestatari.md`

- [ ] qual è la soglia oltre la quale un corrispettivo va integrato, e se il programma la controlli.
- [ ] cosa contiene il campo "Persona" dei cointestatari.
- [ ] come le operazioni speciali entrano nelle comunicazioni IVA.
- [ ] se le due stampe di Operazioni Speciali e Cointestatari usino davvero la stessa maschera, come sembra dal codice.

## Esportazione movimenti

`docs/moduli/contabilita/esportazione-movimenti.md`

- [ ] in quale cartella e con quale nome viene prodotto il file, per ciascuno dei quattro tracciati.
- [ ] se il titolo della finestra cambi secondo il tracciato scelto o resti sempre "Esportazione Prima Nota".
- [ ] come si annulla il segno di "già esportato" su una registrazione, se serve rifare l'esportazione da zero.

## Fatture elettroniche passive

`docs/moduli/contabilita/fatture-elettroniche-passive.md`

- [ ] dove si acquista il credito per il servizio e come si controlla il residuo.
- [ ] cosa succede alle fatture archiviate: dove si ritrovano.
- [ ] quali colonne mostra l'elenco delle fatture da elaborare: il decodificatore non le ha estratte.
- [ ] se la contabilizzazione apra la prima nota precompilata o registri direttamente.
- [ ] cosa fa il pulsante "Filtra", che nella barra usa l'icona del calendario.

## Gestione prima nota

`docs/moduli/contabilita/gestione-prima-nota.md`

- [ ] dove vengono salvati i file allegati con F7 - Allegati e se ci sia un limite di dimensione.
- [ ] come si marca una registrazione come "da verificare" e chi toglie poi la spunta.
- [ ] cosa stampa esattamente F9 - Stampa: l'elenco a video o un brogliaccio completo.

## Liquidazione IVA e ventilazione

`docs/moduli/contabilita/liquidazione-iva.md`

- [ ] quali voci contiene esattamente l'elenco "Trimestre": riporta i dodici mesi, ma non ho verificato come vi compaiano i trimestri.
- [ ] dove si sceglie il metodo di calcolo dell'acconto citato dal messaggio "Indicare il Metodo solo se acconto diverso da Zero!".
- [ ] in che formato e in quale cartella viene prodotto il file dell'Elenco Clienti e Fornitori.
- [ ] se la liquidazione generi anche la registrazione contabile dell'IVA da versare, o solo il prospetto.

## Mastri

`docs/moduli/contabilita/mastri.md`

- [ ] la casella Iva Esente. Che effetto ha sulle registrazioni e sui registri IVA?

## Registrazione di prima nota

`docs/moduli/contabilita/registrazione-prima-nota.md`

- [ ] quali campi della testata compaiono o spariscono secondo la causale scelta.
- [ ] cosa apre esattamente "F9 - Integr." e a cosa servono le integrazioni.
- [ ] da dove si aprono le competenze (ratei e risconti): non ho individuato il comando nella maschera.
- [ ] cosa fa il pulsante "Fatture Elettroniche" nella registrazione: se prelevi i dati dalla fattura ricevuta o apra solo l'elenco.

## Registri IVA

`docs/moduli/contabilita/registri-iva.md`

- [ ] che rapporto c'è fra il campo Mese e i campi Dal/Al: se il mese sia solo l'intestazione o filtri anch'esso.
- [ ] se il titolo della finestra cambi secondo il registro scelto o resti sempre "Stampa Registro".

## Rinumerazione protocolli

`docs/moduli/contabilita/rinumerazione-protocolli.md`

- [ ] con quale criterio vengono riassegnati i protocolli: per data di registrazione, per data documento o per numero di registrazione.
- [ ] se la rinumerazione riparta da 1 o dal primo protocollo dell'anno.
- [ ] se il programma avvisi quando i registri sono già stati stampati sul bollato.

## Scheda cliente, fornitore e conto

`docs/moduli/contabilita/schede-contabili.md`

- [ ] se la Sezione filtri anche il saldo iniziale o solo le righe del periodo.
- [ ] a cosa serve la colonna Sel. oltre che alla stampa: F5 e F6 spuntano tutto, ma non ho individuato quale comando usi la selezione.

## Sezioni

`docs/moduli/contabilita/sezioni.md`

- [ ] in quali casi reali si usano più sezioni? Un esempio concreto renderebbe la pagina molto più utile.

## Sottoconti

`docs/moduli/contabilita/sottoconti.md`

- [ ] la Riclassificazione ha cinque caselle affiancate. Corrispondono ai cinque livelli del codice di riclassificazione? Vanno compilate tutte o solo le prime?
- [ ] il tipo TRANSITORI. In quali casi si usa?

## Stampe contabili

`docs/moduli/contabilita/stampe-contabili.md`

- [ ] dove si leggono i progressivi (pagina, rigo, dare, avere) da riportare nella stampa successiva: presumibilmente nelle Date Bollati della ditta.
- [ ] cosa cambia fra "Tipo Stampa" GRAFICA e TESTO in termini di stampanti supportate.
- [ ] come si indicano più sezioni nel libro giornale, visto che il messaggio parla di "troppe sezioni selezionate".

## Stampe del piano dei conti

`docs/moduli/contabilita/stampe-piano-dei-conti.md`

- [ ] se "Stampa Piano dei Conti con Totali" mostri i saldi del periodo o quelli progressivi a fine periodo.
- [ ] cosa stampa "Stampa Schede Conti" lasciando vuoti Mastro, Conto e Sottoconto.

## Statistiche e controlli contabili

`docs/moduli/contabilita/statistiche-e-controlli.md`

- [ ] cosa contengono esattamente i "rapporti contabili" di Stampa Rapporti.
- [ ] se la compensazione fra i due saldi vada poi registrata a mano o esista una funzione che la genera.
- [ ] quali colonne mostra la griglia dei Saldi Compensazione: il decodificatore delle etichette non le ha estratte.

## Tipi di pagamento

`docs/moduli/contabilita/tipi-di-pagamento.md`

- [ ] il riquadro Tratta IVA. Le tre scelte sono chiare come etichette, ma l'effetto sul documento va spiegato con un esempio: quando conviene "Prima Rata"?
- [ ] gli importi di Spese Bolli e Commissioni Bancarie sono per documento o per rata?
- [ ] questa pagina sostituisce la vecchia "Condizioni di pagamento", che portava un nome non presente a video. Se il nome "condizioni di pagamento" è quello che usano i clienti a voce, conviene aggiungerlo come sinonimo nel glossario.

## Titoli

`docs/moduli/contabilita/titoli.md`

- [ ] quali campi sono obbligatori. La maschera non fa i controlli tipici delle altre tabelle, e il numero è assegnato dal programma: va provata per capire cosa succede salvando un titolo incompleto.
- [ ] le voci di menu Gestione Titoli Scaduti e Gestione Titoli Attivi sono due maschere a sé, da documentare separatamente.
- [ ] il titolo della finestra è "Acquisizione Titoli", mentre la voce di menu dice "Titoli ▸ Inserimento". Quale nome usare nel manuale?

## Acquisizione delle letture

`docs/moduli/inventario/acquisizione-letture.md`

- [ ] se le letture dello stesso articolo e deposito vengano sommate in chiusura o se contino come righe distinte.
- [ ] le voci "EIA THUNDER" e "EIA SOLARIS" dell'elenco Origine puntano allo stesso tipo di terminale: verificare se è voluto.
- [ ] quali sono i nomi esatti delle colonne facoltative del foglio Excel di importazione.

## Chiusura dell'inventario

`docs/moduli/inventario/chiusura-inventario.md`

- [ ] cosa contiene il file di log della chiusura e dove viene scritto.
- [ ] se la chiusura sommi le letture ripetute dello stesso articolo o consideri solo l'ultima.
- [ ] quali sono i campi delle maschere di "Azzeramento Articoli non Inventariati" e "Azzeramento Articoli con Esistenza Negativa" nella versione con taglie e colori, dove il percorso è diverso.

## Stampe dell'inventario

`docs/moduli/inventario/stampe-inventario.md`

- [ ] se "Stampa Articoli Inventariati" consideri inventariato l'articolo per la data ultimo inventario o per la presenza di una lettura.
- [ ] su quale criterio il "Raggruppamento" per GRUPPO e SOTTOGRUPPO aggrega le righe.

## Analisi fornitore

`docs/moduli/listini-fornitori/analisi-fornitore.md`

- [ ] se la maschera consideri tutti gli articoli o solo quelli presenti nel listino del fornitore scelto.
- [ ] se il confronto usi il prezzo di listino o il prezzo netto dopo gli sconti.
- [ ] su quale deposito è calcolata la colonna Esistenza.

## Gestione listini fornitori

`docs/moduli/listini-fornitori/gestione-listini-fornitori.md`

- [ ] la seconda domanda ("Vuoi interrompere la cancellazione ?") è formulata al contrario rispetto alla prima: verificare a video che l'ordine delle risposte sia quello descritto.
- [ ] quali altre colonne del foglio Excel vengono lette oltre a CODICE e BARCODE (prezzo, sconti, pezzi per confezione).
- [ ] come una riga del listino fornitore viene collegata all'articolo di anagrafica.

## Analisi listino da vendite ed esistenza

`docs/moduli/listini-vendita/analisi-listino.md`

- [ ] come si chiama a video, nelle impostazioni della ditta, la causale di rettifica inventario usata dalla colonna Esistenza.
- [ ] su quale listino agisce la colonna "Nuovo Prezzo" e come si sceglie: non ho individuato un campo nella maschera che lo indichi.
- [ ] quali colonne del foglio Excel di importazione vengono lette oltre a CODICE.

## Conferma e confronto dei listini

`docs/moduli/listini-vendita/controllo-listini.md`

- [ ] come un documento diventa "VERIFICATO" nel filtro di Conferma Listini — se basta il salvataggio o serve un'azione esplicita.
- [ ] se in Conferma Listini il salvataggio scriva sempre sul listino 1 o sul listino indicato nel campo in alto.
- [ ] da dove Conferma Listini prende il "Miglior Listino Fornitore": presumibilmente dai listini di acquisto, ma va confermato.

## Copia listini

`docs/moduli/listini-vendita/copia-listini.md`

- [ ] come si chiama a video l'impostazione che rende gli archivi "a gestione comune" fra le ditte, per poterla citare nel messaggio corrispondente.
- [ ] se la copia da altra ditta riporti anche le variazioni di listino programmate, oltre ai prezzi in vigore.

## Gestione listini

`docs/moduli/listini-vendita/gestione-listini.md`

- [ ] in che momento vengono salvate le correzioni fatte direttamente nelle celle della griglia (a ogni cella, alla chiusura, o con un comando che non ho individuato).
- [ ] se i prezzi scritti in celle Excel di tipo numerico vengano importati con i decimali.
- [ ] quale impostazione della ditta fa nascondere la colonna Codice a favore di Cod.Forn. e come si chiama a video.

## Importazione listino

`docs/moduli/listini-vendita/importazione-listino.md`

- [ ] per ciascun formato, quale estensione e quale tracciato il file deve avere; ho potuto accertare solo il .mrc di Fenapro, il renault.txt di Renault e i file Excel dei due formati Tabacchi.
- [ ] quali importazioni inseriscono articoli nuovi e quali si limitano ad aggiornare i prezzi degli articoli già presenti.
- [ ] se le importazioni scrivano i prezzi con effetto immediato o li mettano fra le variazioni programmate.
- [ ] se l'importazione Renault possa leggere un file scelto dall'utente invece del solo "in\renault.txt".

## Stampa listini

`docs/moduli/listini-vendita/stampa-listini.md`

- [ ] cosa fa esattamente l'ordinamento "CASUALE": presumibilmente lascia l'ordine dell'archivio, ma va confermato con una prova.
- [ ] se "Filtro su Desc." accetti davvero i caratteri jolly come gli altri filtri sugli articoli.
- [ ] se il formato "COSTI RICARICO E MAGINE" compaia a video proprio così (il nome del modello di stampa contiene un refuso).

## Variazioni di listino programmate

`docs/moduli/listini-vendita/variazione-listini.md`

- [ ] se le variazioni già applicate restino consultabili da qualche parte, o spariscano dall'elenco di Variazioni Listini.
- [ ] in quale momento esatto il programma propone di apportare le variazioni scadute (all'avvio, al cambio ditta, o entrambi).
- [ ] se "Apporta Variazioni" accetti anche una data futura, applicando in anticipo variazioni non ancora scadute.

## Variazioni di massa dei listini

`docs/moduli/listini-vendita/variazioni-di-massa.md`

- [ ] con Riferimento "PREZZO MEDIO D'ACQUISTO", se il medio è calcolato solo sul deposito attivo o su tutti i depositi.
- [ ] se il campo della variazione, in Varia Listini, accetta valori negativi come mi aspetto.
- [ ] i nomi esatti con cui i tipi di vendita "C.S. Vendita" e "C.S. Trasfert" sono chiamati altrove nel programma: i messaggi di conferma li chiamano "Concessionario" e "Delivery".
- [ ] quale impostazione del programma fa comparire i tipi di vendita oltre a "Normale", e come si chiama a video.

## Anomalie carichi e promozioni sellin

`docs/moduli/magazzino/anomalie-e-promozioni-sellin.md`

- [ ] la struttura della maschera delle promozioni sellin e i suoi campi.
- [ ] i campi delle promozioni sellin.
- [ ] i comandi effettivi della maschera delle promozioni sellin.
- [ ] i messaggi di queste maschere.
- [ ] come l'anomalia si collega al carico su cui è stata riscontrata.
- [ ] cosa produce la contabilizzazione di un'anomalia.
- [ ] come le promozioni sellin entrano nel calcolo dei costi e dei margini.

## Movimenti dei banchi conservatori

`docs/moduli/magazzino/banchi-conservatori-movimenti.md`

- [ ] i messaggi di queste maschere.
- [ ] se il movimento aggiorni da solo lo Stato e il Cliente nella scheda dell'attrezzatura.
- [ ] se la consegna generi un documento di trasporto vero o richieda solo di annotarne gli estremi.
- [ ] come si sceglie quale attrezzatura consegnare: il campo non compare fra le etichette che ho potuto estrarre.

## Carico merci

`docs/moduli/magazzino/carico-merci.md`

- [ ] i messaggi di questa maschera e delle voci che la accompagnano.
- [ ] come si ripartisce la "% Spese" sulle righe: in proporzione al valore, al peso o alla quantità.
- [ ] cosa cambia nel comportamento del programma secondo lo Stato del carico.
- [ ] che rapporto c'è fra il carico e la registrazione di prima nota citata da "Prima Nota. N.".
- [ ] cosa sono i "Carichi Fiscali" e in cosa la loro maschera differisce da questa.

## Categorie merceologiche

`docs/moduli/magazzino/categorie-merceologiche.md`

- [ ] i tre %Ricarico corrispondono ai tre listini di vendita? La corrispondenza va confermata.
- [ ] i campi Cod. Articolo e Suffisso servono alla generazione automatica del codice articolo. Come si combinano con la regola generale già descritta nella scheda degli articoli?
- [ ] le nove coppie di sconto e provvigione corrispondono agli scaglioni indicati sul cliente o sull'agente?

## Causali magazzino

`docs/moduli/magazzino/causali-magazzino.md`

- [ ] il rapporto fra il campo Causale (contropartita) e la casella Movimentazione Interna. Vanno impostati sempre insieme, o esistono casi in cui si usa l'uno senza l'altra?
- [ ] la differenza operativa fra i contatori Venduta e Venduto Periodo, e a quale periodo si riferisce il secondo.
- [ ] conviene pubblicare l'elenco delle causali standard fornite con l'installazione, come riferimento?

## Depositi

`docs/moduli/magazzino/depositi.md`

- [ ] i campi Fornitore e Cod. Destinazione. Si scrivono a mano, senza elenco da cui scegliere: in quale scenario operativo si compilano (conto deposito? magazzini di terzi?).
- [ ] la differenza pratica fra Escludi Visibilità Web e Escludi Interrogazione da Web.

## Gruppi taglie

`docs/moduli/magazzino/gruppi-taglie.md`

- [ ] l'avvertenza sull'ordine delle righe è dedotta da come le giacenze per taglia sono organizzate. Va confermata con una prova prima di pubblicarla.
- [ ] il campo Rifer. a che cosa serve nell'uso quotidiano — è il codice taglia del fornitore, o un riferimento interno?

## Marchi

`docs/moduli/magazzino/marchi.md`

- [ ] le due voci dell'elenco Stock Ecommerce non hanno un'etichetta leggibile nel disegno della maschera. Quali sono, e quale delle due espone le giacenze sul sito?

## Movimenti di magazzino

`docs/moduli/magazzino/movimenti-magazzino.md`

- [ ] i messaggi di questa maschera.
- [ ] se esista una causale di trasferimento che muove entrambi i depositi in un colpo solo.
- [ ] se il movimento generi una registrazione contabile.

## Produzione

`docs/moduli/magazzino/produzione.md`

- [ ] la struttura delle maschere di produzione e i loro campi: non ho potuto estrarne le etichette dalle risorse.
- [ ] i campi delle maschere di produzione.
- [ ] i comandi effettivi delle maschere di produzione.
- [ ] i messaggi delle maschere di produzione.
- [ ] se la distinta ammetta più livelli, cioè componenti che sono a loro volta prodotti finiti.
- [ ] che rapporto c'è fra "Inizio Nuova Produzione" e "Inserimento Carico da produzione": se siano due passi della stessa cosa o due strade alternative.
- [ ] con quale criterio "Aggiornamento Costi" calcola il costo del finito.

## Reparti

`docs/moduli/magazzino/reparti.md`

- [ ] quando si usa Reparto Cassa 2 invece di Reparto Cassa? Serve un esempio di installazione reale.
- [ ] la casella Non Fiscale. Che effetto ha esattamente sullo scontrino?

## Stampe magazzino clienti

`docs/moduli/magazzino/stampe-magazzino-clienti.md`

- [ ] i campi esatti della maschera di selezione: cambiano secondo la stampa e non ho potuto estrarli tutti.
- [ ] i messaggi di queste stampe.
- [ ] cosa distingue "Analisi Vendite" dalle varie sintesi.
- [ ] cosa sono le "sostituzioni" a cui due voci fanno riferimento.

## Stampe magazzino fornitori

`docs/moduli/magazzino/stampe-magazzino-fornitori.md`

- [ ] i campi esatti della maschera di selezione per le stampe fornitori.
- [ ] i messaggi di queste stampe.
- [ ] se queste stampe considerino solo i carichi o anche i resi a fornitore.

## Stampe dei movimenti di magazzino

`docs/moduli/magazzino/stampe-movimenti-magazzino.md`

- [ ] i campi delle maschere proprie di Interrogazione Articolo, Valore Magazzino, Movimenti Periodo, Registro Sostanze Zuccherine ed Esistenze da Lettore Formula 734.
- [ ] i messaggi di queste stampe.
- [ ] cosa misura la "percentuale di sell-out" e come è calcolata.
- [ ] con quale criterio "Valore Magazzino" valorizza le giacenze: ultimo costo, medio o altro.
- [ ] che differenza c'è fra "Movimenti Periodo" e "Sintesi Movimenti per Giorno".

## Tabelle di classificazione

`docs/moduli/magazzino/tabelle-di-classificazione.md`

- [ ] le voci di menu Toni e Colori Interni scrivono sulla stessa tabella. È voluto (due nomi per lo stesso elenco) o è un errore nel menu da correggere?
- [ ] la tabella Periodi. Il nome non dice a quale uso siano destinati questi periodi.
- [ ] la tabella Categorie Fiscali. Come si differenzia dalle Aliquote IVA nell'uso quotidiano?
- [ ] il campo "%Ric. Spese" dei listini di vendita. Dove viene applicato: sul prezzo di vendita, sulle spese del documento, o altro?

## Unità di misura

`docs/moduli/magazzino/unita-di-misura.md`

- [ ] il Coef. Moltip. converte fra quale coppia di unità? Serve un esempio numerico che oggi non ho.
- [ ] la casella Riporta Colli. In quali documenti ha effetto?

## Ordini tabacchi

`docs/moduli/ordini/ordini-tabacchi.md`

- [ ] cosa significano le voci "O", "S" e "M" dell'elenco Tipo: a video compaiono come lettere sole, accanto a SPECIALE e URGENTE che sono per esteso.
- [ ] che aspetto ha il fax U88 e come viene inviato — se in stampa, per posta o su file.

## Richieste offerta

`docs/moduli/ordini/richieste-offerta.md`

- [ ] i messaggi propri delle richieste offerta.
- [ ] se la richiesta offerta venga marcata in qualche modo dopo che ne è stato generato l'ordine.
- [ ] se le richieste offerta compaiano nelle stampe degli ordini per articolo.

## Scambio degli ordini con l'esterno

`docs/moduli/ordini/scambio-ordini.md`

- [ ] cosa contiene esattamente il file di configurazione imp_mobile e chi lo prepara.
- [ ] quale tracciato hanno i file .rsa degli ordini e se è documentato altrove.

## Stampe degli ordini

`docs/moduli/ordini/stampe-ordini.md`

- [ ] i messaggi propri di queste stampe.
- [ ] quali colonne distinguono nel concreto le due stampe (ordxart.rpt e ordxarts.rpt).

## Controllo crediti e debiti

`docs/moduli/scadenze/controllo-crediti.md`

- [ ] i campi di queste maschere: sono cinque diverse e non ho potuto estrarne le etichette dalle risorse.
- [ ] i messaggi di queste maschere, compreso il caso del mittente non impostato per l'invio degli estratti conto.
- [ ] cosa distingue "Credito Circolante" da "Stampa Controllo Crediti".
- [ ] se il Controllo Crediti confronti l'esposizione con il fido del cliente.
- [ ] come vengono inviati gli estratti conto: per posta elettronica, in stampa o entrambi.

## Distinte di incasso e di pagamento

`docs/moduli/scadenze/distinte-incasso-pagamento.md`

- [ ] i messaggi di queste maschere.
- [ ] se la distinta generi la registrazione contabile dell'incasso o solo la chiusura della scadenza.
- [ ] cosa succede a una distinta annullata: se le scadenze tornino aperte.
- [ ] da dove arrivano gli incassi dell'agente e in che formato.

## Effetti e RI.BA.

`docs/moduli/scadenze/effetti-e-riba.md`

- [ ] i messaggi di queste maschere.
- [ ] quali valori contiene l'elenco "Formato Stampa" delle RI.BA. e quali moduli prestampati supporta.
- [ ] in quale cartella e con quale nome viene prodotto il file di flusso, e in che tracciato.
- [ ] quali registrazioni genera "Contabilizza Effetti" e su quali conti.
- [ ] i campi della maschera di generazione del file di flusso: non ho potuto estrarne le etichette.

## Gestione scadenze

`docs/moduli/scadenze/gestione-scadenze.md`

- [ ] i messaggi di questa maschera.
- [ ] quali campi si compilano aprendo una scadenza con F2 - Modifica.
- [ ] come una scadenza viene marcata come pagata: se dalla distinta o a mano da questa maschera.

## Manutenzione dello scadenziario

`docs/moduli/scadenze/manutenzione-scadenze.md`

- [ ] i campi di queste maschere e la struttura del cruscotto: non ho potuto estrarne le etichette dalle risorse.
- [ ] i messaggi di queste maschere.
- [ ] se "Elimina Scadenze" tolga solo le scadenze chiuse o tutte quelle del periodo.
- [ ] cosa mostra il Cruscotto Finaziario e su quali dati è costruito.
- [ ] come il controllo presenta le discordanze: stampa, griglia o messaggio.

## Stampe delle scadenze

`docs/moduli/scadenze/stampe-scadenze.md`

- [ ] i campi propri di Stampa Sintesi, Stampa Interessi di Mora e Stampa Estratto Conto per Documento: non ho potuto estrarli tutti.
- [ ] i messaggi di queste stampe.
- [ ] con quale tasso vengono calcolati gli interessi di mora e dove si imposta.
- [ ] se il testo della lettera di sollecito sia modificabile e dove.

## Esportazione documenti per tracciato

`docs/moduli/trasferimenti/esportazione-documenti.md`

- [ ] quali campi compaiono per ciascun tracciato: la maschera ne nasconde una parte a seconda del formato scelto.
- [ ] i messaggi di questa maschera: il file EsportazioneDocumenti.cpp supera le 24.000 righe e i messaggi sono specifici per tracciato.
- [ ] in quale cartella e con quale nome viene scritto il file di ciascun tracciato.
- [ ] dove si impostano i codici del destinatario su clienti e articoli per ciascun tracciato.
- [ ] se esista un registro delle esportazioni già effettuate.

## Esportazioni con maschera propria

`docs/moduli/trasferimenti/esportazioni-specifiche.md`

- [ ] i messaggi propri della generazione dati per Facile Mobile e della trasmissione 730.
- [ ] in quale cartella finiscono i file generati da ciascuna di queste esportazioni.
- [ ] come Facile ricorda il punto dell'ultima esportazione e come lo si azzera.
- [ ] che cosa comprende esattamente "Genera Dati per Facile Mobile" e come i dati arrivano ai dispositivi.

## Ricezione dati

`docs/moduli/trasferimenti/ricezione-dati.md`

- [ ] i campi delle maschere di importazione WinWork e Diamante.
- [ ] se l'uso della stessa procedura per le promozioni CDS e SIDA sia voluto o un residuo.
- [ ] in quale cartella ciascuna procedura cerca il proprio file.
- [ ] cosa comprende esattamente "Aggiornamento Dati Agenti" e in che verso viaggiano i dati.

## Assistenza

`docs/moduli/utility/assistenza.md`

- [ ] i messaggi finali di riepilogo delle variazioni di codice.
- [ ] quali archivi vengono toccati da ciascuna variazione di codice.
- [ ] cosa fa "Abilita NoSync" e in quali situazioni l'assistenza lo usa.
- [ ] che differenza c'è fra "Inversione Modalità IVA" e la coppia "Articoli IVA Inclusa/Esclusa".

## Esercizi, ditte e chiusure contabili

`docs/moduli/utility/esercizi-e-chiusure.md`

- [ ] cosa comprende esattamente il riporto delle esistenze di magazzino del nuovo esercizio.
- [ ] i campi di "Seleziona Archivio" e cosa succede agli utenti collegati quando si cambia archivio.

## Etichette codici a barre

`docs/moduli/utility/etichette-barcode.md`

- [ ] dove si configurano i formati delle etichette e quali sono quelli standard.
- [ ] quale file viene letto da "Stampa Etichette Barcode da File" e in che formato.

## Gestione della licenza

`docs/moduli/utility/gestione-licenza.md`

- [ ] il testo esatto della richiesta di conferma della disattivazione (stringa IDS_DISATTIVAZIONE).
- [ ] come si comunica a R.S.A. l'attivazione e se serva un collegamento a internet.

## Impostazioni della postazione

`docs/moduli/utility/impostazioni-postazione.md`

- [ ] i campi delle sei finestre minori (stampanti, WebApiService, pagamenti elettronici, EFT Pos, messaggi, stampanti comande).
- [ ] i messaggi di queste maschere.
- [ ] dove sono memorizzate queste impostazioni e se si possano copiare da una postazione all'altra.
- [ ] cosa fa esattamente "Utilizza Server SQL ove Possibile" e quando conviene attivarla.

## Manutenzione degli archivi

`docs/moduli/utility/manutenzione-archivi.md`

- [ ] i messaggi propri dei ricalcoli e della valorizzazione.
- [ ] cosa fa esattamente "Aggiorna Catalogo Dati" sugli archivi.
- [ ] da dove vengono lette le fotografie di "Importa Foto" e con quale criterio sono associate agli articoli.
- [ ] se "Importa" da GESA sia ancora utilizzabile e in quali passaggi.

## Acconti

`docs/moduli/vendite/acconti.md`

- [ ] come l'acconto registrato qui viene scalato dal documento definitivo: se automaticamente o a mano.
- [ ] se l'acconto generi una registrazione contabile o resti solo un promemoria.

## Contabilizzazione dei documenti

`docs/moduli/vendite/contabilizzazione-documenti.md`

- [ ] i campi esatti delle maschere di contabilizzazione e di controllo.
- [ ] i messaggi delle maschere di contabilizzazione e controllo.
- [ ] se la contabilizzazione riconosca i documenti già contabilizzati e li salti.
- [ ] cosa mostra esattamente il risultato del controllo: una stampa, una griglia o un messaggio.
- [ ] perché DDT, bolle e buoni di consegna non hanno la voce Contabilizza: presumibilmente perché si contabilizzano le fatture che ne derivano.

## Documenti accompagnatori semplificati

`docs/moduli/vendite/documenti-accompagnatori-semplificati.md`

- [ ] la struttura della maschera e i suoi campi: non ho potuto estrarne le etichette dalle risorse.
- [ ] i campi del documento accompagnatorio semplificato.
- [ ] i comandi effettivi di questa maschera.
- [ ] i messaggi di questa maschera.
- [ ] quali dati dell'articolo servono per emettere un DAS e dove si impostano.
- [ ] il rapporto fra questi documenti e la Stampa Registro Sostanze Zuccherine del menu Magazzino.

## Documento di vendita

`docs/moduli/vendite/documento-di-vendita.md`

- [ ] i messaggi di questa maschera. È la più grande del programma e i controlli sono molti: vanno raccolti in una passata dedicata.
- [ ] quali campi della testata compaiono o spariscono secondo il tipo di documento.
- [ ] cosa contengono il Piede e i Totali: non ho potuto estrarne le etichette.
- [ ] a cosa serve il pulsante Tracc. e quali dati di tracciabilità raccoglie.
- [ ] in quale momento il documento scarica il magazzino: al salvataggio o alla stampa.

## Esportazione, duplicazione e ricezione dei documenti

`docs/moduli/vendite/esporta-duplica-documenti.md`

- [ ] i campi delle maschere di esportazione e di ricezione.
- [ ] come sono configurati i palmari e il server FTP da cui si ricevono i documenti.

## Fatture elettroniche attive

`docs/moduli/vendite/fatture-elettroniche-attive.md`

- [ ] la struttura delle due finestre e le colonne delle griglie: non ho potuto estrarle dalle risorse.
- [ ] i campi di selezione delle due maschere.
- [ ] i comandi delle due maschere.
- [ ] i messaggi delle due maschere.
- [ ] se il cruscotto scarichi gli esiti da solo o vada aggiornato con un comando.
- [ ] dove si legge il motivo dello scarto di una fattura.

## Fatture ricorrenti

`docs/moduli/vendite/fatture-ricorrenti.md`

- [ ] quali cadenze contiene l'elenco Periodicità oltre ad ANNUALE, SEMESTRALE e QUADRIMESTRALE.
- [ ] come il programma sa quali schede sono in scadenza: se da una data di ultima fatturazione sulla scheda.
- [ ] se l'emissione chieda una data di riferimento o lavori sempre su oggi.

## Gestione documenti

`docs/moduli/vendite/gestione-documenti.md`

- [ ] quali registri compaiono nell'elenco Registro e da dove sono presi.

## Preventivi

`docs/moduli/vendite/preventivi.md`

- [ ] se esista un comando per trasformare un preventivo accettato in ordine o in fattura.
- [ ] se i campi delle condizioni (Consegna, Imballo, Resa, Garanzia) abbiano dei valori proposti o siano sempre da scrivere.

## Promozioni

`docs/moduli/vendite/promozioni.md`

- [ ] i campi della testata della promozione: dalle risorse ho potuto estrarre solo il Registro.
- [ ] gli altri campi della testata — periodo di validità, descrizione, depositi o punti vendita interessati.
- [ ] i messaggi di questa maschera.
- [ ] dove si indica il periodo di validità della promozione.
- [ ] cosa apre esattamente "F9 - Dati".
- [ ] cosa succede alla fine del periodo: se il prezzo torni da solo a quello di listino.
- [ ] il rapporto con le "Promozioni Sellin" del menu Magazzino.

## Provvigioni agenti e capi area

`docs/moduli/vendite/provvigioni-agenti.md`

- [ ] cosa rende una provvigione "anomala" nella stampa di controllo.
- [ ] che differenza c'è fra "Attribuzione Automatica Provvigioni Mancanti" e "Attribuzione Provvigioni per Cliente". Nota: entrambe le voci di menu contengono un doppio spazio.
- [ ] dove si segna una provvigione come saldata, visto che la stampa filtra su "Saldati".
- [ ] cosa calcola esattamente "Incentivi Personale" e su quali dati.

## Riepiloghi e statistiche di vendita

`docs/moduli/vendite/riepiloghi-e-statistiche.md`

- [ ] i campi esatti di ciascuna maschera: variano fra riepiloghi e statistiche e non ho potuto estrarli tutti.
- [ ] cosa distingue "Statistiche" da "Statistiche Mensili".
- [ ] se le sette voci "Fatturato Mensile per…" aprano la stessa maschera con un parametro, come sembra.
- [ ] la voce di menu dice "Fatturato Mensile per Marchio" ma l'identificativo interno parla di stagione: verificare cosa raggruppa davvero.

## Ristampa dei documenti

`docs/moduli/vendite/ristampa-documenti.md`

- [ ] se la ristampa aggiorni la data o il contatore di stampa del documento.
- [ ] dove viene prodotto il file quando è attiva "Solo Esportazione".

## Scontrini

`docs/moduli/vendite/scontrini.md`

- [ ] cosa significa la voce di menu "Altri Scarichi - Scontrini": il titolo del menu e quello della finestra non coincidono.
- [ ] cosa verifica esattamente il "Controllo Conferimento" e su quali dati.
- [ ] quali valori assumono le colonne SF, Azz., Tran. e Sync.

## Stampe e strumenti di vendita

`docs/moduli/vendite/stampe-vendite.md`

- [ ] i campi esatti di ciascuna di queste maschere: sono sette diverse e non ho potuto estrarli tutti.
- [ ] i messaggi di queste maschere.
- [ ] cosa distingue "Stampa Distinta Carico Trasportatori" da "Stampa Distinta Trasportatori".
- [ ] da quali documenti nascono le liste di prelievo e se si possa scegliere quali includere.
- [ ] cosa mostra "Analisi Commessa" rispetto alla scheda della commessa in Archivi.
- [ ] cosa vuol dire "valorizzare" un documento trasfert e quali valori vengono attribuiti.

## Vendita al banco e POS

`docs/moduli/vendite/vendita-al-banco.md`

- [ ] la struttura esatta delle due schermate. Sono costruite a runtime e le etichette non stanno nelle risorse, quindi vanno descritte guardandole a video.
- [ ] i campi delle due schermate di vendita.
- [ ] i messaggi delle due schermate di vendita.
- [ ] che differenza c'è, nei dati registrati, fra la vendita da tastiera e quella da POS touchscreen.
- [ ] come si associa un cliente allo scontrino, per la raccolta punti.
