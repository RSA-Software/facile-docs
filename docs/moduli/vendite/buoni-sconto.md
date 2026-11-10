---
title: Buoni sconto
description: "Come si configura il buono sconto che esce in cassa a fine scontrino: il file di configurazione, le fasce di spesa, il buono in percentuale, la validità e il testo stampato."
modulo: Vendite
maschera_id: FILE_BUONI_SCONTO
---

# Buoni sconto

Il buono sconto è un tagliando con codice a barre che la cassa stampa alla fine
dello scontrino quando il cliente ha speso abbastanza. Quanto vale, da quale
spesa, in quali date si emette, fino a quando si può spendere e cosa c'è scritto
sopra si decide in un **file di testo**, uno per ditta, e non più nella scheda
della ditta.

!!! info "In sintesi"

    - **Dove si configura:** un file di testo nella cartella **cfg** del programma, non una maschera
    - **Nome del file:** `buoni_sconto_00001.ini` per la ditta 1 (il codice della ditta sempre a 5 cifre), oppure `buoni_sconto.ini` per tutte le ditte che non hanno il proprio
    - **Si attiva da:** [Archivi ▸ Ditte](../anagrafiche/ditte.md), scheda **Fidelity - Buoni Sconto**, casella **Abilita Emissione Buoni Sconto**
    - **Modello da scaricare:** [buoni_sconto.ini](../../assets/modelli/buoni_sconto.ini)

---

## A cosa serve

Una promozione tipica: «Chi spende almeno 50 euro riceve un buono del 10% da
usare entro fine gennaio». Il negoziante scrive la regola nel file; da quel
momento ogni scontrino che raggiunge la spesa fa uscire dalla cassa il buono,
già con il suo codice a barre. Alla spesa successiva il cliente lo riporta e
il buono si scala dal totale in cassa.

Il file permette di:

- stabilire fino a cinque **fasce di spesa**, ciascuna con il suo buono;
- scegliere se il buono è un **importo fisso** o una **percentuale** del totale
  dello scontrino;
- limitare l'emissione a un **periodo** (per esempio solo a dicembre);
- fissare la **validità** del buono, con date precise oppure «da domani per 30
  giorni»;
- scrivere le righe che compaiono **in testa e in coda** al buono.

## Prerequisiti

- Nella [ditta](../anagrafiche/ditte.md), scheda **Fidelity - Buoni Sconto**,
  la casella **Abilita Emissione Buoni Sconto** deve essere attiva. Con la
  casella spenta non esce nessun buono, qualunque cosa dica il file.
- Il file di configurazione deve esistere. Se la casella è attiva ma il file
  non c'è, **non esce nessun buono**: la vendita prosegue normalmente e il
  motivo viene annotato nel file degli errori (vedi *Controlli e messaggi*).
- Una cassa fiscale che sappia stampare il buono. Con le altre casse lo
  scontrino si batte come sempre e il buono non esce.

## La maschera

Non applicabile: il buono non ha una maschera. Si configura con un file di
testo, che si modifica con il Blocco note.

Il file va nella cartella **cfg** del programma, la stessa dove stanno gli
altri file di impostazione. Il programma cerca nell'ordine:

1. `buoni_sconto_` seguito dal codice della ditta **a cinque cifre** e da
   `.ini`: per la ditta 1 è `buoni_sconto_00001.ini`, per la 12
   `buoni_sconto_00012.ini`;
2. se questo non c'è, `buoni_sconto.ini`.

Così in un'installazione con più ditte si può dare a ciascuna le proprie regole
con un file per ciascuna, oppure far valere le stesse regole a tutte con un
solo `buoni_sconto.ini`.

Il file si apre con la riga `[OPTIONS]`; sotto vanno le chiavi, una per riga,
nella forma `chiave = valore`. Le righe che iniziano con `;` sono commenti. Il
[modello](../../assets/modelli/buoni_sconto.ini) contiene tutte le chiavi,
commentate una per una, con l'esempio della promozione al 10% da 50 euro.

!!! warning "Salva il file in ANSI"

    Il file va salvato in **ANSI** (Windows-1252). In Blocco note si sceglie
    **ANSI** nel campo **Codifica** di **Salva con nome**. Un file salvato
    in UTF-8 **con BOM** non viene letto: il buono non esce e il programma lo
    scrive nel file degli errori. Un file salvato in UTF-8 **senza BOM** viene
    letto, ma le lettere accentate escono sbagliate sul buono. In tutti e due i
    casi va salvato di nuovo in ANSI.

## Campi

Le **date** si scrivono sempre `gg/mm/aaaa`, per esempio `24/12/2026`. Una data
lasciata vuota è semplicemente non indicata; una data scritta male, invece, è un
errore e il buono non esce.

| Chiave | Valori | Descrizione |
|---|---|---|
| `tipo` | `valore` oppure `percentuale` | Con `valore`, l'importo di ogni fascia (`buono_1`…`buono_5`) è in euro. Con `percentuale` è una percentuale, maggiore di 0 e al massimo 100, del totale dello scontrino. Se manca vale `valore`. |
| `emissione_dal`, `emissione_al` | data | Il periodo in cui i buoni si emettono, estremi compresi. Se uno dei due manca, il periodo è aperto da quella parte. Fuori dal periodo non esce nessun buono e non compare nessun messaggio. |
| `validita_dal`, `validita_al` | data | La validità fissa del buono: vale dal primo al secondo giorno. Vanno scritte **tutte e due**, con `validita_al` non prima di `validita_dal`. |
| `validita_dopo_giorni`, `validita_durata_giorni` | numero di giorni | La validità relativa alla data di emissione: il buono inizia a valere dopo `validita_dopo_giorni` giorni da oggi (0 = oggi) e vale fino al giorno di inizio più `validita_durata_giorni`, compreso. Con 0 e 30, un buono emesso il 09/11 vale dal 09/11 al 09/12. Si usa solo se la validità fissa manca. |
| `multipli` | `0` oppure `1` | Con `tipo = valore`, quando la spesa è un multiplo della soglia. Con `1` escono tanti buoni quante volte la soglia sta nel totale, ciascuno del valore della fascia. Con `0` esce un solo buono, che vale quel valore moltiplicato per lo stesso numero. Con `tipo = percentuale` la chiave non conta: esce sempre un buono solo. |
| `colonne` | da 1 a 45 | La larghezza in caratteri del buono stampato con il formato 3. Se manca vale 45. |
| `header_1` … `header_5` | testo, al massimo 45 caratteri | Le righe in testa al buono. |
| `spesa_1` … `spesa_5` | importo | La spesa minima della fascia. |
| `buono_1` … `buono_5` | importo | Quello che si ottiene con la fascia: euro, o percentuale se `tipo = percentuale`. Un importo in euro si arrotonda al centesimo: `12,345` vale 12,35. |
| `footer_<fascia>_<riga>` | testo, al massimo 45 caratteri | Le righe in coda al buono per la fascia che ha fatto scattare il buono. La fascia va da 1 a 5, la riga da 1 a 5: `footer_2_1` è la prima riga di coda della seconda fascia. |
| `footer_1` … `footer_5` | testo | Righe in coda comuni, usate per le fasce che non hanno nessuna riga `footer_<fascia>_<riga>`. |

Una fascia conta **solo se ha sia la spesa sia il buono maggiori di zero**; le
altre si ignorano. Se nessuna fascia conta il file è sbagliato.

I file vecchi che indicano le date con `start_year`, `start_month`,
`start_day` e `stop_year`, `stop_month`, `stop_day` continuano a funzionare: le
sei chiavi valgono come `validita_dal` e `validita_al` quando queste mancano.

### Il testo del buono: i segnaposti

Nelle righe di testa e di coda si possono scrivere tre segnaposti, che alla
stampa diventano il dato vero del buono:

| Segnaposto | Diventa |
|---|---|
| `{VALORE}` | L'importo del buono con il punto decimale, per esempio `5.56 EURO`. Anche per il buono in percentuale: il buono è sempre stampato per il suo valore in euro. |
| `{DAL}` | Il primo giorno di validità, `gg-mm-aaaa`, per esempio `09-12-2026`. |
| `{AL}` | L'ultimo giorno di validità, `gg-mm-aaaa`. |

Per esempio la riga `Valido dal {DAL} al {AL}` diventa `Valido dal 01-12-2026 al
31-01-2027`.

!!! warning "Nelle tue righe usa il trattino e il punto"

    Su tutte le casse tranne le Epson, la barra `/` e la virgola `,` scritte
    nelle righe di testa e di coda escono sul buono come **spazi**: `Tel. 091/123`
    diventa `Tel. 091 123`. Per questo i segnaposti stampano le date con il
    trattino e l'importo con il punto, e nel tuo testo conviene fare lo stesso:
    scrivi `-` al posto di `/` e `.` al posto di `,`. Solo nelle date delle
    chiavi del file (`emissione_dal`, `validita_al`…) si scrive ancora la barra.

    Con le casse Micrelec (`MICRELEC` e `MICRELEC G100`) le lettere accentate
    delle tue righe escono senza accento: `CAFFÈ` diventa `CAFFE`.

<!-- DA VERIFICARE: con le casse diverse dalle Micrelec, Epson comprese, il codice sembra trasformare in spazi le lettere accentate delle righe del buono (CAFFÈ esce CAFF): è così sulla carta? Se sì, l'avviso su ANSI e UTF-8 qui sopra va rivisto. -->

## Pulsanti e comandi

Non applicabile.

## Come si fa

### Come il programma decide se emettere il buono

Quando si chiude lo scontrino, il programma:

1. controlla che la ditta abbia attiva la casella **Abilita Emissione Buoni
   Sconto**, e legge il file della ditta o, in mancanza, quello generico;
2. se la data di oggi è fuori dal periodo di emissione, si ferma: nessun buono;
3. se il **Formato Stampa** della ditta non è un numero da 0 a 3, o se la
   validità fissa del file è già finita, si ferma senza emettere il buono e
   annota il motivo nel file degli errori;
4. sceglie la fascia: quella con la **spesa più alta che il totale dello
   scontrino raggiunge**. La spesa è raggiunta anche quando il totale è
   **uguale** alla spesa: con una fascia a 60,00 euro, uno scontrino di 60,00
   euro fa uscire il buono;
5. ricava la validità, calcola il valore, stampa il buono e lo registra.

Se il totale non raggiunge nessuna fascia, non esce niente.

### Un buono a fasce di spesa (importo in euro)

Si vuole un buono di 5 euro da 25 euro di spesa e di 12 euro da 50 euro di
spesa, spendibile da domani per 30 giorni.

1. Apri il Blocco note e scrivi:

        [OPTIONS]
        tipo = valore
        validita_dopo_giorni = 1
        validita_durata_giorni = 30
        multipli = 0
        spesa_1 = 25
        buono_1 = 5
        spesa_2 = 50
        buono_2 = 12
        header_1 = BUONO SPESA
        footer_1_1 = Buono di {VALORE}
        footer_1_2 = Valido dal {DAL} al {AL}
        footer_2_1 = Buono di {VALORE}
        footer_2_2 = Valido dal {DAL} al {AL}

2. Scegli **File ▸ Salva con nome**, imposta la **Codifica** su **ANSI** e salva
   il file come `buoni_sconto_00001.ini` (o `buoni_sconto.ini`) nella cartella
   **cfg** del programma.
3. Controlla che nella ditta sia attiva **Abilita Emissione Buoni Sconto**.
4. Batti uno scontrino da 30,00 euro: esce un buono da 5,00 euro. Con uno da
   55,00 euro ne esce uno da 12,00 euro; con uno da 120,00 euro, essendo la
   spesa di 50 euro contenuta due volte, un buono da 24,00 euro (con
   `multipli = 1`, invece, due buoni da 12,00 euro).

### Un buono in percentuale, con soglia unica

Si vuole regalare il 10% della spesa a chi spende almeno 50 euro, solo dall'1 al
24 dicembre 2026, e da spendere entro il 31 gennaio 2027.

1. Scrivi nel file:

        [OPTIONS]
        tipo = percentuale
        emissione_dal = 01/12/2026
        emissione_al = 24/12/2026
        validita_dal = 01/12/2026
        validita_al = 31/01/2027
        spesa_1 = 50
        buono_1 = 10
        header_1 = BUONO SCONTO
        header_2 = PER TE {VALORE}
        footer_1_1 = Buono di {VALORE} sulla prossima spesa
        footer_1_2 = Valido dal {DAL} al {AL}

2. Salva il file in ANSI, come sopra.
3. Batti uno scontrino da 55,55 euro il 10 dicembre: esce un buono da 5,56 euro,
   cioè il 10% del totale arrotondato al centesimo, valido fino al 31
   gennaio 2027.
4. Lo stesso scontrino battuto il 28 dicembre non fa uscire niente e non dà
   nessun messaggio.

!!! info "La percentuale vale solo al momento dell'emissione"

    Il buono in percentuale si calcola **una volta sola, alla chiusura dello
    scontrino**, sul totale dello scontrino. Quello che esce, e che il cliente
    riporta, è un normale buono **a valore**: vale quell'importo in euro e al
    banco si usa come qualunque altro buono a valore. Esce sempre **un buono
    solo**.

### Il buono stampato con il formato 3

Il **Formato Stampa** della ditta decide come è fatto il buono; i numeri sono
spiegati nella [scheda della ditta](../anagrafiche/ditte.md#scheda-fidelity-buoni-sconto).
Con il **formato 3 - Personalizzato da file** il buono contiene solo quello che
hai scritto nel file, in questo ordine (sulle stampanti 3i esce proprio così:
testa, codice a barre e coda, come le hai scritte):

1. le righe `header_1` … `header_5`, fino all'ultima compilata: una riga vuota
   in mezzo esce come riga bianca;
2. il codice a barre, con il numero del buono sotto (dove la cassa non lo
   stampa da sé);
3. le righe in coda della fascia scelta, con la stessa regola: fino
   all'ultima compilata, le vuote in mezzo escono come righe bianche.

Le righe sono centrate nella larghezza stabilita da `colonne`. Gli altri
formati (0, 1 e 2) non sono cambiati:

- **formato 1 e 2:** stampano sempre la cornice «MESSAGGIO PROMOZIONALE»,
  l'importo e le date di validità; le righe di testa e di coda del file non
  vengono usate;
- **formato 0:** se nel file c'è almeno una riga di testa, le righe di testa
  **sostituiscono** la cornice «MESSAGGIO PROMOZIONALE»; senza righe di testa
  esce la cornice. Seguono l'importo, le date di validità e il codice a barre;
  le righe di coda escono solo se ce n'è almeno una nel file.

## Controlli e messaggi

Quando il file non si può usare, **la vendita non si ferma**: lo scontrino esce
regolarmente, ma senza buono. Il motivo si legge nel file degli errori,
`sqlerr.txt`, nella cartella `log` della cartella di lavoro dell'utente se ne
è impostata una, altrimenti della cartella del programma. Ogni riga comincia
con la data e l'ora, per esempio `09/11/2026 10:15:00 - Buoni sconto: …`. Se la
stessa cosa si ripete a ogni scontrino, la riga **non viene ripetuta di
seguito**: non ne compare una per ogni vendita. Torna a comparire solo se nel
frattempo è stato scritto un altro messaggio dei buoni sconto, oppure dopo
aver riavviato Facile.

Nella tabella le parti che cambiano da un caso all'altro (percorsi, nomi,
valori) sono indicate con i puntini.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Buoni sconto: file di configurazione non trovato: …\cfg\buoni_sconto_00001.ini o …\cfg\buoni_sconto.ini* | La ditta ha l'emissione attiva ma nella cartella **cfg** non c'è né il file della ditta né quello generico. | Crea uno dei due file. Il codice della ditta nel nome è a cinque cifre. |
| *Buoni sconto: file di configurazione non trovato o non leggibile: …* | Il file c'è ma il programma non riesce ad aprirlo. | Controlla che non sia aperto in esclusiva da un altro programma e che l'utente di Windows possa leggerlo. |
| *Buoni sconto: il file … e' salvato in UTF-8 con BOM: salvarlo di nuovo in ANSI (Windows-1252)* | Il file è stato salvato in UTF-8 con BOM, e così non viene letto. Senza BOM verrebbe letto, ma le lettere accentate uscirebbero sbagliate. | Aprilo nel Blocco note e salvalo con **Codifica** **ANSI**. |
| *Buoni sconto: tipo sconosciuto: "…" (valori ammessi: valore, percentuale)* | In `tipo` c'è una parola diversa da `valore` e `percentuale`. | Correggi la parola, oppure togli la riga: vale `valore`. |
| *Buoni sconto: data non valida in …: "…" (formato gg/mm/aaaa)* | Una data non è nel formato `gg/mm/aaaa` o non esiste nel calendario (per esempio 31/04/2026). Il messaggio dice in quale chiave. | Correggi la data, oppure lasciala vuota se non serve. |
| *Buoni sconto: data non valida in start_year/start_month/start_day* (o *stop_year/stop_month/stop_day*) | Le date nel vecchio formato a tre chiavi non formano una data vera. | Correggile, oppure scrivi `validita_dal` e `validita_al`. |
| *Buoni sconto: fascia …: la percentuale … supera 100* | Con `tipo = percentuale` un `buono_n` è maggiore di 100. | Metti una percentuale da 1 a 100. |
| *Buoni sconto: nessuna fascia valida (servono spesa_n e buono_n maggiori di zero)* | Nessuna delle cinque fasce ha insieme spesa e buono maggiori di zero. | Compila almeno una coppia `spesa_1` e `buono_1`. |
| *Buoni sconto: validità non determinabile: servono validita_dal/validita_al oppure validita_durata_giorni* | Mancano sia la validità fissa sia la durata. | Scrivi `validita_dal` e `validita_al`, oppure `validita_durata_giorni` (ed eventualmente `validita_dopo_giorni`). |
| *Buoni sconto: validità non determinabile: validita_dal e validita_al vanno impostate entrambe, con validita_al non prima di validita_dal, oppure serve validita_durata_giorni* | La validità fissa è incompleta (una sola data) o la data finale viene prima di quella iniziale, e non c'è la durata. | Scrivi tutte e due le date nell'ordine giusto, oppure `validita_durata_giorni`. |
| *Buoni sconto: validita' gia' scaduta il …* | La validità fissa del file (`validita_al`) è già passata, ma il periodo di emissione è ancora aperto: il buono nascerebbe scaduto, quindi non esce. La data è quella di `validita_al`, scritta `gg-mm-aaaa`. | Sposta in avanti `validita_dal` e `validita_al`, oppure chiudi l'emissione con `emissione_al`. |
| *Buoni sconto: Formato Stampa … della ditta non previsto: valori ammessi da 0 a 3* | Nella scheda **Fidelity - Buoni Sconto** della ditta il **Formato Stampa** è un numero diverso da 0, 1, 2 e 3. Il buono non saprebbe come stamparsi, quindi non viene né stampato né registrato. | Nella [ditta](../anagrafiche/ditte.md#scheda-fidelity-buoni-sconto) imposta il **Formato Stampa** a un numero da 0 a 3. |
| *Buoni sconto: percorso troppo lungo: …* | Il percorso del file supera i limiti di Windows. | Accorcia il percorso della cartella del programma. |

### Quando la cassa non stampa il buono

Con le stampanti fiscali **Epson** e con i registratori **`MICRELEC G100`**, se
la cassa rifiuta un comando mentre stampa il buono — carta finita, coperchio
aperto, un'operazione che in quel momento non accetta — la stampa del buono
**si ferma al primo errore**: il resto del buono non viene mandato e il buono
esce incompleto, o non esce.

- Lo scontrino è già chiuso: la vendita è registrata e non cambia.
- Il buono **resta registrato** in archivio con il suo codice e vale come gli
  altri.
- Se dallo stesso scontrino dovevano uscire più buoni (`multipli = 1`), i
  successivi non vengono né stampati né registrati.
- Sull'Epson compare al massimo una finestra, quella della stampante sul
  comando rifiutato; con `MICRELEC G100` nessuna.
- Nel file degli errori, lo stesso descritto sopra, si legge una riga con il
  codice del buono e il motivo.

Con le altre casse non cambia nulla: la stampa del buono prosegue come prima.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Buoni sconto: buono … da … euro registrato ma non stampato: errore della cassa … (codice …, Err. …)* | Stampante Epson: la stampante ha rifiutato un comando del buono. Dopo *errore della cassa* c'è il punto in cui si è fermata — *all'apertura del non fiscale*, *sulla riga*, *sul barcode* o *alla chiusura del non fiscale* — e fra parentesi il codice di Facile e l'errore della stampante; a volte segue, dopo i due punti, il testo dell'errore. | Risolvi il problema della stampante. Il buono con quel codice è in archivio, ma il cliente non ha il tagliando completo. |
| *Buoni sconto: buono … da … euro registrato ma non stampato: errore della cassa … (codice …): …* | Registratore `MICRELEC G100`: la cassa ha rifiutato un comando del buono. Dopo i due punti c'è l'errore della cassa, per esempio *Errore 0x4C (76) della cassa: errore nei dati del codice a barre*. | Come sopra. |
| *Buoni sconto: altri … buoni da … euro non emessi per l'errore della cassa* | Dallo stesso scontrino dovevano uscire più buoni, e la stampa di uno si è fermata per un errore della cassa: i buoni che seguivano non sono stati emessi. Compare dopo la riga precedente. | Il cliente non ha ricevuto quei buoni. |

<!-- DA VERIFICARE: che cosa deve fare la cassiera con un buono registrato ma non stampato (ristamparlo, consegnare il codice, disattivarlo) e con i buoni non emessi? La decisione è ancora aperta. -->

### Il buono alla cassa

Quando il cliente riporta il buono, il codice si legge in cassa come un normale
buono a valore. Se il buono non si può usare, sul display compare uno dei
messaggi seguenti, nessuno sconto viene applicato e la vendita prosegue.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Codice Organizzazione non Valido* | Il buono è stato emesso da un'altra organizzazione: il suo codice non comincia con il **Codice Organizzazione** della ditta. | Il buono non si può usare in questo negozio. Se invece è un buono vostro, controlla il **Codice Organizzazione** nella scheda **Fidelity - Buoni Sconto** della [ditta](../anagrafiche/ditte.md#scheda-fidelity-buoni-sconto). |
| *Codice Punto Vendita non Valido* | Il buono è stato emesso da un altro punto vendita della stessa organizzazione e nella ditta **Abilita Circolarità** è spenta. | Il buono si usa solo nel punto vendita che l'ha emesso. Per renderlo spendibile in tutti i punti vendita attiva **Abilita Circolarità** nella ditta. |
| *Buono disabilitato* | Il buono è già stato usato: ogni buono si può incassare una volta sola. | Il buono non è più valido: il cliente non ha diritto allo sconto. |
| *Buono fuori termine validita'* | Oggi è prima del primo giorno o dopo l'ultimo giorno di validità del buono. | Se la validità non è ancora cominciata, il cliente può usare il buono dal giorno stampato sopra. Se è finita, il buono non dà più diritto allo sconto. |

## Note

!!! warning "Quello che era nella ditta ora sta nel file"

    Dalla versione 2026 B10 la scheda **Fidelity - Buoni Sconto** della ditta
    non ha più la soglia, la validità, i valori per listino e i moltiplicatori
    per giorno. I valori che c'erano **non sono stati travasati** nel file:
    chi li usava deve scrivere il file `.ini`, altrimenti, con l'emissione
    attiva e nessun file, il buono non esce più.

!!! warning "Un buoni_sconto.ini già presente vale anche per il POS"

    Se nella cartella **cfg** c'è già un file `buoni_sconto.ini`, dalla
    versione 2026 B10 le sue regole valgono anche per la
    [vendita al banco e POS](vendita-al-banco.md), che prima non lo leggeva.
    Con l'emissione attiva nella ditta, la cassa comincia a emettere i buoni
    con le fasce e la validità scritte in quel file: **controllale prima di
    aggiornare**, e se il file non serve più toglilo o rinominalo.

- La soglia è raggiunta anche con un totale **uguale** alla spesa della fascia.
- Il buono si basa sempre sul **totale dello scontrino**.
- Il file viene riletto a ogni scontrino: una modifica vale dallo scontrino
  successivo, senza riavviare Facile.
- Nel file si possono lasciare righe vuote e commenti con `;` quanti se ne
  vogliono.

## Vedi anche

- [Ditte](../anagrafiche/ditte.md#scheda-fidelity-buoni-sconto) — l'attivazione e il formato di stampa.
- [Vendita al banco e POS](vendita-al-banco.md#la-chiusura-dello-scontrino) — dove il buono si emette e si usa.
- [Scontrini](scontrini.md)
