---
title: Ristampa dei documenti
description: Come ristampare in blocco fatture e ordini già emessi, scegliendo l'intervallo, il numero di copie e se rifare anche quelli mai stampati.
modulo: Vendite
maschera_id: IDD_VEN_FAT_STAMPA
---

# Ristampa dei documenti

Capita di dover rifare le stampe: la carta si è inceppata, il cliente ha perso
la copia, il commercialista chiede l'intero mese. **Ristampa** rifà in blocco i
documenti già emessi, senza aprirli uno per uno.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Vendite ▸ Fatture ▸ Ristampa
        - Menu ▸ Ordini ▸ Ordini da Clienti ▸ Ristampa
    - **Scorciatoia:** ++f2++ avvia la stampa, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

La finestra si chiama **Ristampa Fatture**; aperta dagli ordini prende il
titolo **Ristampa Ordini Clienti**. Si indica cosa ristampare — per numero, per
data, per soggetto — quante copie e se comprendere anche i documenti che non
erano mai stati stampati.

Con la ristampa degli ordini la casella **Includi Documenti non Stampati**
arriva già attiva: normalmente serve rifare tutto.

## Prerequisiti

Prima di ristampare occorre avere i documenti in archivio, che si consultano
dalla [gestione documenti](gestione-documenti.md).

L'opzione **Solo Esportazione** non c'è su tutti i documenti: sulle fatture
c'è sempre, sugli ordini solo se l'esportazione è abilitata nei
[parametri della ditta](../anagrafiche/ditte.md), e su DDT, bolle e buoni di
consegna non compare mai.

## La maschera

![Ristampa fatture](../../assets/img/vendite/ristampa-documenti.png)

Una finestra di selezione: il registro, gli intervalli di numero e di data, i
tre filtri sul soggetto, il numero di copie, le due caselle e i pulsanti **F2 -
OK** ed **Esci**.

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Registro** | | Il registro dei documenti da ristampare. Arriva già impostato su quello preferito per il tipo di documento. | voce dell'elenco |
| **Da Numero**, **A Numero** | | L'intervallo dei numeri di documento. | numeri |
| **Da Data**, **A Data** | | Il periodo. | date |
| **Cliente** | | Restringe a un cliente. Vuoto significa `TUTTI`. | codice |
| **Agente** | | Restringe a un [agente](../anagrafiche/anagrafica-agenti.md). Vuoto significa `TUTTI`. | codice |
| **Trasportatore** | | Restringe a un [trasportatore](../anagrafiche/trasportatori.md). Vuoto significa `TUTTI`. | codice |
| **Num. Copie** | | Quante copie stampare di ciascun documento. Arriva già impostato con il numero di copie della [ditta](../anagrafiche/ditte.md). | numero |
| **Includi Documenti non Stampati** | | Comprende anche i documenti mai stampati prima. Sugli ordini arriva già attiva. | attivo/non attivo |
| **Solo Esportazione** | | Non stampa: produce solo il file di esportazione. Compare solo se l'esportazione è abilitata. | attivo/non attivo |

{: .campi }

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia la ristampa. |
| **Esci** | ++esc++ | Chiude senza stampare. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |

## Come si fa

### Rifare le fatture di un mese

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Ristampa**.
2. Controlla il **Registro**.
3. Metti in **Da Data** e **A Data** il primo e l'ultimo giorno del mese.
4. Lascia **Includi Documenti non Stampati** spento se vuoi solo rifare quello
   che era già uscito.
5. Premi **F2 - OK**: durante il lavoro la finestra di attesa dice *Ristampa
   Fatture*, e si può fermare con **Esci**.

### Ristampare una sola fattura in più copie

1. Metti lo stesso numero in **Da Numero** e **A Numero**.
2. Indica **Num. Copie**.
3. Premi **F2 - OK**.

### Produrre solo il file di esportazione

1. Attiva **Solo Esportazione**.
2. Premi **F2 - OK**: non esce nulla dalla stampante, viene prodotto il file.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Vuoi Stampare gli Importi?* | Si stanno ristampando documenti di trasporto, bolle o ordini. | **Sì** stampa anche i valori, **No** li omette. La risposta preimpostata è **No**. |
| *(nessun messaggio, solo un segnale acustico)* | Un campo del filtro non è valido. | Guarda dove si è posizionato il cursore. |

## Note

!!! warning "La ristampa non è una copia di cortesia"

    Facile ristampa il documento come è in archivio, senza alcuna dicitura che
    lo distingua dall'originale. Se serve una copia riconoscibile, va gestita
    fuori dal programma.

!!! warning "Sulle fatture la ristampa può emettere davvero il documento"

    Con **Includi Documenti non Stampati** attiva, una fattura ancora
    *salvata* non viene solo stampata: il programma **ne rifà i calcoli e la
    porta allo stato EMESSA**, come se la si fosse emessa dalla sua maschera.
    Da quel momento non è più una bozza.

    Con la casella spenta le fatture salvate vengono **saltate**: la ristampa
    riguarda solo quelle già emesse o già contabilizzate.

    Sugli ordini funziona diversamente: quelli ancora salvati vengono
    ricalcolati e riscritti, ma **lo stato non cambia**. Gli ordini annullati
    vengono sempre saltati.

!!! note "Non esiste un contatore delle stampe"

    Il documento non porta né il numero di volte che è stato stampato né la
    data dell'ultima stampa, e la ristampa non tocca la sua data. Ristampare
    dieci volte la stessa fattura lascia l'archivio identico.

    L'unica traccia è sugli **ordini**, che portano un segno di «mandato in
    stampa»: si accende alla prima stampa — anche se fatta da qui — e non si
    spegne più. Non è un conteggio: è un sì o no.

!!! info "Dove finisce il file di Solo Esportazione"

    Esce un **PDF per ogni documento**, e niente va alla stampante.

    La cartella è quella che il programma si è annotato la prima volta. Se non
    ce n'è ancora una, si apre una finestra per sceglierla e la scelta viene
    ricordata per le volte successive; lavorando in sessione remota il
    programma non chiede niente e usa la cartella `out` dell'utente.

    Il nome del file può avere due forme, secondo come l'assistenza ha
    configurato l'esportazione:

    | Forma | Esempio |
    |---|---|
    | Estesa | `doc_fatture_N_125_A_04-09-26 - ROSSI MARIO S.R.L..pdf` |
    | Compatta | `fat001202600125a.pdf` — sigla, ditta, anno, numero, registro |

    Le sigle sono `fat` per fatture e acconti, `ord` per gli ordini e `pre`
    per i preventivi.

!!! note "Perché DDT, bolle e buoni non hanno l'esportazione"

    Il PDF viene prodotto solo per **fatture e acconti** già emessi o
    contabilizzati e per **ordini e preventivi** già stampati. Per gli altri
    documenti la funzione non è prevista, ed è il motivo per cui su quelle tre
    ristampe la casella **Solo Esportazione** non compare affatto.

## Vedi anche

- [Gestione documenti](gestione-documenti.md)
- [Inserimento e Modifica documenti](documento-di-vendita.md)
- [Esportazione, duplicazione e ricezione dei documenti](esporta-duplica-documenti.md)
- [Stampe degli ordini](../ordini/stampe-ordini.md)
