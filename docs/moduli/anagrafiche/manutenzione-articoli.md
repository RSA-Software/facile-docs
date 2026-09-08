---
title: Manutenzione degli articoli
description: Le voci che modificano, duplicano, cancellano gli articoli e ne raggruppano in panieri — comprese la modifica da griglia, i dati per il negozio online e le tassonomie.
modulo: Archivi
maschera_id: IDD_ART_ARTICOLI_CANCELLA
---

# Manutenzione degli articoli

Le voci di **Archivi ▸ Articoli** che non stampano nulla ma intervengono
sull'archivio: correggere molti articoli in una volta, caricarne i prezzi,
duplicarne uno, cancellarne un gruppo, raggrupparli in panieri, prepararli per
il negozio online.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Archivi ▸ Articoli ▸ Attribuzione Tassonomie
        - Menu ▸ Archivi ▸ Articoli ▸ Caricamento Prezzi
        - Menu ▸ Archivi ▸ Articoli ▸ Cancellazione Articoli
        - Menu ▸ Archivi ▸ Articoli ▸ Gestione Panieri
        - Menu ▸ Archivi ▸ Articoli ▸ Duplica
    - **Scorciatoia:** ++f2++ salva o conferma, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|

Due voci di questo gruppo hanno una pagina propria:
[Modifica articoli da griglia](modifica-da-griglia.md) e
[Impostazione dati web degli articoli](impostazione-dati-web.md).
| **Attribuzione Tassonomie** | Assegnare agli articoli le tassonomie del catalogo online: sono le categorie con cui il sito raggruppa i prodotti, indipendenti dalla classificazione di magazzino. |
| **Caricamento Prezzi** | Inserire in sequenza i prezzi degli articoli, vedendo accanto ultimo prezzo d'acquisto ed esistenza. |
| **Cancellazione Articoli** | Eliminare in blocco gli articoli che rispondono a certi criteri. |
| **Gestione Panieri** | Raggruppare articoli in un **paniere**, cioè in un insieme richiamabile con un tasto solo alla [vendita touchscreen](../vendite/vendita-al-banco.md). |
| **Duplica** | Creare un articolo copiandone un altro. |

## Prerequisiti

Prima di usare queste maschere occorre avere gli
[articoli](anagrafica-articoli.md) in archivio, e — per **Cancellazione
Articoli** — **una copia di sicurezza recente**.

Per i dati web e le tassonomie serve il collegamento al negozio online
configurato nella scheda **E-Commerce** delle [ditte](ditte.md).

## La maschera

![Cancellazione articoli](../../assets/img/anagrafiche/manutenzione-articoli.png)

Sono maschere diverse fra loro.

**Caricamento Prezzi** è una finestra a campi: in alto l'**Articolo**, e sotto
i dati che aiutano a decidere il prezzo — **Ultimo Prezzo d' Acquisto**,
**Esistenza** — insieme alla classificazione dell'articolo.

**Cancellazione Articoli** è un riquadro di selezione con, in più, tre
condizioni di soglia.

**Gestione Panieri** ha in alto il campo **Paniere** e sotto la griglia degli
articoli che vi appartengono.

**Duplica** ha due soli campi.

## Campi

### Attribuzione Tassonomie

Una griglia con le colonne **Codice**, **Descrizione**, **N. Taxons** — quante
tassonomie ha già l'articolo — **Web**, **Nome Web**, **Rep.**, **Cat.**,
**Mar.** e **Set.**

### Caricamento Prezzi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Articolo** | ● | L'articolo di cui caricare il prezzo. | codice |
| **Listino** | ● | Su quale listino scrivere. | codice |
| **Ultimo Prezzo d' Acquisto** | | Quanto è costato l'ultima volta. Solo lettura. | — |
| **Esistenza** | | Quanto ce n'è. Solo lettura. | — |
| **Cod. Iva**, **Un. Misura**, **Cat. Merc.**, **Reparto**, **Stagione**, **Marchio**, **Gruppo**, **Sottogruppo** | | La classificazione dell'articolo, mostrata per aiutare a decidere. Solo lettura. | — |

{: .campi }

### Cancellazione Articoli

La parte alta è la selezione degli articoli:

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Deposito** | | Su quale [deposito](../magazzino/depositi.md) valutare le condizioni. | codice |
| **Articolo**, **Cod. Iva**, **Reparto**, **Marchio**, **Cat. Merc.**, **Fornitore**, **Stagione**, **Gruppo**, **Sottogruppo** | | I filtri con cui restringere. | codici |

{: .campi }

La parte bassa sono **tre condizioni**, ciascuna con una casella da attivare e
un valore preceduto da `<=`. Valgono solo quelle attivate:

| Condizione | Cancella l'articolo se… |
|---|---|
| **Esistenza** `<=` | l'esistenza è minore o uguale al valore indicato. Mettendo `0` si prendono gli articoli finiti. |
| **Data Ultimo Acquisto** `<=` | l'ultimo acquisto è anteriore o uguale alla data indicata. |
| **Data Ultimo Vendita** `<=` | l'ultima vendita è anteriore o uguale alla data indicata. L'etichetta è scritta *Ultimo* invece di *Ultima*. |

Le tre condizioni si sommano: attivandone più d'una, l'articolo viene cancellato
solo se le soddisfa **tutte**.

### Duplica

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Articolo** | ● | L'articolo da copiare. | codice |
| **Nuovo Articolo** | ● | Il codice del nuovo articolo. Si può farlo generare al programma. | codice |

{: .campi }

### Gestione Panieri

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Paniere** | ● | Quale paniere si sta componendo. | codice |

{: .campi }

La griglia sotto elenca gli articoli del paniere, con **Codice** e
**Descrizione**.

## Pulsanti e comandi

### Attribuzione Tassonomie

| Comando | Effetto |
|---|---|
| **Nuova Tassonomia** | Crea una tassonomia. |
| **Nuovo Elemento** | Crea un elemento dentro una tassonomia. |
| **Modifica**, **Elimina** | Sulla tassonomia scelta. |
| **F5 - Cerca** | Cerca gli articoli da portare in griglia. |
| **F2 - Aggiungi** | Attribuisce la tassonomia agli articoli. |
| **Rimuovi** | Toglie la tassonomia dagli articoli. |
| **F6 - Pulisci** | Svuota la griglia. |
| **Abilita**, **Disabilita** | Abilita o disabilita gli articoli sul negozio online. |
| **Descriz.** | Modifica la descrizione pubblicata. |
| **Classifica** | Classifica gli articoli. |

### Gestione Panieri

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Aggiungi** | ++f2++ | Aggiunge articoli al paniere. |
| **F5 - Selez.** | ++f5++ | Sceglie gli articoli da aggiungere. |
| **F6 - Elimina** | ++f6++ | Toglie dal paniere l'articolo della riga. |

### Le altre maschere

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra. In **Caricamento Prezzi** salva il prezzo e passa all'articolo successivo. |
| **Esci** | ++esc++ | Chiude senza salvare. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Caricare i prezzi di una serie di articoli

1. Apri **Menu ▸ Archivi ▸ Articoli ▸ Caricamento Prezzi**.
2. Indica il primo **Articolo** e il **Listino**.
3. Guarda **Ultimo Prezzo d' Acquisto** ed **Esistenza** per decidere il
   prezzo.
4. Scrivi il prezzo e premi **F2 - Salva**.

### Duplicare un articolo

1. Apri **Menu ▸ Archivi ▸ Articoli ▸ Duplica**.
2. Indica l'**Articolo** da copiare.
3. In **Nuovo Articolo** scrivi il codice nuovo, oppure rispondi **Sì** a
   *«Vuoi generare il codice?»* per farlo assegnare al programma.
4. Alla conferma *«Articolo duplicato!»* apri il nuovo articolo e correggi
   quello che lo distingue dall'originale.

### Cancellare gli articoli che non servono più

1. **Fai una copia di sicurezza degli archivi.**
2. Apri **Menu ▸ Archivi ▸ Articoli ▸ Cancellazione Articoli**.
3. Restringi la selezione con i filtri.
4. Attiva le condizioni che servono: per esempio **Esistenza** `<= 0` e **Data
   Ultimo Vendita** `<=` di due anni fa, per togliere quello che è finito e non
   si vende più.
5. Premi **F2 - OK** e rispondi **Sì** a *«Confermi la Cancellazione degli
   Articoli Selezionati ?»*, poi ancora **Sì** a *«Sei Sicuro ?»*.

### Comporre un paniere per la vendita touchscreen

1. Apri **Menu ▸ Archivi ▸ Articoli ▸ Gestione Panieri**.
2. Indica il **Paniere**: è un codice della tabella dei panieri, fra le
   [tabelle di classificazione](../magazzino/tabelle-di-classificazione.md).
3. Premi **F5 - Selez.** per scegliere gli articoli, poi **F2 - Aggiungi**.
4. Alla [vendita touchscreen](../vendite/vendita-al-banco.md), un tasto
   collegato a quel paniere apre l'elenco dei suoi articoli invece di
   richiamarne uno solo.

### Preparare gli articoli per il negozio online

1. Apri **Attribuzione Tassonomie**: con **F5 - Cerca** porti in griglia gli
   articoli, con **F2 - Aggiungi** attribuisci la tassonomia a tutti insieme,
   con **Abilita** li rendi visibili sul sito.
2. Poi, articolo per articolo, cura nomi, descrizioni e immagini da
   [Impostazione dati web](impostazione-dati-web.md).

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Vuoi generare il codice?* | In **Duplica**, il codice del nuovo articolo non è stato scritto. | **Sì** lo fa assegnare al programma, secondo il formato impostato nelle [ditte](ditte.md). |
| *Articolo duplicato!* | La duplicazione è andata a buon fine. | Nulla: è una conferma. |
| *Confermi la Cancellazione degli Articoli Selezionati ?* | Prima conferma della cancellazione in blocco. | **Sì** prosegue alla seconda domanda. |
| *Sei Sicuro ?* | Seconda conferma della cancellazione. | **Sì** cancella davvero. Non si torna indietro. |
| *Colonna CODICE non trovata nel file excel!<br>Impossibile continuare* | Il foglio da importare nella griglia non ha la colonna attesa. | Correggi le intestazioni del foglio. |
| *Impossibile inizializzare il file excel!* / *Impossibile aprire il file excel!* | L'importazione o l'esportazione non è riuscita. | Controlla che il file non sia già aperto e che la cartella sia scrivibile. |
| *Non è possibile selezionare le tassonomie !* | La selezione richiesta non è ammessa. | Scegli una tassonomia sola, o un elemento. |
| *Vuoi attribuire la tassonomia a tutti gli articoli nella tabella ?* | Si sta attribuendo una tassonomia senza aver scelto righe. | **Sì** la dà a tutti gli articoli in griglia. |

## Note

!!! warning "La cancellazione in blocco non si annulla"

    Chiede due conferme proprio perché è definitiva: senza una copia di
    sicurezza gli articoli cancellati e la loro storia non si recuperano.

!!! warning "Le tre condizioni si sommano"

    Attivandone più d'una, l'articolo viene cancellato solo se le soddisfa
    **tutte**. Attivandone una sola — per esempio la data di ultima vendita —
    finiscono nel mucchio anche articoli con esistenza a magazzino. Controlla
    prima con la [stampa degli articoli invenduti](stampe-articoli.md).

!!! note "Cosa copia la duplicazione, e cosa no"

    **Copia**: tutti i dati anagrafici e di classificazione, e i
    [listini di vendita](../listini-vendita/gestione-listini.md) dell'articolo.

    **Azzera**: le date di ultimo acquisto e ultima vendita, la data di
    creazione, la data di inventario, quelle di primo acquisto e prima vendita,
    gli ultimi ordini a cliente e a fornitore, gli ultimi prezzi d'acquisto, gli
    otto sconti d'acquisto e il collegamento al negozio online.

    **Non copia**: codici a barre aggiuntivi, scorte, ubicazioni, assortimento e
    listini fornitori. Vanno rifatti sull'articolo nuovo.

!!! note "Le tassonomie non sono la classificazione di magazzino"

    Reparto, categoria merceologica e marchio servono al magazzino e alle
    statistiche; le **tassonomie** servono al catalogo del sito e possono
    raggruppare gli articoli in modo del tutto diverso. Un articolo può avere
    più tassonomie: la colonna **N. Taxons** dice quante.

<!-- DA VERIFICARE: cosa fa esattamente il pulsante "Classifica" dell'attribuzione tassonomie. -->

## Vedi anche

- [Anagrafica articoli](anagrafica-articoli.md)
- [Modifica articoli da griglia](modifica-da-griglia.md)
- [Impostazione dati web degli articoli](impostazione-dati-web.md)
- [Scorte, assortimento e ubicazioni](scorte-e-assortimento.md)
- [Gestione listini](../listini-vendita/gestione-listini.md)
- [Vendita e POS touchscreen](../vendite/vendita-al-banco.md)
- [Ditte](ditte.md)
