---
title: Fatture elettroniche attive
description: L'invio massivo delle fatture elettroniche emesse e il cruscotto da cui se ne segue lo stato.
modulo: Vendite
maschera_id: IDD_VEN_FATTURE_INVIO, IDD_VEN_CRUSCOTTO_FATTURE_PA
---

# Fatture elettroniche attive

Le fatture emesse vanno trasmesse per via elettronica e il loro esito va
seguito. **Invio Massivo** le manda in blocco, il **Cruscotto** mostra a che
punto sono.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Vendite ▸ Fatture ▸ Invio Massivo Fatture Elettroniche
        - Menu ▸ Vendite ▸ Fatture ▸ Cruscotto Fatture Elettroniche
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md); serve anche **Abilita download Stati Fatture Attive** sull'utente

---

## A cosa serve

**Invio Massivo Fatture Elettroniche** prende le fatture emesse e non ancora
trasmesse e le manda tutte insieme, invece di una per volta dal documento.

**Cruscotto Fatture Elettroniche** è il quadro degli esiti: quali sono partite,
quali sono state accettate, quali scartate e vanno rifatte.

## Prerequisiti

Prima di usare queste maschere occorre:

- avere emesso le [fatture](documento-di-vendita.md) con il **Tipo Documento**
  giusto;
- avere i dati fiscali dei clienti completi, compreso il codice destinatario o
  la PEC;
- avere **credito** sul servizio di trasmissione;
- avere l'utente abilitato al download degli stati.

## La maschera

![Cruscotto fatture elettroniche](../../assets/img/vendite/fatture-elettroniche-attive.png)

Sono due finestre a griglia: l'elenco dei documenti con il loro stato, e i
comandi per mandarli e per aggiornare gli esiti.

Sono **due finestre diverse**, una per mandare e una per seguire.

**Invio Fatture Emesse** ha in alto i filtri, e sotto una griglia con le
fatture da mandare: si spuntano quelle che interessano e si preme *Invio*.

**Cruscotto Fatture PA** ha in alto i filtri e sotto **due griglie**: quella
grande con le fatture — numero, data, cliente, partita IVA, totale e stato —
e sotto, per la fattura selezionata, quella degli **esiti**: un'icona, la data,
l'ora, lo **Stato** e il **Messaggio**. Gli esiti cambiano scorrendo le righe
della griglia di sopra.

## Campi

### Invio Fatture Emesse

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | | Il periodo delle fatture da elencare. | date |
| **Cliente** | | Restringe a un cliente. | codice |
| **Visualizza documenti già inviati** | | Mostra anche quelle già trasmesse, che di norma spariscono dall'elenco. | attivo/non attivo |

### Cruscotto Fatture PA

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | | Il periodo. | date |
| **Filtra** | | Restringe l'elenco a quelle andate male. | `TUTTE`, `SCARTATE DIGITHUB`, `SCARTATE SDI` |

!!! tip "I due scarti non sono la stessa cosa"

    **SCARTATE DIGITHUB** sono quelle fermate dall'intermediario prima di
    partire; **SCARTATE SDI** quelle partite e respinte dal Sistema di
    Interscambio. Le prime si correggono e si rimandano subito; le seconde
    hanno un esito ufficiale da leggere.

Non applicabile.

## Pulsanti e comandi

### Invio Fatture Emesse

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **Selez. Tutti**, **Deselez. Tutti** | | Spunta o toglie la spunta a tutte le righe. |
| **F2 - Invio** | ++f2++ | Manda le fatture spuntate. |
| **F3 - Esporta** | ++f3++ | Salva il documento in XML. |
| **F4 - Modifica Doc.** | ++f4++ | Apre il documento selezionato. |
| **F5 - Modifica Cliente** | ++f5++ | Apre il cliente del documento, per correggerne i dati. |
| **F6 - Email** | ++f6++ | Manda la fattura per email. |
| **F7 - Trova** | ++f7++ | Cerca nella griglia. |

### Cruscotto Fatture PA

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Sincronizza** | ++f2++ | Scarica gli stati aggiornati. **Non c'è sempre**: vedi la nota qui sotto. |
| **F3 - Credito Residuo** | ++f3++ | Calcola quante trasmissioni restano. |
| **F4 - Esporta** | ++f4++ | Esporta in XML. |
| **F5 - Trova** | ++f5++ | Cerca nella griglia. |
| **F6 - https://fatture.facilecloud.net** | ++f6++ | Apre il portale nel browser. Compare solo se il codice cliente per le fatture PA è impostato sulla ditta. |
| doppio clic su una riga degli esiti | | Se l'esito ha un allegato, propone di salvarlo: parte dalla cartella `out` dell'utente. |

Non applicabile.

## Come si fa

### Trasmettere le fatture del giorno

1. Emetti e controlla le fatture dalla
   [gestione documenti](gestione-documenti.md).
2. Apri **Menu ▸ Vendite ▸ Fatture ▸ Invio Massivo Fatture Elettroniche**.
3. Avvia l'invio.
4. Il giorno dopo apri il **Cruscotto** e controlla gli esiti.

### Rimediare a una fattura scartata

1. Nel **Cruscotto** individua il documento scartato e leggi il motivo.
2. Correggi il documento o l'anagrafica del cliente.
3. Rimanda il documento, dalla gestione documenti con **F8 - Forza Invio**
   oppure con un nuovo invio massivo.

## Controlli e messaggi

| Messaggio | Dove | Causa | Cosa fare |
|---|---|---|---|
| *Nessuna Fattura è stata selezionata per l'invio dell'Email!* | Invio | Nessuna riga spuntata. | Spuntare le fatture. |
| *Impossibile trovare il documento in archivio!* | Invio | Il documento della riga non c'è più. | Ricaricare l'elenco. |
| *Impossibile trovare il cliente in archivio!* | Invio | Il cliente è stato cancellato. | Sistemare l'anagrafica. |
| *Registro Fatture PA non impostato sulla Ditta!* — e le gemelle su causale contabile, sezione e note di credito | Invio | Mancano le impostazioni fiscali per le fatture PA, o quelle del documento non coincidono. | Rispondere **No** e sistemare [Ditte](../anagrafiche/ditte.md); continuare manda un documento che può essere scartato. |
| *Continuando l'operazione imposterai questo computer come l'unico abilitato alla sincronizzazione degli stati.* | Cruscotto | Prima sincronizzazione. | Rispondere **Sì** solo dal computer che deve farlo sempre. |
| *Credito Esaurito!* | Cruscotto | Finite le trasmissioni disponibili. | Acquistare credito. |
| *Errore di comunicazione! Impossibile contattare l'Authorization Server.* | Cruscotto | Rete o servizio non raggiungibile. | Attendere qualche minuto e riprovare. |
| *Partita Iva Ditta non impostata!* / *Codice Abilitazione Invio Fatture Elettroniche non impostato!* | Cruscotto | Manca un dato sulla ditta. | Compilarlo in [Ditte](../anagrafiche/ditte.md). |
| *Esportazione Conclusa!* | entrambe | L'XML è stato scritto. | — |

Non applicabile.

## Note

!!! note "Lo stato si vede anche nella gestione documenti"

    La colonna **Sync** della [gestione documenti](gestione-documenti.md) dice
    se il documento è stato preso in carico, e **F8 - Forza Invio** lo rimanda.
    Il cruscotto serve quando si vuole il quadro d'insieme.

!!! warning "Gli esiti non arrivano da soli, e non da tutti i computer"

    Il cruscotto **non scarica niente all'apertura**: mostra quello che c'è in
    archivio. Per aggiornarlo si preme **F2 - Sincronizza**.

    E quel pulsante **non compare dappertutto**. Servono due cose insieme:

    - sull'utente dev'essere acceso **Abilita download Stati Fatture Attive**;
    - il computer dev'essere **quello designato** sulla ditta — oppure non
      dev'essercene ancora nessuno.

    La designazione avviene alla prima sincronizzazione, e il programma lo dice
    chiaramente prima di farlo. **Da quel momento gli altri computer vedono il
    cruscotto ma non il pulsante**: se gli stati sembrano fermi, la domanda da
    farsi è se qualcuno abbia sincronizzato dal computer giusto.

!!! tip "Il motivo dello scarto sta nella griglia di sotto"

    Selezionando la fattura nella griglia grande, quella in basso mostra la sua
    storia: una riga per esito, con **Stato** e **Messaggio**. Il motivo dello
    scarto è il testo della colonna **Messaggio** dell'ultimo esito.

    Se l'esito ha un allegato — la ricevuta ufficiale — il **doppio clic** sulla
    riga propone di salvarlo, partendo dalla cartella `out` dell'utente.

## Vedi anche

- [Gestione documenti](gestione-documenti.md)
- [Documento di vendita](documento-di-vendita.md)
- [Fatture elettroniche passive](../contabilita/fatture-elettroniche-passive.md)
