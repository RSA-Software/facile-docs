---
title: Casse e Bilance
description: Il menu Casse e Bilance di Facile — invio degli articoli, ricezione del venduto, frontalini e stampe di controllo.
---

# Casse e Bilance

Il menu **Casse e Bilance** tiene il dialogo fra Facile e le macchine che stanno
al banco. Il giro è sempre lo stesso, qualunque sia la marca:

1. **Si mandano gli articoli** — codici, descrizioni, prezzi, offerte.
2. Si vende.
3. **Si riprende il venduto**, che diventa movimento di magazzino.

Facile parla con cinque famiglie di casse e otto di bilance. Le voci di menu
cambiano nome da una all'altra, ma fanno le stesse cose.

## Le macchine

- [Casse](casse.md) — SysPC, Ditron e compatibili, Brainpos 8, Aladino EPOS,
  Custom Retail; più la gestione fidelity e le promozioni.
- [Bilance](bilance.md) — Zenith, Omega, Macchi, Bizerba, Elga, Dibal, Helmac,
  Mettler Toledo.

## Il negozio

- [Frontalini](frontalini.md) — i cartellini di scaffale con descrizione,
  prezzo e prezzo promozionale.
- [Stampe e manutenzione](stampe-casse-bilance.md) — cosa è stato mandato,
  cosa è stato scartato, cosa resta da mandare.

!!! tip "Quando il venduto non torna"

    1. **[Stampa Scarti da Ricezione](stampe-casse-bilance.md)**: i codici
       venduti che Facile non ha riconosciuto. Ogni riga è una vendita senza
       movimento di magazzino.
    2. **[Stampa Articoli Gestione Bilance](stampe-casse-bilance.md)**: due
       articoli sullo stesso bancone e PLU si mangiano a vicenda.
    3. Il [giornale di magazzino](../magazzino/stampe-movimenti-magazzino.md)
       del giorno, per vedere cosa è effettivamente entrato.

!!! warning "L'invio globale e l'azzeramento del flag vanno maneggiati con cura"

    **Invio Globale Articoli** rimanda tutto e su archivi grandi impiega molto;
    **Azzera Flag Variazioni Articoli** chiede conferma, ma se rispondi **Sì**
    lascia casse e bilance con quello che hanno finché i prezzi non cambiano di
    nuovo. Sono operazioni da fare sapendo perché.

!!! note "Facile scrive i file, il trasferimento lo fa la macchina"

    Per quasi tutte le famiglie Facile prepara i file nella cartella `out` del
    programma e legge quelli che trova in `in`; a portarli alla cassa o alla
    bilancia è il programma del fornitore, richiamato dai file di comando
    installati a parte. Se il trasferimento non avviene, il problema è quasi
    sempre lì.
