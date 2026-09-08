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
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Stampa Riepilogo** | L'elenco degli ordini di un periodo. |
| **Stampa Ordini per Cliente** | Gli ordini raggruppati per cliente: cosa deve ancora ricevere ciascuno. |
| **Stampa Ordini per Articolo** | Gli ordini raggruppati per articolo: quanto è impegnato di ogni cosa. È la stampa da cui si decide cosa ordinare al fornitore. |
| **Cancellazione Ordini Evasi** | Toglie dall'archivio gli ordini completamente evasi, per non trascinarseli dietro. |

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
pulsanti **F2 - OK** ed **Esci**. **Cancellazione Ordini Evasi** non ha invece
alcuna maschera: parte subito con le domande di conferma.

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
4. Rispondi **Sì** alle due domande di conferma.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Vuoi Cancellare gli Ordini Evasi ?* poi *Confermi la Cancellazione degli Ordini ?* | Hai avviato la cancellazione. | Rispondi **Sì** a entrambe solo se sei sicuro. La risposta preimpostata è **No**. |
| *(nessun messaggio, solo un segnale acustico)* | Un campo del filtro non è valido. | Guarda dove si è posizionato il cursore. |

## Note

!!! warning "La cancellazione degli ordini evasi è definitiva"

    Gli ordini cancellati spariscono dall'archivio con la loro storia. Stampa il
    riepilogo prima, e fai una copia degli archivi.

!!! note "Non si sceglie il periodo"

    **Cancellazione Ordini Evasi** non chiede nulla oltre alle due conferme:
    toglie **tutti** gli ordini in stato *evaso*, di qualunque data. Un ordine è
    evaso quando ogni sua riga è stata consegnata per intero.

## Vedi anche

- [Documento di vendita](documento-di-vendita.md)
- [Gestione documenti](gestione-documenti.md)
- [Emissione fatture da documenti](emissione-fatture-da-documenti.md)
- [Stampe degli ordini](../ordini/stampe-ordini.md)
- [Ordini in lavorazione e in ricezione](../ordini/ordini-in-lavorazione-e-ricezione.md)
