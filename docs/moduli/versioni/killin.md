---
title: Killin
description: Il ramo di menu con le stampe dei ricavi a costo medio e a costo Killin, i riepiloghi con le foto degli articoli e lo scambio dati con Gesa.
modulo: Killin
maschera_id: nessuna dialog propria
---

# Killin

Il menu **Killin** raccoglie alcune stampe sui ricavi e un giro di scambio dati
con un altro programma. È una **personalizzazione**: esiste solo nelle
installazioni allestite per quel settore.

!!! warning "Se non trovi il menu, la tua versione non lo prevede"

    Come gli altri rami delle [versioni specifiche](index.md), all'avvio il
    programma toglie dalla barra l'intero menu quando la versione non è quella.

---

## Le stampe dei ricavi

Le prime due voci aprono **la stessa maschera** delle
[stampe di magazzino](../magazzino/stampe-movimenti-magazzino.md), con lo stesso
elenco di filtri, e cambiano soltanto il costo con cui si calcola il ricavo:

| Voce di menu | Ricavo calcolato su |
|---|---|
| **Ricavi Vendite Costo Medio** | Il costo medio degli articoli. |
| **Ricavi Vendite Costo Killin** | Il costo specifico della gestione Killin. |

!!! tip "Il confronto fra le due è il punto"

    Le due stampe hanno senso **lette insieme**: la differenza fra i due ricavi
    dice quanto il costo specifico si discosta dal costo medio di magazzino, ed
    è lì che si nascondono gli articoli fuori linea.

## I riepiloghi con le foto

Tre voci si appoggiano alla maschera delle
[stampe articoli](../anagrafiche/stampe-articoli.md), con i suoi filtri
abituali, e cambiano il modello di stampa:

| Voce di menu | Titolo della finestra | Che cosa stampa |
|---|---|---|
| **Riepilogo Acquisti-Vendite con Foto** | *Riepilogo Acquisti-Vendite con Foto* | Acquistato e venduto di ogni articolo, con la sua immagine. |
| **Riepilogo Articoli venduti con Foto** | *Articoli Venduti con Foto* | I soli articoli venduti, con l'immagine. |
| **Stampa Confronto Listino1 ↔ Listino2** | *Stampa Confronto Listino1 <--> Listino 2* | I due listini a confronto, articolo per articolo. |

Se in archivio non c'è nessun articolo, il riepilogo degli articoli venduti si
ferma con *Non ci sono articoli in archivio!*.

## Importazione Foto

Carica in blocco le immagini degli articoli.

Facile chiede **la cartella** dove stanno le foto — e si ricorda quella scelta
per la volta successiva — poi le carica una per una mostrando l'avanzamento.
Il nome del file è quello che lega la foto all'articolo.

!!! note "Se le librerie delle immagini non ci sono, non parte"

    All'avvio della procedura, se il componente di gestione immagini non si
    carica, Facile risponde *Impossibile caricare le DLL di Imagekit!* e si
    ferma. È una installazione incompleta: va sistemata dall'assistenza.

## Lo scambio dati con Gesa

Quattro voci fanno viaggiare i dati fra Facile e **Gesa**, il programma di
cassa usato in quelle installazioni.

| Voce di menu | Direzione | Che cosa porta |
|---|---|---|
| **Allineamento Costi Killin da Gesa** | ← in entrata | Riallinea i costi degli articoli con quelli di Gesa. |
| **Importazione Vendite da Gesa** | ← in entrata | Porta in Facile i movimenti di vendita registrati da Gesa. |
| **Esportazione Vendite** | → in uscita | Manda a Gesa i movimenti di vendita. |
| **Esportazione Listino** | → in uscita | Manda a Gesa il listino. |
| **Esportazione Movimenti** | → in uscita | Manda a Gesa i movimenti di magazzino. |

L'importazione delle vendite genera movimenti di magazzino, e per questo
pretende che la causale indicata sia in regola. Se non lo è, lo dice prima di
cominciare:

| Messaggio | Causa |
|---|---|
| *Il codice della Causale di Magazzino richiesto non è valido o disponibile.* | La causale non esiste. |
| *La Causale non è in relazione con i Clienti.* | La causale non movimenta i clienti. |
| *La Causale deve essere impostata come Scarico.* | La causale non è di scarico: una vendita scarica il magazzino. |
| *Il codice del Deposito non è valido o disponibile.* | Il deposito indicato non esiste. |

!!! warning "Le importazioni non si annullano"

    Importare due volte lo stesso periodo scarica il magazzino due volte. Non
    c'è un segno che dica «questo l'ho già preso»: tenere nota di che cosa è
    stato importato, e fino a quando, resta a chi lavora.

## Vedi anche

- [Versioni specifiche](index.md)
- [Stampe articoli](../anagrafiche/stampe-articoli.md)
- [Stampe dei movimenti](../magazzino/stampe-movimenti-magazzino.md)
