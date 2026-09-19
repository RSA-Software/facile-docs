---
title: Le tabelle
description: Soggetti obbligati, registri, firme DAS e le tabelle ministeriali dei prodotti energetici, con le importazioni dai fogli dell'Agenzia delle Dogane.
modulo: Energy
maschera_id: IDD_ENE_SOGGETTI
---

# Le tabelle

Il modulo Energy poggia su una decina di tabelle. Si dividono in due famiglie, e
vale la pena tenerle distinte: **quelle che descrivono il deposito**, che si
compilano a mano una volta sola, e **quelle che vengono dall'Agenzia delle
Dogane**, che non si inventano ma si importano.

---

## Le tabelle del deposito

### Soggetti Obbligati

Chi risponde all'Agenzia per quel deposito.

| Campo | Descrizione |
|---|---|
| **Codice** | Il codice interno. |
| **Tipo** | `ESERCENTI DEPOSITI COMMERCIALI` oppure `OLI LUBRIFICANTI E BITUMI DI PETROLIO`. |
| **Descrizione** | Il nome del soggetto. |
| **Ufficio Dogane** | L'ufficio competente. |
| **Cod. Ditta** | Il codice con cui l'Agenzia conosce la ditta. |
| **Cod. UA** | Il codice dell'unità amministrativa, che finisce nel nome del file di flusso. |
| **Ultimo Flusso** | Numero e data dell'ultimo flusso trasmesso. Lo aggiorna il programma. |

{: .campi }

### Registri

I registri su cui si scrive.

| Campo | Descrizione |
|---|---|
| **Codice**, **Descrizione** | Come si chiama il registro. |
| **Tipo Registro** | `M - MATERIE PRIME E SEMILAVORATI` o `F - PRODOTTI FINITI`. |
| **Sog. Obbligato** | A chi appartiene. |
| **Ufficio Dogane** | L'ufficio competente. |
| **Protocollo**, **Anno** | Gli estremi di vidimazione del registro. |
| **Non Attivo** | Lo mette da parte senza cancellarlo. |
| **Giacenza KG**, **Giacenza LT** | Le giacenze correnti. |
| **Calcola Giacenza KG**, **Calcola Giacenza LT** | Se il registro deve produrre la giacenza di fine giornata, e in quale misura. |
| **Ultimo Rigo Registro Inviato** | Fin dove si è arrivati con le trasmissioni. |
| **Ultimo Rigo Registro Attribuito** | L'ultimo rigo numerato. |

{: .campi }

!!! warning "Le due caselle «Calcola Giacenza» decidono chi riceve le giacenze"

    [Inserimento Giacenze](movimenti.md) considera **solo i registri attivi che
    hanno almeno una delle due caselle spuntata**. Un registro che dovrebbe
    avere la giacenza e non ce l'ha non dà nessun errore: semplicemente resta
    senza, e il buco si scopre al controllo.

!!! danger "I due «ultimo rigo» non si toccano a mano"

    Sono la memoria di che cosa è già stato trasmesso. Correggerli a mano
    significa far ripartire la numerazione da un punto sbagliato: o si
    ritrasmettono righe già inviate, o se ne saltano. Se non tornano, è un caso
    da [assistenza](../../utility/assistenza.md).

### Firme DAS

L'elenco di chi può firmare i DAS. È la
[maschera comune delle tabelle](../../magazzino/tabelle-di-classificazione.md),
con codice e descrizione, e si stampa da **Firme ▸ Stampa**.

## Le tabelle dell'Agenzia delle Dogane

Queste tabelle **le pubblica l'Agenzia**, in fogli Excel identificati da una
sigla. Facile le importa da quei fogli: si scarica il foglio aggiornato, si
lancia l'importazione, si sceglie il file.

| Tabella | Foglio | Voce di menu |
|---|---|---|
| Uffici Agenzia Dogane | **TA03** | Uffici Agenzia Dogane ▸ Importa (TA03) |
| Tipi Documento | **TA05** | Tipi Documento ▸ Importa (TA05) |
| Nazioni | **TA06** | Nazioni ▸ Importa (TA06) |
| Causali Movimenti | **TA08** | Causali Movimenti ▸ Importa Causali Scarico / Carico |
| Periodi Movimentazione Imposta | **TA09** | Periodi Movimentazione Imposta ▸ Importa (TA09) |
| Tributi | **TA10** | Tributi ▸ Importa (TA10) |
| Posizioni Fiscali | **TA12** | Posizioni Fiscali ▸ Importa (TA12) |
| Prodotti Energetici | **TA13** | Prodotti Energetici ▸ Importa (TA13) |

### Come funziona l'importazione

Si apre la finestra di scelta del file, che propone i **Documenti Excel 2003
(\*.xls)** e i **Documenti Excel 2007 (\*.xlsx)**. Facile legge il foglio
cercando le colonne **dalle intestazioni**, non dalla posizione: quello che
conta è che ci siano le colonne attese — `CODICE`, `DESCRIZIONE`, e per gli
uffici anche `NAZIONE`.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Colonna CODICE non trovata nel documento !* | Il foglio non ha quella colonna, o l'intestazione è scritta diversamente. | Verificare di aver scaricato il foglio giusto e di non aver rinominato le colonne. |
| *Colonna DESCRIZIONE non trovata nel documento !* | Come sopra. | Come sopra. |
| *Colonna NAZIONE non trovata nel documento !* | Manca nel foglio degli uffici. | Come sopra. |
| *Formato file non compatibile!* | Il file non è un foglio Excel leggibile. | Riaprirlo in Excel e risalvarlo come `.xls` o `.xlsx`. |
| *File utilizzato da un' altra applicazione o formato file non compatibile!* | Il foglio è aperto in Excel. | Chiuderlo e riprovare. |
| *Impossibile Creare la tabella* | Non si riesce a preparare la tabella di appoggio. | È un caso da assistenza. |

!!! tip "Le tabelle ministeriali si aggiornano, non si correggono"

    Quando l'Agenzia cambia un codice, la strada giusta è **riscaricare il
    foglio e rifare l'importazione**, non ritoccare la riga a mano: così le
    descrizioni restano quelle ufficiali e le importazioni successive non
    trovano incoerenze.

    I movimenti già registrati con il vecchio codice si sistemano con
    [Varia Codice Prodotto Energetico](movimenti.md).

### Uffici Agenzia Dogane

Oltre a codice e descrizione, questa tabella ha l'**ID Ufficio**.

!!! warning "L'ID Ufficio ha una forma precisa"

    Deve essere di **otto caratteri**, e dal terzo in poi **solo cifre**. Un ID
    scritto male non dà fastidio finché si registra: salta fuori al momento di
    generare il flusso, con *ID Ufficio Dogana non valido !*, e il flusso non
    parte.

### Prodotti Energetici

| Campo | Descrizione |
|---|---|
| **Codice** | Il codice ministeriale del prodotto. |
| **CPA**, **NC**, **TARIC**, **CADD** | Le classificazioni doganali del prodotto. |
| **Descrizione** | Su due righe. |
| **Un. Misura** | L'unità di misura. |
| **Tassato** | `SI` o `NO`. |
| **Categoria** | La categoria ministeriale: `E410-BENZINA CON PIOMBO`, `E420-BENZINA SENZA PIOMBO`, `E430-GASOLIO NON COLORATO`, `E440-GASOLIO COLORATO`, `E910-FAMAE`, oppure vuota. |
| **Non Attivo** | Lo mette da parte. |

{: .campi }

### Causali Movimenti

| Campo | Descrizione |
|---|---|
| **Codice** | Il codice della causale. |
| **Tipo** | `CARICO` o `SCARICO`. |
| **Descrizione** | Come si chiama. |
| **Normativa** | Il riferimento di legge della causale. |
| **Mov. Interna**, **Mov. Esterna** | `SI` o `NO`: se la causale riguarda movimenti interni al deposito, esterni, o entrambi. |
| **Non Attiva** | La mette da parte. |

{: .campi }

Le causali si importano **in due passaggi distinti** — prima quelle di scarico,
poi quelle di carico — perché l'Agenzia le pubblica in due fogli separati.

### Tipi Documento, Posizioni Fiscali, Tributi, Periodi

Tutte con **codice e descrizione**, più la casella che le disattiva (**Non
Abilitato** per i tipi documento, **Non Attiva** per le posizioni fiscali).
Tributi e Periodi usano la
[maschera comune delle tabelle](../../magazzino/tabelle-di-classificazione.md) e
hanno la loro stampa.

!!! note "Disattivare invece di cancellare"

    Un codice ministeriale che non si usa più **non va cancellato**: i movimenti
    vecchi continuano a richiamarlo, e senza la riga in tabella le stampe
    perdono la descrizione. Si spunta la casella che lo disattiva: sparisce
    dalle scelte nuove e resta leggibile nelle scritture passate.

## Vedi anche

- [Movimenti](movimenti.md)
- [Flussi e riepiloghi](flussi-e-riepiloghi.md)
- [Tabelle di classificazione](../../magazzino/tabelle-di-classificazione.md)
