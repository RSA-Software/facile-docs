"""Estrae le etichette dei campi dalle maschere di Facile.

Serve perche' le etichette NON stanno nel file .rc come testo: i controlli
`pvtext3d` sono ActiveX e la loro didascalia e' sepolta nei blocchi DLGINIT,
come flusso di parole esadecimali. Senza questo script le maschere si possono
leggere solo aprendo il programma.

Uso:

    .venv/Scripts/python.exe tools/etichette-maschere.py <file.rc> [IDD_FILTRO]

Esempi:

    ... tools/etichette-maschere.py C:/rsawin/Facile/RSAFornitori/RSAFornitori.rc IDD_FOR_FORNITORI_GENERALE
    ... tools/etichette-maschere.py C:/rsawin/Facile/RSATblCom/RSATblCom.rc IDD_TBC_BANCHE

Il filtro e' una sottostringa: per un confronto esatto filtrare l'output, per
esempio con awk sulla riga "=== <IDD>".

Note:
  - i sorgenti sono CP1252, non UTF-8 (vedi la memoria facile-encoding-cp1252):
    il file viene letto con quella codifica e le accentate restano corrette;
  - le stringhe di un solo carattere vengono scartate: per vedere combo con
    valori come "=", "+", "--" abbassare MIN_LEN a 1;
  - le colonne delle griglie compaiono nella riga del controllo SPREAD, in
    fondo, dopo molto rumore binario;
  - questo script legge il disegno della maschera, non il codice: campi
    nascosti o rinominati a runtime (per versione, o secondo i dati azienda)
    vanno cercati nel .cpp corrispondente.
"""

import re
import sys

MIN_LEN = 2
RUMORE_FONT = ("MS Sans Serif", "MS Shell Dlg", "Tahoma", "Arial", "Segoe")


def blocchi_dlginit(percorso: str) -> dict[str, list[tuple[str, bytes]]]:
    """Restituisce {IDD: [(IDC, byte del blocco), ...]}."""
    testo = open(percorso, "rb").read().decode("cp1252")
    righe = testo.splitlines()
    blocchi: dict[str, list[tuple[str, bytes]]] = {}

    i = 0
    while i < len(righe):
        m = re.match(r"^(IDD_\w+)\s+DLGINIT\s*$", righe[i])
        if not m:
            i += 1
            continue
        idd = m.group(1)
        i += 2  # salta la riga BEGIN
        voci: list[tuple[str, bytes]] = []
        idc = None
        dati = bytearray()
        while i < len(righe) and righe[i].strip() != "END":
            intestazione = re.match(
                r"^\s+(IDC_\w+),\s*0x[0-9a-fA-F]+,\s*(\d+),\s*0\s*$", righe[i]
            )
            if intestazione:
                if idc:
                    voci.append((idc, bytes(dati)))
                idc = intestazione.group(1)
                dati = bytearray()
            else:
                for parola in re.findall(r"0x([0-9a-fA-F]{1,4})", righe[i]):
                    v = int(parola, 16)
                    dati.append(v & 0xFF)
                    dati.append((v >> 8) & 0xFF)
            i += 1
        if idc:
            voci.append((idc, bytes(dati)))
        blocchi[idd] = voci
        i += 1
    return blocchi


def stringhe(dati: bytes) -> list[str]:
    fuori: list[str] = []
    corrente = bytearray()
    for ch in dati:
        if 32 <= ch <= 126 or 0xC0 <= ch <= 0xFF or ch in (0xE0, 0xE8, 0xE9, 0xEC, 0xF2, 0xF9, 0xB0):
            corrente.append(ch)
        else:
            if len(corrente) >= MIN_LEN:
                fuori.append(corrente.decode("cp1252"))
            corrente = bytearray()
    if len(corrente) >= MIN_LEN:
        fuori.append(corrente.decode("cp1252"))
    return fuori


def ripulisci(grezze: list[str]) -> list[str]:
    tenute: list[str] = []
    for s in grezze:
        if re.fullmatch(r"[0-9A-F]{16,}X?#?", s):  # il GUID del controllo
            continue
        if any(f in s for f in RUMORE_FONT):
            s = s
            for f in RUMORE_FONT:
                s = s.replace(f, "")
            s = s.strip()
            if len(s) < MIN_LEN:
                continue
        if s not in tenute:
            tenute.append(s)
    return tenute


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    percorso = sys.argv[1]
    filtro = sys.argv[2] if len(sys.argv) > 2 else None

    for idd, voci in blocchi_dlginit(percorso).items():
        if filtro and filtro not in idd:
            continue
        print("===", idd)
        for idc, dati in voci:
            testi = ripulisci(stringhe(dati))
            print("  %-32s %s" % (idc, " | ".join(testi)))


if __name__ == "__main__":
    main()
