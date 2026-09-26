---
title: Chiusura della vendita
description: La chiusura giornaliera della vendita nel modulo Ortofrutta, le stampe che produce e come annullarla.
modulo: Ortofrutta
maschera_id: IDD_ORT_CHIUSURA_VENDITA
---

# Chiusura della vendita

A fine giornata si **chiude la vendita**: Facile stampa il quadro del giorno,
segna le partite che si sono esaurite e registra la data. È l'operazione che
scandisce il lavoro del modulo, e va fatta **tutti i giorni**.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Ortofrutta ▸ Chiusura Vendita
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Si annulla:** sì, ma solo l'ultima — vedi in fondo

---

## La maschera

| Campo | Descrizione |
|---|---|
| **Ultima Chiusura** | La data dell'ultima chiusura fatta. Non si scrive: la mostra il programma. |
| **Data Chiusura** | Il giorno da chiudere. |
| **Stampa** | Cinque caselle: **Cassa**, **Banca**, **Saldi Clienti**, **Saldi Fornitori**, **Partite Chiuse**. |
| **Formato Stampa Partite Chiuse** | `SINTETICO` o `DETTAGLIATO`, per l'ultima delle cinque. |
| **Partita**, **Fornitore** | Restringono la stampa delle partite chiuse a una sola partita o a un solo produttore. |

Sotto, la griglia mostra le partite interessate dalla chiusura.

## Che cosa fa, nell'ordine

1. **Ripulisce** la data scelta da una eventuale chiusura precedente dello
   stesso giorno, così rifarla non raddoppia niente.
2. Stampa il **bilancino** — è l'unica stampa che fa sempre, senza casella.
3. Stampa, se le caselle sono spuntate, **movimenti di cassa**, **movimenti di
   banca**, **saldi clienti**, **saldi fornitori** e **partite chiuse**.
4. Registra la data come **ultima chiusura eseguita**.

Alla fine dice *Operazioni di chiusura eseguite con successo !*. Se qualcosa si
è fermato per strada, *Operazioni di chiusura interrotte !* — e in quel caso la
data **non** viene registrata: la chiusura è da rifare.

!!! warning "Le chiusure si fanno in fila, giorno per giorno"

    Prima di partire Facile controlla che **fra l'ultima chiusura e il giorno
    scelto non ci siano movimenti**. Se ce ne sono, si ferma:

    *Nei giorni trascorsi dall' ultima chiusura ci sono movimenti ! Devono
    essere eseguite le chiusure dei giorni precedenti.*

    Non è un capriccio: le stampe di chiusura sono la storia della giornata, e
    saltarne una lascerebbe un giorno senza quadratura. Si recuperano
    chiudendo i giorni arretrati uno alla volta, in ordine.

!!! note "Lo sbilancio non blocca, ma avvisa"

    Se il bilancino non torna, Facile chiede:

    *E' stato rilevato uno sbilancio ! Vuoi mostrare l' anteprima ed
    interrompere l' elaborazione ?*

    Rispondendo **Sì** si vede l'anteprima e la chiusura si ferma, così si può
    cercare l'errore prima di andare avanti. Rispondendo **No** la chiusura
    prosegue e lo sbilancio resta — segnalato sulla stampa, ma resta.

## Annulla Ultima Chiusura

Rimette le cose come stavano prima dell'ultima chiusura: le partite tornano
aperte e la data di fine vendita viene tolta.

Chiede due conferme, entrambe con **No** già selezionato:

> *Vuoi annullare la chiusura del 19/09/2026 ?*
>
> *Confermi l' annullamento della chiusura ?*

La data nella prima domanda è quella dell'ultima chiusura registrata: **è
l'unica che si può annullare**. Per tornare più indietro bisogna annullare una
chiusura alla volta, a ritroso.

!!! warning "Le stampe non si annullano"

    L'annullamento tocca gli archivi, non la carta: i fogli già stampati —
    bilancino, saldi, partite chiuse — restano quelli, e dopo l'annullamento
    non corrispondono più. Conviene rifare la chiusura e buttare i fogli
    vecchi, per non ritrovarsi due versioni dello stesso giorno.

## Vedi anche

- [Partite](partite.md)
- [Esercizi, ditte e chiusure](../../utility/esercizi-e-chiusure.md)
