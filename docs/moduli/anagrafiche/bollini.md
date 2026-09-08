---
title: Bollini
description: Le tre elaborazioni che azzerano e ricalcolano i bollini della raccolta punti dei clienti.
modulo: Archivi
maschera_id: nessuna dialog propria
---

# Bollini

Tre voci di menu per governare la raccolta punti: azzerare i bollini della
campagna in corso, azzerare quelli della campagna precedente, ricalcolarli
tutti dagli scontrini.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Archivi ▸ Clienti ▸ Azzeramento Bollini Campagna Attuale
        - Menu ▸ Archivi ▸ Clienti ▸ Azzeramento Bollini Campagna Precedente
        - Menu ▸ Archivi ▸ Clienti ▸ Ricalcolo Bollini
    - **Scorciatoia:** nessuna; le elaborazioni partono dal menu
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](utenti.md)

---

## A cosa serve

La raccolta punti ha un inizio e una fine. Quando la campagna si chiude, i
bollini vanno azzerati per ripartire; quando i conteggi non tornano, si
rifanno dagli scontrini.

| Voce di menu | Cosa fa |
|---|---|
| **Azzeramento Bollini Campagna Attuale** | Azzera i bollini di tutti i clienti a una data che si indica. |
| **Azzeramento Bollini Campagna Precedente** | Azzera i bollini della campagna chiusa in precedenza. |
| **Ricalcolo Bollini** | Ricostruisce i bollini rileggendo gli scontrini. |

## Prerequisiti

Prima di lanciare queste elaborazioni occorre:

- **avere una copia di sicurezza recente degli archivi**: non c'è modo di
  tornare indietro;
- per il ricalcolo, avere gli scontrini del periodo ancora in archivio.

## La maschera

Non c'è una maschera vera e propria: le tre voci fanno partire l'elaborazione
dopo aver chiesto conferma.

**Azzeramento Bollini Campagna Attuale** apre prima la finestrella **Data
Azzeramento Bollini**, che chiede la data a cui azzerare. Le altre due partono
dalla sola conferma.

Durante il lavoro compare la finestra di avanzamento, con la scritta
*Azzeramento Bollini Clienti...* oppure *Ricalcolo Bollini Clienti...*.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Azzeramento Bollini** | ● | La data a cui azzerare i bollini. Compare solo per la campagna attuale. | data |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **OK** | ++f2++ | Conferma la data e prosegue. |
| **Esci** | ++esc++ | Annulla l'elaborazione. |
| **Interrompi** | | Durante l'elaborazione, il pulsante della finestra di avanzamento ferma il lavoro. |

## Come si fa

### Chiudere la campagna in corso

1. Apri **Menu ▸ Archivi ▸ Clienti ▸ Azzeramento Bollini Campagna Attuale**.
2. Indica la data nella finestrella **Data Azzeramento Bollini** e conferma.
3. Rispondi **Sì** a *«Confermi l'azzeramento dei bollini alla data
   indicata ?»*.
4. Attendi la fine dell'elaborazione.

### Azzerare la campagna precedente

1. Apri **Menu ▸ Archivi ▸ Clienti ▸ Azzeramento Bollini Campagna
   Precedente**.
2. Rispondi **Sì** alla prima domanda.
3. Rispondi **No** alla seconda, che chiede se vuoi *annullare* l'azzeramento.

### Rifare i conti dei bollini

1. Apri **Menu ▸ Archivi ▸ Clienti ▸ Ricalcolo Bollini**.
2. Alla domanda *«Vuoi azzerare i valori iniziali ?»* rispondi **Sì** solo se
   vuoi ripartire da zero; **No** conserva i saldi di partenza e ricalcola solo
   il movimentato.
3. L'elaborazione azzera, poi rilegge gli scontrini e ricostruisce i saldi.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Confermi l'azzeramento dei bollini alla data indicata ?* | Conferma dell'azzeramento della campagna attuale. | **Sì** azzera i bollini di tutti i clienti. La domanda propone **No**. |
| *Confermi l'azzeramento dei bollini della campagna precedente ?* | Prima conferma dell'azzeramento della campagna precedente. | **Sì** prosegue. La domanda propone **No**. |
| *Vuoi annullare l 'azzeramento dei bollini della campagna precedente ?* | Seconda domanda, subito dopo la prima. | Rispondi **No** per procedere davvero. La domanda propone **Sì**. |
| *Vuoi azzerare i valori iniziali ?* | Il ricalcolo chiede se ripartire da zero. | **Sì** azzera anche i saldi di partenza. |

## Note

!!! warning "Attenzione"

    **Le tre elaborazioni toccano tutti i clienti e non si annullano.** Non
    c'è un filtro e non c'è un ripristino: l'unico modo per tornare indietro è
    ricaricare una copia di sicurezza.

    **La seconda domanda dell'azzeramento è formulata al contrario.** Per
    azzerare davvero la campagna precedente si risponde **Sì** alla prima
    domanda e **No** alla seconda. La seconda propone **Sì** come risposta
    predefinita, cioè propone di annullare: leggila con attenzione.

<!-- DA VERIFICARE: che ruolo abbia la data indicata nell'azzeramento della campagna attuale — se sia la data di chiusura registrata sul cliente o un filtro sui movimenti. -->

<!-- DA VERIFICARE: cosa distingue "campagna attuale" da "campagna precedente" negli archivi, e dove si stabilisce quando una campagna finisce. -->

<!-- DA VERIFICARE: da quali documenti il ricalcolo rilegga i bollini: la finestra di avanzamento cita gli scontrini, ma non è detto siano gli unici. -->

## Vedi anche

- [Anagrafica clienti](anagrafica-clienti.md)
- [Stampe clienti](stampe-clienti.md)
