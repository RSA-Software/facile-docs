---
title: Ordini clienti
description: Le voci proprie degli ordini dei clienti — le tre stampe di riepilogo e la cancellazione degli ordini evasi.
modulo: Vendite
maschera_id: nessuna dialog propria
---

# Ordini clienti

L'ordine del cliente si registra come gli altri
[documenti di vendita](documento-di-vendita.md) e si consulta dalla
[gestione documenti](gestione-documenti.md). Questa pagina copre le voci che
appartengono solo agli ordini: le stampe di riepilogo e la pulizia degli ordini
già evasi.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Vendite ▸ Ordini Clienti ▸ Stampa Riepilogo *(oppure* Stampa Ordini per Cliente*,* Stampa Ordini per Articolo *o* Cancellazione Ordini Evasi*)*
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md); **Cancellazione Ordini Evasi** richiede in più che l'utente non abbia il **Blocco Cancellazioni Dati**

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Stampa Riepilogo** | L'elenco degli ordini di un periodo. |
| **Stampa Ordini per Cliente** | Gli ordini raggruppati per cliente: cosa deve ancora ricevere ciascuno. |
| **Stampa Ordini per Articolo** | Gli ordini raggruppati per articolo: quanto è impegnato di ogni cosa. È la stampa da cui si decide cosa ordinare al fornitore. |
| **Cancellazione Ordini Evasi** | Toglie dall'archivio gli ordini completamente evasi di un periodo che scegli tu, per non trascinarseli dietro. |

Le altre voci del sottomenu — **Gestione**, **Inserimento**, **Modifica**,
**Duplica** e **Fatturazione da Ordini** — sono descritte in
[Gestione documenti](gestione-documenti.md),
[Documento di vendita](documento-di-vendita.md),
[Esportazione e duplicazione](esporta-duplica-documenti.md) e
[Emissione fatture da documenti](emissione-fatture-da-documenti.md).

!!! note "Le stesse voci, più complete, sotto il menu Ordini"

    Questo sottomenu è la versione ridotta di **Ordini ▸ Ordini da Clienti**,
    che ha le stesse voci più tutte le altre. I campi delle tre stampe sono
    descritti per esteso in [Stampe degli ordini](../ordini/stampe-ordini.md).

## Prerequisiti

Prima di usare queste stampe occorre avere registrato gli ordini.

Prima della cancellazione occorre **una copia di sicurezza recente degli
archivi**: non c'è modo di tornare indietro.

## La maschera

![Stampa ordini](../../assets/img/vendite/ordini-clienti.png)

Le tre stampe sono finestre di selezione con gli intervalli e i filtri, e i
pulsanti **F2 - OK** ed **Esci**. **Cancellazione Ordini Evasi** apre invece
una finestra piccola, con le sole **Data Iniziale** e **Data Finale** del
periodo da ripulire e gli stessi due pulsanti.

## Campi

I campi delle tre stampe sono quelli descritti in
[Stampe degli ordini](../ordini/stampe-ordini.md): intervalli di cliente,
articolo e data, la zona, il deposito, il registro e la casella **Includi
Ordini Totalmente Evasi**.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia la stampa. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |

## Come si fa

### Sapere cosa ordinare al fornitore

1. Apri **Menu ▸ Vendite ▸ Ordini Clienti ▸ Stampa Ordini per Articolo**.
2. Indica il periodo e premi **F2 - OK**.
3. Confronta le quantità impegnate con le esistenze: la differenza è quello che
   manca.

### Vedere cosa deve ancora ricevere un cliente

1. Apri **Menu ▸ Vendite ▸ Ordini Clienti ▸ Stampa Ordini per Cliente**.
2. Indica il **Cliente** e stampa.

### Ripulire gli ordini chiusi

1. **Fai una copia di sicurezza degli archivi.**
2. Stampa prima il **Riepilogo**, per avere traccia di cosa stai per togliere.
3. Apri **Menu ▸ Vendite ▸ Ordini Clienti ▸ Cancellazione Ordini Evasi**.
4. Indica **Data Iniziale** e **Data Finale**. All'apertura sono tutte e due
   quella di oggi: il periodo va allargato a mano.
5. Premi **F2 - OK**.
6. Leggi il messaggio, che dice **quanti** ordini sta per cancellare e in che
   periodo. Se il numero non è quello che ti aspettavi, rispondi **No** e
   ricontrolla le date.
7. Rispondi **Sì**. Alla fine Facile dice quanti documenti ha cancellato.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Verranno cancellati definitivamente … ordini evasi con data fra il … e il …, insieme alle loro righe. L' operazione non si può annullare. Vuoi continuare ?* | La conferma della cancellazione, con il numero dei documenti trovati. | Controlla il numero e il periodo. **Sì** cancella; la risposta preimpostata è **No**. |
| *Nessun ordine evaso con data fra il … e il …* | Nel periodo indicato non c'è niente da cancellare. | Allarga il periodo, o non c'era nulla da ripulire. |
| *Cancellati … documenti.* | La cancellazione è finita. | Nulla: è il resoconto. |
| *Cancellazione interrotta: … documenti su …* | Hai premuto **Annulla** sulla barra di avanzamento. | I documenti già cancellati non tornano: ripeti pure la procedura per togliere i rimanenti. |
| *Cancellazioni non abilitate per l' utente !* | L'utente ha il **Blocco Cancellazioni Dati**. | Serve un utente abilitato, o va tolto il blocco da [Archivi ▸ Utenti](../anagrafiche/utenti.md). |
| *La data è esterna all' esercizio corrente.* | Una delle due date non appartiene all'esercizio aperto. | Correggila: gli ordini degli altri esercizi stanno in archivi separati. |
| *(nessun messaggio, solo un segnale acustico)* | Un campo del filtro non è valido. | Guarda dove si è posizionato il cursore. |

## Note

!!! warning "La cancellazione degli ordini evasi è definitiva"

    Gli ordini cancellati spariscono dall'archivio con le loro righe e la loro
    storia. Stampa il riepilogo prima, e fai una copia degli archivi.

!!! note "Quali ordini entrano nel periodo"

    Conta la **data del documento**, cioè quella con cui l'ordine è stato
    registrato, non quella in cui è stato evaso: la data di evasione non è
    scritta sulla testata dell'ordine.

    Un ordine è *evaso* quando ogni sua riga è stata consegnata per intero;
    quelli evasi solo in parte restano dove sono. Il periodo non può uscire
    dall'esercizio aperto: gli ordini degli esercizi precedenti stanno in
    archivi separati e si ripuliscono entrando in quell'esercizio.

!!! note "Chi non può cancellare non può nemmeno da qui"

    Se l'utente ha il **Blocco Cancellazioni Dati** in
    [Archivi ▸ Utenti](../anagrafiche/utenti.md), la voce risponde
    *Cancellazioni non abilitate per l' utente !* e non apre nemmeno la finestra
    del periodo. Vale la stessa regola delle cancellazioni una per una.

## Vedi anche

- [Documento di vendita](documento-di-vendita.md)
- [Gestione documenti](gestione-documenti.md)
- [Emissione fatture da documenti](emissione-fatture-da-documenti.md)
- [Stampe degli ordini](../ordini/stampe-ordini.md)
- [Ordini in lavorazione e in ricezione](../ordini/ordini-in-lavorazione-e-ricezione.md)
