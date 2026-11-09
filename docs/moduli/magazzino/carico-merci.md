---
title: Carico merci
description: La registrazione della merce che arriva dal fornitore, con il controllo dei prezzi e delle quantità in entrata.
modulo: Magazzino
maschera_id: IDD_MAG_CARICO_MERCI
---

# Carico merci

La merce che arriva dal fornitore entra in magazzino da qui. Il carico porta
con sé gli estremi del documento del fornitore, i prezzi pagati e lo stato in
cui la merce è stata accettata.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Magazzino ▸ Nuovo Carico Merci *(oppure* Modifica Carico Merci*,* Modifica Carichi Fiscali*,* Controllo Merci in Entrata*,* Stampa Riepilogo Carichi*,* Generazione e Carico Buoni Regalo *o* Stampa Giornale Carichi Prodotti Fiscali*)*
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Il carico è il gesto con cui la merce diventa esistenza: aggiorna le giacenze,
scrive l'ultimo prezzo di acquisto sull'articolo — quello che poi la
[gestione listini](../listini-vendita/gestione-listini.md) usa come termine di
paragone — e lascia traccia di cosa il fornitore ha consegnato.

| Voce di menu | A cosa serve |
|---|---|
| **Nuovo Carico Merci**, **Modifica Carico Merci** | Registrano e correggono il carico. |
| **Modifica Carichi Fiscali** | Corregge i carichi dei prodotti soggetti ad accisa. |
| **Controllo Merci in Entrata** | Verifica quello che è arrivato rispetto a quello che era stato ordinato. |
| **Stampa Riepilogo Carichi** | L'elenco dei carichi di un periodo. |
| **Generazione e Carico Buoni Regalo** | Genera i buoni regalo e li carica a magazzino. |
| **Stampa Giornale Carichi Prodotti Fiscali** | Il giornale dei carichi dei prodotti soggetti ad accisa. |

## Prerequisiti

Prima di usare questa maschera occorre:

- avere gli [articoli](../anagrafiche/anagrafica-articoli.md) e i
  [fornitori](../anagrafiche/anagrafica-fornitori.md) in archivio;
- avere i [depositi](depositi.md) e le
  [causali di magazzino](causali-magazzino.md) impostate;
- avere le [aliquote IVA](../contabilita/aliquote-iva.md).

## La maschera

![Carico merci](../../assets/img/magazzino/carico-merci.png)

In alto la testata — chi ha consegnato, con quali documenti, a quali condizioni
—, sotto le righe della merce.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Numero** | | Numero del carico. Lo assegna il programma. | numero |
| **Data** | ● | Data del carico. | data |
| **Operatore** | | Chi ha registrato il carico. | codice |
| **Fornitore** | ● | Da chi arriva la merce. | codice |
| **Prima Nota. N.** | | Il riferimento alla registrazione contabile, quando c'è. | numero |
| **INS** | | Segnala che il carico è in inserimento. | — |
| **Fattura** | | Gli estremi della fattura del fornitore. | numero e data |
| **DDT / Bolla** | | Gli estremi del documento di trasporto. | numero e data |
| **Ordine** | | Il riferimento all'ordine a fornitore. | numero |
| **Sezione** | | La [sezione](../contabilita/sezioni.md) contabile. | codice |
| **% Sconto** | | Lo sconto generale sul carico. | percentuale |
| **% Spese** | | Le spese da ripartire sulla merce. | percentuale |
| **Stato** | | In che condizioni la merce è stata accettata. | `NORMALE`, `PREZZI DA CONTROLLARE`, `MERCE ACCETTATA CON RISERVA`, `PREZZI NON CONFORMI ALL' ORDINE` |

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra il carico e aggiorna le esistenze. |
| **F3 - Prec.**, **F4 - Succ.** | ++f3++, ++f4++ | Passano al carico precedente o successivo. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco dei carichi. |
| **F6 - Elimina** | ++f6++ | Cancella il carico, previa conferma. |
| **F7 - Stampa** | ++f7++ | Stampa il carico. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Caricare una fornitura

1. Apri **Menu ▸ Magazzino ▸ Nuovo Carico Merci**.
2. Indica il **Fornitore** e gli estremi di **Fattura** e **DDT / Bolla**.
3. Se i prezzi non sono quelli concordati, metti **Stato** su `PREZZI NON
   CONFORMI ALL' ORDINE`: te lo ritroverai nel **Controllo Merci in Entrata**.
4. Inserisci le righe con articolo, quantità e prezzo pagato.
5. Premi **F2 - Salva**: le esistenze si aggiornano e l'ultimo prezzo di
   acquisto degli articoli viene riscritto.

### Caricare da un foglio Excel o da un CSV

Il foglio porta i nomi delle colonne nella prima riga. Servono **CODICE** e
**DESCRIZIONE**; le altre più usate sono **QUANTITA**, **PREZZO_IMP** (il
prezzo senza IVA, oppure **PREZZO** con l'IVA compresa), **IVA**, **BARCODE**
e **BARCODE2**.

1. Apri **Menu ▸ Magazzino ▸ Nuovo Carico Merci** e indica il **Fornitore**.
2. Premi **F7 - Dati** e scegli **Foglio Excel**.
3. Rispondi **Sì** a *Vuoi importare gli Articoli da un foglio Excel ?* e
   scegli il file: `.xlsx`, `.xls` o `.csv`.
4. Rispondi **Sì** a *Vuoi procedere con l' importazione del Carico ?*: le righe
   del foglio entrano nella griglia.
5. Controlla le righe e premi **F2 - Salva**: solo adesso le esistenze e i
   prezzi di acquisto si aggiornano.

Gli articoli e i barcode del foglio vengono invece scritti in archivio già
durante l'importazione, anche se poi il carico non si salva.

Ogni testo letto dal foglio viene ripulito dai caratteri che non si vedono: gli
spazi non separabili, gli a capo e le tabulazioni dentro la cella diventano
spazi normali, gli spazi a larghezza zero, i trattini morbidi e i segni di
direzione del testo si tolgono. Lettere accentate, € e apostrofi tipografici
arrivano giusti anche dai CSV salvati in UTF-8.

### Rivedere i prezzi di vendita dopo il carico

Apri [Conferma Listini](../listini-vendita/controllo-listini.md), scegli
**Stato** `DA VERIFICARE` e **Tipo** `CARICHI`: escono gli articoli il cui
costo si è mosso, con il prezzo che servirebbe per tenere il margine.

### Controllare cosa è arrivato rispetto all'ordine

1. Apri **Menu ▸ Magazzino ▸ Controllo Merci in Entrata**.
2. Confronta quantità e prezzi con l'ordine.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Troppe aliquote IVA. Il Max Consentito è 7 !* | Il documento ha più di sette aliquote diverse. | Spezzare il carico in due documenti. |
| *Vuoi chiudere le partite aperte ?* | Chiesto al salvataggio quando restano partite aperte. | Rispondere **Sì** se il fornitore ha finito di consegnare. |
| *Vuoi applicare il costo degli imballaggi?* | Il fornitore ha imballaggi a costo. | **Sì** li somma al costo della merce. |
| *Stampante Etichette colli non impostata!* | Manca la stampante delle etichette. | Impostarla nelle [impostazioni della postazione](../utility/impostazioni-postazione.md). |
| *Vuoi Stampare solo la Rimanenza?* | Chiesto stampando. | Sceglie fra il documento intero e la sola rimanenza. |
| *Nel foglio c'e' un barcode in notazione esponenziale (…): Excel ne ha perso le cifre e non si puo' ricostruire.<br><br>Riga : …<br><br>Quel barcode non sara' salvato e non servira' a cercare l' articolo.<br><br>Vuoi procedere con l' importazione del Carico ?* | Nel foglio importato c'è un barcode scritto come lo mostra Excel, per esempio *8,00123E+12*: le cifre vere non ci sono più. Capita con i CSV aperti e risalvati da Excel. | **Sì** importa il carico senza quel barcode; **No** ferma l'importazione. Per avere il barcode serve il file originale: vedi la nota sui barcode passati da Excel. |
| *Nel foglio ci sono N barcode in notazione esponenziale (per esempio …): Excel ne ha perso le cifre e non si possono ricostruire.<br><br>Righe : …<br><br>Quei barcode non saranno salvati e non serviranno a cercare gli articoli.<br><br>Vuoi procedere con l' importazione del Carico ?* | Come sopra, per più barcode: l'elenco riporta le prime dieci righe del foglio. | Come sopra. |

!!! note "I messaggi sono tanti e quasi tutti domande"

    È la maschera più grande del programma e la maggior parte dei suoi avvisi
    sono richieste di conferma, non errori: la regola è che **rispondere Sì
    prosegue e rispondere No riporta al campo**. Quelli che bloccano davvero
    sono pochi, e sono in tabella.

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio. | Compila il campo su cui si è posizionato il cursore. |
| *Cancellazioni non abilitate per l' utente !* | L'utente ha il **Blocco Cancellazioni Dati**. | Serve un utente abilitato, o va tolto il blocco da [Archivi ▸ Utenti](../anagrafiche/utenti.md). |

## Note

!!! warning "Il carico riscrive l'ultimo prezzo di acquisto"

    Salvando il carico, l'ultimo prezzo di acquisto degli articoli caricati
    viene aggiornato. È il valore su cui poggiano margini, ricarichi e la
    [conferma dei listini](../listini-vendita/controllo-listini.md): un prezzo
    sbagliato sul carico si propaga.

!!! info "Il penultimo prezzo si sposta una volta sola per carico"

    Quando salvi un carico, l'ultimo prezzo di acquisto di ogni articolo
    diventa il penultimo e il prezzo del carico prende il suo posto. Questo
    succede **una volta per carico**, anche nei due casi in cui il carico tocca
    lo stesso articolo più di una volta:

    - **salvi di nuovo un carico già registrato**, per correggere una riga o
      per aggiungere gli estremi della fattura: l'ultimo prezzo prende il
      valore corretto e il penultimo resta quello del carico precedente;
    - **lo stesso articolo è su più righe dello stesso carico** (taglie,
      colori, lotti diversi, o righe ripetute nel foglio importato): l'ultimo
      prezzo è quello dell'ultima riga salvata e il penultimo resta quello del
      carico precedente.

    Lo stesso vale per la data dell'ultimo e del penultimo acquisto.

<!-- DA VERIFICARE: il ricalcolo dei contatori di magazzino ricostruisce anche il penultimo prezzo dell'articolo, per sistemare gli articoli toccati prima della correzione? -->

!!! warning "I barcode passati da Excel"

    Excel mostra un barcode di 13 cifre come **8E+12** o **8,00123E+12**, e
    toglie gli zeri iniziali: *0012345678905* diventa *12345678905*. Quello
    che arriva a Facile dipende da come il file è stato salvato:

    - un **.xlsx** o un **.xls** salvato da Excel conserva tutte le cifre e
      Facile legge il barcode intero, anche se Excel lo mostra abbreviato;
    - un **CSV aperto e risalvato da Excel** contiene il barcode come Excel
      lo mostrava, *8,00123E+12*: le altre cifre non ci sono più.

    Prima di importare, Facile conta i barcode in notazione esponenziale e lo
    dice con le righe del foglio dove sono. Quei barcode non vengono salvati
    sull'articolo e non servono a cercarlo. Se invece la notazione porta
    ancora tutte le cifre (*8,001234567890E+12*), il barcode viene ricostruito
    intero senza dire niente. Nelle installazioni con taglie e colori lo
    stesso controllo vale anche per **Foglio Excel Miniconf s.p.a.** e
    **Foglio Excel Macron Sports**.

    Per non perdere i barcode, importa il file `.xlsx` che hai ricevuto, oppure
    il CSV del fornitore senza aprirlo e risalvarlo con Excel. Se devi passarlo
    da Excel, aprilo da **Dati ▸ Da testo/CSV** e imposta come **Testo** le
    colonne dei barcode: così restano anche gli zeri iniziali, che Facile non
    può rimettere.

!!! info "La % Spese va sul valore netto, riga per riga"

    Non è una ripartizione di un totale: è una **percentuale applicata al
    prezzo netto di ogni riga**, cioè al prezzo dopo lo sconto di testata e i
    sette sconti di riga. Il risultato finisce nella colonna **Spese** della
    riga, come importo unitario, e da lì entra nel costo.

    Quindi **non c'entrano né il peso né la quantità**: due righe di pari valore
    prendono la stessa quota di spese anche se una pesa il doppio.

    Cambiando lo **sconto di testata** le spese si ricalcolano da sole, perché
    cambia la base su cui la percentuale si applica.

!!! info "Lo Stato è una nota, non un comando"

    Lo **Stato** non cambia quello che il programma fa: non blocca il
    salvataggio, non altera i calcoli, non impedisce la contabilizzazione. È
    un'**etichetta per chi legge dopo**, e si ritrova nella colonna *Stato* del
    [Controllo Carichi](stampe-magazzino-fornitori.md).

    Le voci sono dodici: `NORMALE`, `PREZZI DA CONTROLLARE`, `MERCE ACCETTATA
    CON RISERVA`, `PREZZI NON CONFORMI ALL' ORDINE`, `PREZZI NON CONFORMI AI
    LISTINI`, `SCONTISTICA PATTUITA NON RISPETTATA`, `CONFEZIONI DANNEGGIATE`,
    `QUANTITA' NON CONFORMI ALL' ORDINE`, `PAGATO ALLA CONSEGNA`, `PARZIALMENTE
    PAGATO ALLA CONSEGNA`, `RESO RIPARAZIONE` e `SOSTITUZIONE`.

    Serve a segnalare al collega, o a sé stessi fra un mese, perché quel carico
    va guardato: il posto dove lo si rilegge è il Controllo Carichi, non questa
    maschera.

!!! tip "Prima Nota. N. è il collegamento, non una copia"

    Il campo tiene il **numero della registrazione** nata da questo carico:
    finché è vuoto il documento non è stato contabilizzato.

    Il carico e la registrazione restano **due cose distinte**: correggere il
    carico non corregge la prima nota, e viceversa. Se cambiano gli importi
    dopo la contabilizzazione, la registrazione va sistemata a parte.

!!! warning "Modifica Carichi Fiscali non c'è in tutte le installazioni"

    È una maschera **diversa** da questa e vive solo nella versione allestita
    per la gestione fiscale: dove quella versione non c'è, la voce di menu non
    fa niente.

    Dove c'è, **chiede una password prima di aprirsi**: è il segno di che cosa
    serve — intervenire sui movimenti già fiscalmente rilevanti, cosa che non si
    fa nel lavoro di tutti i giorni. Il carico merci normale resta questo.

## Vedi anche

- [Movimenti di magazzino](movimenti-magazzino.md)
- [Causali magazzino](causali-magazzino.md)
- [Conferma e confronto dei listini](../listini-vendita/controllo-listini.md)
- [Anagrafica fornitori](../anagrafiche/anagrafica-fornitori.md)
