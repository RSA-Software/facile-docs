---
title: Rinumerazione protocolli
description: L'elaborazione che rinumera da capo i protocolli dei registri IVA, quando la numerazione ha dei buchi o degli errori.
modulo: Contabilità
maschera_id: IDD_CON_RENUM_PROT
---

# Rinumerazione protocolli

Rinumera da capo i protocolli dei registri IVA scelti. Serve quando la
numerazione si è sporcata — un buco, un doppione, registrazioni inserite fuori
ordine — e va rimessa in fila.

!!! info "In sintesi"

    **Percorso:** Menu ▸ Contabilità ▸ Rinumerazione Protocolli
    **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    **Permessi richiesti:** nessun profilo predefinito; la voce di menu si abilita per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Il protocollo è il numero progressivo con cui una registrazione compare sul
registro IVA. Se si inserisce una fattura dimenticata, o se ne cancella una,
la sequenza non è più continua — e un registro con dei buchi non va bene.

Questa elaborazione ripercorre le registrazioni dei registri scelti e riassegna
i protocolli in ordine.

## Prerequisiti

Prima di lanciarla occorre:

- **avere una copia di sicurezza recente degli archivi**;
- avere finito di registrare il periodo: rinumerare e poi inserire altre
  fatture rimette il problema da capo;
- **non aver ancora stampato i registri sul bollato**, o averlo fatto sapendo
  che i numeri cambieranno.

## La maschera

![Rinumerazione protocolli](../../assets/img/contabilita/rinumerazione-protocolli.png)

Una finestra sola: l'elenco della **Sezione**, sei caselle — una per registro —
e i pulsanti **F2 - OK** ed **Esci**.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Sezione** | ● | Su quale [sezione](sezioni.md) contabile intervenire. | codice, oppure `TUTTE` |
| **Registro Acquisti** | | Rinumera il registro acquisti. | attivo/non attivo |
| **Registro Fatture Emesse** | | Rinumera il registro delle fatture emesse. | attivo/non attivo |
| **Registro Corrispettivi** | | Rinumera il registro dei corrispettivi. | attivo/non attivo |
| **Registro Fatture in Sospensione** | | Rinumera il registro delle fatture a esigibilità differita. | attivo/non attivo |
| **Registro Acquisti CEE** | | Rinumera il registro degli acquisti intracomunitari. | attivo/non attivo |
| **Registro Fatture Emesse CEE** | | Rinumera il registro delle cessioni intracomunitarie. | attivo/non attivo |

{: .campi }

Almeno una casella dev'essere spuntata.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia la rinumerazione dei registri spuntati. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo **Sezione**, apre l'elenco delle sezioni. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Rimettere in ordine i protocolli del registro acquisti

1. **Fai una copia di sicurezza degli archivi.**
2. Verifica di aver registrato tutte le fatture del periodo.
3. Apri **Menu ▸ Contabilità ▸ Rinumerazione Protocolli**.
4. Scegli la **Sezione**, o lascia `TUTTE`.
5. Spunta **Registro Acquisti** e lascia spente le altre.
6. Premi **F2 - OK**.
7. Ristampa il **Brogliaccio Movimenti** filtrato su quel registro e controlla
   che la sequenza sia continua.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Selezionare almeno un registro !* | Nessuna delle sei caselle è spuntata. | Spunta il registro o i registri da rinumerare. |

## Note

!!! warning "Attenzione"

    **I numeri di protocollo cambiano, e non si torna indietro.** Se i registri
    sono già stati stampati sul bollato, i numeri sulla carta non
    corrisponderanno più a quelli in archivio. Non esiste un annullamento:
    l'unico rimedio è ricaricare una copia di sicurezza.

    **Rinumera per ultimo.** Registra tutto il periodo, controlla le
    [squadrature](statistiche-e-controlli.md), poi rinumera, poi stampa.

<!-- DA VERIFICARE: con quale criterio vengono riassegnati i protocolli: per data di registrazione, per data documento o per numero di registrazione. -->

<!-- DA VERIFICARE: se la rinumerazione riparta da 1 o dal primo protocollo dell'anno. -->

<!-- DA VERIFICARE: se il programma avvisi quando i registri sono già stati stampati sul bollato. -->

## Vedi anche

- [Registri IVA](registri-iva.md)
- [Stampe contabili](stampe-contabili.md)
- [Registrazione di prima nota](registrazione-prima-nota.md)
