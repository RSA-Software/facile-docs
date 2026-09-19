---
title: Preventivi
description: La maschera dei preventivi, con oggetto, condizioni di fornitura e note, e la stampa del riepilogo.
modulo: Vendite
maschera_id: IDD_VEN_PREVENTIVI
---

# Preventivi

Il preventivo ha una maschera propria, diversa da quella degli altri
[documenti di vendita](documento-di-vendita.md): oltre alle righe di merce
porta l'oggetto e le condizioni di fornitura che sul preventivo vanno scritte.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Vendite ▸ Preventivi ▸ Inserimento *(oppure* Modifica*,* Gestione*,* Stampa Riepilogo *o* Duplica*)*
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca, ++f7++ stampa, ++f8++ corpo, ++f9++ email
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Un preventivo non è un documento fiscale: non numera sui registri, non scarica
il magazzino, non genera scadenze. Serve a mettere per iscritto un'offerta, con
le condizioni a cui vale.

Le voci **Gestione** e **Duplica** aprono le maschere comuni descritte in
[Gestione documenti](gestione-documenti.md) e
[Esportazione e duplicazione](esporta-duplica-documenti.md).

## Prerequisiti

Prima di usare questa maschera occorre avere in archivio i
[clienti](../anagrafiche/anagrafica-clienti.md) e gli
[articoli](../anagrafiche/anagrafica-articoli.md) da preventivare.

## La maschera

![Preventivi](../../assets/img/vendite/preventivi.png)

In alto i destinatari, poi il blocco delle condizioni di fornitura, in basso i
dati del documento — numero, date, sconto, sezione — e il tipo di offerta con
il suo esito. Le righe della merce stanno in una finestra a parte, che si apre
con **F8 - Corpo**.

Il titolo è *Inserimento Preventivo* o *Modifica Preventivo* secondo la voce da
cui sei entrato.

## Campi

### Destinatari e condizioni

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Intestatario** | ● | Il [cliente](../anagrafiche/anagrafica-clienti.md) a cui il preventivo è intestato. Sotto compare il suo indirizzo. | codice |
| **Destinatario** | | La destinazione, se diversa. Sotto compare il suo indirizzo. | codice |
| **All' Attenzione** | | La persona a cui il preventivo va indirizzato. | testo, 130 caratteri |
| **Oggetto** | | Di cosa tratta l'offerta. | testo, 130 caratteri |
| **Consegna** | | I tempi o le modalità di consegna offerti. | testo, 130 caratteri |
| **Imballo** | | Come la merce viene imballata e a carico di chi. | testo, 130 caratteri |
| **Resa** | | La resa concordata. | testo, 130 caratteri |
| **Garanzia** | | La garanzia offerta. | testo, 130 caratteri |
| **Note** | | Le note libere che compaiono sul preventivo. | testo, 130 caratteri |

{: .campi }

I sei campi di testo sono liberi e **partono vuoti**: il programma non propone
niente, non c'è una tabella di frasi da cui pescare e la ditta non ha un testo
predefinito. Vanno riscritti ogni volta — o, più comodamente, si duplica un
preventivo che li ha già (vedi *Come si fa*).

### Riferimenti

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Operatore** | | Chi ha preparato il preventivo. | codice |
| **Commessa** | | La [commessa](../contabilita/commesse.md) a cui il preventivo si riferisce. | codice |
| **Pagamento** | | Le condizioni di pagamento offerte. | codice |
| **Gruppo** | | Sigla libera per raggruppare i preventivi. | testo |
| **Agente** | | L'[agente](../anagrafiche/anagrafica-agenti.md) che segue l'offerta. | codice |
| **Registro** | | Il registro di numerazione. Sparisce se la ditta è impostata a registro unico. | da `A` a `Z` |

{: .campi }

### Documento

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Num. Preventivo** | ● | Numero del preventivo. | numero |
| **Data Prev.** | ● | Data del preventivo. Deve cadere nell'anno di lavoro. | data |
| **Vostra Rich.**, **Del** | | Estremi della richiesta del cliente a cui si risponde. | testo, data |
| **Data Apertura** | | Da quando l'offerta vale. | data |
| **Scadenza** | | Fino a quando l'offerta vale. Se compilata non può essere anteriore né alla **Data Prev.** né alla **Data Apertura**. | data |
| **% Sconto** | | Sconto di piede applicato a tutto il preventivo. | percentuale |
| **Sezione** | | La [sezione](../contabilita/sezioni.md) contabile. | codice |
| **Prezzi Iva Inclusa** | | I prezzi delle righe si intendono comprensivi di IVA. | attivo/non attivo |
| **Stampa Totali** | | Stampa il riepilogo dei totali in calce al preventivo. | attivo/non attivo |
| **Tipo Offerta** | | Che genere di offerta è. | `VENDITA`, `RIPARAZIONE`, `MANUTENZIONE`, `INSTALLAZIONE` |
| **Esito** | | Com'è andata. **Si mette a mano**: il programma non lo aggiorna mai da sé. | `APERTO`, `NEGATIVO`, `POSITIVO` |
| **Totale Documento** | | Il totale. Lo calcola il programma e compare solo dopo la prima stampa. | Sola lettura |

{: .campi }

Le righe della merce si compilano come nel
[documento di vendita](documento-di-vendita.md).
## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra il preventivo. |
| **F3 - Prec.**, **F4 - Succ.** | ++f3++, ++f4++ | Passano al preventivo precedente o successivo. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco dei preventivi. |
| **F6 - Elimina** | ++f6++ | Cancella il preventivo, previa conferma. |
| **F7 - Stampa** | ++f7++ | Stampa il preventivo. |
| **F8 - Corpo** | ++f8++ | Apre la finestra delle righe di merce. |
| **F9 - Email** | ++f9++ | Manda il preventivo per posta elettronica. |
| **Totali** | | Mostra i totali del documento. |
| **Anteprima** | | Anteprima di stampa, senza stampare. |
| **Allegati** | | Apre gli allegati del preventivo. |
| **Nuovo** | | Comincia un altro preventivo. Solo in inserimento. |
| **Annulla** | | Cambia lo stato del documento. Solo in modifica. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |
## Come si fa

### Preparare un preventivo

1. Apri **Menu ▸ Vendite ▸ Preventivi ▸ Inserimento**.
2. Indica l'**Intestatario** e, se serve, **All' Attenzione**.
3. Scrivi l'**Oggetto** e compila **Consegna**, **Imballo**, **Resa** e
   **Garanzia**: sono le condizioni che il cliente leggerà.
4. Indica fino a quando l'offerta vale, in **Scadenza**.
5. Premi **F8 - Corpo** e inserisci le righe della merce.
6. Premi **F2 - Salva** e poi **F7 - Stampa**.

### Rifare un preventivo cambiando poco

1. Apri **Menu ▸ Vendite ▸ Preventivi ▸ Duplica**.
2. Indica il preventivo da copiare.
3. Apri la copia e correggi quello che cambia.

### Vedere tutti i preventivi aperti

1. Apri **Menu ▸ Vendite ▸ Preventivi ▸ Stampa Riepilogo**.
2. Indica il periodo e stampa.

### Trasformare un preventivo accettato in ordine o in fattura

Si passa dalla schermata di [vendita al banco](vendita-al-banco.md), che è
l'unico punto del programma da cui le righe di un preventivo si travasano in
un altro documento.

1. Apri **Menu ▸ Vendite ▸ Vendita**.
2. Premi **F6 - Dati** e scegli **Preventivo**.
3. Scegli il preventivo: le sue righe compaiono sul banco.
4. Premi **F4 - Documenti** e scegli che documento emettere — un ordine, una
   fattura, un DDT.
5. Completa e salva il documento.

Il preventivo di partenza passa a **CONFERMATO**, o a **CONFERMATO PARZ.** se
ne hai preso solo una parte, e resta riselezionabile per il resto.

## Controlli e messaggi

I controlli di questa maschera sono silenziosi: niente messaggi, solo un
segnale acustico e il cursore che si posiziona sul campo da correggere. Sono,
nell'ordine:

- l'**Intestatario** dev'essere indicato;
- il **Num. Preventivo** non può essere zero;
- la **Data Prev.** dev'essere compilata e cadere **nell'anno di lavoro**;
- la **Scadenza**, se compilata, non può essere anteriore alla **Data
  Apertura** né alla **Data Prev.**

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Uno dei controlli qui sopra non è passato. | Compila o correggi il campo su cui si è posizionato il cursore. |

## Note

!!! note "Il preventivo non impegna nulla"

    Non numera sui registri IVA, non scarica il magazzino e non genera
    scadenze: resta un documento interno finché non lo si riprende dentro a un
    ordine o a una fattura.

!!! note "Non c'è un comando «trasforma in ordine»"

    Nella maschera del preventivo non c'è nessun pulsante che lo trasformi, e
    nemmeno nella maschera del [documento di
    vendita](documento-di-vendita.md): la strada passa dalla schermata di
    [vendita al banco](vendita-al-banco.md), dove **F6 - Dati ▸ Preventivo**
    carica le righe del preventivo e **F4 - Documenti** decide che documento
    emettere.

    Lo stesso **F6 - Dati** offre **Ordine** e **DDT Conto Vendita**: è il
    meccanismo unico con cui in Facile un documento nasce da un altro.

    La [duplicazione](esporta-duplica-documenti.md) non serve a questo: copia
    un documento dello **stesso tipo**, salvo le due voci di menu che fanno la
    fattura da una pro forma e l'ordine da una richiesta di offerta.

!!! note "Lo stato del preventivo"

    Compare in alto solo quando è diverso da *salvato*:

    | Stato | Vuol dire |
    |---|---|
    | *(nessuna scritta)* | `SALVATO`: preparato ma non ancora stampato. |
    | **STAMPATO** | È stato stampato o mandato al cliente. |
    | **CONFERMATO** | È stato ripreso per intero in un ordine o in una fattura. |
    | **CONFERMATO PARZ.** | Ne è stata ripresa solo una parte: il resto è ancora disponibile. |
    | **ANNULLATO** | È stato annullato. |
    | **ERRORE** | Errore nella trasmissione. |

!!! warning "Esito e stato sono due cose diverse, e l'Esito non si aggiorna da sé"

    Lo **stato** lo muove il programma: *STAMPATO* alla stampa, *CONFERMATO*
    quando le righe finiscono in un altro documento.

    L'**Esito** — `APERTO`, `NEGATIVO`, `POSITIVO` — lo mette **solo
    l'operatore**. Nessuna elaborazione lo tocca: un preventivo trasformato in
    fattura resta `APERTO` finché qualcuno non lo cambia a mano. Se ci si vuole
    contare per sapere quante offerte sono andate a buon fine, va tenuto
    aggiornato di persona.

!!! note "I testi vanno in maiuscolo"

    **All' Attenzione**, **Oggetto**, **Consegna**, **Imballo**, **Resa**,
    **Garanzia**, **Note** e **Gruppo** vengono registrati **tutti in
    maiuscolo**, comunque li si scriva. È il programma a convertirli al
    salvataggio: sul preventivo stampato compariranno in maiuscolo.

    Ognuno tiene al massimo **130 caratteri**: quello che eccede viene tagliato
    senza avviso.
## Vedi anche

- [Documento di vendita](documento-di-vendita.md)
- [Gestione documenti](gestione-documenti.md)
- [Ordini clienti](ordini-clienti.md)
