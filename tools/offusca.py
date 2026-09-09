"""Offuscamento dei dati personali negli screenshot del manuale.

Il manuale e' pubblico e indicizzabile: ragioni sociali, nomi e cognomi,
partite IVA, codici fiscali, telefoni, cellulari ed email non devono restare
leggibili, nemmeno se lo screenshot viene da un archivio dimostrativo.

Due reti, in cascata:

1. **Per controllo.** Le maschere sono dialog MFC: ogni campo e' una finestra
   figlia con un identificatore numerico che `resource.h` traduce in un nome
   parlante (`IDC_CLI_RAGSOC`, `IDC_FOR_PIVA`...). Le regole in
   `regole-privacy.yml` lavorano su quei nomi: e' il modo deterministico, non
   dipende da cosa c'e' scritto a video.
2. **Per testo (OCR).** Rete di sicurezza per griglie ed elenchi, dove i dati
   non stanno in un controllo per campo. Riconosce email, partite IVA, codici
   fiscali e numeri di telefono per forma. Richiede Tesseract, quindi e'
   facoltativa: si attiva con --ocr.

L'offuscamento e' sfocatura **piu'** pixelatura: la sola sfocatura gaussiana
e' in parte invertibile, la riduzione a blocchi no.
"""

import fnmatch
import os
import re
import shutil
import unicodedata
from pathlib import Path

from PIL import Image, ImageFilter

MARGINE = 2  # qualche pixel oltre il bordo del controllo, per sicurezza

RE_SENSIBILI = [
    re.compile(r"[\w.+-]+@[\w-]+\.[\w.]{2,}"),                      # email
    re.compile(r"\b[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]\b", re.I),  # codice fiscale
    re.compile(r"\b\d{11}\b"),                                       # partita IVA
    re.compile(r"\b(?:\+39[\s.]?)?3\d{2}[\s.]?\d{6,7}\b"),           # cellulare
    re.compile(r"\b0\d{1,3}[\s./-]?\d{5,8}\b"),                      # fisso
]


def carica_regole(percorso: Path) -> dict:
    import yaml

    if not percorso.exists():
        return {}
    return yaml.safe_load(percorso.read_text(encoding="utf-8")) or {}


def nomi_dei_controlli(radice_sorgenti: Path) -> dict:
    """Numero del controllo -> nomi simbolici.

    Facile e' diviso in piu' progetti, ognuno con il suo resource.h, e lo
    stesso numero puo' avere nomi diversi in maschere diverse: per questo il
    valore e' una lista e la regola scatta se **almeno un** nome corrisponde.
    """
    mappa = {}
    for header in radice_sorgenti.rglob("resource.h"):
        try:
            testo = header.read_text(encoding="cp1252", errors="replace")
        except OSError:
            continue
        for m in re.finditer(r"^\s*#define\s+(IDC_\w+)\s+(0x[0-9A-Fa-f]+|\d+)", testo, re.M):
            mappa.setdefault(int(m.group(2), 0), set()).add(m.group(1))
    return {k: sorted(v) for k, v in mappa.items()}


def _corrisponde(nomi, motivi) -> bool:
    return any(fnmatch.fnmatch(n.upper(), m.upper()) for n in nomi for m in motivi)


def regioni_da_controlli(controlli, regole, mappa_nomi, maschera_id="") -> list:
    """`controlli`: lista di dict {id, classe, testo, rect} in coordinate
    relative alla finestra catturata."""
    motivi = regole.get("per_nome_controllo") or []
    classi_griglia = [c.upper() for c in (regole.get("classi_griglia") or [])]
    per_maschera = (regole.get("per_maschera") or {}).get(maschera_id) or {}
    motivi_extra = per_maschera.get("aggiungi") or []
    esclusi = per_maschera.get("escludi") or []

    regioni = []
    for c in controlli:
        nomi = mappa_nomi.get(c["id"], [])
        if nomi and _corrisponde(nomi, esclusi):
            continue
        sensibile = _corrisponde(nomi, motivi + motivi_extra)
        if not sensibile and c["classe"].upper() in classi_griglia:
            sensibile = bool(per_maschera.get("offusca_griglie", regole.get("offusca_griglie", False)))
        if sensibile:
            regioni.append(tuple(c["rect"]))

    for r in per_maschera.get("rettangoli") or []:
        regioni.append(tuple(r))
    return regioni


def _tesseract():
    """pytesseract cerca tesseract.exe nel PATH: appena installato non c'e'
    ancora, e in un terminale gia' aperto il PATH e' quello vecchio. Qui si
    guarda anche nei posti dove finisce di solito."""
    try:
        import pytesseract
    except ImportError:
        return None

    if not shutil.which("tesseract"):
        candidati = [
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe"),
            os.path.expandvars(r"%LOCALAPPDATA%\Tesseract-OCR\tesseract.exe"),
        ]
        for percorso in candidati:
            if os.path.exists(percorso):
                pytesseract.pytesseract.tesseract_cmd = percorso
                break
        else:
            return None
    return pytesseract


def _leggi(immagine, pytesseract):
    """L'italiano migliora il riconoscimento ma il pacchetto lingua puo' non
    esserci: in quel caso si ripiega sulla lingua predefinita."""
    for lingua in ("ita", None):
        try:
            return pytesseract.image_to_data(
                immagine, output_type=pytesseract.Output.DICT,
                **({"lang": lingua} if lingua else {}),
            )
        except Exception:
            continue
    return None


# --------------------------------------------------------------- per etichetta

CLASSI_ETICHETTA = ("AfxOleControl42", "Static")
CLASSI_CAMPO = ("Edit", "ComboBox", "RichEdit20W", "RICHEDIT50W")


def _sigla(testo: str) -> str:
    """Forma confrontabile di un'etichetta: 'Rag. Sociale 1/Cognome' e
    'Rag. Soc. 1 / Cognome' non devono essere due cose diverse."""
    testo = unicodedata.normalize("NFKD", testo or "")
    testo = "".join(c for c in testo if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9*]", "", testo.lower())


def regioni_da_etichette(controlli, regole, maschera_id="") -> list:
    """Riconosce i campi da coprire dall'etichetta che il lettore vede a video.

    Il numero del controllo non serve: in Facile lo stesso numero ricompare in
    maschere diverse con nomi diversi (l'id 295 e' insieme IDC_CLI_D_START e
    IDC_CLI_FIRST_VAL2), quindi una regola sui nomi copre cose a caso. Le
    etichette invece sono quelle stampate accanto al campo: 'Telefono' e'
    'Telefono' in tutte le maschere.

    Nelle dialog di Facile l'etichetta e' un controllo senza identificatore che
    precede il campo sulla stessa riga; i campi che seguono la ereditano finche'
    non ne arriva un'altra.
    """
    motivi = [_sigla(e) for e in (regole.get("etichette_sensibili") or [])]
    per_maschera = (regole.get("per_maschera") or {}).get(maschera_id) or {}
    motivi += [_sigla(e) for e in (per_maschera.get("aggiungi_etichette") or [])]
    esclusi = [_sigla(e) for e in (regole.get("etichette_escluse") or [])
               + (per_maschera.get("escludi_etichette") or [])]
    larghezza_minima = int(per_maschera.get("larghezza_minima",
                                            regole.get("larghezza_minima", 70)))

    def sensibile(testo: str) -> bool:
        s = _sigla(testo)
        if not s or any(fnmatch.fnmatch(s, m) for m in esclusi):
            return False
        return any(fnmatch.fnmatch(s, m) for m in motivi)

    regioni = []
    etichetta = None
    for c in controlli:
        testo = (c.get("testo") or "").strip()
        if c["id"] == 0 and c["classe"] in CLASSI_ETICHETTA and testo:
            etichetta = c
            continue
        if c["classe"] not in CLASSI_CAMPO or not etichetta:
            continue
        # solo i campi sulla stessa riga dell'etichetta: senza questo vincolo
        # un'etichetta si trascina dietro mezza maschera
        if abs(c["rect"][1] - etichetta["rect"][1]) > 8:
            continue
        # il campicino del codice accanto alla descrizione non contiene nomi
        if c["rect"][2] < larghezza_minima:
            continue
        if sensibile(etichetta["testo"]):
            regioni.append(tuple(c["rect"]))
    return regioni


# ------------------------------------------------------------------- griglie

def _senza_barre(rett, controlli) -> tuple:
    """Le barre di scorrimento stanno dentro l'ingombro della griglia e hanno
    un bordo scuro su ogni riga: lasciarle dentro fa credere che i dati
    arrivino fino in fondo."""
    x, y, larg, alt = rett
    for c in controlli:
        if "SCRLBAR" not in c["classe"].upper() and "SCROLLBAR" not in c["classe"].upper():
            continue
        bx, by, blarg, balt = c["rect"]
        if bx + blarg <= x or bx >= x + larg or by + balt <= y or by >= y + alt:
            continue
        if blarg < balt and bx > x + larg / 2:      # barra verticale a destra
            larg = min(larg, bx - x)
        elif balt < blarg and by > y + alt / 2:     # barra orizzontale in basso
            alt = min(alt, by - y)
    return x, y, larg, alt


def regioni_da_griglia(immagine, controlli, regole, maschera_id="") -> list:
    """Le griglie (SPR32A80_SpreadSheet, cioe' FarPoint Spread) sono un unico
    controllo disegnato: le celle non esistono come finestre. Si copre allora
    la colonna intera, riconosciuta dalla sua intestazione.

    Con Tesseract la colonna si trova da sola; senza, servono le frazioni
    scritte a mano in regole-privacy.yml.
    """
    classi = [c.upper() for c in (regole.get("classi_griglia") or [])]
    per_maschera = (regole.get("per_maschera") or {}).get(maschera_id) or {}
    intestazioni = [_sigla(e) for e in (regole.get("colonne_sensibili") or [])]

    regioni = []
    for c in controlli:
        if not any(c["classe"].upper().startswith(k) for k in classi):
            continue
        x, y, larg, alt = _senza_barre(c["rect"], controlli)
        if larg < 100 or alt < 60:
            continue

        colonne = per_maschera.get("colonne")
        if colonne:
            for frazione in colonne:
                da, a = float(frazione[0]), float(frazione[1])
                regioni.append((x + int(larg * da), y, int(larg * (a - da)), alt))
            continue

        regioni += _colonne_da_ocr(immagine, (x, y, larg, alt), intestazioni)
    return regioni


def _linee_scure(matrice, minimo: float = 0.8, delta: int = 10) -> list:
    """Colonne (o righe, se si passa la trasposta) piu' scure delle vicine su
    quasi tutta l'altezza: sono i divisori disegnati dalla griglia. Il testo
    non passa questo filtro perche' occupa solo la fascia centrale."""
    import numpy as np

    trovate = []
    for i in range(2, matrice.shape[1] - 2):
        vicini = (matrice[:, i - 2] + matrice[:, i + 2]) / 2
        if (matrice[:, i] < vicini - delta).mean() >= minimo:
            trovate.append(i)
    gruppi = []
    for x in trovate:
        if gruppi and x - gruppi[-1][-1] <= 3:
            gruppi[-1].append(x)
        else:
            gruppi.append([x])
    return [int(sum(g) / len(g)) for g in gruppi]


def _fine_dei_dati(g, fondo: int) -> int:
    """Ultima riga della griglia che contiene qualcosa.

    Sotto l'ultima riga scritta c'e' solo sfondo: sfocarlo si vedrebbe come
    una banda sfumata in mezzo al vuoto. Si guarda tutta la larghezza in una
    volta — una colonna puo' avere celle vuote a meta' elenco, l'elenco no —
    saltando la colonna dei numeri di riga a sinistra, che ha un bordo scuro
    su ogni riga e da solo falserebbe la misura.
    """
    import numpy as np

    altezza, larghezza = g.shape
    ultima = fondo
    for y in range(fondo, altezza, 4):
        fascia = g[y:y + 4, 30:max(31, larghezza - 4)]
        if fascia.size == 0:
            break
        if (np.abs(fascia - np.median(fascia)) > 40).mean() > 0.004:
            ultima = y + 4
    return ultima


def _colonne_da_ocr(immagine, rett, motivi) -> list:
    """Colonne da coprire in una griglia disegnata.

    L'intestazione non si legge bene insieme al resto — Tesseract sulla
    griglia intera salta proprio la riga dei titoli — quindi si procede in
    due tempi: prima si trovano i divisori delle celle guardando i pixel,
    poi si legge una cella per volta, ingrandita.
    """
    import numpy as np
    from PIL import Image, ImageOps

    pytesseract = _tesseract()
    if not pytesseract:
        return []

    x, y, larg, alt = rett
    griglia = immagine.crop((x, y, x + larg, y + alt))
    g = np.array(ImageOps.grayscale(griglia), dtype=float)

    alto = min(int(alt * 0.25), 120)
    orizzontali = _linee_scure(np.ascontiguousarray(g[:alto].T))
    fondo = next((v for v in orizzontali if v > 8), None)
    if not fondo:
        return []

    banda = np.ascontiguousarray(g[2:max(3, fondo - 2)])
    divisori = [0] + _linee_scure(banda) + [larg]
    basso = _fine_dei_dati(g, fondo)

    regioni = []
    for i in range(len(divisori) - 1):
        x0, x1 = divisori[i], divisori[i + 1]
        if x1 - x0 < 14:
            continue
        cella = griglia.crop((x0, 2, x1, fondo - 1))
        cella = ImageOps.autocontrast(ImageOps.grayscale(
            cella.resize((cella.width * 4, cella.height * 4), Image.LANCZOS)))
        try:
            testo = pytesseract.image_to_string(cella, config="--psm 7").strip()
        except Exception:
            continue
        if not any(fnmatch.fnmatch(_sigla(testo), m) for m in motivi):
            continue
        if basso > fondo:
            regioni.append((x + x0, y + fondo, x1 - x0, basso - fondo))
    return regioni


def regioni_da_ocr(immagine: Image.Image) -> list:
    """Rete di sicurezza: cerca a video le forme tipiche dei dati personali."""
    pytesseract = _tesseract()
    if not pytesseract:
        return []
    dati = _leggi(immagine, pytesseract)
    if not dati:
        return []
    regioni = []
    for i, parola in enumerate(dati["text"]):
        parola = (parola or "").strip()
        if not parola:
            continue
        if any(r.search(parola) for r in RE_SENSIBILI):
            regioni.append(
                (dati["left"][i], dati["top"][i], dati["width"][i], dati["height"][i])
            )
    return regioni


def _ha_inchiostro(zona: Image.Image, soglia: int = 25) -> bool:
    """Un campo vuoto e' una macchia di colore uniforme. Coprirlo lo fa
    sembrare disabilitato e sporca la schermata senza proteggere niente:
    conviene coprire solo dove c'e' davvero qualcosa scritto. Il bordo del
    controllo si scarta restringendo il ritaglio."""
    l, a = zona.size
    if l > 8 and a > 8:
        zona = zona.crop((3, 3, l - 3, a - 3))
    grigi = zona.convert("L")
    minimo, massimo = grigi.getextrema()
    return (massimo - minimo) >= soglia


def applica(immagine: Image.Image, regioni: list, salta_vuoti: bool = True) -> Image.Image:
    fuori = immagine.copy()
    L, A = fuori.size
    for x, y, w, h in regioni:
        x0, y0 = max(0, x - MARGINE), max(0, y - MARGINE)
        x1, y1 = min(L, x + w + MARGINE), min(A, y + h + MARGINE)
        if x1 - x0 < 3 or y1 - y0 < 3:
            continue
        zona = fuori.crop((x0, y0, x1, y1))
        if salta_vuoti and not _ha_inchiostro(zona):
            continue
        # il lato del blocco va rapportato all'altezza del testo, non a quella
        # della zona: su una colonna alta 140 pixel un blocco da 35 spappola
        # tutto in una macchia unica e la schermata diventa illeggibile
        lato = max(3, min(10, (y1 - y0) // 4))
        zona = zona.resize(
            (max(1, (x1 - x0) // lato), max(1, (y1 - y0) // lato)), Image.BILINEAR
        ).resize((x1 - x0, y1 - y0), Image.NEAREST)
        zona = zona.filter(ImageFilter.GaussianBlur(radius=max(2, lato / 2)))
        fuori.paste(zona, (x0, y0))
    return fuori
