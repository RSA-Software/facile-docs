---
title: Promozioni
description: Le promozioni sugli articoli, con il periodo di validità e i prezzi promozionali applicati alla vendita.
modulo: Vendite
maschera_id: IDD_PRM_PROMOZIONI_HEAD
---

# Promozioni

La promozione è un prezzo che vale per un periodo su un insieme di articoli.
Registrata qui, viene applicata da sola in vendita finché la promozione è
aperta.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Vendite ▸ Promozioni ▸ Inserimento *(oppure* Modifica *o* Stampa*)*
    - **Scorciatoia:** ++f7++ aggiunge articoli, ++f8++ stampa, ++f9++ dati
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Serve a preparare i volantini e i cartellini: si dice quali articoli sono in
promozione, a che prezzo e da quando a quando. Il punto cassa applica il prezzo
promozionale senza che nessuno debba ricordarsene, e alla fine del periodo i
prezzi tornano quelli di listino.

I margini della promozione si controllano poi dall'
[analisi listino](../listini-vendita/analisi-listino.md), che ha le colonne
**Margine Promo %** e **Fine Promo**.

## Prerequisiti

Prima di usare questa maschera occorre avere gli
[articoli](../anagrafiche/anagrafica-articoli.md) con i
[listini](../listini-vendita/gestione-listini.md) valorizzati: il prezzo
promozionale si giudica rispetto a quello normale.

## La maschera

![Promozioni](../../assets/img/vendite/promozioni.png)

In alto la testata della promozione — chi è, quando vale, dove vale — e sotto
l'elenco degli articoli che vi appartengono, con i prezzi promozionali.

La testata sta su tre righe:

- la **prima** dice chi è la promozione: registro, numero, descrizione, a quale
  livello di clienti si rivolge, e la spunta **Abilitata**;
- la **seconda** dice quando vale: data e ora di inizio, data e ora di fine, e i
  sette giorni della settimana;
- la **terza** dice dove vale: il deposito, con la possibilità di estenderla a
  tutti o di sceglierne un elenco, e il listino su cui agisce.

La griglia sotto elenca le righe: una per articolo, con il tipo di offerta, le
soglie e l'esito. Alcune colonne sono di servizio e restano nascoste — il
codice della riga, quello della testata, le date e la descrizione, che sono
quelle della testata.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Registro** | ● | Il registro su cui la promozione è numerata. Cambiandolo, il numero si rifà sul primo libero di quel registro. | `A` … `Z` |
| **Codice** | ● | Il numero della promozione dentro il registro. Proposto dal programma. | numero |
| **Descrizione** | ● | Il nome della promozione. È quello che arriva al punto cassa, dove sono usati i primi **20 caratteri**. | testo |
| **Liv.Clienti** | | Il livello di clientela a cui la promozione è riservata. Con `-1` vale per tutti. | da `-1` a `100` |
| **Abilitata** | | Se togliendo la spunta la promozione resta in archivio ma non viene più applicata. | spunta |
| **Inizio Validità** | ● | Il giorno e l'**ora** da cui la promozione parte. | data e ora |
| **Fine Validità** | ● | Il giorno e l'**ora** in cui finisce. Non può precedere l'inizio. | data e ora |
| **Dom** … **Sab** | | I giorni della settimana in cui la promozione vale. **Spuntato = vale**: togliendo la spunta si esclude quel giorno. Almeno uno deve restare spuntato. | sette spunte |
| **Deposito** | ● | Il deposito o punto vendita a cui la promozione si applica. | codice |
| **Abilita su Tutti i Depositi** | | Estende la promozione a tutti i depositi. Con la spunta messa, il pulsante **Seleziona Depositi** sparisce. | spunta |
| **Seleziona Depositi** | | Apre *Depositi Associati alla Promozione*, dove si scelgono gli altri depositi oltre a quello indicato sopra — fino a cinquanta. | elenco |
| **Listino** | ● | Il listino di vendita su cui la promozione agisce. | codice |

{: .campi }

!!! warning "Deposito e listino si scelgono una volta sola"

    Dopo il primo salvataggio **Registro**, **Codice**, **Deposito** e
    **Listino** diventano non modificabili: sono i dati che le righe hanno già
    ereditato. Per cambiarli va rifatta la promozione — conviene partire da
    **Duplica**.

### Le righe della promozione

Ogni riga della promozione si apre in una finestra propria, dove si stabilisce
che cosa viene offerto e a quali condizioni.

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Articolo** | ● | L'articolo in promozione. | codice |
| **Listino** | | Il listino su cui la promozione agisce. | codice |
| **Tipo Offerta** | ● | La forma dell'offerta: sconto in valore o in percentuale, sul singolo articolo o sul subtotale, prendi M paghi N, regalo, bollino, coupon, fascia di prezzo, netto reparto, punti di pagamento e le varianti a più soglie. | 17 voci, da `01 - Ammontare Subtotale` a `23 - Regalo Articolo su Subtotale`: la numerazione salta dal 13 al 20 |
| **Offerta Cumulativa** | | Come si comporta l'offerta quando l'articolo compare più volte nello scontrino. | `(Si) - Più Articoli Stessa Offerta`, `(No) - Articoli Autonomi`, `(Set) - Più Articoli Stessa Q.tà`, `(Pan) - Paniere` |
| **Applicabilità** | | Quante volte l'offerta può scattare. | `Contingentata`, `Una Volta nello Scontrino`, `Sempre`, `In Continuo dopo la Soglia`, `n Volte Nello Scontrino` |
| **Volte** | | Quante volte, quando l'applicabilità lo richiede. | numero |
| **Limite Minimo**, **Limite Massimo** | | I limiti entro cui l'offerta vale. | numero |
| **Casualità** | | La quota di casualità nell'applicazione dell'offerta. La usano **solo le casse SysPC**. | da `0` a `32767` |
| **Frontalino** | | Il formato del frontalino da stampare per questa riga. | `PICCOLO`, `MEDIO`, `GRANDE`, `NESSUNO` |
| **Codice Mix** | | Il codice che lega fra loro le righe di un'offerta mista. | codice |

{: .campi }

Aprendo una riga nuova, i campi non partono vuoti: **periodo, ora, giorni,
deposito, listino, livello clienti e la spunta Abilitata** sono quelli della
testata, e l'offerta parte già impostata su `02 - Ammontare Articolo`,
`(No) - Articoli Autonomi`, applicabilità **Sempre**, limiti da `0,01` a
`9.999.999,99` e frontalino `PICCOLO`.

!!! warning "In Facile valgono solo tre tipi di offerta su diciassette"

    Le diciassette forme di offerta descrivono quello che sa fare il **punto
    cassa**. Quando invece è Facile a fare il documento — vendita al banco,
    fattura, scontrino dal gestionale — il prezzo promozionale viene applicato
    **solo** se la riga è di uno di questi tre tipi:

    - `02 - Ammontare Articolo`, che toglie un importo fisso dal prezzo;
    - `04 - Percentuale Articolo`, che toglie una percentuale;
    - `07 - Bollino`, che non cambia il prezzo ma assegna punti.

    e in più deve avere **Applicabilità = Sempre** e nessuna soglia di
    quantità superiore a uno né soglia di ammontare.

    Tutte le altre — il 3x2, il paniere, i coupon, le multisoglia — sono
    trasmesse alle casse e applicate lì: sul documento fatto da Facile non
    hanno effetto.

!!! note "Come si leggono Tipo Offerta, Cumulativa e Applicabilità insieme"

    I tre campi rispondono a tre domande diverse:

    | Campo | Risponde a |
    |---|---|
    | **Tipo Offerta** | che cosa fa l'offerta — sconto, regalo, punti, prezzo a fascia |
    | **Offerta Cumulativa** | come si comporta quando l'articolo, o più articoli della stessa promozione, compaiono insieme nello scontrino |
    | **Applicabilità** | quante volte può scattare nello stesso scontrino |

    Le combinazioni più usate:

    | Caso | Tipo Offerta | Cumulativa | Applicabilità |
    |---|---|---|---|
    | Sconto fisso sull'articolo, sempre | `02 - Ammontare Articolo` | `(No)` | `Sempre` |
    | Sconto percentuale sull'articolo, sempre | `04 - Percentuale Articolo` | `(No)` | `Sempre` |
    | Prendi 3 paghi 2 | `05 - MxN` | `(Si)` | `Sempre` |
    | Sconto solo sul primo pezzo dello scontrino | `02` oppure `04` | `(No)` | `Una Volta nello Scontrino` |
    | Regalo al raggiungimento di una soglia | `06 - Regalo Articolo` | `(Set)` | `In Continuo dopo la Soglia` |
    | Sconto su un insieme di articoli diversi | `10` o `11` — gruppo articoli | `(Pan) - Paniere` | `Sempre` |

    Le soglie in fondo alla finestra sono gli scaglioni: la prima è quella da
    cui l'offerta parte, le altre nove servono alle offerte **multisoglia**
    (tipi `20`, `21`, `22`). Vanno compilate in ordine crescente: una soglia
    non può essere minore o uguale alla precedente.

!!! note "La Casualità serve solo alle casse SysPC"

    È un numero da `0` a `32767` che **Facile non usa**: lo registra e lo
    trasmette insieme all'offerta, e a interpretarlo è la cassa. A farci
    qualcosa sono **solo le casse [SysPC](../casse-bilance/casse.md)**; sulle
    altre famiglie il campo o non parte nemmeno, o arriva e viene ignorato.

    Su un impianto che non ha casse SysPC, quindi, il valore scritto qui non ha
    alcun effetto: tanto vale lasciarlo a zero.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F7 - Aggiungi** | ++f7++ | Aggiunge **una** riga. Apre un menu con due voci: *Promozione Standard*, che chiede l'articolo, e *Promozione con Filtro*, che al posto dell'articolo chiede marchio, reparto o categoria merceologica. |
| **F9 - Dati** | ++f9++ | Aggiunge **molte** righe: apre la ricerca articoli, dove se ne selezionano quanti servono. Per il primo si compila la finestra della riga; se l'offerta è a percentuale o a regalo, il programma chiede se applicare la stessa condizione a tutti gli altri. |
| **F8 - Stampa** | ++f8++ | Apre un menu con le stampe: elenco della promozione, frontalini, frontalini di fine promozione *(solo a promozione scaduta)*, promozione d'acquisto, e due formati di andamento. |
| **Excel** | | **Importa** articoli da un foglio Excel. Non esporta. |
| **Lettori** | | **Importa** le letture fatte con un terminale portatile: EIA Thunder, BCP8000/ET8000, DENSO N661 o palmare Android. Non manda niente alle casse. |
| **Duplica** | | Crea una copia completa della promozione — testata e righe, periodo compreso — con un codice nuovo, e ci si posiziona sopra. |
| **Trova** | | Cerca un testo in **qualunque** colonna della griglia, anche parziale. Ripremendo **F2 - Trova** passa all'occorrenza successiva. |
| **F6 - Elimina** | ++f6++ | Cancella la promozione e tutte le sue righe, previa conferma. |

!!! tip "I comandi si accendono dopo il primo salvataggio"

    Su una promozione nuova la barra è quasi tutta spenta: prima va salvata la
    testata. Subito dopo il salvataggio, se la promozione non ha ancora righe,
    il programma apre da solo la finestra della prima riga.

## Come si fa

### Preparare la promozione del mese

1. Apri **Menu ▸ Vendite ▸ Promozioni ▸ Inserimento**.
2. Compila la testata: descrizione, periodo con le ore, deposito e listino.
3. Salva con **F2**. Il programma apre la finestra della prima riga.
4. Aggiungi gli articoli, uno per volta con **F7 - Aggiungi** o molti insieme
   con **F9 - Dati**, e indica per ciascuno tipo di offerta ed esito.
5. Premi **F8 - Stampa ▸ Stampa Frontalini Promozione** per i cartellini.
6. Manda la promozione alle casse da **Menu ▸ Casse e Bilance**, con
   [Invio Variazioni Articoli](../casse-bilance/casse.md).

### Rifare la promozione dell'anno prima

1. Apri la promozione da riusare.
2. Premi **Duplica** e correggi periodo e prezzi sulla copia.

### Controllare se la promozione conviene

1. Apri l'[analisi listino](../listini-vendita/analisi-listino.md).
2. Guarda **Margine Promo %** accanto a **Margine %**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio, o una data è fuori ordine, o il limite massimo non supera il minimo. | Guarda dove si è posizionato il cursore: è il campo da correggere. |
| *Tutti i giorni della settimana sono stati esclusi dalla promozione !* | Nessuno dei sette giorni è spuntato. | Spunta almeno un giorno. |
| *Indicare solo uno tra articolo regalo e paniere articoli!* | Su un'offerta a regalo sono stati indicati sia l'articolo omaggio sia il paniere. | Lascia uno solo dei due. |
| *Primo esito = 0* — *Vuoi Continuare ?* | La riga non ha un valore di offerta, e non è un'offerta a regalo. | **No** torna sul campo. **Sì** salva la riga così: non farà nulla. La risposta preimpostata è **No**. |
| *L'articolo fa parte di un Gruppo Mix!* — *Vuoi inserire tutti gli altri articoli del gruppo ?* | L'articolo appena messo in promozione appartiene a un gruppo mix. | **Sì** aggiunge in blocco gli altri articoli del gruppo, con la stessa offerta. |
| *Raggiunto limite massimo di righe nella promozione!* | La promozione ha raggiunto il numero massimo di righe. | Dividi gli articoli su più promozioni. |
| *Vuoi Cancellare tutte le righe della promozione ?* | Hai premuto **F6 - Elimina**. | **Sì** cancella testata e righe. La risposta preimpostata è **No**. |
| *Confermi la duplicazione della promozione ?* | Hai premuto **Duplica**. | **Sì** crea subito la copia. La risposta preimpostata è **No**. |
| *Vuoi applicare la stessa promozione a tutti gli articoli selezionati?* | Hai selezionato più articoli con **F9 - Dati** e la prima offerta è a percentuale o a regalo. | **Sì** ripete la stessa condizione su tutti senza più chiedere. La risposta preimpostata è **No**. |
| *Colonna CODICE non trovata nel documento !* | Il foglio Excel da importare non ha l'intestazione `CODICE` sulla prima riga. | Correggi l'intestazione del foglio. |
| *Colonna OFFERTA e/o SCONTO_PERC non trovata nel documento !* | Il foglio non ha né la colonna `OFFERTA` né `SCONTO_PERC`. | Ne serve almeno una delle due. |
| *Formato file non compatibile!* | Il file scelto non è un foglio Excel. | Scegli un `.xls`. |
| *File utilizzato da un' altra applicazione o formato file non compatibile!* | Il foglio è aperto in Excel. | Chiudilo e riprova. |
| *Vuoi controllare gli orari di inizio e fine promozioni?* | Solo in assistenza: compare all'apertura della maschera. | È una manutenzione, non un'operazione di tutti i giorni: rimette dentro le 24 ore gli orari fuori scala. La risposta preimpostata è **No**. |

### Il foglio Excel da importare

Il file è un `.xls` e va cercato nella cartella `in`. L'intestazione sta sulla
**prima riga** e i nomi delle colonne sono riconosciuti così:

| Colonna | Obbl. | Contenuto |
|---|:---:|---|
| `CODICE` | ● | Il codice dell'articolo. |
| `OFFERTA` |  | Il valore dell'offerta. |
| `SCONTO_PERC` |  | La percentuale di sconto. |
| `DESCRIZIONE` | | Ignorata nella scrittura: serve solo a rileggere il foglio. |
| `LISTINO` | | Il prezzo di listino di partenza. |

Fra `OFFERTA` e `SCONTO_PERC` **almeno una** deve esserci. L'ordine delle
colonne non conta: contano i nomi.

## Note

!!! note "Le promozioni sui punti cassa"

    Registrare la promozione in Facile non basta perché il prezzo arrivi alla
    cassa: va trasmessa da **Menu ▸ Casse e Bilance**, con
    [Invio Variazioni Articoli o Invio Globale Articoli](../casse-bilance/casse.md).
    Il pulsante **Lettori** di questa maschera fa il contrario — legge gli
    articoli raccolti con un terminale portatile.

!!! note "Alla fine del periodo il prezzo torna da solo"

    Il prezzo promozionale non viene mai scritto sul
    [listino](../listini-vendita/gestione-listini.md): è calcolato al momento,
    ogni volta che si batte l'articolo, partendo dal listino e applicando
    l'offerta. Finito il periodo — o tolta la spunta **Abilitata**, o in un
    giorno della settimana escluso — non c'è niente da rimettere a posto: il
    prezzo che si vede è di nuovo quello di listino.

    Vale anche l'inverso: cambiando il prezzo di listino durante la promozione,
    lo sconto si applica al prezzo nuovo.

!!! note "Quale promozione vince, se più di una copre lo stesso articolo"

    Facile le mette in ordine e prende la prima che passa i controlli. Conta
    per prima cosa **quanto è mirata**:

    1. la riga intestata a quell'articolo;
    2. quella per marchio;
    3. quella per reparto;
    4. quella per categoria merceologica;
    5. quella valida per tutti gli articoli.

    A parità, vince quella che **finisce più tardi**, e a parità di scadenza
    quella con il codice più alto — cioè l'ultima inserita. La riga deve
    comunque essere abilitata, nel periodo e nell'orario, in un giorno non
    escluso, sul deposito giusto e — se il livello non è `-1` — su un cliente
    di quel livello.

!!! note "Promozioni e Promozioni Sellin sono due cose diverse"

    Le **Promozioni** di questo menu sono in **vendita**: il prezzo che il
    cliente paga. Le
    [Promozioni Sellin](../magazzino/anomalie-e-promozioni-sellin.md) del menu
    Magazzino sono in **acquisto**: le condizioni che il fornitore concede a
    noi, con il suo periodo di cessione.

    Sono due archivi separati, e nessuno dei due alimenta l'altro. Le sellin si
    ritrovano nella scheda articolo alla linguetta *Promo Sellin*, nel
    [controllo listini](../listini-vendita/controllo-listini.md), dove
    concorrono al miglior prezzo d'acquisto, nell'analisi fornitore e nella
    proposta di riordino.

## Vedi anche

- [Analisi listino da vendite ed esistenza](../listini-vendita/analisi-listino.md)
- [Vendita al banco e POS](vendita-al-banco.md)
- [Gestione listini](../listini-vendita/gestione-listini.md)
