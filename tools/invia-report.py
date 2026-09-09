"""Manda per email il report delle maschere che non si sono aperte.

Serve a chiudere il giro senza doversi ricordare di guardare il file: le
maschere che il programma rifiuta perche' l'archivio e' vuoto vanno rifatte su
un archivio popolato, e questa e' la lista.

    python tools/invia-report.py

La password si legge da FACILE_SMTP_PASSWORD, o da [email] in cattura.ini.
"""

import configparser
import json
import os
import smtplib
import ssl
import sys
from email.message import EmailMessage
from pathlib import Path

TOOLS = Path(__file__).resolve().parent


def main() -> None:
    cfg = configparser.ConfigParser()
    cfg.read(TOOLS / "cattura.ini", encoding="utf-8")
    if not cfg.has_section("email") or not cfg.getboolean("email", "attivo", fallback=False):
        print("invio email disattivato in cattura.ini")
        return

    report = json.loads((TOOLS / "catture-report.json").read_text(encoding="utf-8"))
    non_aperte = report.get("non_aperte") or []
    if not non_aperte:
        print("nessuna maschera da segnalare")
        return

    corpo = [
        f"Catture del {report['eseguito']}: {report['catturate']} su {report['totale']}.",
        "",
        f"{len(non_aperte)} maschere non si sono aperte — probabilmente l'archivio",
        "non ha i dati necessari. Vanno rifatte su un archivio popolato:",
        "",
    ]
    for e in non_aperte:
        corpo.append(f"- {e['titolo']}")
        corpo.append(f"    percorso: {e['percorso']}")
        corpo.append(f"    messaggio: {e.get('messaggio') or '(nessuno)'}")
        corpo.append(f"    comando: python tools/cattura-schermate.py --slug {e['slug']}")
        corpo.append("")

    messaggio = EmailMessage()
    messaggio["Subject"] = f"Manuale Facile — {len(non_aperte)} maschere da rifare"
    messaggio["From"] = cfg["email"]["mittente"]
    messaggio["To"] = cfg["email"]["destinatario"]
    messaggio.set_content("\n".join(corpo))

    password = os.environ.get("FACILE_SMTP_PASSWORD") or cfg["email"].get("password", "")
    if not password:
        sys.exit("manca la password SMTP (FACILE_SMTP_PASSWORD)")

    contesto = ssl.create_default_context()
    with smtplib.SMTP_SSL(cfg["email"]["server"], cfg.getint("email", "porta"), context=contesto) as smtp:
        smtp.login(cfg["email"]["mittente"], password)
        smtp.send_message(messaggio)
    print(f"inviata a {cfg['email']['destinatario']}: {len(non_aperte)} maschere")


if __name__ == "__main__":
    main()
