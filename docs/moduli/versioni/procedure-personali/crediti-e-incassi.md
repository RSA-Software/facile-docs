---
title: Crediti e incassi
description: Sviluppo dei crediti mensili, registrazione dei crediti, estratti conto, incassi, rettifiche e il lato fornitori nella versione Studio.
modulo: Procedure Personali
maschera_id: IDD_STU_REG_CREDITI
---

# Crediti e incassi

Il ciclo del cliente: **nasce il credito, si incassa, si rettifica**, e quando
serve si emette la fattura.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Procedure Personali ▸ *(la voce)*
    - **Scorciatoia:** ++f2++ salva o conferma, ++f5++ seleziona lo scoperto, ++esc++ esce

---

## Sviluppo Crediti Mensili

Genera in un colpo solo **gli addebiti del mese per tutti i clienti** che hanno
un importo fisso concordato.

| Campo | Descrizione |
|---|---|
| **Causale Contabile** | La [causale](../../contabilita/causali-contabili.md) con cui nascono gli addebiti. |
| **Codice Iva** | L'[aliquota](../../contabilita/aliquote-iva.md) da applicare. |
| **Mese Accrediti** | Il mese da sviluppare. |
| **Data** | La data da mettere sugli addebiti. |
| **Sez.** | La [sezione](../../contabilita/sezioni.md). |

{: .campi }

++f2++ avvia; la barra in basso mostra l'avanzamento.

!!! warning "Sviluppare due volte lo stesso mese raddoppia gli addebiti"

    La procedura non controlla se quel mese è già stato sviluppato: rilanciarla
    crea **una seconda serie di addebiti**, identica alla prima. Non c'è un
    annullamento: gli addebiti in più vanno tolti uno per uno.

    Vale la pena tenere una nota di quali mesi sono già stati fatti — il
    programma non la tiene.

## Registrazione Crediti

Il singolo credito, a mano.

| Campo | Descrizione |
|---|---|
| **N. Registrazione** | Il numero della registrazione. |
| **Data Registrazione** | Quando nasce il credito. |
| **Cliente** | Chi deve. |
| **Cat. Economica** | La [categoria economica](../../anagrafiche/categorie-economiche.md) del cliente. |
| **Fisso** | L'importo fisso concordato, quello che lo sviluppo mensile userà. |
| **Importo** | L'importo di questa registrazione. |
| **Contropartita** | Mastro, conto e sottoconto su cui va il ricavo. |
| **Descrizione** | Che cosa si sta addebitando. |

{: .campi }

!!! tip "«Fisso» e «Importo» non sono la stessa cosa"

    **Importo** è quanto vale questa registrazione. **Fisso** è invece il valore
    di riferimento del cliente, quello che lo [sviluppo
    mensile](#sviluppo-crediti-mensili) riprende ogni mese: cambiarlo qui
    cambia gli addebiti futuri, non quelli già fatti.

## Registrazione Debiti

È **la stessa maschera**, dal lato del fornitore: al posto del cliente c'è il
fornitore, e il credito diventa un debito. Gli stessi campi, lo stesso modo di
compilarli.

## Estratti Conto Clienti e Fornitori

Aprono l'[estratto conto](../../contabilita/schede-contabili.md) — la scheda
contabile del soggetto — una volta sui clienti e una volta sui fornitori.

## Incassi Cliente

La finestra si chiama *Incassi Clienti*.

| Campo | Descrizione |
|---|---|
| **Cliente** | Di chi si sta incassando. |
| **Data** | La data dell'incasso. |

{: .campi }

Scelto il cliente, la griglia elenca le sue partite aperte. Si indica quanto si
incassa su ciascuna, e in basso i tre totali si aggiornano:

| Totale | Che cosa dice |
|---|---|
| **Importo** | Quanto si sta incassando. |
| **Scoperto** | Quanto resta ancora da incassare. |
| **SALDO** | Il saldo che rimane al cliente. |

++f5++ — **Seleziona Scoperto** — riempie da sé l'incasso con tutto lo scoperto,
invece di scriverlo riga per riga.

++f2++ registra, e l'incasso finisce in prima nota con la causale prevista.

!!! warning "Servono le causali configurate, e vengono chieste solo al momento di salvare"

    L'incasso scrive in prima nota, e per farlo pretende che le causali siano
    impostate nelle [impostazioni della ditta](../../anagrafiche/ditte.md). Se
    manca qualcosa lo dice **solo quando si salva**, dopo aver compilato tutto:

    | Messaggio | Che cosa manca |
    |---|---|
    | *Causale Contabile Incasso tramite Cassa non Impostata o non valida.* | La causale dell'incasso per cassa. |
    | *Causale Contabile Incasso tramite Banca non Impostata o non valida.* | Quella dell'incasso per banca. |
    | *Causale Contabile Rettifiche Clienti non Impostata o non Valida.* | La causale delle rettifiche. |
    | *Causale contabilizzazione IVA Fatture x Cassa non impostata o non valida.* | La causale IVA per gli incassi per cassa. |
    | *Causale contabilizzazione IVA Fatture x Banca non impostata o non valida.* | La stessa, per banca. |

## Incassi con Emissione Fattura

È la stessa finestra — *Incassi Clienti con Emissione Fattura* — ma oltre a
registrare l'incasso **emette la fattura** per quello che si sta incassando.
Si usa quando la fattura si fa al momento del pagamento e non prima.

## Rettifiche Clienti

Ancora la stessa finestra, intitolata *Rettifiche Clienti*, usata per
**correggere il dovuto** invece di incassarlo: abbuoni, storni, correzioni di
importi sbagliati. La rettifica va in prima nota con la sua causale.

!!! tip "Rettificare non è incassare"

    L'incasso dice «questo denaro è arrivato»; la rettifica dice «questo importo
    non era dovuto». Usare l'uno per l'altro fa tornare il saldo del cliente ma
    sballa la cassa — e la differenza si trova mesi dopo, quando non si ricorda
    più com'è andata.

## Pagamento Fornitori e Rettifiche Fornitori

Le stesse due finestre — *Pagamento Fornitori* e *Rettifiche Fornitori* — dal
lato dei fornitori, con le causali corrispondenti:

| Messaggio | Che cosa manca |
|---|---|
| *Causale Contabile Pagamento tramite Cassa non Impostata o non valida.* | La causale del pagamento per cassa. |
| *Causale Contabile Pagamento tramite Banca non Impostata o non valida.* | Quella per banca. |
| *Causale Contabile Rettifiche Fornitori non Impostata o non Valida.* | La causale delle rettifiche fornitori. |

## Emissione Fatture Crediti Mensili

Apre la maschera comune di [emissione fatture da
documenti](../../vendite/emissione-fatture-da-documenti.md), che trasforma in
fatture i crediti maturati.

## Vedi anche

- [Titoli, sospesi e analisi](titoli-e-analisi.md)
- [Schede contabili](../../contabilita/schede-contabili.md)
