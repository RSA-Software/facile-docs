---
title: Movimenti
description: Inserimento e modifica dei movimenti del registro energetico, importazione dai DAS, generazione delle giacenze, cambio del codice prodotto e stampe di controllo.
modulo: Energy
maschera_id: IDD_ENE_MOVPROENE
---

# Movimenti

Il **registro dei prodotti energetici**: ogni carico, ogni scarico e la giacenza
di fine giornata, con tutto quello che l'Agenzia delle Dogane vuole sapere.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Energy ▸ Movimenti ▸ Inserimento Movimento *(oppure* Modifica Movimento*)*
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca, ++f6++ elimina
    - **Prerequisiti:** registro, soggetto obbligato, ufficio, prodotto e causale — vedi [Le tabelle](tabelle.md)

---

## Inserimento e Modifica Movimento

La maschera è divisa in fasce, dall'alto in basso.

### L'identificazione

| Campo | Descrizione |
|---|---|
| **Codice** | Anno e numero del movimento. |
| **Data** | La data del movimento. |
| **Tipo Richiesta** | Che cosa si sta comunicando: `I - INSERIMENTO`, `C - CANCELLAZIONE`, `A - INSERIMENTO RIENTRO TERZA COPIA DAA`, `D - CANCELLAZIONE RIENTRO TERZA COPIA DAA`. |

!!! note "Le cancellazioni si comunicano, non si cancellano"

    Un movimento già trasmesso non si toglie dal registro: si registra un
    movimento di **cancellazione** (`C`), che l'Agenzia abbina al precedente.
    È il motivo per cui il **Tipo Richiesta** sta in cima alla maschera e non
    fra i dettagli.

### Il registro

| Campo | Descrizione |
|---|---|
| **Registro** | Il [registro](tabelle.md) su cui scrivere. |
| **Protocollo**, **Anno**, **Rigo** | Protocollo del registro, anno e numero di rigo: il posto esatto della scrittura. |
| **Tipo Registro** | `M - MATERIE PRIME E SEMILAVORATI` oppure `F - PRODOTTI FINITI`. |
| **Sogg. Obblig.** | Il [soggetto obbligato](tabelle.md) titolare del deposito. |
| **Ufficio** | L'ufficio dell'Agenzia delle Dogane competente. |

### Il movimento

| Campo | Descrizione |
|---|---|
| **Tipo Mov.** | `C - CARICO`, `S - SCARICO` o `G - GIACENZA A FINE GIORNATA`. |
| **Causale** | La [causale](tabelle.md) del movimento, distinta fra carico e scarico. |
| **Cliente** | La controparte: cliente per gli scarichi, fornitore per i carichi. |
| **Tipo Docum.**, **Data Docum.**, **Num. Docum.** | Il documento che accompagna il movimento. |
| **Provenienza** | La nazione di provenienza. |
| **DAS Collettivo** | Il numero del DAS collettivo, quando c'è. |

### Il prodotto e le quantità

| Campo | Descrizione |
|---|---|
| **Prodotto** | Il [prodotto energetico](tabelle.md), con il codice ministeriale. |
| **Q.ta (KG)** | La quantità in chilogrammi. |
| **Densità 15°** | La densità a 15 gradi, che lega i chili ai litri. |
| **Q.ta (LT)** | La quantità in litri. |
| **Tipo Stoccaggio** | `S - SFUSO` o `C - CONDIZIONATO`. |
| **Q.ta Nominale**, **Confezioni** | Per il condizionato: quanto contiene una confezione e quante ce ne sono. |
| **Escludi da Calcolo Giacenze** | Tiene il movimento fuori dal conteggio della giacenza. |
| **Movimento da Controllare** | Lo segna come da verificare. È un promemoria per chi lavora, non un dato da trasmettere. |

!!! tip "Chili e litri vanno insieme"

    Il registro vuole **tutte e due** le misure, e la densità è il ponte fra
    loro. Compilare i chili e lasciare i litri a zero (o viceversa) produce un
    registro formalmente compilato ma inutilizzabile per i controlli: le
    giacenze in litri non torneranno mai.

### La fiscalità

| Campo | Descrizione |
|---|---|
| **Posiz. Fisc.** | La [posizione fiscale](tabelle.md) del movimento — accisa assolta, sospensione d'imposta, e così via. |
| **Tributi Erariali a Debito** | L'importo dei tributi che il movimento fa nascere. |
| **Note** | Testo libero. |

## Inserimento Movimenti DAS

Invece di riscrivere a mano quello che è già stato emesso, si **importano i
DAS** di una giornata.

Facile chiede la data, poi conferma:

> *Confermi l' importazione dei movimenti dei DAS ?*

e trasforma in movimenti del registro tutte le righe dei DAS di quel giorno,
saltando quelli annullati.

!!! warning "Serve un tipo documento con codice DAS"

    Se in tabella non esiste il tipo documento `DAS`, la voce si ferma subito:

    *Tipo Documento DAS non trovato in archivio !*

    Si aggiunge dai [tipi documento](tabelle.md).

## Inserimento Giacenze

Genera in un colpo solo **le giacenze di fine giornata** di tutti i registri.

Chiede conferma — *Confermi la generazione dei movimenti con le giacenze ?*, con
**No** preimpostato — poi la data, e scrive un movimento di tipo `G` per ogni
registro.

!!! note "Solo i registri che lo chiedono"

    Vengono considerati **soltanto i registri attivi** che hanno spuntato
    **Calcola Giacenza KG** o **Calcola Giacenza LT** nella loro scheda. Un
    registro disattivato, o che non ha nessuna delle due caselle, non riceve
    nessuna giacenza — ed è così che si escludono i registri che non ne hanno
    bisogno.

## Varia Codice Prodotto Energetico

Cambia il codice del prodotto su un intervallo di movimenti già registrati.
Serve quando l'Agenzia rinumera un prodotto, o quando ci si accorge di aver
usato il codice sbagliato per un periodo.

| Campo | Descrizione |
|---|---|
| **Data Iniziale**, **Data Finale** | Il periodo su cui intervenire. |
| **Da Prodotto** | Il codice da sostituire. |
| **A Prodotto** | Il codice nuovo. |
| **Varia codice anche su DAS** | Estende la sostituzione ai DAS, non solo ai movimenti del registro. |

!!! danger "È una variazione di massa e non si annulla"

    Tocca tutti i movimenti del periodo in una volta e non c'è modo di tornare
    indietro. Prima di lanciarla conviene restringere bene le date e assicurarsi
    che nessun altro stia lavorando.

    Se i movimenti interessati sono **già stati trasmessi**, cambiare il codice
    qui non cambia quello che l'Agenzia ha ricevuto: la correzione va comunicata
    con i movimenti di cancellazione e reinserimento.

## Stampa Movimenti

| Campo | Descrizione |
|---|---|
| **Data Iniziale**, **Data Finale** | Il periodo. |
| **Registro** | Un registro solo, o vuoto per tutti. |
| **Sog. Obbligato** | Restringe a un soggetto obbligato. |
| **Tipo Movim.** | `C - CARICO`, `S - SCARICO`, `G - GIACENZA A FINE GIORNATA` o `T - TUTTI`. |

## Stampa Controllo Giacenze

Verifica che le giacenze tornino: parte da una giacenza iniziale dichiarata e
la confronta con quella che risulta dai movimenti.

| Campo | Descrizione |
|---|---|
| **Data Iniziale**, **Data Finale** | Il periodo da controllare. |
| **Registro** | Il registro da controllare. |
| **Giacenza Iniziale (KG)** | I chilogrammi da cui partire. |
| **Giacenza Iniziale (LT)** | I litri da cui partire. |

!!! tip "È il controllo da fare prima di trasmettere"

    Una differenza qui è quasi sempre un movimento sbagliato o mancante, ed è
    molto più comodo trovarla adesso che dopo aver mandato il flusso.

## Vedi anche

- [Flussi e riepiloghi](flussi-e-riepiloghi.md)
- [Le tabelle](tabelle.md)
