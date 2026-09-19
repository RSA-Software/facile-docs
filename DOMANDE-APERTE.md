# Domande aperte del manuale Facile

Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.
Aggiornato al 2026-09-19 — **154 domande** su 58 pagine.

Ogni voce corrisponde a un commento HTML dentro la pagina indicata: rispondendo
alla domanda, la correzione va fatta nella pagina e il marcatore va tolto.
Per rigenerare questo elenco:

    .venv/Scripts/python.exe tools/domande-aperte.py

## Convenzioni del manuale

`docs/introduzione/convenzioni.md`

- [ ] come si chiamano a video i livelli di licenza (Lite, Standard, Professional) e se il manuale debba dichiararlo esplicitamente.

## Canali di vendita

`docs/moduli/altre-tabelle/canali-di-vendita.md`

- [ ] le quattro voci di "Cess. da Costo" (ULTIMO, MEDIO, NETTO, FINITO) e le quattro caselle accanto (del Canale Specifico, No Agg. se in offerta, Ribalt. Sconti F.Ft., Totale). Il programma le registra sul canale e le rilegge quando riapri la maschera, ma nessun'altra parte del programma le consulta: del canale, altrove, si usano solo il codice, la descrizione e i tre codici dei trasferimenti. Sono impostazioni che serviranno a un modulo esterno, o sono rimaste indietro rispetto al calcolo dei prezzi di cessione?

## Anagrafica agenti

`docs/moduli/anagrafiche/anagrafica-agenti.md`

- [ ] il palmare degli agenti. Dal lato Facile si vedono solo i due campi qui sopra, la ricezione ordini via FTP e la data dell'ultimo invio al tablet; l'applicazione che gira sul palmare è un programma a sé. Il manuale deve avere una pagina che racconti il giro completo — cosa si manda, quando, che cosa torna indietro — o l'applicazione dell'agente ha un manuale suo e qui basta il rimando?

## Codici catastali comuni

`docs/moduli/anagrafiche/codici-catastali-comuni.md`

- [ ] il Codice Ufficio Registro ha due caselle uguali, di tre caratteri ciascuna e senza etichetta propria. Nel programma nessuna delle due viene mai riletta, quindi il codice non dice a cosa servano. La seconda era per la sezione staccata dell'ufficio, o per qualcos'altro? Se non servono più, vale la pena toglierle dalla maschera.

## Ditte

`docs/moduli/anagrafiche/ditte.md`

- [ ] i campi delle schede Parametri Hotel e CRM, che nella copia in uso non sono state esaminate.

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

## Banche

`docs/moduli/contabilita/banche.md`

- [ ] conviene che la maschera calcoli il CIN da ABI, CAB e numero di conto, e controlli il carattere di controllo dell'IBAN? Oggi non lo fa nessuno dei due, in nessun punto del programma, e l'unico effetto di un IBAN sbagliato e' che sparisce dalla fattura elettronica senza un messaggio.

## Causali contabili

`docs/moduli/contabilita/causali-contabili.md`

- [ ] nella colonna Imputazione la maschera accetta solo le cifre da 0 a 9, mentre il programma conosce imputazioni fino a 18 (saldo cauzioni, imponibile+IVA indetraibile, commissioni, imponibile e IVA positivi/negativi, reverse charge). Quelle da 10 in su si riescono a impostare, e come? Se no, la colonna andrebbe cambiata in un elenco a discesa.

## Commesse di contabilità analitica

`docs/moduli/contabilita/commesse.md`

- [ ] Varianti e Claims sono due elenchi identici distinti solo dall'etichetta. C'e' una regola di casa su cosa va nell'uno e cosa nell'altro, da scrivere nel manuale?
- [ ] nella scheda Carichi l'intestazione della colonna si legge «Nnum. Fat.», refuso per «Num. Fat.». Sta dentro la definizione della griglia nel .rc, quindi si corregge dal designer delle risorse (oppure con una sostituzione della stessa lunghezza nel DLGINIT). La correggo?

## Rinumerazione protocolli

`docs/moduli/contabilita/rinumerazione-protocolli.md`

- [ ] questa elaborazione riscrive i protocolli di tutto l'anno e non chiede nessuna conferma: basta un clic per distruggere la corrispondenza con i registri gia' stampati. Vale la pena metterci davanti una richiesta di conferma, o un avviso quando le Date Bollati della ditta dicono che il registro e' gia' stato stampato?

## Titoli

`docs/moduli/contabilita/titoli.md`

- [ ] il titolo della finestra è "Acquisizione Titoli", mentre la voce di menu dice "Titoli ▸ Inserimento". Quale nome usare nel manuale?

## Acquisizione delle letture

`docs/moduli/inventario/acquisizione-letture.md`

- [ ] se le letture dello stesso articolo e deposito vengano sommate in chiusura o se contino come righe distinte.
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

## Causali magazzino

`docs/moduli/magazzino/causali-magazzino.md`

- [ ] conviene pubblicare l'elenco delle causali standard fornite con l'installazione, come riferimento?

## Stampe dei movimenti di magazzino

`docs/moduli/magazzino/stampe-movimenti-magazzino.md`

- [ ] restano da elencare i campi di Interrogazione Articolo, Registro Sostanze Zuccherine ed Esistenze da Lettore Formula 734.

## Ordini tabacchi

`docs/moduli/ordini/ordini-tabacchi.md`

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

## Vendita al banco e POS

`docs/moduli/vendite/vendita-al-banco.md`

- [ ] la struttura esatta delle due schermate. Sono costruite a runtime e le etichette non stanno nelle risorse, quindi vanno descritte guardandole a video.
- [ ] i campi delle due schermate di vendita.
- [ ] i messaggi delle due schermate di vendita.
- [ ] che differenza c'è, nei dati registrati, fra la vendita da tastiera e quella da POS touchscreen.
- [ ] come si associa un cliente allo scontrino, per la raccolta punti.

## Tabella vuoti

`docs/moduli/versioni/cauzioni-vuoti.md`

- [ ] in quale documento la cauzione viene addebitata, e se il reso generi una riga di accredito automatica.
- [ ] il testo esatto della conferma di cancellazione e degli altri messaggi di questa maschera.
- [ ] confermare che i movimenti già registrati conservino la cauzione applicata al momento della consegna.

## Valenze di lavorazione

`docs/moduli/versioni/oreficerie-valenze.md`

- [ ] in quali maschere la valenza viene richiamata, e se l'importo sia proposto o imposto.
- [ ] il testo esatto della conferma di cancellazione e degli altri messaggi di questa maschera.

## Responsabili e collaboratori

`docs/moduli/versioni/studio-collaboratori.md`

- [ ] in quali maschere dello studio il collaboratore viene richiamato, e se l'attribuzione influisca su compensi o statistiche.
- [ ] il testo esatto della conferma di cancellazione e degli altri messaggi di questa maschera.
