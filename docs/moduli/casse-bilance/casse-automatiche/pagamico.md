---
title: Cassa automatica PagAmico
description: Come Facile incassa con la cassa automatica PagAmico attraverso il FacileWebApiService, come si configura il collegamento e come si leggono gli esiti degli incassi.
modulo: Casse e Bilance
---

# Cassa automatica PagAmico

La PagAmico è la cassa automatica rendiresto di PayPrint. Facile non la
comanda direttamente: la pilota il **FacileWebApiService**, e Facile chiede al
servizio di incassare, di erogare o di leggere lo stato della macchina.

!!! info "In sintesi"

    - **Voce:** `PAGAMICO` in **Cassa Automatica**, in [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
    - **Serve:** il FacileWebApiService installato e configurato
    - **Configurazione:** la macchina nel servizio ([casse_automatiche.json](../../../assets/modelli/casse_automatiche.json)), la scelta della macchina nella postazione ([pagamico.ini](../../../assets/modelli/pagamico.ini))
    - **Uso al banco:** vedi [Incassare con la cassa automatica PagAmico](../../vendite/vendita-al-banco.md#incassare-con-la-cassa-automatica-pagamico)
    - **Licenza:** separata, in aggiunta a quella di Facile

---

## Come funziona

```
Facile  ──►  FacileWebApiService  ──►  PagAmico
             (cfg\casse_automatiche.json)   (rete, porta 9100)
```

1. Quando chiudi lo scontrino con il rendiresto, Facile chiede al servizio di
   aprire un incasso per il totale.
2. Il servizio manda il comando alla macchina e ne raccoglie gli aggiornamenti:
   Facile li legge e mostra quanto il cliente ha già inserito.
3. A incasso finito il servizio comunica l'**esito** — vedi più sotto — e
   Facile chiude lo scontrino con il contante incassato.

Il servizio tiene un **giornale** di ogni cassa, con tutti i comandi e le
risposte della macchina: serve a ricostruire un incasso quando qualcosa va
storto.

Lo stesso servizio e la stessa macchina li usa anche RistoFacile: la
configurazione è una sola.

## Prerequisiti

- La **licenza** del collegamento con le casse automatiche, separata da quella
  di Facile.
- Il **FacileWebApiService** installato, in esecuzione e raggiungibile dalla
  postazione, configurato in **Impostazioni Postazione ▸ Impostazione
  FacileWebApiService** (vedi [Impostazioni Postazione](../../utility/impostazioni-postazione.md)).
- La PagAmico collegata alla rete, con un **indirizzo fisso**.
- **Nessun altro programma collegato alla macchina** mentre lavora il servizio:
  la PagAmico accetta un solo collegamento alla volta, e dopo una caduta
  riaccetta solo lo stesso computer. I programmi di prova del fornitore e l'app
  di simulazione vanno chiusi.

## Configurare il collegamento

### 1. La macchina nel servizio

Le casse automatiche si configurano nel servizio, nel file
`cfg\casse_automatiche.json` della sua cartella di installazione. Si può
compilare dalle impostazioni di RistoFacile oppure a mano, partendo dal
[file di esempio](../../../assets/modelli/casse_automatiche.json):

```json
{
  "CasseAutomatiche": [
    {
      "Id": 1,
      "Descrizione": "Cassa 1",
      "Tipo": "PagAmico",
      "Indirizzo": "192.168.1.61",
      "Porta": 0,
      "Password": "",
      "Predefinita": true,
      "PosAbilitato": false
    }
  ]
}
```

| Campo | Descrizione |
|---|---|
| `Id` | Il numero della cassa, che le postazioni usano per sceglierla. |
| `Descrizione` | Come la chiamate in negozio, per esempio *Cassa 1*. |
| `Tipo` | `PagAmico`. |
| `Indirizzo` | L'indirizzo di rete della macchina. Senza indirizzo la cassa non è considerata configurata. |
| `Porta` | `0` per quella di fabbrica, la 9100. |
| `Password` | La password di erogazione, se è impostata nel setup della macchina: senza, la macchina rifiuta i comandi che fanno uscire denaro, come il prelievo. |
| `Predefinita` | `true` per la cassa da usare quando la postazione non ne indica una. |
| `PosAbilitato` | `true` solo se alla macchina è collegato un POS attivo. |

Il servizio rilegge il file a ogni richiesta: dopo una modifica non serve
riavviarlo.

### 2. La postazione

1. Apri **Menu ▸ Utility ▸ Impostazioni Postazione**.
2. In **Cassa Automatica** scegli `PAGAMICO`.
3. Se nel servizio c'è più di una cassa, indica quale usa questa postazione nel
   file `cfg\pagamico.ini` di Facile, chiave `id_cassa` della sezione
   `[OPTIONS]`, con il suo `Id` ([file di esempio](../../../assets/modelli/pagamico.ini)).
   Senza il file, o con `0`, si usa la cassa **predefinita**, oppure la prima
   configurata se nessuna è predefinita.
4. Premi **F2 - OK**.
5. Apri il banco: se la macchina segnala scorte basse o cassetti pieni, l'avviso
   compare già all'apertura della schermata.

## Che cosa si fa da Facile

| Operazione | Dove | Vedi |
|---|---|---|
| Incassare uno scontrino | ++f6++ **Rendiresto** nella chiusura della vendita, o il tasto **PagAmico** sul **Pos Touchscreen** | [Incassare con la cassa automatica](../../vendite/vendita-al-banco.md#incassare-con-la-cassa-automatica-pagamico) |
| Vedere quanti pezzi di ogni taglio ci sono | **Funzioni ▸ Cassa Automatica ▸ Mostra Livelli** | [Gestire la cassa PagAmico](../../vendite/vendita-al-banco.md#gestire-la-cassa-pagamico) |
| Prelevare contante | **Funzioni ▸ Cassa Automatica ▸ Preleva Contante** | come sopra |
| Chiudere un incasso rimasto aperto | **Funzioni ▸ Cassa Automatica ▸ Chiudi Incasso Sospeso** | come sopra |
| Ricaricare il fondo cassa | **Funzioni ▸ Cassa Automatica ▸ Ricarica Fondo Cassa** | [Ricaricare il fondo cassa](#ricaricare-il-fondo-cassa) |
| Rendere il denaro di un reso | Il reso al banco, chiuso con il rendiresto | [Registrare un reso](../../vendite/vendita-al-banco.md#registrare-un-reso) |

Gli **svuotamenti** non si fanno da Facile: si fanno dal pannello della
macchina, seguendo il manuale del fornitore.

## Ricaricare il fondo cassa

Per mettere nella macchina il fondo cassa — monete e banconote per il resto:

1. Dal **Pos Touchscreen** apri **Funzioni ▸ Cassa Automatica** e premi
   **Ricarica Fondo Cassa**.
2. Si apre la finestra **Ricarica Fondo Cassa** con *Inserire monete e
   banconote nella cassa*: inserisci il denaro; la finestra mostra quanto è
   già stato caricato.
3. Quando hai finito premi **Annulla** e conferma con **Sì** la domanda
   *Terminare la ricarica del fondo cassa?*.
4. A ricarica chiusa compare *Importo Caricato nella Cassa*, con il totale.

La ricarica si può chiudere anche dal pannello della macchina: Facile se ne
accorge e mostra lo stesso il totale.

Se dopo la conferma la finestra resta aperta — la macchina non ha ancora chiuso
la ricarica, o l'ha rifiutata — premi di nuovo **Annulla**: puoi ripetere la
richiesta, continuare ad aspettare o smettere di aspettare.

Mentre una ricarica è aperta la macchina non incassa. Se Facile si chiude a
ricarica aperta, ripremendo **Ricarica Fondo Cassa** la si riprende da dove era
rimasta.

## Gli esiti di un incasso

Il servizio chiude ogni incasso con uno di questi esiti:

| Esito | Che cosa è successo | Che cosa fa Facile |
|---|---|---|
| **Completato** | Il cliente ha pagato tutto e la macchina ha reso il resto. | Chiude lo scontrino. Se una parte del resto non è uscita per mancanza di tagli, lo dice e indica la cifra da dare a mano. |
| **Trattenuto** | L'incasso è stato chiuso tenendo il denaro inserito: è un **pagamento parziale**. | Registra quanto è entrato e lascia lo scontrino aperto per il resto. |
| **Annullato** | L'incasso è stato chiuso restituendo il denaro al cliente. | Non registra niente; avvisa se è tornato meno di quanto era entrato. |
| **Rifiutato** | La macchina non ha accettato il comando: occupata, fuori servizio, importo fuori limite. Non è entrato niente. | Mostra il messaggio del servizio: si può ripetere. |
| **Errore** | La macchina ha risposto con un errore a incasso aperto. | Mostra il messaggio del servizio. |
| **Incerto** | La comunicazione si è interrotta a incasso aperto: il denaro potrebbe essere dentro la macchina, e non si sa quanto. | Mostra il messaggio del servizio. **Non ripetere l'incasso** prima di aver guardato la macchina. |

!!! warning "Prima di ripetere un incasso, guarda la macchina"

    Dopo un esito **incerto**, o dopo che Facile o il servizio si sono chiusi a
    metà di un incasso, guarda il display della PagAmico. Se l'incasso è ancora
    aperto chiudilo con **Chiudi Incasso Sospeso**, restituendo o trattenendo
    il denaro, e controlla sul display l'importo effettivamente trattenuto
    prima di registrare la vendita.

## Quando qualcosa non va

| Sintomo | Causa probabile | Cosa fare |
|---|---|---|
| *Assenza di Comunicazione con la cassa automatica…* con il motivo del servizio | Il servizio non risponde, oppure non raggiunge la macchina. | Controlla che il servizio sia avviato (**F3 - Test** in **Impostazione FacileWebApiService**) e che la macchina sia accesa e raggiungibile. |
| Il servizio risponde *Nessuna cassa automatica configurata su questo impianto* | Manca `casse_automatiche.json`, o la cassa non ha l'indirizzo. | Configura la macchina nel servizio. |
| Il servizio risponde *Nessuna cassa automatica con identificativo …* | L'`id_cassa` della postazione non corrisponde a nessuna cassa del servizio. | Correggi `pagamico.ini`. |
| *Incasso in corso su questa cassa: l'operazione si puo' fare solo a incasso chiuso.* | Un'altra postazione, o RistoFacile, sta incassando sulla stessa macchina. | Aspetta la fine di quell'incasso. |
| La macchina rifiuta il prelievo | Manca la password di erogazione. | Indica `Password` in `casse_automatiche.json`. |
| La macchina non risponde dopo una caduta di rete | È collegata a un altro programma, oppure aspetta il computer di prima. | Chiudi gli altri programmi collegati alla macchina; il servizio deve girare sempre sullo stesso computer. |

Per ricostruire un incasso, il giornale del servizio è nella sua cartella di
installazione, in `Log\CasseAutomatiche`, un file per cassa e per giorno:
`cassa-<numero>-<AAAAMMGG>.log`.

I messaggi che compaiono al banco durante un incasso, con la causa e il
rimedio, sono in [Vendita al banco](../../vendite/vendita-al-banco.md#quando-si-incassa-con-la-cassa-automatica-pagamico).

## Vedi anche

- [Casse automatiche](index.md)
- [Vendita al banco](../../vendite/vendita-al-banco.md)
- [Impostazioni Postazione](../../utility/impostazioni-postazione.md)
