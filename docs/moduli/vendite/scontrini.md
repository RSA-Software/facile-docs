---
title: Scontrini
description: Il riepilogo degli scontrini battuti, la stampa dei punti fedeltà, il riepilogo IVA e il controllo del conferimento.
modulo: Vendite
maschera_id: IDD_VEN_SCONTRINI_GRID
---

# Scontrini

Il sottomenu **Scontrini** serve a rileggere quello che è stato battuto alla
cassa: l'elenco degli scontrini, il riepilogo IVA, i punti fedeltà maturati e
il controllo del conferimento.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Vendite ▸ Scontrini ▸ Altri Scarichi - Scontrini *(oppure* Stampa Punti*,* Riepilogo Scontrini*,* Riepilogo IVA Scontrini *o* Controllo Conferimento*)*
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

| Voce di menu | A cosa serve |
|---|---|
| **Altri Scarichi - Scontrini** | L'elenco degli scontrini battuti, da cui si cerca e si controlla. |
| **Stampa Punti** | I punti fedeltà maturati dai clienti. |
| **Riepilogo Scontrini** | Il riepilogo degli scontrini di un periodo. |
| **Riepilogo IVA Scontrini** | Il riepilogo per aliquota, che alimenta il registro dei corrispettivi. |
| **Controllo Conferimento** | Registra il rientro dei punti fedeltà leggendo il codice a barre del buono. |

## Prerequisiti

Prima di usare queste maschere occorre avere battuto gli scontrini dalla
[vendita al banco](vendita-al-banco.md) o dal punto cassa.

## La maschera

![Scontrini](../../assets/img/vendite/scontrini.png)

**Altri Scarichi - Scontrini** apre una griglia con i filtri in alto e il
**Totale** in fondo; le altre voci aprono finestre di selezione con il periodo.

La griglia ha queste colonne:

| Colonna | Contenuto |
|---|---|
| **Anno**, **Codice**, **Numero** | Identificano lo scontrino. |
| **Data**, **Ora** | Quando è stato battuto. |
| **Importo** | Il totale. |
| **Matricola** | La matricola del registratore di cassa. |
| **SF** | Il **numero dello scontrino fiscale** assegnato dal registratore di cassa. |
| **Azz.** | Il **numero dell'azzeramento** — la chiusura fiscale — dentro cui lo scontrino ricade. |
| **Fidelity** | La tessera fedeltà usata. |
| **Tran.** | Casella spuntata se la transazione è già stata mandata alla piattaforma. |
| **Sync.** | Casella spuntata se lo scontrino è già stato sincronizzato, con accanto fra parentesi **quante volte** lo è stato. |
| **Lotteria** | Il codice lotteria degli scontrini. |
| **Cliente** | Il cliente, se identificato. |
| **Operatore** | Chi ha battuto. |

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale**, **Data Finale** | | Il periodo da mostrare. | date |
| **Registro** | | Restringe a un registro. | voce dell'elenco |
| **Matricola** | | Restringe a un registratore di cassa. | matricola |
| **Cliente** | | Restringe a un cliente. | codice |
| **Tipologia** | | Restringe a un tipo di scontrino. | voce dell'elenco |
| **Operatore** | | Restringe a chi ha battuto. | codice |

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Applica i filtri, oppure avvia la stampa. |
| **F5 - Cerca Scontrini** | ++f5++ | Rilegge l'elenco con i filtri impostati. |
| **F9 - Trova** | ++f9++ | Cerca un testo dentro la griglia. |
| **F7 - Invio Dati Naima** | ++f7++ | Manda alla piattaforma le transazioni non ancora inviate. |
| **F8 - Forza Invio** | ++f8++ | Rimette in coda di sincronizzazione gli scontrini selezionati. |
| Doppio clic su una riga | | Apre il dettaglio dello scontrino. |
| **Esci** | ++esc++ | Chiude. |
| Elenco di scelta | ++f10++ o ++space++ | Sul campo con il codice, apre l'elenco da cui scegliere. |
| **Calcolatrice** | ++f12++ | Apre la calcolatrice. |
| **Consultazione** | ++f11++ | Apre la consultazione. |

## Come si fa

### Controllare la giornata di cassa

1. Apri **Menu ▸ Vendite ▸ Scontrini ▸ Altri Scarichi - Scontrini**.
2. Metti **Data Iniziale** e **Data Finale** al giorno da controllare.
3. Confronta il **Totale** con il rapporto della cassa.

### Preparare i dati per il registro dei corrispettivi

1. Apri **Menu ▸ Vendite ▸ Scontrini ▸ Riepilogo IVA Scontrini**.
2. Indica il periodo e stampa.
3. Il risultato è quello che finisce nel
   [registro dei corrispettivi](../contabilita/registri-iva.md).

### Vedere i punti fedeltà maturati

1. Apri **Menu ▸ Vendite ▸ Scontrini ▸ Stampa Punti**.
2. Indica il periodo e stampa. I saldi si azzerano poi con
   [Bollini](../anagrafiche/bollini.md).

### Registrare i buoni punti che rientrano

1. Apri **Menu ▸ Vendite ▸ Scontrini ▸ Controllo Conferimento**.
2. Passa il lettore sul codice a barre del buono. Il cursore è già sul campo
   giusto.
3. Il programma carica lo scontrino, somma i punti e li mostra in **Punti
   Rientrati**; in **Totale Rientrati** si accumulano quelli di tutti i buoni
   letti.
4. Passa al buono seguente: il campo si è già svuotato.
5. A fine giro, **F2 - OK** azzera il totale — previa conferma — e si
   ricomincia.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Un campo del filtro non è valido. | Guarda dove si è posizionato il cursore. |
| *Codice a barre non valido!* | Nel **Controllo Conferimento**, il codice letto non ha la forma prevista. | Rileggi il buono; se il messaggio torna, quel buono non è del formato di Facile. |
| *Conferimento: numero dello scontrino non valido!* | Nel codice a barre il numero dello scontrino manca o è zero. | Rileggi il buono; se il messaggio torna, quel buono non è del formato di Facile. |
| *Conferimento: registro dello scontrino non valido!* | Nel codice a barre manca il registro. | Come sopra. |
| *Conferimento non trovato in archivio!* | Lo scontrino indicato dal buono non esiste nell'anno di lavoro. | Controlla di essere nell'anno giusto. |
| *Punti rientrati superiori ai punti erogati!* | Su quello scontrino sono già rientrati più punti di quanti ne fossero stati dati. | I punti vengono sommati lo stesso: verifica se il buono è stato letto due volte. |
| *Cliente sul barcode diverso da cliente su Conferimento!* | Il cliente scritto sul buono non è quello dello scontrino. | I punti vengono sommati lo stesso: controlla che il buono sia di quel cliente. |
| *Confermi l'azzeramento del totale?* | Hai premuto **F2 - OK** nel Controllo Conferimento. | **Sì** azzera il **Totale Rientrati** a video. La risposta preimpostata è **No**. |

## Note

!!! note "Gli scontrini si consultano, non si correggono"

    Da qui gli scontrini si rileggono; sono documenti fiscali già emessi dal
    registratore di cassa. Le rettifiche si fanno con i resi dalla
    [schermata di vendita](vendita-al-banco.md).

!!! note "Perché la voce si chiama «Altri Scarichi» e la finestra no"

    Il nome della voce di menu è quello della **finestra di dettaglio**, non
    dell'elenco: facendo doppio clic su una riga si apre lo scontrino singolo, e
    quella finestra si intitola *Altri Scarichi - Scontrini*, con accanto fra
    parentesi il [deposito](../magazzino/depositi.md) — per esempio
    *[ Dep. 001 - SEDE ]*.

    L'elenco da cui si parte si intitola invece **Riepilogo Scontrini**, che è
    anche il nome di **un'altra voce dello stesso menu**: quella apre una
    finestrella di stampa, non l'elenco. È una sovrapposizione di nomi che
    conviene conoscere, perché a video non si distinguono.

!!! info "Che cos'è il Controllo Conferimento"

    Non controlla le consegne: **registra il rientro dei punti fedeltà**. La
    finestra si intitola infatti *Controllo Rientro Punti*.

    Si tiene il lettore in mano e si passano i buoni uno dietro l'altro. Il
    codice a barre del buono contiene quattro informazioni separate dalla
    chiocciola — **numero dello scontrino**, **registro**, **codice cliente** e
    **punti** — e per ogni lettura il programma:

    1. cerca quello scontrino nell'anno di lavoro;
    2. **somma i punti** del buono a quelli già rientrati su quello scontrino, e
       salva subito;
    3. mostra numero, registro, data e cliente dello scontrino, i **Punti
       Erogati** e i **Punti Rientrati**;
    4. aggiorna il **Totale Rientrati**, che conta i punti di tutti i buoni letti
       da quando la finestra è aperta.

    Due avvisi non bloccano niente ma vanno letti: quando i punti rientrati
    superano quelli erogati, e quando il cliente sul buono non è quello dello
    scontrino. In tutti e due i casi **i punti vengono registrati lo stesso**.

!!! warning "SF e Azz. sono numeri, non stati"

    Sono i due contatori del registratore di cassa: **SF** è il numero che la
    stampante fiscale ha dato allo scontrino, **Azz.** è il numero della
    chiusura fiscale dentro cui quello scontrino cade. Servono a ritrovare uno
    scontrino sul rotolo o nel rapporto della cassa.

    **Tran.** e **Sync.** invece sono due caselle da spuntare, e riguardano gli
    invii verso l'esterno: la prima dice se la transazione è partita, la seconda
    se lo scontrino è stato sincronizzato — e fra parentesi quante volte. Uno
    scontrino con `(3)` è stato mandato tre volte.

## Vedi anche

- [Vendita al banco e POS](vendita-al-banco.md)
- [Bollini](../anagrafiche/bollini.md)
- [Registri IVA](../contabilita/registri-iva.md)
