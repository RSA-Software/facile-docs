---
title: Associazione gruppi e giri
description: Le regole che, per un cliente e un gruppo di articoli, dicono quale agente, vettore e pagamento usare, e su quali giri di visita sta il cliente.
modulo: Archivi
maschera_id: IDD_CLI_ASSOCIAZIONI
---

# Associazione gruppi e giri

Due maschere quasi identiche per assegnare in fretta a un cliente — o a una sua
destinazione — le condizioni commerciali e i giri di visita dell'agente, senza
passare dall'anagrafica completa.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Archivi ▸ Clienti ▸ Associazione Gruppi
        - Menu ▸ Archivi ▸ Agenti ▸ Associazione Giri
    - **Scorciatoia:** ++f2++ salva, ++f6++ cancella l'associazione
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](utenti.md)

---

## A cosa serve

Un cliente può essere servito da un agente quando ordina i surgelati e da un
altro quando ordina il secco, e farsi consegnare da vettori diversi a seconda
della merce. L'anagrafica del cliente ha un agente solo e un vettore solo:
queste due maschere servono a dire **«per questo cliente, su questa merce, vale
invece quest'altro»**.

Ogni riga che registri qui è una regola a sé, identificata da tre cose:
il **cliente**, la sua **destinazione** e il **gruppo di articoli**. Le regole
non toccano l'anagrafica del cliente: restano in un archivio loro, e il
programma le va a leggere quando serve.

**Associazione Clienti - Gruppi** copre gruppo, agente, vettore, pagamento e i
tre giri. **Associazione Giri Agenti** si limita ad agente e giri.

Un cliente può stare su **tre giri diversi**, ciascuno con la sua sequenza: il
numero d'ordine con cui l'agente lo visita all'interno del giro.

## Prerequisiti

Prima di usare queste maschere occorre avere in archivio:

- i [clienti](anagrafica-clienti.md) e le loro destinazioni;
- gli [agenti](anagrafica-agenti.md), i
  [trasportatori](trasportatori.md) e i
  [tipi di pagamento](../contabilita/tipi-di-pagamento.md);
- i **giri agenti**, che si creano da **Menu ▸ Archivi ▸ Agenti ▸ Inserimento
  Giro** (vedi
  [Tabelle di classificazione](../magazzino/tabelle-di-classificazione.md)).

## La maschera

![Associazione clienti - gruppi](../../assets/img/anagrafiche/associazioni.png)

Sono maschere a finestra unica. In alto si sceglie **il chi** — cliente ed
eventualmente destinazione — e sotto la linea si assegna **il che cosa**. In
fondo i tre pulsanti **F2 - Salva**, **F6 - Canc.** ed **Esci**.

## Campi

### Chi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Cliente** | ● | Il [cliente](anagrafica-clienti.md) a cui assegnare le condizioni. | codice |
| **Destinazione** | | Una destinazione merce del cliente. Lasciandola vuota la regola vale per i documenti **senza** destinazione; indicandola vale **solo** per quella. | codice |

{: .campi }

### Che cosa — solo in Associazione Clienti - Gruppi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Gruppo** | | Il **gruppo di articoli** a cui la regola si riferisce — la stessa tabella *Gruppi* che si indica sull'articolo, non il gruppo del cliente. Lasciandolo vuoto la regola vale per i documenti senza gruppo prevalente. | codice |
| **Trasportatore** | | Il [vettore](trasportatori.md) che lo serve. | codice |
| **Pagamento** | | Il [tipo di pagamento](../contabilita/tipi-di-pagamento.md) da proporgli. | codice |

{: .campi }

### Che cosa — in entrambe

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Agente** | | L'[agente](anagrafica-agenti.md) che lo segue. | codice |
| **Giro Agente** (primo) e **Sequenza** | | Il primo giro di visita e la posizione del cliente al suo interno. | codice e numero |
| **Giro Agente** (secondo) e **Sequenza** | | Il secondo giro. | codice e numero |
| **Giro Agente** (terzo) e **Sequenza** | | Il terzo giro. | codice e numero |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Salva** | ++f2++ | Registra l'associazione. |
| **F6 - Canc.** | ++f6++ | Cancella l'associazione del cliente indicato. |
| **Esci** | ++esc++ | Chiude senza salvare. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Mettere un cliente nel giro del lunedì

1. Apri **Menu ▸ Archivi ▸ Agenti ▸ Associazione Giri**.
2. Indica il **Cliente** e, se serve, la **Destinazione**.
3. Indica l'**Agente**.
4. Nel primo **Giro Agente** indica il giro del lunedì e in **Sequenza** il
   numero d'ordine con cui va visitato.
5. Premi **F2 - Salva**.

### Far consegnare da un vettore diverso la merce di un gruppo

1. Apri **Menu ▸ Archivi ▸ Clienti ▸ Associazione Gruppi**.
2. Indica il **Cliente** e, se la regola riguarda una sola destinazione, la
   **Destinazione**.
3. Indica il **Gruppo** di articoli a cui la regola si riferisce.
4. Compila il **Trasportatore** e premi **F2 - Salva**.
5. D'ora in poi, gli ordini di quel cliente fatti in prevalenza di articoli di
   quel gruppo nascono con quel trasportatore, se non ne hanno già uno.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca il **Cliente**. | Compila il campo su cui si è posizionato il cursore. |

## Note

!!! note "L'anagrafica del cliente non viene toccata"

    Queste maschere **non scrivono nella scheda del cliente**: registrano una
    riga in un archivio proprio. Aprendo il cliente dopo aver salvato qui non
    troverai niente di cambiato, ed è giusto così.

    **F6 - Canc.** cancella la riga di associazione, non il cliente.

!!! info "Chi legge queste regole, e come"

    Le regole entrano in gioco quando da un **ordine in lavorazione** si
    genera il documento. Il programma guarda le righe dell'ordine, stabilisce
    qual è il **gruppo di articoli prevalente** — quello con più righe — e
    cerca la regola del cliente, della destinazione del documento e di quel
    gruppo.

    Se la trova, **completa i campi rimasti vuoti** sul documento: l'agente se
    il documento non ne ha, il pagamento se non ne ha, il trasportatore se non
    ne ha. Quello che il documento ha già **non viene mai sovrascritto**.

    I giri e le sequenze non servono ai documenti: servono alle stampe e alle
    etichette dei giri dell'agente.

!!! warning "La ricerca è a corrispondenza esatta, senza ripieghi"

    Cliente, destinazione e gruppo devono coincidere **tutti e tre**. Non
    esiste una regola generale a cui ricadere:

    - una regola registrata **senza destinazione** non vale per i documenti
      con destinazione, e viceversa;
    - una regola registrata **su un gruppo** non vale se nell'ordine prevale
      un altro gruppo.

    Se la regola non si trova, semplicemente non succede niente — nessun
    messaggio.

    I campi lasciati **vuoti** dentro una regola non azzerano niente: valgono
    come «su questo non dico nulla», e il documento si tiene quello che
    aveva.

## Vedi anche

- [Anagrafica clienti](anagrafica-clienti.md)
- [Anagrafica agenti](anagrafica-agenti.md)
- [Stampe agenti](stampe-agenti.md)
