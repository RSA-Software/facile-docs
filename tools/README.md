# Strumenti di redazione

Servono a scrivere le schede del manuale, non a costruire il sito. Si lanciano
dalla radice del repository.

## `etichette-maschere.py`

Estrae le etichette dei campi da un file `.rc` di Facile. È indispensabile:
le etichette **non** stanno nel `.rc` come testo, perché i controlli
`pvtext3d` sono ActiveX e la didascalia è dentro i blocchi `DLGINIT`, in
esadecimale. Senza questo script le maschere si leggono solo aprendo il
programma.

```
.venv/Scripts/python.exe tools/etichette-maschere.py C:/rsawin/Facile/RSATblCom/RSATblCom.rc IDD_TBC_BANCHE
```

Legge il **disegno** della maschera. Campi nascosti o rinominati a runtime —
per versione del programma, o secondo i dati dell'azienda — si trovano solo
nel `.cpp` corrispondente.

## `appendice-messaggi.py`

Rigenera `docs/appendici/messaggi-errore.md` leggendo la sezione «Controlli e
messaggi» di **tutte** le schede. L'appendice non si scrive a mano: si
aggiunge il messaggio alla scheda della sua maschera e si rilancia questo.

```
.venv/Scripts/python.exe tools/appendice-messaggi.py
```

Prende solo le tabelle con le colonne `| Messaggio | Causa | Cosa fare |`: una
tabella con colonne diverse, dentro quella sezione, viene ignorata. I messaggi
identici su piu' schede diventano una riga sola, e oltre sei schede la colonna
*Dove* dice «Molte maschere».

## `domande-aperte.py`

Raccoglie i marcatori `DA VERIFICARE` sparsi nelle schede e rigenera
`DOMANDE-APERTE.md`.

```
.venv/Scripts/python.exe tools/domande-aperte.py
```

## `segnaposto-schermata.ps1`

Disegna il segnaposto di una schermata, nello stile delle altre. Ogni scheda
ne vuole uno finché non c'è lo screenshot vero.

```powershell
$tabs = @('Generale','Impostazioni','Totali')
.\tools\segnaposto-schermata.ps1 -Titolo 'Facile - Nome maschera' `
    -Testata 'Testata: Codice, Descrizione' -Tabs $tabs `
    -Out 'docs\assets\img\<modulo>\<slug>.png'
```

Per una maschera senza schede passare `-Tabs @()`.

---

# Cattura degli screenshot reali

Sostituisce i segnaposto con le schermate vere di Facile. Tre script in
sequenza; i primi due sono solo testo e girano ovunque, il terzo pilota il
programma e gira **solo su Windows**, sul PC dove Facile e' installato.

```
.venv\Scripts\pip.exe install -r tools\requisiti-cattura.txt
copy tools\cattura.ini.esempio tools\cattura.ini    (poi compilarlo)
```

## 1. `comandi-menu.py`

Legge `IDR_MAINFRAME MENU` in `FacWin.rc` e `resource.h`, e scrive la mappa
`voce di menu -> numero del comando`.

```
.venv\Scripts\python.exe tools\comandi-menu.py C:\rsawin\Facile > tools\comandi-menu.json
```

## 2. `inventario-schermate.py`

Mette insieme le schede del manuale (titolo, `maschera_id`, riga *Percorso*,
segnaposto da sostituire) con quella mappa, e scrive `tools/schermate.yml`.

```
.venv\Scripts\python.exe tools\inventario-schermate.py
```

Le voci che non si risolvono restano con `stato: da-mappare` e un
`suggerimenti:` con le voci di menu piu' vicine. Capita quando la scheda cita
la voce con parole diverse da quelle del programma — *Scadenziario* contro
*Scadenzario*, *Promozioni* contro *Promozioni Sellout*: e' un segnale che va
corretta la scheda, non lo script. Le correzioni stabili vanno in
`tools/schermate-override.yml`, che vince sul generato.

## 3. `cattura-schermate.py`

Manda `WM_COMMAND` alla finestra principale, aspetta la maschera, scatta e
salva **sopra** il segnaposto: il Markdown non cambia.

```
.venv\Scripts\python.exe tools\cattura-schermate.py --solo "Archivi > Clienti" --solo "Archivi > Fornitori"
```

`--prova` elenca cosa farebbe senza toccare niente. `--slug nome` rifa' una
singola scheda. `--ocr` aggiunge la rete di sicurezza sui dati a video.

Chiude sempre con Annulla/ESC, mai con Invio o F2: la corsa non scrive
sull'archivio. Se una finestra resta aperta si ferma, invece di continuare
alla cieca.

Una maschera che non si apre non e' un errore: spesso e' Facile che si rifiuta
perche' l'archivio non ha i dati. Il messaggio finisce in
`tools/catture-report.md` e `catture-report.json`, con il comando pronto per
rifarla su un archivio popolato. `invia-report.py` manda quella lista per
email.

## `offusca.py` e `regole-privacy.yml`

Il manuale e' pubblico: ragioni sociali, nomi, partite IVA, codici fiscali,
telefoni ed email vengono coperti prima del salvataggio.

Il riconoscimento e' per **etichetta**, cioe' per la scritta che il lettore
vede accanto al campo, elencata in `regole-privacy.yml`. Non per nome del
controllo: in Facile lo stesso numero ricompare in maschere diverse con nomi
diversi — l'id 295 e' insieme `IDC_CLI_D_START` e `IDC_CLI_FIRST_VAL2` —
quindi una regola sui nomi copre cose a caso. Non per contenuto: vale anche a
campo vuoto.

Un'etichetta si riconosce dalla **classe**, dal **testo** e dal fatto che sta
sulla stessa riga del campo. **Non dall'identificatore:** con le vecchie
PVTEXT3D era un controllo senza id e il filtro si basava su quello, ma le
maschere convertite a `CRSALabel` hanno bisogno di un id vero per il
`DDX_Control`. Finche' il filtro ha guardato l'id, quelle maschere
risultavano senza etichette e non veniva coperto **niente, in silenzio**
(trovato il 23/09/2026 su `IDD_TCN_SUBAPPALTATORE`: la ragione sociale del
fornitore sarebbe finita nel manuale in chiaro).

`larghezza_minima` serve a non sfocare il campicino del codice accanto alla
descrizione. E' in **pixel a 96 DPI**, e viene riportata alla scala della
cattura da `fattore_dpi()`: al 150% la soglia predefinita di 70 diventa 105,
e un campo da 45 unita' di dialog — che a quella scala misura 101 — resta
giustamente fuori. Senza la correzione la soglia non escludeva piu' niente e
veniva coperto anche il codice: innocuo per la riservatezza, ma la schermata
perdeva un dato utile. Chi rielabora uno screenshot catturato **altrove** puo'
passare la scala di quella cattura come quarto argomento di
`regioni_da_etichette`.

La copertura e' sfocatura **piu'** pixelatura, perche' la sola sfocatura si
puo' in parte invertire.

C'e' anche una seconda rete, per **testo**: riconosce email, partite IVA,
codici fiscali e telefoni per forma, ed e' pensata per griglie ed elenchi dove
i dati non stanno in un controllo per campo. Richiede Tesseract e si attiva
con `--ocr`.
