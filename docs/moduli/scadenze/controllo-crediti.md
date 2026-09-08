---
title: Controllo crediti e debiti
description: Le stampe che misurano l'esposizione — controllo crediti, ritardi medi di incasso, credito circolante, crediti per agente, estratti conto ed esposizione verso i fornitori.
modulo: Scadenze
maschera_id: IDD_CON_CONTROLLO_CREDITI
---

# Controllo crediti e debiti

Le scadenze dicono cosa si deve incassare; queste stampe dicono **come si sta
messi**: chi paga tardi e quanto, quanto credito è in circolo, quanto si è
esposti verso i fornitori.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Controllo Crediti
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Ritardi Medi di Incasso
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Situazione Crediti per Agente
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Credito Circolante
        - Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Calcolo e Invio Estratti Conto
        - Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Stampe Esposizione Verso Fornitori
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | Cosa mostra |
|---|---|
| **Stampa Controllo Crediti** | La situazione dei crediti verso i clienti. |
| **Stampa Ritardi Medi di Incasso** | Con quanti giorni di ritardo ciascun cliente paga mediamente. Apre la stessa maschera del controllo crediti, con un parametro diverso. |
| **Stampa Situazione Crediti per Agente** | I crediti raggruppati per [agente](../anagrafiche/anagrafica-agenti.md). |
| **Credito Circolante** | Quanto credito è in circolo in un momento dato. |
| **Calcolo e Invio Estratti Conto** | Calcola gli estratti conto dei clienti e li manda. |
| **Stampe Esposizione Verso Fornitori** | Quanto si deve ai fornitori, il rovescio del controllo crediti. |

## Prerequisiti

Prima di usare queste stampe occorre avere le scadenze in archivio e — per i
ritardi medi — avere registrato gli incassi con le
[distinte](distinte-incasso-pagamento.md), perché è dal confronto fra data di
scadenza e data di incasso che il ritardo si misura.

Per l'invio degli estratti conto servono l'indirizzo di posta dei clienti e il
mittente impostato sull'[utente](../anagrafiche/utenti.md) o sulla
[ditta](../anagrafiche/ditte.md).

## La maschera

![Controllo crediti](../../assets/img/scadenze/controllo-crediti.png)

Sono finestre di selezione con il periodo e i filtri, e i pulsanti **F2 - OK**
ed **Esci**.

<!-- DA VERIFICARE: i campi di queste maschere: sono cinque diverse e non ho potuto estrarne le etichette dalle risorse. -->

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo da esaminare. | date |
| **Cliente** | | Restringe a un cliente. Nell'esposizione verso fornitori è il **Fornitore**. | codice |
| **Agente** | | Restringe a un [agente](../anagrafiche/anagrafica-agenti.md). | codice |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia la stampa o l'elaborazione. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |

## Come si fa

### Capire quali clienti pagano tardi

1. Apri **Menu ▸ Scadenze ▸ Scadenziario Clienti ▸ Stampa Ritardi Medi di
   Incasso**.
2. Indica un periodo abbastanza lungo perché la media abbia senso.
3. Premi **F2 - OK**: la stampa dice, cliente per cliente, di quanti giorni si
   sfora mediamente.

### Mandare gli estratti conto ai clienti

1. Apri **Calcolo e Invio Estratti Conto**.
2. Indica il periodo e avvia.
3. Controlla che i clienti abbiano l'indirizzo di posta: chi non ce l'ha non
   riceve nulla.

### Sapere quanto si deve ai fornitori

1. Apri **Menu ▸ Scadenze ▸ Scadenziario Fornitori ▸ Stampe Esposizione Verso
   Fornitori**.
2. Indica il periodo e stampa.

## Controlli e messaggi

<!-- DA VERIFICARE: i messaggi di queste maschere, compreso il caso del mittente non impostato per l'invio degli estratti conto. -->

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca una delle date. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! note "Il fido del cliente"

    Il **Controllo Crediti** ha senso pieno se sui clienti è impostato il fido:
    è confrontando l'esposizione con quel limite che si capisce chi è oltre.
    Vedi [Anagrafica clienti](../anagrafiche/anagrafica-clienti.md).

<!-- DA VERIFICARE: cosa distingue "Credito Circolante" da "Stampa Controllo Crediti". -->

<!-- DA VERIFICARE: se il Controllo Crediti confronti l'esposizione con il fido del cliente. -->

<!-- DA VERIFICARE: come vengono inviati gli estratti conto: per posta elettronica, in stampa o entrambi. -->

## Vedi anche

- [Gestione scadenze](gestione-scadenze.md)
- [Stampe delle scadenze](stampe-scadenze.md)
- [Anagrafica clienti](../anagrafiche/anagrafica-clienti.md)
