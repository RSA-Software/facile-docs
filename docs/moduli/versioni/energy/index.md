---
title: Energy
description: "Il ramo di menu della versione per i depositi di prodotti energetici: registro telematico, flussi all'Agenzia delle Dogane, accise, ravvedimenti e tabelle ministeriali."
modulo: Energy
maschera_id: nessuna dialog propria
---

# Energy

Il menu **Energy** c'è solo nella versione di Facile allestita per chi tiene un
**deposito di prodotti energetici** — gasolio, oli lubrificanti, bitumi — e deve
rispondere all'**Agenzia delle Dogane e dei Monopoli**.

Non è un modulo di magazzino: è **il registro fiscale** di quel deposito, con le
scritture che vanno tenute, i tributi che vanno calcolati e i file che vanno
trasmessi.

!!! warning "Se non trovi il menu, la tua versione non lo prevede"

    Come gli altri rami delle [versioni specifiche](../index.md), all'avvio il
    programma toglie dalla barra l'intero menu quando la versione non è quella.

---

## Come è fatto il modulo

Tre strati, uno sopra l'altro.

**Sotto stanno le tabelle**, e non sono tabelle qualunque: la maggior parte è
**pubblicata dall'Agenzia delle Dogane**, che le distribuisce in fogli Excel
identificati da una sigla — TA03 gli uffici, TA05 i tipi documento, TA06 le
nazioni, TA08 le causali, TA09 i periodi, TA10 i tributi, TA12 le posizioni
fiscali, TA13 i prodotti energetici. Facile le importa da quei fogli, così i
codici sono quelli giusti e restano allineati quando l'Agenzia li aggiorna. Le
altre tabelle — soggetti obbligati, registri, firme — descrivono invece **il
deposito**, e si compilano una volta sola.

**In mezzo stanno i movimenti**: ogni carico, ogni scarico e la giacenza di fine
giornata, riga per riga, con prodotto, quantità in chilogrammi e in litri,
densità, controparte, documento e posizione fiscale.

**Sopra sta quello che si manda fuori**: i **flussi** per l'Agenzia, i
**riepiloghi** dei tributi dovuti, i **ravvedimenti** quando si paga in ritardo,
e i file XML dei corrispettivi.

## Il giro di una giornata

1. I movimenti entrano nel registro — a mano, oppure automaticamente **dai DAS**
   già emessi.
2. A fine giornata si generano le **giacenze**, una per registro.
3. Si controlla con le due stampe: **movimenti** e **controllo giacenze**.
4. Quando è il momento, si genera il **flusso** e lo si trasmette.
5. A fine periodo si compilano i **riepiloghi** di accise e crediti, e se serve
   il **ravvedimento**.

## Le pagine di questa sezione

| Pagina | Cosa contiene |
|---|---|
| [Movimenti](movimenti.md) | L'inserimento dei movimenti, i DAS, le giacenze, il cambio di codice prodotto e le due stampe di controllo. |
| [Flussi e riepiloghi](flussi-e-riepiloghi.md) | La generazione del flusso per l'Agenzia, i riepiloghi di accise e crediti, i ravvedimenti. |
| [Corrispettivi in XML](corrispettivi-xml.md) | I due file XML dei corrispettivi e dei periodi di inattività. |
| [Le tabelle](tabelle.md) | Soggetti obbligati, registri, firme e tutte le tabelle ministeriali, con le rispettive importazioni. |

!!! note "Prima le tabelle, poi tutto il resto"

    Un movimento non si registra se prima non esistono il **registro**, il
    **soggetto obbligato**, l'**ufficio delle dogane**, il **prodotto
    energetico** e la **causale**. La messa in opera comincia sempre dalle
    [tabelle](tabelle.md).

## Vedi anche

- [Versioni specifiche](../index.md)
