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
