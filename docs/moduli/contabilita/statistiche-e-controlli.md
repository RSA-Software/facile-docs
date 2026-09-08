---
title: Statistiche e controlli contabili
description: Le stampe di controllo della contabilità — statistiche vendite e acquisti, saldi di compensazione, squadrature dei movimenti e rapporti.
modulo: Contabilità
maschera_id: IDD_CON_STATISTICA
---

# Statistiche e controlli contabili

Cinque voci che non registrano nulla: leggono quello che è stato registrato e
lo raccontano — quanto si è venduto e comprato, chi è insieme cliente e
fornitore, e dove la contabilità non quadra.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Contabilità ▸ Saldi Compensazione Clienti/Fornitori
        - Menu ▸ Contabilità ▸ Statistica Vendite
        - Menu ▸ Contabilità ▸ Statistica Acquisti
        - Menu ▸ Contabilità ▸ Statistica Acquisti su Conto
        - Menu ▸ Contabilità ▸ Squadrature Movimenti
        - Menu ▸ Contabilità ▸ Stampa Rapporti
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Statistica Vendite** | Quanto si è venduto a ciascun cliente in un periodo. La finestra si chiama *Statistica Vendite*. |
| **Statistica Acquisti** | Quanto si è comprato da ciascun fornitore. Apre la stessa maschera, con il campo intestato **Fornitore**. |
| **Statistica Acquisti su Conto** | Gli acquisti raggruppati per conto invece che per fornitore: dice **su cosa** si è speso. |
| **Saldi Compensazione Clienti/Fornitori** | I soggetti che sono insieme clienti e fornitori, con i due saldi affiancati: quanto ti devono e quanto devi. |
| **Squadrature Movimenti** | Le registrazioni in cui dare e avere non coincidono. È il controllo da fare prima di ogni stampa fiscale. |
| **Stampa Rapporti** | I rapporti contabili a una data. |

## Prerequisiti

Prima di usare queste maschere occorre avere le registrazioni di
[prima nota](registrazione-prima-nota.md) del periodo.

## La maschera

![Statistica vendite](../../assets/img/contabilita/statistiche-e-controlli.png)

Sono finestre di selezione con pochi campi e i pulsanti **F2 - OK** ed
**Esci**. **Saldi Compensazione Clienti / Fornitori** si apre invece a tutto
schermo, con la griglia dei soggetti.

## Campi

### Statistica Vendite e Statistica Acquisti

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | ● | Il periodo da esaminare. | date |
| **Sezione (0 = Tutte)** | | Restringe a una [sezione](sezioni.md). | codice, `0` per tutte |
| **Cliente** | | Restringe a un nominativo. Nella statistica acquisti l'etichetta è **Fornitore**. | codice |

{: .campi }

### Statistica Acquisti su Conto

Gli stessi campi, più:

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Conto** | | Restringe a un [conto](conti.md). | codice |
| **Ordinamento** | | Come ordinare la stampa. | `CODICE`, `ALFABETICO` |

{: .campi }

### Squadrature Movimenti

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Sezione** | | La [sezione](sezioni.md) da controllare. A fianco l'etichetta ricorda **( 0 Tutte le Sezioni )**. | codice, `0` per tutte |
| **Da Num. Reg.**, **A Num. Reg.** | | Intervallo di numeri di registrazione. | numeri |
| **Da Data Reg.**, **A Data Reg.** | | Intervallo di date di registrazione. | date |
| **Causale** | | Restringe a una [causale](causali-contabili.md). | codice |

{: .campi }

### Stampa Rapporti

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data** | ● | La data a cui riferire i rapporti. | data |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia l'elaborazione e mostra il risultato. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Controllare che la contabilità quadri

1. Apri **Menu ▸ Contabilità ▸ Squadrature Movimenti**.
2. Lascia **Sezione** a `0` e indica il periodo in **Da Data Reg.** e **A Data
   Reg.**.
3. Premi **F2 - OK**. **Ogni riga che esce è una registrazione da
   correggere**: aprila dalla [gestione prima nota](gestione-prima-nota.md) e
   sistema la squadratura.
4. Ripeti finché la stampa esce vuota, poi procedi con le
   [stampe contabili](stampe-contabili.md).

### Sapere quanto si è venduto a un cliente

1. Apri **Menu ▸ Contabilità ▸ Statistica Vendite**.
2. Indica il periodo e il **Cliente**.
3. Premi **F2 - OK**.

### Vedere chi è insieme cliente e fornitore

1. Apri **Menu ▸ Contabilità ▸ Saldi Compensazione Clienti/Fornitori**.
2. La griglia elenca i soggetti presenti in entrambi gli archivi con i due
   saldi: è da lì che si decide se compensare.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca una delle date obbligatorie. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! warning "Le squadrature vanno azzerate prima delle stampe fiscali"

    Una registrazione squadrata falsa il bilancio e i registri. Fai girare
    **Squadrature Movimenti** prima di stampare il libro giornale, i registri
    IVA e il bilancio di verifica.

<!-- DA VERIFICARE: cosa contengono esattamente i "rapporti contabili" di Stampa Rapporti. -->

<!-- DA VERIFICARE: se la compensazione fra i due saldi vada poi registrata a mano o esista una funzione che la genera. -->

<!-- DA VERIFICARE: quali colonne mostra la griglia dei Saldi Compensazione: il decodificatore delle etichette non le ha estratte. -->

## Vedi anche

- [Gestione prima nota](gestione-prima-nota.md)
- [Stampe contabili](stampe-contabili.md)
- [Liquidazione IVA](liquidazione-iva.md)
