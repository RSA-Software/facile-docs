---
title: Acconti
description: La registrazione delle caparre versate dai clienti, la ricevuta che ne esce e il riepilogo di controllo.
modulo: Vendite
maschera_id: IDD_LAD_ACCONTI
---

# Acconti

**Solo Taglie e Colori.** Registra le somme versate dal cliente prima della
consegna e stampa la ricevuta da consegnargli.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Vendite ▸ Acconti ▸ Inserimento *(oppure* Modifica *o* Stampa*)*
    - **Scorciatoia:** ++f2++ salva, ++f5++ cerca, ++f7++ ristampa la ricevuta
    - **Versione:** **solo Taglie e Colori.** Nelle altre versioni le tre voci restano nel menu ma non aprono nulla
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Il cliente lascia una caparra all'ordine: la si registra qui e il programma
stampa subito la ricevuta da dargli. La voce **Stampa** produce il riepilogo
degli acconti di un periodo o di un cliente.

L'acconto resta un **promemoria a sé stante**: non entra in nessun documento e
non genera nessuna scrittura contabile — vedi la nota in fondo.

## Prerequisiti

Prima di usare questa maschera occorre avere in archivio i
[clienti](../anagrafiche/anagrafica-clienti.md), e — per la ricevuta — aver
impostato la **Stampante Testo**.

## La maschera

![Acconti](../../assets/img/vendite/acconti.png)

È una maschera a finestra unica con quattro campi. La stampa apre una
finestrella con gli intervalli di selezione.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Codice** | ● | Identificativo dell'acconto. In inserimento il programma propone il primo numero libero, ma si può cambiare; in modifica non si tocca. | numero |
| **Data** | ● | Quando l'acconto è stato versato. Proposta la data di oggi. | data |
| **Importo** | | Quanto è stato versato. | importo |
| **Cliente** | ● | Chi ha versato. Accanto compare la ragione sociale, che non si modifica. | codice |

{: .campi }

Nella stampa si indicano **Da Codice** e **A Codice**, **Da Data** e **A
Data**, e il **Cliente**. I quattro estremi arrivano già compilati con il primo
e l'ultimo codice e la prima e l'ultima data presenti in archivio; il
**Cliente** è a zero e accanto si legge `TUTTI`.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra l'acconto. In inserimento stampa anche la ricevuta. |
| **F3 - Prec.**, **F4 - Succ.** | ++f3++, ++f4++ | Passano all'acconto precedente o successivo. |
| **F5 - Cerca** | ++f5++ | Apre l'elenco degli acconti. |
| **F6 - Elimina** | ++f6++ | Cancella l'acconto, previa conferma. |
| **F7 - Stampa** | ++f7++ | Ristampa la ricevuta. Compare **solo in modifica**. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo **Cliente**, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Registrare una caparra

1. Apri **Menu ▸ Vendite ▸ Acconti ▸ Inserimento**.
2. Il **Codice** e la **Data** arrivano già proposti: correggili se serve.
3. Scrivi l'**Importo** e indica il **Cliente** con ++f10++.
4. Premi **F2 - Salva**. La ricevuta esce dalla stampante testo e la maschera
   si azzera, pronta per l'acconto seguente.

### Ristampare una ricevuta

1. Apri **Menu ▸ Vendite ▸ Acconti ▸ Modifica** e carica l'acconto con
   **F5 - Cerca**.
2. Premi **F7 - Stampa**.

### Controllare gli acconti di un cliente

1. Apri **Menu ▸ Vendite ▸ Acconti ▸ Stampa**.
2. Indica il **Cliente** e, se serve, restringi il periodo.
3. Premi **F2 - OK**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca il **Codice**, la **Data** o il **Cliente**; oppure, nella stampa, un estremo è maggiore di quello finale. | Compila o correggi il campo su cui si è posizionato il cursore. |
| *Stampante Testo non impostata !* | Non è stata scelta la stampante testo su cui esce la ricevuta. | Impostala nelle preferenze del programma, poi ripeti. |
| *Impossibile aprire la stampa!* | La stampante testo è impostata ma non risponde. | Verifica che sia accesa e collegata. |
| *In archivio è già presente un record con lo stesso codice.* | Il **Codice** digitato è già di un altro acconto. | Cambia codice. |

## Note

!!! warning "L'acconto non viene scalato da nessuna parte"

    Registrarlo qui non lo fa comparire nel
    [documento di vendita](documento-di-vendita.md), non apre una partita e non
    produce nessuna registrazione di
    [prima nota](../contabilita/registrazione-prima-nota.md). Nessun'altra
    maschera del programma legge questo archivio.

    Quando si emette il documento definitivo, la caparra va scalata **a mano**:
    per esempio con una riga di sconto o un abbuono in piede.

!!! note "Cosa c'è sulla ricevuta"

    Una ricevuta stretta, 40 colonne, sulla **stampante testo**: in alto i dati
    della [ditta](../anagrafiche/ditte.md) — denominazione, indirizzo, CAP,
    città, provincia, partita IVA e telefono se c'è — poi la parola `ACCONTO`
    con l'importo a destra, la data, `ACCONTO NUM. n`, una riga di trattini e
    uno spazio in bianco per la firma.

    Il **nome del cliente non compare**: la ricevuta dice solo quanto è stato
    versato e con che numero.

!!! note "Il salvataggio stampa da sé"

    In **inserimento** il **F2 - Salva** stampa la ricevuta senza chiedere
    niente. Se la stampante testo non è pronta, l'acconto **resta registrato lo
    stesso**: il messaggio riguarda solo la stampa, e la ricevuta si recupera
    poi da **Modifica** con **F7 - Stampa**.

!!! note "Un cliente con acconti non si cancella"

    Finché resta anche un solo acconto intestato a un cliente,
    l'[anagrafica clienti](../anagrafiche/anagrafica-clienti.md) rifiuta di
    eliminarlo.

!!! note "Che cosa stampa la voce Stampa"

    Il riepilogo *Riepilogo Acconti*: l'elenco degli acconti del periodo,
    ordinato per codice e data, con l'intestazione della ditta.

    Non c'è nessuna nozione di acconto «aperto» o «utilizzato» — l'archivio non
    registra se una caparra sia stata poi impiegata. Il riepilogo elenca tutto
    quello che rientra nei filtri.

## Vedi anche

- [Documento di vendita](documento-di-vendita.md)
- [Anagrafica clienti](../anagrafiche/anagrafica-clienti.md)
