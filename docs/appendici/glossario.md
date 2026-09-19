---
title: Glossario
description: I termini usati in Facile e nel manuale, spiegati in una riga.
---

# Glossario

<!-- Voci in ordine alfabetico. Le pagine delle maschere rimandano qui con
     link del tipo: ../../appendici/glossario.md#partita -->

## Acconto

Denaro ricevuto dal cliente **prima** del documento che lo giustifica. Resta a
credito del cliente finché non viene scalato da una fattura o da uno scontrino.
Si registra dagli [acconti](../moduli/vendite/acconti.md).

## Autofattura

Fattura che si emette **a sé stessi** al posto del fornitore, nei casi in cui la
legge lo richiede. In Facile si compila nella stessa
[maschera del documento di vendita](../moduli/vendite/documento-di-vendita.md),
scegliendo il tipo di documento adatto, e spesso nasce da un
[carico merci](../moduli/magazzino/carico-merci.md).

## Causale contabile

Dice alla [prima nota](#prima-nota) che cosa sta registrando: quali conti
movimentare, in che segno, se c'è IVA e su quale registro. Si definiscono nelle
[causali contabili](../moduli/contabilita/causali-contabili.md).

## Causale di magazzino

L'equivalente per la merce: dice se il movimento **carica** o **scarica**, se
riguarda clienti o fornitori, se aggiorna i costi. Si definiscono nelle
[causali di magazzino](../moduli/magazzino/causali-magazzino.md).

## Commessa

Un lavoro o una pratica a cui attribuire costi e ricavi, per sapere alla fine
quanto è costato e quanto ha reso. Si tiene nelle
[commesse di contabilità analitica](../moduli/contabilita/commesse.md).

## Condizioni di pagamento

Il modo in cui si è concordato di pagare un documento: in quante rate, a quale
scadenza, con quale mezzo. In Facile si registrano una volta per tutte nella
tabella [Tipi di pagamento](../moduli/contabilita/tipi-di-pagamento.md) e poi
si richiamano per codice sul cliente, sul fornitore e sul documento.

A video la voce si chiama **Tipi di pagamento**: *condizioni di pagamento* è il
modo in cui se ne parla comunemente, ed è la stessa cosa.

## Contabilizzazione

Il passaggio con cui un documento di vendita **diventa una registrazione di
prima nota**. Fino a quel momento il documento esiste solo nel suo archivio e
la contabilità non lo vede. Vedi
[Contabilizza e controlli](../moduli/vendite/contabilizzazione-documenti.md).

## Corrispettivo

L'incasso di una vendita al pubblico, che non genera fattura ma va riepilogato
ai fini IVA. È quello che producono gli
[scontrini](../moduli/vendite/scontrini.md) e la
[vendita al banco](../moduli/vendite/vendita-al-banco.md).

## Deposito

Il magazzino fisico in cui la merce si trova. Un articolo ha
un'[esistenza](#esistenza) per ogni deposito, e un utente può essere limitato a
vederne uno solo. Si definiscono nei
[depositi](../moduli/magazzino/depositi.md).

## Distinta

L'elenco delle [scadenze](#scadenza) che si presentano insieme alla banca — per
incassarle o per pagarle — trattate come un blocco unico. Vedi
[Distinte di incasso e pagamento](../moduli/scadenze/distinte-incasso-pagamento.md).

## Effetto

Un titolo di credito che rappresenta un pagamento a scadenza: cambiale, tratta,
ricevuta bancaria. Vedi [Effetti e RI.BA.](../moduli/scadenze/effetti-e-riba.md).

## Esercizio

L'anno di gestione su cui si sta lavorando. Gli archivi sono divisi per
esercizio, e la barra del titolo mostra sempre quale è aperto. Si cambia da
[Esercizi, ditte e chiusure](../moduli/utility/esercizi-e-chiusure.md).

## Esistenza

Quanta merce risulta presente, adesso, in un [deposito](#deposito): l'esistenza
iniziale più i carichi meno gli scarichi. Nel manuale *esistenza* e *giacenza*
sono usate come sinonimi, così come fa il programma.

## Fido

Il limite di esposizione concesso a un cliente. Superandolo Facile avvisa; a
seconda di come è configurata l'installazione lascia proseguire oppure no.

## Imputazione

Dice a quale parte della registrazione corrisponde una riga di
[causale contabile](#causale-contabile): l'imponibile, l'IVA, il totale, la
ritenuta. È la colonna che rende una causale capace di scrivere da sola la
prima nota.

## Listino

L'insieme dei prezzi di vendita. Un articolo può avere prezzi diversi su
listini diversi, e il listino applicato a un documento arriva dal cliente o si
sceglie a mano. Vedi [Listini di vendita](../moduli/listini-vendita/index.md).

## Lotto

Un blocco di merce identificato da un codice e, di solito, da una scadenza:
serve a sapere **quale** partita di prodotto è finita a quale cliente. Vedi
[Analisi e giacenza lotti](../moduli/analisi-dati/analisi-lotti.md).

## Mastro, conto, sottoconto

I tre livelli del piano dei conti, dal più generale al più particolare: il
**mastro** raccoglie i **conti**, il conto raccoglie i **sottoconti**. Il
singolo cliente o fornitore è un sottoconto. Vedi
[Mastri](../moduli/contabilita/mastri.md),
[Conti](../moduli/contabilita/conti.md) e
[Sottoconti](../moduli/contabilita/sottoconti.md).

## Matricola

Il numero che identifica **il singolo pezzo** — non il modello. Un articolo
gestito a matricola si vende per forza a quantità intere, e ogni pezzo venduto
porta con sé il suo numero.

## Movimento di magazzino

La singola riga che fa entrare o uscire merce da un [deposito](#deposito), con
la sua [causale](#causale-di-magazzino), la quantità e il valore. Vedi
[Inserimento e modifica movimenti](../moduli/magazzino/movimenti-magazzino.md).

## Partita

Il singolo credito o debito aperto verso un cliente o un fornitore, generato da
un documento e chiuso da un incasso o un pagamento.

## Partita (ortofrutta)

Nella [versione Ortofrutta](../moduli/versioni/ortofrutta/index.md) la parola ha
un altro significato: è **la merce che un produttore ha conferito in una
volta**, con il numero del documento di carico che la identifica. Le due
accezioni non si incontrano mai nella stessa schermata, ma vale la pena non
confonderle.

## PLU

Il numero con cui una cassa o una bilancia conosce un articolo. Non è il codice
articolo di Facile: è un numero a parte, che va tenuto allineato fra il
programma e l'apparecchio.

## Preventivo

Un'offerta al cliente: non muove magazzino, non genera scadenze e non è un
documento fiscale. Accettato, si trasforma in un documento vero. Vedi
[Preventivi](../moduli/vendite/preventivi.md).

## Prima nota

Il registro delle scritture contabili in ordine cronologico: è dove finiscono,
una volta [contabilizzati](#contabilizzazione), i documenti, gli incassi e i
pagamenti. Vedi
[Gestione prima nota](../moduli/contabilita/gestione-prima-nota.md).

## Protocollo

Il numero progressivo con cui una registrazione è annotata **sul registro
IVA**. È diverso dal numero del documento: la stessa fattura ha un numero suo e
un protocollo nel registro in cui viene annotata.

## Provvigione

La quota che spetta all'agente sul venduto. Matura quando il documento viene
emesso, non quando viene salvato. Vedi
[Provvigioni agenti](../moduli/vendite/provvigioni-agenti.md).

## Registro

Il numeratore dei documenti, che corrisponde a un registro IVA. Ogni registro
ha la sua serie di numeri, e **la lettera del registro fa parte del numero del
documento**: per questo due fatture dello stesso anno possono avere lo stesso
numero se stanno su registri diversi.

## Reparto cassa

Il raggruppamento con cui il registratore di cassa classifica quello che vende,
e su cui tiene i totali. Ogni articolo venduto al banco deve averne uno:
senza, lo scontrino non si chiude.

## Ricarico e margine

Due modi di guardare lo stesso guadagno. Il **ricarico** è quanto si aggiunge
al costo per arrivare al prezzo; il **margine** è quanto di quel prezzo resta
come guadagno. Sullo stesso articolo il ricarico è sempre il numero più grande.

## Scadenza

L'impegno a pagare o a incassare un importo a una certa data, nato dalle
[condizioni di pagamento](#condizioni-di-pagamento) del documento. L'insieme
delle scadenze è lo **scadenzario**. Vedi
[Gestione scadenze](../moduli/scadenze/gestione-scadenze.md).

## Scorta minima e sottoscorta

La **scorta minima** è la quantità sotto la quale non si vuole scendere;
**sottoscorta** è la condizione di un articolo che ci è sceso. È il criterio con
cui si decide che cosa riordinare. Vedi
[Scorte, assortimento e ubicazioni](../moduli/anagrafiche/scorte-e-assortimento.md).

## Sezione

Una suddivisione contabile dell'azienda — un punto vendita, un ramo di
attività — che permette di tenere conti e documenti separati pur restando
nella stessa ditta. Vedi [Sezioni](../moduli/contabilita/sezioni.md).

## Stato del documento

Dove si trova un documento nel suo percorso: **salvato** (scritto, ma la merce
non si è mossa), **emesso** (stampato: magazzino, scadenze e provvigioni sono
partiti), **contabilizzato**, **annullato**. È la distinzione più importante di
tutto il modulo vendite.

## Ventilazione

Il metodo che ripartisce i [corrispettivi](#corrispettivo) fra le aliquote IVA
in proporzione agli acquisti, quando al momento della vendita non si è
distinta l'aliquota. Vedi
[Liquidazione IVA e ventilazione](../moduli/contabilita/liquidazione-iva.md).

## Vuoto a rendere

Il contenitore — cassa, bottiglia, bancale — consegnato al cliente con una
cauzione, che torna indietro quando lui lo restituisce. Vedi
[Tabella vuoti](../moduli/versioni/cauzioni-vuoti.md).
