---
title: Esecuzione continua del connettore Shopify
description: L'operazione 979 esegue a giri le operazioni Shopify scelte nel file ini, ciascuna con la sua frequenza, finché non la si ferma con il flag exit o con il file di stop.
modulo: E-commerce ▸ Shopify
---

# Esecuzione continua

Invece di pianificare un'attività per ogni operazione, l'operazione **979**
le esegue tutte da un solo file di configurazione: fa le operazioni accese,
una dopo l'altra, aspetta qualche minuto e ricomincia. Si avvia una volta,
per esempio all'accensione del computer, e lavora finché non la si ferma.

!!! info "In sintesi"

    - **Operazione:** 979, con la sezione `[CICLO]` nel file di configurazione
    - **Per ogni operazione:** `0` = no, `1` = a ogni giro, un numero = al
      massimo una volta ogni tanti secondi
    - **Per fermarla:** `exit = 1` nella sezione `[CICLO]`, oppure il file di
      stop
    - **Una sola copia** per file di configurazione

---

## La sezione [CICLO]

```ini
[COMMAND]
operation         = 979
interval          = 2

[CICLO]
pausa             = 300
exit              = 0
setup             = 0
abbina            = 0
ordini            = 1
prodotti          = 3600
giacenze          = 1
prezzi            = 1
ingrosso          = 0
stato_ordini      = 0
immagini          = 86400
```

| Chiave | Descrizione |
|---|---|
| `pausa` | I secondi di attesa fra la fine di un giro e l'inizio del successivo. Il minimo è 10; se manca, 300 (5 minuti). |
| `exit` | Con `1` il ciclo si ferma, e finché resta a `1` non riparte. Vedi [Fermare il ciclo](#fermare-il-ciclo). |
| `setup` | La [configurazione](installazione.md#4-lancia-la-configurazione) del negozio (988). Normalmente `0`: si lancia a mano all'installazione. |
| `abbina` | L'[abbinamento](installazione.md#5-abbina-il-catalogo-gia-presente) del catalogo esistente (987). Normalmente `0`. |
| `ordini` | L'[importazione degli ordini](ordini.md) (980). Quanti giorni rileggere lo dice `interval` nella sezione `[COMMAND]`. |
| `prodotti` | [Prodotti e collezioni](prodotti-e-immagini.md) (984). |
| `giacenze` | Le [giacenze](giacenze-e-prezzi.md) (982). |
| `prezzi` | I [prezzi](giacenze-e-prezzi.md#i-prezzi) (983). |
| `ingrosso` | Il [listino ingrosso](giacenze-e-prezzi.md#il-listino-ingrosso) (991), solo con `modalita = MISTO`. |
| `stato_ordini` | Lo [stato degli ordini](ordini.md#comunicare-a-shopify-gli-ordini-evasi-o-annullati) verso Shopify (990). |
| `immagini` | Le [immagini](prodotti-e-immagini.md#le-immagini) (985). |

Per ciascuna operazione il valore significa:

| Valore | Significato |
|---|---|
| `0`, o chiave assente | L'operazione non si fa. |
| `1` | L'operazione si fa a ogni giro. |
| Un numero di secondi | L'operazione si fa al massimo una volta ogni tanti secondi: `3600` ogni ora, `86400` una volta al giorno. |

Nell'esempio, a ogni giro si importano gli ordini e si aggiornano giacenze e
prezzi; i prodotti si controllano una volta all'ora e le immagini una volta
al giorno.

Tutte le altre sezioni — `[LOGIN]`, `[ECOMMERCE]`, `[ARTICOLI]`, `[STATI]`,
`[PAGAMENTI]`, `[STATO_ORDINI]`, `[TAGLIECOL]` — stanno nello stesso file e
valgono per tutte le operazioni: vedi [Il file di configurazione](configurazione.md).

## Come lavora

1. Al primo giro si fanno **tutte** le operazioni accese.
2. Le operazioni si fanno sempre in quest'ordine: configurazione,
   abbinamento, ordini, prodotti, giacenze, prezzi, listino ingrosso, stato
   degli ordini, immagini. Gli ordini vengono prima delle giacenze perché
   l'ordinato clienti riduce la disponibilità; le immagini sono per ultime
   perché sono le più lente.
3. Dal secondo giro in poi, un'operazione con un numero di secondi si fa
   solo se dall'ultima volta è passato almeno quel tempo.
4. Finito il giro, il programma aspetta `pausa` secondi e ricomincia.

Un'operazione che finisce con un errore **non ferma** le altre: il registro
lo riporta e il giro continua. Al giro successivo l'operazione ci riprova.

Il ciclo scrive nel registro `operation_979_<data>.txt`, che **cambia file
ogni giorno** anche se il programma resta acceso. All'avvio il registro
riporta la pausa e quali operazioni sono accese, con la loro frequenza; a
ogni giro, la durata di ogni operazione e del giro intero.

## Una sola copia per file

Il ciclo non può girare due volte con lo stesso file di configurazione, perché
due copie lavorerebbero insieme sullo stesso negozio. Una seconda copia
lanciata mentre la prima è accesa scrive nel registro

```
Ciclo Shopify gia' in esecuzione con ciclo_shopify.ini: questa copia si ferma
```

e si chiude. Se il programma si chiude in modo anomalo, il blocco si libera
da solo e il ciclo si può rilanciare subito.

## Fermare il ciclo

Ci sono due modi.

**Con il flag `exit`.** Apri il file di configurazione, imposta `exit = 1`
nella sezione `[CICLO]` e salva. Il ciclo si ferma entro un secondo se è in
pausa, alla fine dell'articolo che sta inviando se è dentro un'operazione
lunga (prodotti, prezzi, immagini), alla fine dell'operazione in corso
negli altri casi. Finché `exit` resta a `1` il ciclo **non riparte**, nemmeno
se viene rilanciato: per farlo ripartire rimetti `exit = 0`.

**Con il file di stop.** Crea nella cartella `cfg` un file vuoto con lo
stesso nome del file di configurazione ed estensione `.stop`, per esempio
`ciclo_shopify.stop`. Il ciclo si ferma negli stessi momenti e **cancella il
file**, così al prossimo avvio riparte normalmente.

| | `exit = 1` | File di stop |
|---|---|---|
| Ferma il ciclo in corso | Sì | Sì |
| Impedisce le partenze successive | Sì, finché resta a 1 | No: il file viene cancellato |
| Adatto per | Sospendere il collegamento, per esempio durante una manutenzione | Fermare e far ripartire, per esempio prima di un aggiornamento di Facile |

Fermare il ciclo a metà di un'operazione non lascia niente a metà: gli
articoli già inviati restano inviati, quelli rimasti partono al prossimo
avvio.

!!! warning "Non chiudere il programma a forza"

    Chiudere FacileToWeb dal Task Manager mentre lavora non rovina i dati, ma
    l'articolo in corso di invio viene rimandato per intero al giro dopo.
    Usa `exit` o il file di stop.

## Avviarlo con il computer

1. Prepara il file di configurazione con la sezione `[CICLO]` e lancialo una
   volta a mano, per controllare il registro del primo giro.
2. Fermalo con `exit = 1`, poi rimetti `exit = 0`.
3. Crea nell'Utilità di pianificazione un'attività che avvii FacileToWeb
   **all'avvio del computer**, come descritto in
   [E-commerce](../index.md#avviarlo-a-orari-fissi), con i parametri per
   esempio `-iniciclo_shopify.ini -ditta1`.
4. Riavvia il computer, oppure avvia l'attività a mano: nel registro di oggi
   compare `Ciclo Shopify: inizio del giro 1`.

## Messaggi principali

| Riga del registro | Che cosa significa |
|---|---|
| `Ciclo Shopify: pausa di N s fra un giro e l'altro; per fermarlo [CICLO] exit = 1 o il file ...` | Il ciclo è partito. |
| `Ciclo Shopify: attive ...`, `Ciclo Shopify: spente ...` | Le operazioni accese, con la loro frequenza, e quelle spente. |
| `Ciclo Shopify: nessuna operazione attiva in [CICLO] di ...` | Tutte le operazioni sono a `0`: il ciclo non parte. |
| `Ciclo Shopify: ... finita con errori in N s` | L'operazione ha avuto degli errori, descritti nelle righe precedenti. Il ciclo continua. |
| `Ciclo Shopify: ... interrotta da un errore ...` | L'operazione si è fermata per un errore imprevisto. Il ciclo continua con la successiva. |
| `Ciclo Shopify: fine del giro N in N s, operazioni N (con errori N); il prossimo fra N s` | Il riepilogo del giro. |
| `Ciclo Shopify: [CICLO] exit = 1 in ..., il ciclo non parte` | È stato lanciato con `exit = 1`. |
| `Ciclo Shopify fermato da [CICLO] exit = 1 (per ripartire rimetterlo a 0)` | Fermato con il flag. |
| `Ciclo Shopify fermato dal file di stop` | Fermato con il file di stop, che è stato cancellato. |
| `Ciclo Shopify: tolto il file di stop rimasto da un arresto precedente (...)` | All'avvio c'era un file di stop dimenticato: è stato tolto e il ciclo parte. |
| `Prodotti: arresto richiesto, gli articoli rimasti si inviano al prossimo avvio` | L'arresto è arrivato durante un'operazione lunga. Lo stesso per prezzi e immagini. |

## Vedi anche

- [Il file di configurazione](configurazione.md)
- [E-commerce: avvio e registro di FacileToWeb](../index.md)
- [Messaggi del registro](messaggi.md)
