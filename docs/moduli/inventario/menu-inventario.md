---
title: Inventario
description: Il menu Inventario di Facile — acquisizione delle letture, stampe di controllo, chiusura e azzeramenti.
---

# Inventario

Il menu **Inventario** serve a rimettere d'accordo il magazzino di carta con il
magazzino vero. Si conta quello che c'è, si confronta con quello che Facile
credeva di avere, e la differenza diventa un movimento di rettifica.

Tutte le voci di questo menu lavorano **solo sull'anno corrente**: se stai
consultando un anno precedente, ti fermano con un messaggio.

## Il giro dell'inventario

- [Acquisizione delle letture](acquisizione-letture.md) — le quantità contate
  entrano a mano, dal terminalino, da un carico merci o da un foglio Excel; e
  da qui si correggono.
- [Stampe dell'inventario](stampe-inventario.md) — dati acquisiti, tabulato
  delle rettifiche, articoli inventariati e non inventariati.
- [Chiusura dell'inventario](chiusura-inventario.md) — le letture diventano
  esistenze; e gli azzeramenti che la precedono e la seguono.

!!! tip "L'ordine dei passi"

    1. **Azzeramento Letture**, per ripartire pulito.
    2. Si conta, e le quantità entrano con l'[acquisizione](acquisizione-letture.md).
    3. **Stampa Dati Acquisiti**: la prova di quello che è stato contato.
    4. **Stampa Articoli non Inventariati**: cosa è rimasto fuori. Si torna a
       contare, oppure si decide di lasciarlo com'è.
    5. **Stampa Tabulato Rettifiche**: quello che la chiusura sta per scrivere.
       È il documento da leggere con attenzione.
    6. Copia di sicurezza degli archivi.
    7. **[Chiusura Inventario](chiusura-inventario.md)**.

!!! warning "Prima di chiudere, la causale"

    La chiusura si rifiuta di partire se la causale di magazzino per
    l'inventario non è impostata bene nei
    [parametri della ditta](../anagrafiche/ditte.md) — verso dell'esistenza
    coerente con il tipo di movimento, e flag *Aggiorna Data Inventario*
    attivo. È il controllo che ferma più spesso chi chiude per la prima volta:
    i messaggi sono spiegati in [Chiusura dell'inventario](chiusura-inventario.md).

!!! note "L'inventario non è la valorizzazione"

    Qui si sistemano le **quantità**. Quanto vale il magazzino dopo averle
    sistemate lo dice la stampa del valore, fra le
    [stampe dei movimenti](../magazzino/stampe-movimenti-magazzino.md).
