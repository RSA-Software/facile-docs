---
name: manuale-maschere
description: Genera o aggiorna la scheda di manuale utente di una maschera di Facile, leggendo il codice sorgente della dialog e producendo un file Markdown per il sito MkDocs. Usare quando l'utente chiede di documentare una maschera, una form o una dialog, di scrivere il manuale di un modulo, o di aggiornare la documentazione dopo una modifica al codice.
---

# Documentare una maschera di Facile

Questa skill produce **una scheda di manuale utente per ogni maschera** del
gestionale Facile. L'output finale è un file Markdown nel repository
`facile-docs`, pubblicato con MkDocs Material.

## Regola fondamentale

Il manuale è scritto **per l'utente finale**, non per lo sviluppatore. Il
codice sorgente è la fonte dei fatti — nomi dei campi, lunghezze, controlli di
validazione, testi dei messaggi — ma non deve mai trasparire nel testo:

- ✅ «Il codice può contenere fino a 8 caratteri.»
- ❌ «Il campo `m_strCodice` è un `CString` limitato a 8 dal `DDX_Text`.»

Non citare mai nomi di variabili, classi, funzioni, tabelle del database o ID
di risorsa nel corpo del documento. L'unico posto dove può comparire un
riferimento tecnico è il campo `maschera_id` del front matter.

## Procedimento

### 1. Individuare le fonti nel codice

Per la maschera richiesta, raccogliere:

- il **file .rc** (template della dialog): etichette esatte dei campi e dei
  pulsanti, ordine di tabulazione, controlli presenti;
- il file **.h/.cpp** della classe dialog: `DoDataExchange` per il legame
  campo↔dato, `DDV_*` e i controlli manuali per le regole di validazione, i
  gestori `On*` per il comportamento dei pulsanti;
- le **stringhe di messaggio** (string table o costanti) usate dalla maschera:
  servono per la sezione *Controlli e messaggi*, riportate con il testo
  **esatto** che l'utente vede a video;
- il **menu** da cui si apre la maschera e l'eventuale acceleratore da
  tastiera, per il blocco «In sintesi».

### 2. Verificare prima di scrivere

Ogni affermazione del documento deve poggiare su qualcosa che hai letto nel
codice. Se un'informazione non è ricavabile — per esempio il significato
funzionale di un campo dal nome ambiguo, o il flusso di lavoro in cui la
maschera si inserisce — **non inventarla**: inserisci un marcatore

    <!-- DA VERIFICARE: <domanda precisa> -->

e riportalo nel riepilogo finale, così l'autore può rispondere in un secondo
momento. Un manuale con dieci domande aperte è recuperabile; uno con dieci
affermazioni inventate va riscritto da capo.

### 3. Scrivere il documento

Partire da `templates/documento-maschera.md` e rispettarne la struttura
**senza aggiungere, togliere o riordinare le sezioni** — l'uniformità tra le
schede è ciò che rende il manuale consultabile. Se una sezione non si applica,
scrivere «Non applicabile.» invece di eliminarla.

Regole di scrittura:

- lingua **italiana**, registro professionale, rivolgersi all'utente con il
  **tu** («Premi **Salva**»), come già fa il template;
- le etichette dei campi e dei pulsanti vanno riportate **esattamente** come
  appaiono a video, in **grassetto**;
- le procedure sono elenchi numerati di passi all'imperativo, ciascuno con una
  sola azione, e l'ultimo passo descrive il risultato osservabile;
- i tasti si scrivono con la sintassi `++f2++`, `++ctrl+n++`;
- i percorsi di menu con il separatore ▸;
- i riquadri `!!! warning` sono riservati a effetti irreversibili o
  comportamenti non ovvi: se ne metti uno su ogni pagina, smettono di essere
  letti;
- niente frasi di riempimento («questa maschera è molto utile», «come è noto»).

### 4. Salvare e collegare

1. Salvare in `docs/moduli/<modulo>/<slug-maschera>.md`, dove lo slug è il nome
   della maschera in minuscolo, senza accenti, con i trattini
   (*Anagrafica clienti* → `anagrafica-clienti.md`).
2. Aggiungere la voce nel `nav:` di `mkdocs.yml`. **Il `nav` ricalca il menu di
   Facile**, non i moduli del codice: la voce va messa nel ramo e nella
   posizione che la maschera ha nel menu, con l'etichetta della voce di menu.
   Il riferimento è il menu completo, `IDR_PROFESSIONAL` in `FacWin.rc`; se la
   maschera è raggiungibile da più voci, si sceglie quella principale e le
   altre si citano nella pagina. Il campo `modulo` del front matter riporta lo
   stesso ramo (`Archivi`, `Archivi ▸ Magazzino`, `Vendite`…).
3. Aggiungere la maschera nell'elenco dentro l'indice del ramo
   (`docs/moduli/archivi.md`, `docs/moduli/<sottomenu>/index.md`).
4. Riportare i messaggi di errore anche nella tabella cumulativa di
   `docs/appendici/messaggi-errore.md`.
5. Inserire il riferimento allo screenshot come
   `assets/img/<modulo>/<slug-maschera>.png` anche se l'immagine non esiste
   ancora: verrà aggiunta a mano.

### 5. Controllare

Prima di considerare finito il lavoro:

- `mkdocs build --strict` non deve segnalare errori (link interni rotti,
  pagine fuori dal `nav`);
- ogni link `Vedi anche` punta a un file esistente;
- il front matter ha `title`, `description`, `modulo`, `maschera_id`
  valorizzati; la `description` è una frase di senso compiuto, perché è quella
  che compare nei risultati di Google.

## Lavorare su un modulo intero

Se la richiesta riguarda più maschere, procedere **una maschera alla volta**,
salvando ogni file prima di passare alla successiva, e presentare all'utente
il riepilogo dei marcatori `DA VERIFICARE` solo alla fine. Cominciare dalla
maschera più usata del modulo: è quella su cui conviene tarare il livello di
dettaglio prima di replicarlo sulle altre.
