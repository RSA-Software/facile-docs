---
title: Registratori telematici RCH
description: Come si collegano a Facile i registratori telematici RCH Print!F RT e Print! 3.0 RT, con il protocollo XON/XOFF su seriale o in rete oppure attraverso il Multidriver di RCH.
modulo: Casse e Bilance
---

# Registratori telematici RCH

Facile pilota i registratori telematici RCH — **Print!F RT**, **Print! 3.0 RT**,
**ONDA/SPOT RT** — in tre modi diversi, che corrispondono a tre voci
dell'elenco **Stampante Fiscale**. Questa pagina spiega quale scegliere, come
prepararlo e che cosa aspettarsi da ciascuno.

!!! info "In sintesi"

    - **Dove si sceglie:** Menu ▸ Utility ▸ [Impostazioni Postazione](../../utility/impostazioni-postazione.md), campo **Stampante Fiscale**
    - **Voci:** `RCH XON / XOFF (9600,N,8,1)`, `RCH XON / XOFF LAN`, `RCH MULTIDRIVER SERVER`
    - **Configurazione:** un file nella cartella `cfg` di Facile — [rch.ini](../../../assets/modelli/rch.ini) per lo XON/XOFF, [RCH_Multidriver.ini](../../../assets/modelli/RCH_Multidriver.ini) per il Multidriver

---

## Quale collegamento scegliere

I tre modi non sono intercambiabili: cambiano i comandi, il mezzo di trasporto
e quello che il registratore risponde.

| Voce in **Stampante Fiscale** | Come funziona | Collegamento |
|---|---|---|
| `RCH XON / XOFF (9600,N,8,1)` | Facile manda i comandi direttamente al registratore. | Seriale, con il cavo RCH CABA0056 |
| `RCH XON / XOFF LAN` | Lo stesso, in rete. | Ethernet |
| `RCH MULTIDRIVER SERVER` | Facile scrive i comandi in un file e li fa consegnare dal programma Multidriver di RCH. | Rete, USB o seriale, come configurato nel Multidriver |

- Lo **XON/XOFF** è il più semplice e diretto, ma Facile non riceve risposte dal
  registratore: un comando rifiutato si vede solo sul display e sulla stampa
  della cassa.
- Il **Multidriver** è più lento, perché a ogni scontrino avvia il programma di
  RCH, ma restituisce un esito: Facile sa se lo scontrino è stato stampato e
  avvisa l'operatore in caso di errore o di fine carta.

!!! note "I vecchi modelli RCH"

    Le voci `RCH NUCLEO`, `RCH GLOBE` e `RCH ONDA` non sono più nell'elenco e
    non vanno usate sulle installazioni nuove.

## Preparare il registratore

Sul registratore, dal menu **SERVICE ▸ Connettività**, abilita il protocollo
XON/XOFF scegliendo la connessione seriale o Ethernet. Due parametri della cassa
decidono che cosa Facile può fare:

- **FIDELITY**: va acceso se servono i codici a barre sullo scontrino; spento,
  i codici a barre vengono ignorati senza alcun avviso. Se non servono, RCH
  consiglia di lasciarlo spento.
- **Gestione FATTURA**: va abilitata in modalità SERVICE perché funzioni la
  fattura interna. Esiste solo sul Print!F, non sul Print! 3.0 RT.

In [Impostazioni Postazione](../../utility/impostazioni-postazione.md) compila
anche la **Matricola** del registratore: con lo XON/XOFF Facile non la può
leggere dalla cassa, e serve ai documenti di reso e di annullo, che la vogliono
di 11 caratteri.

## Protocollo XON/XOFF

### Collegamento

- **Seriale:** 9600 baud, nessuna parità, 8 bit di dati, 1 bit di stop,
  controllo di flusso XON/XOFF, cavo RCH CABA0056 (DB9 verso RJ45). In
  **Porta** indica la porta seriale.
- **Rete** (voce `RCH XON / XOFF LAN`): l'indirizzo e la porta del registratore
  si scrivono in `rch.ini`.

### Il file rch.ini

Tutto quello che distingue un'installazione dall'altra sta nel file `rch.ini`
della cartella `cfg` di Facile. Puoi partire dal
[file di esempio](../../../assets/modelli/rch.ini), già commentato.

| Sezione | Chiave | Predefinito | Descrizione |
|---|---|---|---|
| `[OPTIONS]` | `ip` | — | Indirizzo del registratore, solo per `RCH XON / XOFF LAN`. |
| `[OPTIONS]` | `port` | 9100 | Porta di rete, solo per `RCH XON / XOFF LAN`. |
| `[OPTIONS]` | `COL_PRIMA_RIGA` | 24 | Caratteri della riga di vendita. |
| `[OPTIONS]` | `COL_RIGHE_AGG` | 24 | Caratteri delle righe di descrizione aggiuntive. |
| `[OPTIONS]` | `delay_time` | 0 | Pausa fra due comandi, in millisecondi. Lasciala a 0 e alzala solo se il registratore perde battute o risponde con l'errore 24. |
| `[PAGAMENTI]` | vedi sotto | — | Le forme di pagamento del registratore. |

Le colonne sono 24 su tutti e due i modelli; il documento gestionale accetta
fino a 48 caratteri per riga e i messaggi fino a 35.

### Le forme di pagamento

Ogni pagamento di Facile finisce su una **forma di pagamento** del registratore,
indicata con un numero. Quella tabella è riprogrammabile e cambia da cliente a
cliente: per questo i numeri stanno in `rch.ini`, nella sezione `[PAGAMENTI]`.
I valori predefiniti sono quelli di fabbrica dei registratori con firmware 8.0.0
o successivo:

| Chiave | Predefinito | Chiave | Predefinito |
|---|---|---|---|
| `contante` | 1 | `non_riscosso_fattura` | 7 |
| `non_riscosso_beni` | 2 | `non_riscosso_ssn` | 8 |
| `assegni` | 3 | `sconto_a_pagare` | 9 |
| `elettronico` | 4 | `buoni_multiuso` | 10 |
| `tickets` | 5 | `buoni_celiachia` | 11 |
| `non_riscosso_servizi` | 6 | | |

!!! warning "Un numero sbagliato non dà errore"

    Il Print!F gestisce le forme da 1 a 30, il Print! 3.0 RT solo da 1 a 11.
    Un numero oltre il massimo non dà errore: il registratore usa l'ultima
    forma disponibile e l'incasso finisce sul totale sbagliato, che si scopre
    solo in chiusura. Controlla i numeri sulla programmazione della cassa
    installata. Un numero `0` disabilita la forma: in quel caso Facile segnala
    il pagamento come non supportato, che è meglio di un totale sbagliato.

### Resi e annulli

Sui registratori telematici il reso di una riga non esiste più: il reso si apre
con un documento di reso, che richiama lo scontrino originale, e le righe da
rendere si registrano come normali vendite. Facile lo fa da solo: quando registri
un [reso](../../vendite/vendita-al-banco.md#registrare-un-reso) apre il
documento di reso e manda le righe con la quantità positiva. Reso e annullo
riportano la matricola del registratore.

### Cosa non si può fare

- **Leggere lo stato della cassa.** Con lo XON/XOFF il registratore non
  risponde: Facile non legge matricola, numero dell'ultimo scontrino né
  ultimo azzeramento. Il numero degli scontrini lo conta Facile.
- **Vedere gli errori del registratore.** Un comando rifiutato si vede sul
  display e sulla stampa della cassa, non in Facile.
- **Righe a doppia altezza o in grassetto** nei documenti gestionali: il
  registratore non le prevede e vengono stampate normali.

??? note "Per l'assistenza: i comandi inviati con lo XON/XOFF"

    Gli importi sono in centesimi.

    | Operazione | Comando |
    |---|---|
    | Vendita | `"DESC"<prezzo>H<reparto>R`, con `<qta>*` davanti al prezzo se diversa da 1 |
    | Storno riga | prefisso `0M` |
    | Righe di descrizione aggiuntive | `"TESTO"@` |
    | Sconto / maggiorazione % su articolo | `<perc>*1M` / `<perc>*5M` |
    | Sconto / maggiorazione % su subtotale | `<perc>*2M` / `<perc>*6M` |
    | Sconto / maggiorazione a valore su articolo | `<imp>H3M` / `<imp>H7M` |
    | Sconto / maggiorazione a valore su subtotale | `<imp>H4M` / `<imp>H8M` |
    | Subtotale | `=` |
    | Acconto / omaggio / buono monouso | `<imp>H16M` / `<imp>H17M` / `<imp>H18M` |
    | Pagamento | `<imp>H<n>T`, oppure `<n>T` per chiudere sul residuo |
    | Cancellazione | `K` |
    | Annullo documento | `k` |
    | Documento gestionale | apertura `j`, righe `"TESTO"@`, chiusura `J` |
    | Codice fiscale del cliente | `"CODICE"@39F` |
    | Codice lotteria | `"CODICE"@37F` |
    | Codice a barre EAN-13 | `"CODICE"1Z` |
    | Reso da documento RT | `"ZZZZ-NNNN-gg-mm-aa-matricola"104M` |
    | Annullamento documento RT | `"ZZZZ-NNNN-gg-mm-aa-matricola"105M` |
    | Fattura interna (solo Print!F) | `9F` poi `"NNNNN"101M`, intestazioni `"TESTO"@38F` |
    | Entrate / prelievi di cassa | `<imp>H10M` / `<imp>H11M` |
    | Lettura e chiusura giornaliera | `x1Fc` / `z1Fc` |
    | Lettura e azzeramento reparti | `x2Fc` / `z2Fc` |
    | Selezione operatore | `<n>O` |
    | Apertura cassetto | `a` |
    | Messaggi sul display | `"RIGA 1"1%` e `"RIGA 2"2%` |

    Il dialetto XON/XOFF di RCH coincide con quello delle casse DTR e Custom,
    non con quello delle 3i: il codice lotteria va sul `37F` (il `38F` sono i
    dati del cliente), e acconto, omaggio e buono monouso sono `16M`, `17M` e
    `18M`. Comandi di un altro dialetto non danno errore, stampano la riga
    sbagliata.

## Multidriver di RCH

### Come funziona

Con la voce `RCH MULTIDRIVER SERVER` Facile non parla direttamente con il
registratore, ma attraverso il programma **MULTIDRIVER_APP** di RCH, che va
installato sulla postazione:

1. mentre batti lo scontrino, Facile scrive i comandi in un file nella cartella
   indicata da `PATH_IN`;
2. alla chiusura, rinomina il file in `scontrino.inp` e avvia il Multidriver;
3. il Multidriver consegna i comandi al registratore e scrive l'esito nella
   cartella indicata da `PATH_OUT`;
4. Facile legge l'esito: se il registratore ha segnalato un errore, o se manca
   la carta, avvisa l'operatore;
5. Facile prepara il file per lo scontrino successivo.

Facile **non ripete** uno scontrino andato male: il file è già passato al
registratore, e una seconda consegna stamperebbe due volte. L'avviso chiede
di controllare la stampa prima di proseguire.

### Il file RCH_Multidriver.ini

Si trova nella cartella `cfg` di Facile. Puoi partire dal
[file di esempio](../../../assets/modelli/RCH_Multidriver.ini), che riporta
anche le configurazioni per seriale, USB e rete.

| Sezione | Chiave | Descrizione |
|---|---|---|
| `[OPTIONS]` | `PATH_EXE` | Il percorso completo di `MULTIDRIVER_APP.exe`. |
| `[OPTIONS]` | `PATH_IN` | La cartella in cui Facile scrive i comandi. |
| `[OPTIONS]` | `PATH_OUT` | La cartella in cui il Multidriver scrive l'esito. Se manca, si usa `PATH_IN`. |
| `[OPTIONS]` | `IP`, `TCPPORT` | Indirizzo e porta, per il collegamento in rete. |
| `[OPTIONS]` | `USB` | `USB` per il collegamento USB. |
| `[OPTIONS]` | `SERIAL`, `SERIALCONF` | Numero della porta seriale e parametri, per esempio `9600,N,8,1`. |
| `[OPTIONS]` | `COL_PRIMA_RIGA` | Caratteri della riga di vendita; se manca, 35. |
| `[OPTIONS]` | `COL_RIGHE_AGG` | Caratteri delle righe aggiuntive; se manca, 25. |
| `[PAGAMENTI]` | vedi sotto | Le forme di pagamento del registratore. |

!!! warning "Le cartelle devono coincidere"

    `PATH_IN` e `PATH_OUT` devono essere le stesse impostate nel file
    `Multidriver.ini` del Multidriver, nella sua cartella di installazione. Se
    non coincidono, Facile non legge l'esito e un errore del registratore passa
    inosservato.

!!! note "Il collegamento seriale"

    Il Multidriver accetta solo porte seriali a una cifra: da `COM10` in su
    risponde *PORTA NON VALIDA*. Quando è possibile, preferisci il
    collegamento in rete.

### Le forme di pagamento

Valgono le stesse regole dello XON/XOFF, ma i valori predefiniti del file sono
diversi: sono quelli che Facile usava prima che la tabella diventasse
configurabile, e dalla sesta voce in avanti non coincidono con quelli di
fabbrica.

| Chiave | Predefinito nel file | Di fabbrica (firmware 8.0.0 e successivi) |
|---|---|---|
| `contante` | 1 | 1 |
| `non_riscosso_beni` | 2 | 2 |
| `assegni` | 3 | 3 |
| `elettronico` | 4 | 4 |
| `tickets` | 5 | 5 |
| `buoni_celiachia` | 6 | 11 |
| `non_riscosso_servizi` | 7 | 6 |
| `non_riscosso_fattura` | 8 | 7 |
| `non_riscosso_ssn` | 9 | 8 |
| `sconto_a_pagare` | 10 | 9 |
| `buoni_multiuso` | 11 | 10 |

Verifica sempre i numeri sulla programmazione della cassa installata (vedi
[Leggere la programmazione della cassa](#leggere-la-programmazione-della-cassa)):
un registratore con firmware 8.0.0 o successivo, mai riprogrammato, vuole i
valori di fabbrica.

### Cosa non si può fare

- **Leggere il numero dello scontrino:** il Multidriver non lo restituisce, e
  il numero lo conta Facile.
- **Il codice a barre sullo scontrino** non viene stampato con il Multidriver.

??? note "Per l'assistenza: i comandi inviati con il Multidriver"

    | Operazione | Comando |
    |---|---|
    | Vendita | `=R<rep>/$<prezzo>/(DESC)`, con `/*<qta>` se diversa da 1 |
    | Righe di descrizione aggiuntive | `="/?A/(TESTO)` |
    | Sconto / maggiorazione percentuale | `=%/*<perc>` / `=%+/*<perc>` |
    | Sconto / maggiorazione a valore | `=V/*<imp>` / `=V+/*<imp>` |
    | Subtotale | `=S` |
    | Acconto / omaggio / buono monouso | `=R<rep>/$<imp>/&2`, `/&1`, `/&3` |
    | Pagamento | `=T<n>/$<imp>`, con `/&<qta>` per i buoni pasto |
    | Cancellazione e chiave in registrazione | `=K` poi `=C1` |
    | Documento gestionale | `=o` per aprire e per chiudere, righe `="/(TESTO)` |
    | Codice fiscale | `="/?C/(CODICE)` |
    | Codice lotteria | `="/?L/$1/(CODICE)` |
    | Reso / annullamento documento RT | `=r/&ggmmaa/!0/[Z/]N/(matricola)` / `=k/...` |
    | Fattura libera | `=F/*5/$<imp>/&0/]1`, corpo `="/(TESTO)`, chiusura `=c` |
    | Entrate / prelievi | `=e/$<imp>` / `=p/$<imp>` |
    | Lettura e chiusura giornaliera | `=C2`/`=C3`, poi `=C10`, poi `=C1` |
    | Lettura e azzeramento reparti | `=C2`/`=C3`, poi `=C501/$1`, poi `=C1` |
    | Selezione operatore | `=O<n>` |
    | Apertura cassetto | `=C86` |
    | Messaggi sul display | `=D1/(RIGA 1)` e `=D2/(RIGA 2)` |

    Le chiavi sono `=C1` registrazione, `=C2` letture, `=C3` letture e
    azzeramenti, `=C4` programmazione, `=C5` service: ogni sequenza che cambia
    chiave torna in `=C1` alla fine. Nelle descrizioni non sono ammessi la
    barra, le parentesi tonde e la parola TOTALE: Facile le toglie prima di
    comporre il comando.

    Con le forme TICKETS l'importo è il totale e la quantità il numero di buoni:
    `=T5/$1000/&2` sono due buoni da cinque euro. È la convenzione opposta allo
    XON/XOFF, dove l'importo è il valore del singolo buono.

## Il display cliente

Il display attaccato al registratore si pilota attraverso il registratore. In
[Impostazioni Postazione](../../utility/impostazioni-postazione.md) scegli in
**Customer Display - 1** il tipo che corrisponde alla stampante fiscale, con la
stessa **Porta**:

| Stampante Fiscale | Customer Display |
|---|---|
| `RCH XON / XOFF (9600,N,8,1)` | `RCH XON/XOFF` |
| `RCH XON / XOFF LAN` | `RCH XON/XOFF LAN` |
| `RCH MULTIDRIVER SERVER` | `RCH MULTIDRIVER SERVER` |

Sul Print!F la seconda riga del display non è gestita e viene ignorata; sul
Print! 3.0 RT funziona. La parola TOTALE non è ammessa nei messaggi e viene
sostituita.

## Diagnostica

| Cosa | Dove |
|---|---|
| Il traffico verso il registratore | `log\socket_log.txt`, con il log seriale attivo nelle impostazioni |
| Gli esiti del Multidriver | `log\multidriver_log.txt`, con il log seriale attivo |
| Il log del Multidriver | Il file indicato in `LOGPATH` del file `multidriver.xml` del Multidriver, con `LOG=1` |
| I comandi di uno scontrino non consegnato | Nella cartella `PATH_IN`, un file `SCO<postazione>-<progressivo>.cmd` |

### Leggere la programmazione della cassa

Per sapere a quali numeri corrispondono le forme di pagamento di un registratore
collegato al Multidriver, si fa leggere al Multidriver la programmazione della
cassa: nella cartella di log del Multidriver compare il file `ECRData.out`, in
cui le righe `T001`, `T002` e seguenti riportano numero e descrizione di ogni
forma di pagamento. Sono quei numeri che vanno scritti nella sezione
`[PAGAMENTI]`.

<!-- DA VERIFICARE: le righe da mettere in scontrino.inp per far leggere al Multidriver la programmazione (nel documento tecnico «Gestione Driver RCH» sono andate perse) -->

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Attenzione! Il driver della cassa ha segnalato un errore: … Controllare la stampa prima di proseguire.* | Con il Multidriver, il registratore ha rifiutato lo scontrino o non è stato raggiungibile; al posto dei puntini c'è il testo dell'errore, vedi la tabella qui sotto. | Controlla che cosa è stato stampato. Facile non ristampa da solo: se lo scontrino non è uscito, ripetilo. |
| *Impossible Eseguire il protocollo di Shell!* | Il Multidriver non si è potuto avviare. | Controlla `PATH_EXE` in `RCH_Multidriver.ini`. |

I testi d'errore più comuni del Multidriver, in italiano o in inglese secondo la
lingua impostata nel Multidriver:

| Testo | Che cosa significa |
|---|---|
| `FINE CARTA - scontrino da ristampare` | Il registratore è rimasto senza carta durante la stampa. |
| `FINE CARTA` / `PAPER END` | Come sopra. |
| `CONNESSIONE RIFIUTATA` / `NOT CONNECTED EXCEPTION` | Il registratore non è raggiungibile. |
| `INDIRIZZO IP NON VALIDO` / `INVALID IP ADDRESS`, `PORTA NON VALIDA` / `INVALID IP PORT` | Indirizzo o porta sbagliati nella configurazione del Multidriver. |
| `ERRORE TIME OUT` / `TIME OUT EVENT ERROR` | Il registratore non ha risposto in tempo. |
| `ERRORE ESECUZIONE COMANDO` / `ERROR COMMAND EXECUTE`, `CODICE DI ERRORE` / `ERROR CODE` | Il registratore ha rifiutato un comando. |
| `ERRORE STATO PAGAMENTO FISCALE` / `FISCAL PAYMENT` | Il pagamento non è stato accettato. |
| `SCONTRINO.INP NON TROVATO` / `SCONTRINO.INP MISSING` | Il Multidriver non ha trovato il file: le cartelle non coincidono con quelle del suo `Multidriver.ini`. |

## Vedi anche

- [Registratori telematici](index.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
