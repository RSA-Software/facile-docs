# Domande aperte del manuale Facile

Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.
Aggiornato al 2026-09-19 — **9 domande** su 8 pagine.

Ogni voce corrisponde a un commento HTML dentro la pagina indicata: rispondendo
alla domanda, la correzione va fatta nella pagina e il marcatore va tolto.
Per rigenerare questo elenco:

    .venv/Scripts/python.exe tools/domande-aperte.py

## Canali di vendita

`docs/moduli/altre-tabelle/canali-di-vendita.md`

- [ ] le quattro voci di "Cess. da Costo" (ULTIMO, MEDIO, NETTO, FINITO) e le quattro caselle accanto (del Canale Specifico, No Agg. se in offerta, Ribalt. Sconti F.Ft., Totale). Il programma le registra sul canale e le rilegge quando riapri la maschera, ma nessun'altra parte del programma le consulta: del canale, altrove, si usano solo il codice, la descrizione e i tre codici dei trasferimenti. Sono impostazioni che serviranno a un modulo esterno, o sono rimaste indietro rispetto al calcolo dei prezzi di cessione?

## Anagrafica agenti

`docs/moduli/anagrafiche/anagrafica-agenti.md`

- [ ] il palmare degli agenti. Dal lato Facile si vedono solo i due campi qui sopra, la ricezione ordini via FTP e la data dell'ultimo invio al tablet; l'applicazione che gira sul palmare è un programma a sé. Il manuale deve avere una pagina che racconti il giro completo — cosa si manda, quando, che cosa torna indietro — o l'applicazione dell'agente ha un manuale suo e qui basta il rimando?

## Codici catastali comuni

`docs/moduli/anagrafiche/codici-catastali-comuni.md`

- [ ] il Codice Ufficio Registro ha due caselle uguali, di tre caratteri ciascuna e senza etichetta propria. Nel programma nessuna delle due viene mai riletta, quindi il codice non dice a cosa servano. La seconda era per la sezione staccata dell'ufficio, o per qualcos'altro? Se non servono più, vale la pena toglierle dalla maschera.

## Banche

`docs/moduli/contabilita/banche.md`

- [ ] conviene che la maschera calcoli il CIN da ABI, CAB e numero di conto, e controlli il carattere di controllo dell'IBAN? Oggi non lo fa nessuno dei due, in nessun punto del programma, e l'unico effetto di un IBAN sbagliato e' che sparisce dalla fattura elettronica senza un messaggio.

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

## Causali magazzino

`docs/moduli/magazzino/causali-magazzino.md`

- [ ] conviene pubblicare l'elenco delle causali standard fornite con l'installazione, come riferimento?
