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
telefoni ed email vengono coperti prima del salvataggio. Il riconoscimento e'
per **nome del controllo** (`IDC_..._RAGSOC`), letto dai `resource.h` dei
sorgenti, non per contenuto: vale anche a campo vuoto. La copertura e'
sfocatura piu' pixelatura, perche' la sola sfocatura si puo' in parte
invertire.
