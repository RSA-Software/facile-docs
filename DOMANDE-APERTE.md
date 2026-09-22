# Domande aperte del manuale Facile

Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.
Aggiornato al 2026-09-22 — **4 domande** su 4 pagine.

Ogni voce corrisponde a un commento HTML dentro la pagina indicata: rispondendo
alla domanda, la correzione va fatta nella pagina e il marcatore va tolto.
Per rigenerare questo elenco:

    .venv/Scripts/python.exe tools/domande-aperte.py

## Anagrafica agenti

`docs/moduli/anagrafiche/anagrafica-agenti.md`

- [ ] il palmare degli agenti. Dal lato Facile si vedono solo i due campi qui sopra, la ricezione ordini via FTP e la data dell'ultimo invio al tablet; l'applicazione che gira sul palmare è un programma a sé. Il manuale deve avere una pagina che racconti il giro completo — cosa si manda, quando, che cosa torna indietro — o l'applicazione dell'agente ha un manuale suo e qui basta il rimando?

## Codici catastali comuni

`docs/moduli/anagrafiche/codici-catastali-comuni.md`

- [ ] le due caselle del Codice Ufficio Registro sono identiche e senza etichetta propria. Verificato che nessuna delle due viene mai riletta (ne' per campo, ne' per nome di colonna SQL, ne' nei report). La seconda era per la sezione staccata dell' ufficio? E vale la pena togliere dalla maschera tutti i codici che non servono, o restano per gli archivi storici?

## Banche

`docs/moduli/contabilita/banche.md`

- [ ] conviene che la maschera calcoli il CIN da ABI, CAB e numero di conto, e controlli il carattere di controllo dell'IBAN? Oggi non lo fa nessuno dei due, in nessun punto del programma, e l'unico effetto di un IBAN sbagliato e' che sparisce dalla fattura elettronica senza un messaggio.

## Commesse di contabilità analitica

`docs/moduli/contabilita/commesse.md`

- [ ] Varianti e Claims sono due elenchi identici distinti solo dall'etichetta. C'e' una regola di casa su cosa va nell'uno e cosa nell'altro, da scrivere nel manuale?
