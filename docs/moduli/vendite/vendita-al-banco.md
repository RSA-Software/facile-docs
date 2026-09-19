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

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Attenzione!<br><br>Non e' stato impostato il listino di vendita.<br>Saranno riportati per la vendita i prezzi<br>di acquisto.* | La [ditta](../anagrafiche/ditte.md) non ha un listino di vendita. | Impostalo: altrimenti si vende al prezzo di acquisto. Il messaggio compare all'apertura della schermata. |
| *Attenzione!<br><br>Non e' stato impostato il listino di vendita per i trasfert.<br>Saranno riportati per la vendita i prezzi<br>di acquisto.* | Come sopra, per le vendite in trasferta. | Impostalo nella ditta. |

<!-- DA VERIFICARE: gli altri messaggi delle due schermate. Sono trecento fra Vendita e Pos Touchscreen: vanno raccolti in una passata dedicata, come per il documento di vendita. -->

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
