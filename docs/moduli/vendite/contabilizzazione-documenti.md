---
title: Contabilizzazione dei documenti
description: Come i documenti di vendita diventano registrazioni di prima nota, e come si controlla che le due cose corrispondano.
modulo: Vendite
maschera_id: IDD_VEN_FAT_CONTABILIZZA
---

# Contabilizzazione dei documenti

Un documento emesso non è ancora una registrazione contabile. **Contabilizza**
genera le registrazioni di [prima nota](../contabilita/registrazione-prima-nota.md)
dai documenti del periodo; **Controllo Fatture <-> Mov. Contabili** e
**Controllo Fat. Pro Forma <-> Mov. Contabili** verificano che documenti e
registrazioni corrispondano.

!!! info "In sintesi"

    - **Percorso:**
        - Menu ▸ Vendite ▸ Fatture ▸ Contabilizza
        - Menu ▸ Vendite ▸ Fatture Pro Forma ▸ Contabilizza
        - Menu ▸ Vendite ▸ Ricevute Fiscali ▸ Contabilizza
        - Menu ▸ Vendite ▸ Autofatture - Integrazioni ▸ Contabilizza
        - Menu ▸ Vendite ▸ Fatture ▸ Controllo Fatture <-> Mov. Contabili
        - Menu ▸ Vendite ▸ Fatture Pro Forma ▸ Controllo Fat. Pro Forma <-> Mov. Contabili
    - **Scorciatoia:** ++f2++ avvia, ++esc++ esce
    - **Permessi richiesti:** nessun profilo predefinito; le singole voci di menu si abilitano per ogni utente da [Archivi ▸ Utenti](../anagrafiche/utenti.md)

---

## A cosa serve

Chi emette i documenti e chi tiene la contabilità spesso non sono la stessa
persona: il documento nasce in Vendite e diventa una scrittura contabile in un
secondo momento. **Contabilizza** fa quel passaggio in blocco, sui documenti di
un periodo.

I due **Controllo <-> Mov. Contabili** servono dopo: dicono se qualche
documento è rimasto senza registrazione o se qualche registrazione non ha più
il suo documento.

## Prerequisiti

Prima di contabilizzare occorre:

- avere emesso e controllato i [documenti](documento-di-vendita.md) del
  periodo;
- avere sui documenti la **Cau. Contabile** giusta, perché è quella che decide
  registro e conti;
- avere il piano dei conti e le
  [causali contabili](../contabilita/causali-contabili.md) impostati;
- **avere una copia di sicurezza recente**.

## La maschera

![Contabilizzazione documenti](../../assets/img/vendite/contabilizzazione-documenti.png)

**Contabilizza** apre una finestra di selezione: in alto il registro e gli
intervalli di numero e di data, al centro i sei conti su cui imputare le voci
che non hanno una riga di merce, in basso la data della registrazione.

**Controllo <-> Mov. Contabili** invece **non ha nessuna finestra**: parte
subito, e parla solo con i messaggi che mostra.

## Campi

### Contabilizza

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Registro** | | Il registro dei documenti da contabilizzare. | da `A` a `Z` |
| **Da Numero**, **A Numero** | ● | L'intervallo dei numeri di documento. | numeri |
| **Da Data**, **A Data** | ● | Il periodo. | date |
| **Imputazione Bolli** | | Mastro, conto e sottoconto su cui girare i bolli. Accanto compare la descrizione del sottoconto. | codici del piano dei conti |
| **Imputazione Spese Accessorie** | | Il conto delle spese accessorie. | codici |
| **Imputazione Abbuoni** | | Il conto degli abbuoni. | codici |
| **Imputazione Acconti** | | Il conto degli acconti. | codici |
| **Imputazione Omaggi** | | Il conto degli omaggi. | codici |
| **Imputazione Ritenuta Acconto** | | Il conto della ritenuta d'acconto. | codici |
| **Data Contabilizzazione** | | La data da dare alle registrazioni. Lasciandola in bianco ogni registrazione prende **la data del suo documento**: è il caso normale. | data |

{: .campi }

I sei conti di imputazione servono per le voci del piede che non hanno una
riga di merce a cui agganciarsi. Vanno compilati una volta e restano.

### Controllo <-> Mov. Contabili

*Nessun campo.* Il controllo non chiede niente e lavora su **tutto l'anno di
lavoro**.
## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - OK** | ++f2++ | Avvia la contabilizzazione o il controllo. |
| **Esci** | ++esc++ | Chiude senza fare nulla. |
| **Interrompi** | | Durante l'elaborazione, ferma il lavoro. |

## Come si fa

### Contabilizzare le fatture del mese

1. Controlla le fatture con il [riepilogo](riepiloghi-e-statistiche.md).
2. Apri **Menu ▸ Vendite ▸ Fatture ▸ Contabilizza**.
3. Indica il periodo e avvia.
4. Apri la [gestione prima nota](../contabilita/gestione-prima-nota.md) e
   verifica le registrazioni generate.

### Verificare che nulla sia rimasto indietro

1. Apri **Menu ▸ Vendite ▸ Fatture ▸ Controllo Fatture <-> Mov. Contabili**.
2. Il controllo parte subito, senza chiedere niente, e scorre tutte le fatture
   contabilizzate dell'anno.
3. **Ogni anomalia è un messaggio a sé**, da chiudere con **OK**: tieni carta e
   penna, perché non resta un elenco.
4. Alla fine, se non c'è stato nessun messaggio, compare *Nessun errore
   riscontrato durante il controllo!*.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *(nessun messaggio, solo un segnale acustico)* | Manca una delle date, o il numero finale è minore di quello iniziale. | Compila o correggi il campo su cui si è posizionato il cursore. |
| *La Fattura N. … non risulta contabilizzata* | Il documento risulta contabilizzato, ma in prima nota non c'è nessuna registrazione con quel numero. | La registrazione è stata cancellata: rifalla a mano, oppure fai riportare il documento a *emesso* dall'assistenza e ricontabilizza. |
| *I Totali per la Fattura N. … e per il movimento Contabile N. … non coincidono.<br>Totale Fattura …   Totale Doc. …* | Il totale del documento e quello della registrazione sono diversi. | Quasi sempre il documento è stato corretto dopo la contabilizzazione: allinea la registrazione dalla [gestione prima nota](../contabilita/gestione-prima-nota.md). |
| *Esistono diversi movimenti contabili per la Fattura N. …<br><br>Mov. Prima Nota N. …* | Per quel documento ci sono più registrazioni. Ne vengono elencate fino a dieci. | Cancella quelle di troppo. |
| *Nessun errore riscontrato durante il controllo!* | Il controllo è finito senza trovare anomalie. | Nessuna azione. |

## Note

!!! note "Rilanciare la contabilizzazione non crea doppioni"

    La contabilizzazione prende **solo i documenti in stato *emesso***. Appena
    uno viene contabilizzato passa allo stato *contabilizzato* e la volta dopo
    non viene più preso: si può quindi rilanciare sullo stesso periodo senza
    paura, ed è anzi il modo normale di recuperare le fatture emesse dopo la
    prima passata.

    Se la registrazione non riesce, il documento **torna indietro a *emesso***:
    non resta mai un documento segnato come contabilizzato senza la sua
    registrazione.

    Le fatture ancora **salvate** e quelle **annullate** non vengono toccate.

!!! warning "Il controllo parla a messaggi, uno per volta"

    Non produce né una stampa né una griglia: per ogni anomalia apre una
    finestrella da chiudere con **OK**, e va avanti. Su un anno con molte
    discordanze diventa lungo — c'è il pulsante per interrompere
    l'avanzamento.

    Il controllo guarda **tutto l'anno di lavoro**, non un periodo, e confronta
    ogni documento *contabilizzato* con le registrazioni dei registri delle
    **fatture emesse** — comprese quelle a esigibilità differita e quelle CEE.
    Cerca tre cose: la registrazione che manca, il totale che non torna, e le
    registrazioni doppie.

    Il controllo parte **dai documenti**: una registrazione di prima nota senza
    più il suo documento non viene segnalata.

!!! note "Perché DDT, bolle e buoni non hanno la voce Contabilizza"

    Perché non sono documenti fiscali: non vanno sul registro IVA delle vendite
    e non c'è niente da registrare. Quello che si contabilizza è la **fattura
    che ne deriva** — la fattura differita o quella immediata — e infatti
    **Contabilizza** compare solo su fatture, ricevute fiscali, autofatture e
    fatture pro forma.

## Vedi anche

- [Documento di vendita](documento-di-vendita.md)
- [Registrazione di prima nota](../contabilita/registrazione-prima-nota.md)
- [Causali contabili](../contabilita/causali-contabili.md)
