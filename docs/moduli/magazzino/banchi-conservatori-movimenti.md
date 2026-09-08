---
title: Movimenti dei banchi conservatori
description: Consegne, ritiri e rottamazioni delle attrezzature date in comodato, con la modifica e la stampa dei movimenti.
modulo: Magazzino
maschera_id: IDD_MAG_BANCHI_CONSEGNA
---

# Movimenti dei banchi conservatori

Le attrezzature registrate in
[Banchi conservatori](../anagrafiche/banchi-conservatori.md) si muovono: vanno
dal cliente, tornano, si rompono, si rottamano. Ogni movimento si registra qui,
e le cinque voci di consegna aprono **la stessa maschera** con un verso diverso.

!!! info "In sintesi"

    **Percorso:** Menu ▸ Magazzino ▸ Banchi Conservatori ▸ Consegna in Comodato Gratuito *(oppure* Consegna in Conto Vendita*,* Consegna per Riparazione*,* Ritiro Comodato Gratuito / Riparazione*,* Rottamazione*,* Modifica Movimenti *o* Stampa Movimenti*)*
    **Scorciatoia:** ++f2++ salva, ++esc++ esce
    **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | Cosa registra |
|---|---|
| **Consegna in Comodato Gratuito** | L'attrezzatura va dal cliente, in comodato. |
| **Consegna in Conto Vendita** | Va dal cliente in conto vendita. |
| **Consegna per Riparazione** | Esce per essere riparata. |
| **Ritiro Comodato Gratuito / Riparazione** | Torna indietro. |
| **Rottamazione** | Esce definitivamente perché rottamata. |
| **Modifica Movimenti** | Corregge un movimento già registrato. |
| **Stampa Movimenti** | Stampa i movimenti di un periodo. |

## Prerequisiti

Prima di registrare un movimento occorre:

- avere l'attrezzatura registrata in
  [Banchi conservatori](../anagrafiche/banchi-conservatori.md);
- avere in archivio il [cliente](../anagrafiche/anagrafica-clienti.md) presso
  cui va.

## La maschera

![Consegna banchi conservatori](../../assets/img/magazzino/banchi-conservatori-movimenti.png)

Una finestra sola per tutte e cinque le consegne: chi riceve, con quale
documento, e a che titolo.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Cliente** | ● | Il [cliente](../anagrafiche/anagrafica-clienti.md) presso cui l'attrezzatura va o da cui torna. | codice |
| **Destinazione** | | La destinazione merce del cliente. | codice |
| **Num. D.D.T.**, **Data. D.D.T.** | | Gli estremi del documento di trasporto che accompagna l'attrezzatura. | numero e data |
| **Registro** | | Il registro del documento. | voce dell'elenco |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra il movimento e aggiorna lo stato dell'attrezzatura. |
| **Esci** | ++esc++ | Chiude senza salvare. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |

## Come si fa

### Consegnare un frigorifero a un cliente

1. Apri **Menu ▸ Magazzino ▸ Banchi Conservatori ▸ Consegna in Comodato
   Gratuito**.
2. Indica il **Cliente** e la **Destinazione**.
3. Compila gli estremi del **D.D.T.** con cui l'attrezzatura viaggia.
4. Premi **F2 - Salva**.

### Ritirare un'attrezzatura

1. Apri **Ritiro Comodato Gratuito / Riparazione**.
2. Indica il cliente da cui l'attrezzatura torna e il documento di rientro.
3. Salva, poi aggiorna lo **Stato** nella
  [scheda dell'attrezzatura](../anagrafiche/banchi-conservatori.md).

### Controllare cosa è in giro

Apri **Stampa Movimenti** e stampa il periodo: la stampa dice cosa è uscito e
cosa è tornato.

## Controlli e messaggi

<!-- DA VERIFICARE: i messaggi di queste maschere. -->

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca un campo obbligatorio. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! note "Cinque voci, una maschera"

    Le cinque voci di consegna e ritiro aprono la stessa finestra: cambia il
    tipo di movimento registrato, non i campi da compilare. Il titolo della
    finestra e la voce da cui si è entrati sono l'unico modo per sapere cosa si
    sta registrando.

<!-- DA VERIFICARE: se il movimento aggiorni da solo lo Stato e il Cliente nella scheda dell'attrezzatura. -->

<!-- DA VERIFICARE: se la consegna generi un documento di trasporto vero o richieda solo di annotarne gli estremi. -->

<!-- DA VERIFICARE: come si sceglie quale attrezzatura consegnare: il campo non compare fra le etichette che ho potuto estrarre. -->

## Vedi anche

- [Banchi conservatori e attrezzature in comodato](../anagrafiche/banchi-conservatori.md)
- [Anagrafica clienti](../anagrafiche/anagrafica-clienti.md)
