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

!!! info "Non esiste una tabella delle campagne"

    Una campagna, per Facile, sono **tre numeri scritti sul cliente**:
    i bollini della campagna **attuale**, quelli della campagna
    **precedente**, e la **data di inizio** della campagna in corso. Li
    trovi sulla scheda del cliente, fra i dati della fidelity.

    Non c'è un archivio delle campagne, non c'è una data di scadenza e il
    programma non chiude niente da solo: **la campagna finisce quando
    lanci l'azzeramento**, e ricomincia da quel momento.

!!! info "Che cosa fanno i due azzeramenti"

    **Azzeramento Campagna Attuale** fa tre cose su **tutti** i clienti,
    in un colpo solo:

    1. copia i bollini attuali in quelli della **campagna precedente**,
       sovrascrivendo quello che c'era;
    2. azzera i **bollini attuali**;
    3. scrive su ogni cliente, come **data di inizio campagna**, la data
       che hai indicato.

    Quella data non filtra niente e non è la data di chiusura: è il
    **giorno da cui parte la campagna nuova**, e viene scritta uguale su
    tutti.

    **Azzeramento Campagna Precedente** azzera soltanto i bollini della
    campagna vecchia, e non tocca né quelli in corso né la data. Si usa
    quando i premi della campagna passata sono stati tutti consegnati.

!!! warning "Il ricalcolo legge solo gli scontrini"

    Nient'altro: non fatture, non documenti di trasporto, non movimenti di
    magazzino. Somma, sugli scontrini del periodo indicato e intestati a un
    cliente, i bollini **caricati meno quelli scaricati**, e **sostituisce**
    il totale nei bollini attuali del cliente.

    Attenzione alla differenza fra le due scelte:

    - **azzerando prima**, tutti i clienti partono da zero, quindi chi non
      ha scontrini nel periodo resta a zero: è la ricostruzione vera;
    - **senza azzerare**, chi non ha scontrini nel periodo **si tiene il
      valore che aveva**, e il risultato è un misto fra il vecchio conteggio
      e quello nuovo.

    Se i bollini vengono caricati anche altrove — a mano sulla scheda del
    cliente, o da un'integrazione esterna — il ricalcolo **li perde**: per
    quei clienti sostituisce il totale con il solo conteggio degli
    scontrini.

## Vedi anche

- [Anagrafica clienti](anagrafica-clienti.md)
- [Stampe clienti](stampe-clienti.md)
