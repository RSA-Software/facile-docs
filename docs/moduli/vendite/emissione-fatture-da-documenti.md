---
title: Emissione fatture da documenti
description: La fatturazione differita — come da documenti di trasporto, bolle, buoni, pro forma e ordini si generano le fatture.
modulo: Vendite
maschera_id: nessuna dialog propria
---

# Emissione fatture da documenti

Chi consegna con documento di trasporto e fattura a fine mese non riscrive le
fatture: le fa generare dai documenti già emessi. Ogni tipo di documento ha la
sua voce **Emissione Fatture**.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Vendite ▸ Doc. di Trasporto ▸ Emissione Fatture
        - Menu ▸ Vendite ▸ Bolle di Accompagnamento ▸ Emissione Fatture
        - Menu ▸ Vendite ▸ Buoni di Consegna ▸ Emissione Fatture
        - Menu ▸ Vendite ▸ Fatture Pro Forma ▸ Emissione Fatture
        - Menu ▸ Vendite ▸ Doc. di Trasporto Consegne Terzi ▸ Emissione Fatture
        - Menu ▸ Vendite ▸ Ordini Clienti ▸ Fatturazione da Ordini
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | Da cosa genera la fattura |
|---|---|
| **Doc. di Trasporto ▸ Emissione Fatture** | Dai documenti di trasporto del periodo. |
| **Bolle di Accompagnamento ▸ Emissione Fatture** | Dalle bolle. |
| **Buoni di Consegna ▸ Emissione Fatture** | Dai buoni di consegna. |
| **Fatture Pro Forma ▸ Emissione Fatture** | Dalle pro forma del periodo. |
| **Fatture Pro Forma ▸ Emissiona Fattura da Pro Forma** | Da una singola pro forma. |
| **Fatture Pro Forma ▸ Fatture Pro Forma da Ordini** | Genera pro forma partendo dagli ordini. |
| **Doc. di Trasporto Consegne Terzi ▸ Emissione Fatture** | Dai documenti di consegna a terzi. |
| **Doc. di Trasporto Consegne Terzi ▸ Emissione Note di Credito Concessionari** | Genera le note di credito per i concessionari. |
| **Ordini Clienti ▸ Fatturazione da Ordini** | Dagli ordini clienti. |

Il documento di partenza resta in archivio e risulta fatturato; la fattura ne
riporta gli estremi.

## Prerequisiti

Prima di fatturare occorre:

- avere emesso e **controllato** i documenti da fatturare: dopo, correggerli è
  molto più scomodo;
- avere sui clienti le condizioni giuste — pagamento, banca, sconti — perché la
  fattura le riprende;
- avere impostato registri e numeratori nella
  [ditta](../anagrafiche/ditte.md);
- **avere una copia di sicurezza recente**.

## La maschera

![Emissione fatture](../../assets/img/vendite/emissione-fatture-da-documenti.png)

La finestra prende il nome dall'operazione: **Fatturazione da Ordini** aprendola
dagli ordini, e poi **Emissione DDT**, **Fatture Pro Forma da Ordini**,
**Fatturazione da D.D.T. Consegnati da Terzi**, **Emissione Note di Credito da
Resi Clienti**.

Non è una semplice finestra di selezione: **è una griglia**. In alto i filtri
con cui si cercano i documenti, al centro l'elenco di quelli trovati con una
casella per riga, in basso i dati da mettere sulle fatture da generare. Si
cerca, si sceglie, si emette.

## Campi

### I filtri di ricerca

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo dei documenti da fatturare. Devono ricadere **nello stesso mese**. | date |
| **Cliente** | | Restringe a un cliente. | codice |
| **Registri** | | I registri da cui pescare i documenti. Si scrivono le lettere separate da virgola. | lettere e virgole |
| **Operatore** | | Restringe ai documenti di un [operatore](../altre-tabelle/operatori.md). | codice |

{: .campi }

### L'elenco dei documenti trovati

Le colonne sono **Tipo Doc.**, **Codice**, **Fatturato**, **Sel.**, **Anno**,
**Tipo**, **Numero**, **Data**, **Sezione**, **Cod. Cli.**, **Cliente**, **Cod.
Dest.** e **Destinazione**.

**Sel.** è la casella con cui si sceglie cosa fatturare; **Fatturato** segna le
righe già elaborate, che vengono saltate.

### I dati delle fatture da generare

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Tipo. Docum.** | ● | Il tipo di documento ai fini della fattura elettronica. | `TD01 - FATTURA`, `TD24 - FATTURA DIFFERITA DI CUI ALL'ART. 21, COMMA 4, LETT. A)`, `TD25 - FATTURA DIFFERITA DI CUI ALL'ART. 21, COMMA 4, TERZO PERIODO LETT. B)` |
| **N. Doc. Iniziale** | | Il numero da cui far partire la numerazione. | numero |
| **Registro** | ● | Il registro su cui numerare le fatture. | voce dell'elenco |
| **Sezione** | | La [sezione](../contabilita/sezioni.md) delle fatture. | codice |
| **Data Documenti** | ● | La data da mettere sulle fatture generate. Deve ricadere nello stesso mese del periodo cercato, o nel mese successivo. | data |
| **Raggruppamento** | ● | **Come i documenti si raggruppano in fattura.** | `NUMERO DOCUMENTO`, `ARTICOLI` |
| **Tipo Stampa** | | Cosa fare dopo aver generato. | `STAMPA IMMEDIATA`, `ANTEPRIMA DI STAMPA`, `SOLO GENERAZIONE` |
| **Copie** | | Quante copie stampare. | numero |
| **Accorpa Lotti** | | Mette insieme le righe dello stesso articolo con lotti diversi. | attivo/non attivo |
| **Controlla Date DDT** | | Verifica che le date dei documenti siano congrue. | attivo/non attivo |
| **Emetti Fatture IVA Esente** | | Emette le fatture con l'aliquota di esenzione invece che con quella dei documenti. Richiede un codice IVA esente impostato. | attivo/non attivo |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Emissione Fatture** | ++f2++ | Genera le fatture dai documenti spuntati. L'etichetta cambia con l'operazione: **F2 - Emissione DDT**, **F2 - Emissione Pro Forma**, **F2 - Emissione Note Credito**. |
| **F5 - Cerca Documenti da Fatturare** | ++f5++ | Cerca i documenti e li porta in griglia. Anche qui l'etichetta segue l'operazione. |
| **F3 - Seleziona Tutti** | ++f3++ | Spunta tutte le righe. |
| **F4 - Deseleziona Tutti** | ++f4++ | Toglie tutte le spunte. |
| **F6 - Trova** | ++f6++ | Cerca dentro la griglia. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |

## Come si fa

### Fatturare i DDT di fine mese

1. Apri la [gestione DDT](gestione-documenti.md) e controlla che i documenti
   del mese siano tutti giusti.
2. Apri **Menu ▸ Vendite ▸ Doc. di Trasporto ▸ Emissione Fatture**.
3. Indica **Data Iniziale** e **Data Finale** dentro lo stesso mese, e premi
   **F5 - Cerca Documenti da Fatturare**.
4. Controlla l'elenco e spunta cosa fatturare, oppure premi **F3 - Seleziona
   Tutti**.
5. In basso indica **Registro**, **Data Documenti** e il **Raggruppamento**.
6. Metti **Tipo Stampa** su `SOLO GENERAZIONE` la prima volta: così puoi
   rileggere le fatture prima di stamparle.
7. Premi **F2 - Emissione Fatture** e conferma.

### Fatturare un ordine evaso

1. Apri **Menu ▸ Ordini ▸ Ordini da Clienti ▸ Fatturazione da Ordini** — la
   stessa voce è sotto **Vendite ▸ Ordini Clienti**.
2. Cerca gli ordini del periodo con **F5**, spuntali e genera con **F2**.
3. Dopo la fatturazione, ripulisci con **Cancellazione Ordini Evasi**, vedi
   [Ordini clienti](ordini-clienti.md).

### Scegliere come raggruppare

- `NUMERO DOCUMENTO` — le righe restano divise per documento di origine, con il
  riferimento in fattura. È quello che i clienti si aspettano di vedere.
- `ARTICOLI` — le righe dello stesso articolo si sommano in una sola. Fattura
  più corta, ma il riferimento al singolo documento si perde.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Non è stato selezionato nessun documento!* | Nessuna riga è spuntata. | Spunta le righe, o usa **F3 - Seleziona Tutti**. |
| *Data Iniziale e Data Finale sul filtro di ricerca non possono ricadere in due mesi diversi!* | Il periodo cercato attraversa due mesi. | Fattura un mese per volta. |
| *La date delle fatture non è compatibile con le date indicate nella ricerca.<br>Deve ricadere nello stesso mese o nel mese successivo.* | La **Data Documenti** è troppo lontana dal periodo. | Correggi la data. |
| *L'intervallo di date selezionato non sembra essere congruo con la data di emissione delle fatture!.<br>Vuoi continuare?* | Le date sono insolite ma ammesse. | Controlla prima di rispondere **Sì**. |
| *Codice IVA non impostato o non valido !<br>Impossibile continuare* | È attiva **Emetti Fatture IVA Esente** ma manca l'aliquota. | Impostala nei [parametri della ditta](../anagrafiche/ditte.md). |
| *Il codice IVA impostato non è esente !<br>Impossibile continuare* | L'aliquota indicata non è di esenzione. | Usa un'[aliquota](../contabilita/aliquote-iva.md) esente. |
| *Il campo registri può contenere solo lettere e virgole!* | Il filtro **Registri** contiene altri caratteri. | Scrivi per esempio `A,B`. |
| *Confermi l' emissione delle Fatture  ?* | Conferma prima di generare. Nelle altre operazioni: *Confermi l' emissione di DDT ?*, *Confermi l' emissione di Fatture Pro Forma ?*, *Confermi l' emissione delle Note di Credito ?* | **Sì** genera i documenti. La risposta preimpostata è **No**. |

## Note

!!! warning "L'emissione crea documenti fiscali"

    Le fatture generate sono numerate sul registro: annullarle vuol dire
    lasciare buchi nella numerazione. Controlla il periodo, il cliente e il
    registro **prima** di premere **F2 - OK**, e rileggi il risultato prima di
    trasmettere.

!!! note "Rilanciare l'emissione non raddoppia le fatture"

    La ricerca porta in griglia i documenti **ancora da fatturare**, e la colonna
    **Fatturato** segna quelli già elaborati: una riga segnata viene saltata
    anche se resta spuntata. Rilanciare sullo stesso periodo è quindi
    ragionevolmente sicuro, ma la verifica vera si fa rileggendo le fatture dalla
    [gestione documenti](gestione-documenti.md).

!!! note "«Emissione Fatture» e «Emissiona Fattura da Pro Forma» sono due cose diverse"

    **Emissione Fatture** è la fatturazione di massa descritta in questa pagina:
    cerca molti documenti e ne fa le fatture. **Emissiona Fattura da Pro Forma**
    — con il refuso nell'etichetta di menu — trasforma **una singola** pro forma
    in una fattura, e usa la maschera della
    [duplicazione](esporta-duplica-documenti.md).

## Vedi anche

- [Documento di vendita](documento-di-vendita.md)
- [Gestione documenti](gestione-documenti.md)
- [Ordini clienti](ordini-clienti.md)
- [Contabilizzazione dei documenti](contabilizzazione-documenti.md)
