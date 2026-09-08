---
title: Gestione compleanni
description: L'elenco dei clienti che compiono gli anni in un periodo, da cui mandare gli auguri per email o SMS.
modulo: Archivi
maschera_id: IDD_CLI_COMPLEANNI
---

# Gestione compleanni

Chiede un periodo e mostra i clienti che compiono gli anni in quei giorni. Da
lì si mandano gli auguri per email o SMS, o si stampa l'elenco.

!!! info "In sintesi"

    - **Percorso:** Menu ▸ Archivi ▸ Clienti ▸ Gestione Compleanni
    - **Scorciatoia:** ++f2++ seleziona, ++f4++ email, ++f5++ SMS, ++f6++ stampa
    - **Permessi richiesti:** nessun profilo predefinito; la voce di menu si abilita per ogni utente da [Archivi ▸ Utenti](utenti.md)

---

## A cosa serve

È una cortesia commerciale che si automatizza: ogni lunedì si guardano i
compleanni della settimana e si manda un messaggio. Funziona solo per i clienti
di cui si è registrata la data di nascita.

## Prerequisiti

Prima di usare questa maschera occorre:

- avere la **data di nascita** compilata nell'anagrafica dei
  [clienti](anagrafica-clienti.md): chi non ce l'ha non compare;
- avere i recapiti — email o cellulare — dei clienti a cui si vuole scrivere;
- avere impostato l'indirizzo del mittente, altrimenti l'invio si ferma.

## La maschera

![Gestione compleanni](../../assets/img/anagrafiche/gestione-compleanni.png)

La finestra *Gestione Compleanni* ha in alto **Data Iniziale** e **Data
Finale**, sotto la griglia dei festeggiati e in basso i sei pulsanti.

La griglia ha queste colonne:

| Colonna | Contenuto |
|---|---|
| **Sel** | La spunta che include la riga nell'invio. |
| **Sms**, **Mail** | Segnano se il cliente è raggiungibile per SMS o per posta. |
| **Compleanno** | Il giorno in cui li compie. |
| **Data Nascita** | La data di nascita registrata. |
| **Cognome e Nome** | Il cliente. |
| **Telefono**, **Telefoni Cellulari**, **Cellulare 2**, **Cellulare 3** | I recapiti telefonici. |
| **Email** | L'indirizzo di posta. |
| **Indirizzo**, **Città**, **Cap**, **Prov** | L'indirizzo postale. |

## Campi

| Campo | Obbl. | Descrizione | Valori ammessi |
|---|:---:|---|---|
| **Data Iniziale** | ● | Primo giorno del periodo da esaminare. | data |
| **Data Finale** | ● | Ultimo giorno del periodo. | data |

{: .campi }

Il periodo si legge su giorno e mese: l'anno di nascita non entra nel
confronto.

## Pulsanti e comandi

| Comando | Scorciatoia | Effetto |
|---|---|---|
| **F2 - Selez.** | ++f2++ | Spunta tutte le righe. |
| **F3 - Deselez.** | ++f3++ | Toglie la spunta a tutte le righe. |
| **F4 - Email** | ++f4++ | Manda l'email di auguri ai selezionati. |
| **F5 - SMS** | ++f5++ | Manda l'SMS di auguri ai selezionati. |
| **F6 - Stampa** | ++f6++ | Stampa l'elenco. |
| **Esci** | ++esc++ | Chiude la finestra. |

## Come si fa

### Mandare gli auguri della settimana

1. Apri **Menu ▸ Archivi ▸ Clienti ▸ Gestione Compleanni**.
2. Indica **Data Iniziale** e **Data Finale** della settimana.
3. Guarda la colonna **Mail**: solo chi è segnato riceverà l'email.
4. Premi **F2 - Selez.** per spuntare tutti, poi togli la spunta a chi non
   vuoi scrivere.
5. Premi **F4 - Email**.

### Mandare gli SMS a chi non ha l'email

1. Imposta il periodo.
2. Premi **F3 - Deselez.** e spunta a mano solo le righe con la colonna **Sms**
   valorizzata e la colonna **Mail** vuota.
3. Premi **F5 - SMS**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Indirizzo email del mittente non impostato!* / *Impossibile procedere* | Manca l'indirizzo da cui inviare. | Impostalo nei dati dell'[utente](utenti.md) o della [ditta](ditte.md) e riprova. |

## Note

!!! note "Chi non ha la data di nascita non compare"

    L'elenco si costruisce sulla data di nascita registrata in anagrafica: i
    clienti che non ce l'hanno non compaiono, per quanto si allarghi il
    periodo. Vale soprattutto per le persone giuridiche, che una data di
    nascita non ce l'hanno.

<!-- DA VERIFICARE: come si compone il testo degli auguri: non ho individuato il punto in cui si scrive. -->

<!-- DA VERIFICARE: se il programma tenga traccia degli auguri già mandati, per non ripeterli. -->

<!-- DA VERIFICARE: a cosa servono le colonne mmdd, Cod_Cli, Cod_Fid e Data Nas. che compaiono in coda alla griglia. -->

## Vedi anche

- [Anagrafica clienti](anagrafica-clienti.md)
- [Mailing list](mailing-list.md)
