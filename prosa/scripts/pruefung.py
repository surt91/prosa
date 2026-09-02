#!/usr/bin/env python3
"""Mechanische Prüfung eines deutschen Fließtexts auf Claudismen.

Aufruf:
    python3 pruefung.py TEXT.md
    python3 pruefung.py TEXT.md --vergleich STILPROBE.md
    python3 pruefung.py TEXT.md --kurz

Das Skript zählt, es urteilt nicht. Ein Treffer ist ein Hinweis, den man liest
und dann entscheidet. Die Richtwerte im Bericht sind Standardwerte; ein
Stilprofil kann andere vorgeben. Mit --vergleich werden die Kennzahlen einer
Stilprobe daneben gestellt.
"""

import re
import statistics
import sys

# --------------------------------------------------------------------------
# Muster. Jede Gruppe: (Name, Richtwert-Text, [Regex, ...])
# Regex werden mit re.IGNORECASE auf einzelne Sätze angewendet, außer wenn
# sie mit "SATZPAAR:" beginnen, dann auf Paare aufeinanderfolgender Sätze.
# --------------------------------------------------------------------------

MUSTER = [
    ("Nicht X, sondern Y",
     "höchstens 1 pro Kapitel",
     [r"\b(nicht|kein|keine|keinen|keinem|keiner|nie|niemals|weniger)\b[^.!?;]{0,120}\bsondern\b",
      r"^(nicht|kein|keine)\b[^,]{1,40},\s+\w+[^,]{0,25}[.!?]$",  # "Nicht besser, anders."
      r"SATZPAAR:\b(ist|war|sind|waren|geht|ging|gefragt)\b[^.!?]{0,80}\b(nicht|kein|keine)\b[^.!?]{0,80}[.!?]\s+(es|sie|er|das|gefragt|gemeint)\s+(ist|war|sind|waren|geht|ging)\b",
      r"\bnicht als\b[^.!?]{0,40}\bsondern als\b",
      ]),
    ("Das klingt X, ist aber Y",
     "höchstens 1 pro Kapitel",
     [r"\b(das|es|was)\s+(klingt|klang|wirkt|scheint|mag)\b[^.!?]{0,60}\b(aber|doch|ist es nicht|als es)\b",
      r"\bklingt (nach|wie|zunächst|erst einmal|banal|paradox|esoterisch|harmlos)\b"]),
    ("Abgewehrter Einwand",
     "nur, wenn der Einwand belegt vorkommt",
     [r"\bes wäre (falsch|verfehlt|verkürzt|ein fehler|ein missverständnis)\b",
      r"\bdamit (ist|soll) nicht gesagt\b", r"\bdas (heißt|bedeutet|soll) (nicht|nichts)\b",
      r"\bwill (hier |damit )?nicht (den eindruck|behaupten|sagen)\b",
      r"\bich (behaupte|sage|meine) (hier |damit )?nicht\b", r"\bman könnte (einwenden|entgegnen|meinen)\b",
      r"\bnatürlich (gibt es|ist|kann|hat)\b", r"\bversteh(en Sie|t) mich nicht falsch\b",
      r"\bum nicht missverstanden\b", r"\bdas (wäre|ist) (gelogen|zu einfach|zu kurz gegriffen)\b"]),
    ("Bedeutungsankündigung",
     "streichen",
     [r"\bder punkt ist\b", r"\bkurz gesagt\b", r"\banders (gesagt|formuliert|ausgedrückt)\b",
      r"\bmit anderen worten\b", r"\bhier wird es\b", r"\bdamit nicht genug\b", r"\bgenau (darin|hier|das ist|deshalb|deswegen)\b",
      r"\b(das|der|die) (entscheidende|eigentliche|wesentliche|wichtigste|zentrale)\b",
      r"\b(gern|oft|häufig|meist) (übersehen|vergessen|unterschätzt)\b", r"\bselten (liest|hört|sagt)\b",
      r"\bam (schönsten|deutlichsten|besten) (lässt|zeigt|sieht)\b", r"\bin diesem zusammenhang\b",
      r"\bworauf es (ankommt|hinausläuft)\b", r"\bwas (dabei|hier) (zählt|wichtig ist)\b",
      r"\bes lohnt sich\b", r"\bwichtig (ist|zu)\b", r"\bbemerkenswert(erweise)?\b", r"\bes ist kein zufall\b"]),
    ("Dreierreihe / Anapher",
     "Anapher höchstens 1 pro Kapitel; Dreierreihen ohne Parallelbau",
     [r"\b([a-zäöüß]+),\s+([a-zäöüß]+)\s+(und|oder)\s+([a-zäöüß]+)\b(?![^.!?]*\b(und|oder)\b)",
      r"\b(kein|keine|keinen|ohne|nach|für|von|mit)\s+[^,.;]{2,30},\s+(kein|keine|keinen|ohne|nach|für|von|mit)\s+[^,.;]{2,30},\s+(kein|keine|keinen|ohne|nach|für|von|mit)\b",
      r"\bsowohl\b[^.!?]{0,60}\bals auch\b[^.!?]{0,60}\b(und|als auch)\b"]),
    ("Füllwörter mit Gewicht",
     "genau, und zwar: je 1 pro Kapitel; eigentlich/tatsächlich nur als Korrektur",
     [r"\bgenau\b", r"\bund zwar\b", r"\beigentlich\b", r"\btatsächlich\b", r"\bim grunde\b", r"\bletztlich\b",
      r"\bim kern\b", r"\bschlicht(weg)?\b", r"\bbloß\b", r"\bam ende\b", r"\bimmerhin\b", r"\bwohlgemerkt\b",
      r"\bausgerechnet\b", r"\bpraktisch\b"]),
    ("Bedeutungs- und Werbewörter",
     "streichen oder durch die Sache ersetzen",
     [r"\bentscheidend", r"\bzentral", r"\bwesentlich", r"\bfaszinierend", r"\bspannend", r"\bbeeindruckend",
      r"\bunterstreich", r"\bspielt\w* eine\b[^.!?]{0,20}\brolle\b", r"\bzeugnis\b", r"\bwendepunkt", r"\btief verwurzelt",
      r"\bnahtlos", r"\bvielschichtig", r"\bfacettenreich", r"\bbeleucht", r"\beintauch", r"\blandschaft\b",
      r"\bmeilenstein", r"\bprägend", r"\bbleibend"]),
    ("Körperkatalog (Erzähltext)",
     "Gefühl über Handlung, Rede, Auslassung zeigen",
     [r"\batem\b", r"\batmete\b", r"\bin (ihrer|seiner|der) brust\b", r"\bkloß\b", r"\bim hals\b", r"\bkehle\b",
      r"\bschluckte\b", r"\bzitterte\b", r"\bmagen\b", r"\bin (ihr|ihm) (riss|zog|brach|zerbrach|kippte)\b",
      r"\betwas in (ihr|ihm)\b", r"\bherz(schlag)? (schlug|pochte|raste)\b", r"\bhände (zitterten|ballten)\b"]),
    ("Kulissen-Details (Erzähltext)",
     "Standarddetails des Modells; prüfen, ob sie nötig sind",
     [r"\bsägemehl\b", r"\bsägespäne\b", r"\bmaschinenöl\b", r"\bstaub\b", r"\blichtstrahl", r"\bsonnenstrahl",
      r"\bkalte[nr]? kaffee\b", r"\btick(te|en)\b", r"\bheizkörper\b", r"\bknarrte\b", r"\bsummte\b",
      r"\bgeruch (nach|von)\b", r"\broch nach\b", r"\bstill(e)?\b", r"\bleise\b", r"\bsehr lange\b"]),
    ("Inquit-Formeln (Erzähltext)",
     "nur „sagte“ oder nichts",
     [r"\b(sagte|fragte|antwortete) (sie|er) (leise|ruhig|langsam|schließlich|nur|knapp|tonlos)\b",
      r"\bmurmelte\b", r"\bflüsterte\b", r"\berwiderte\b", r"\bentgegnete\b", r"\bmeinte\b", r"\bseufzte\b"]),
    ("Gespielte Offenheit / Einwände-Runde (Blog)",
     "den Punkt direkt machen",
     [r"\behrlich gesagt\b", r"\bum ehrlich zu sein\b", r"\bich (will|muss) ehrlich\b", r"\bja, ich weiß\b",
      r"\bspoiler\b", r"\bich gebe zu\b", r"\bzugegeben\b", r"^ja, ", r"\bund ja, ", r"\brückblickend\b",
      r"\bwas ich (unterschätzt|übersehen|gelernt) habe\b", r"\bwas ich eigentlich\b",
      r"\büber (den|die|das) ich (am wenigsten|nicht) gern(e)? (rede|spreche)\b"]),
    ("Formelhafte Analogie / Aphorismus",
     "höchstens 1 pro Kapitel",
     [r"\bist (mein|meine|unser|unsere|das|die|der) \w+, (das|die|der) \w+ (ist|die|der|das) \w+\b",
      r"\bist (die|der|das) \w+ (des|der) \w+\b", r"\bist kein \w+, (sondern )?ein \w+\b",
      r"\bhat kein gedächtnis\b", r"\bvergisst\b", r"\bkennt kein\b"]),
]

SATZENDE = re.compile(r"(?<=[.!?…])[\"“”»«']?\s+(?=[A-ZÄÖÜ„“»«\"'*(])")
INITIALEN = re.compile(r"\b([A-ZÄÖÜ])\.\s(?=[A-ZÄÖÜ]\.|[A-ZÄÖÜ][a-zäöü])")
ABKUERZUNGEN = re.compile(r"\b(z\.\s?B|u\.\s?a|d\.\s?h|usw|etc|bzw|Nr|Dr|Prof|ca|vgl|Jh|Std|Min|Sept|Okt|Nov|Dez|Jan|Febr|Aug|Mio|Mrd|St|Hr|Fr|J)\.\s")


def lade(pfad):
    with open(pfad, encoding="utf-8") as f:
        return f.read()


def absaetze(text):
    bloecke = re.split(r"\n\s*\n", text.strip())
    out = []
    for b in bloecke:
        b = b.strip()
        if not b or b.startswith("#") or b.startswith("---"):
            continue
        b = re.sub(r"\s*\n\s*", " ", b)
        out.append(b)
    return out


def saetze(absatz):
    geschuetzt = ABKUERZUNGEN.sub(lambda m: m.group(0).replace(".", "§"), absatz)
    geschuetzt = INITIALEN.sub(lambda m: m.group(1) + "§ ", geschuetzt)
    teile = SATZENDE.split(geschuetzt)
    return [t.replace("§", ".").strip() for t in teile if t.strip()]


def woerter(s):
    return re.findall(r"[A-Za-zÄÖÜäöüß0-9][A-Za-zÄÖÜäöüß0-9'\-]*", s)


def kennzahlen(text):
    abs_ = absaetze(text)
    alle_saetze = []
    abs_laengen = []
    einzeiler = 0
    pointen_enden = []
    anaphern = []
    for a in abs_:
        ss = saetze(a)
        alle_saetze.extend(ss)
        abs_laengen.append(len(woerter(a)))
        if len(ss) <= 1:
            einzeiler += 1
        if ss and len(ss) >= 3:
            mittel = statistics.mean(len(woerter(x)) for x in ss[:-1])
            letzte = len(woerter(ss[-1]))
            if letzte <= 6 or letzte < 0.5 * mittel:
                pointen_enden.append(ss[-1])
        elif ss and len(woerter(ss[-1])) <= 6:
            pointen_enden.append(ss[-1])
        # Anapher: drei aufeinanderfolgende Sätze mit gleichem ersten Wort
        starts = [woerter(s)[0].lower() if woerter(s) else "" for s in ss]
        for i in range(len(starts) - 2):
            if starts[i] and starts[i] == starts[i + 1] == starts[i + 2]:
                anaphern.append(" | ".join(x[:50] for x in ss[i:i + 3]))
                break
    satz_laengen = [len(woerter(s)) for s in alle_saetze] or [0]
    n_w = sum(satz_laengen)
    pro_tausend = lambda n: (n / n_w * 1000) if n_w else 0.0
    gedankenstriche = len(re.findall(r"[–—]", text))
    doppelpunkte = len(re.findall(r":\s+[^\n\"„»]", text))
    semikola = len(re.findall(r";", text))
    fragen = len(re.findall(r"\?", text))
    kursiv = len(re.findall(r"(?<!\*)\*[^*\n]+\*(?!\*)|(?<!\w)_[^_\n]+_(?!\w)", text))
    fragmente = [s for s in alle_saetze if len(woerter(s)) <= 3]
    return {
        "woerter": n_w,
        "saetze": len(alle_saetze),
        "absaetze": len(abs_),
        "satz_mittel": statistics.mean(satz_laengen),
        "satz_median": statistics.median(satz_laengen),
        "satz_std": statistics.pstdev(satz_laengen) if len(satz_laengen) > 1 else 0,
        "satz_min": min(satz_laengen),
        "satz_max": max(satz_laengen),
        "kurz_anteil": sum(1 for l in satz_laengen if l <= 5) / len(satz_laengen),
        "lang_anteil": sum(1 for l in satz_laengen if l >= 30) / len(satz_laengen),
        "abs_mittel": statistics.mean(abs_laengen) if abs_laengen else 0,
        "abs_std": statistics.pstdev(abs_laengen) if len(abs_laengen) > 1 else 0,
        "abs_min": min(abs_laengen) if abs_laengen else 0,
        "abs_max": max(abs_laengen) if abs_laengen else 0,
        "einzeiler": einzeiler,
        "pointen_enden": pointen_enden,
        "pointen_anteil": len(pointen_enden) / len(abs_) if abs_ else 0,
        "fragmente": fragmente,
        "anaphern": anaphern,
        "gedankenstriche_pt": pro_tausend(gedankenstriche),
        "gedankenstriche": gedankenstriche,
        "doppelpunkte_pt": pro_tausend(doppelpunkte),
        "semikola_pt": pro_tausend(semikola),
        "semikola": semikola,
        "fragen": fragen,
        "kursiv": kursiv,
        "_saetze": alle_saetze,
    }


def treffer(alle_saetze):
    ergebnis = []
    for name, richtwert, regexe in MUSTER:
        funde = []
        for rx in regexe:
            if rx.startswith("SATZPAAR:"):
                muster = re.compile(rx[len("SATZPAAR:"):], re.IGNORECASE)
                for a, b in zip(alle_saetze, alle_saetze[1:]):
                    if muster.search(a + " " + b):
                        funde.append((a + " " + b)[:160])
            else:
                muster = re.compile(rx, re.IGNORECASE | re.MULTILINE)
                for s in alle_saetze:
                    m = muster.search(s)
                    if m:
                        funde.append(s[:160])
        # Dubletten entfernen, Reihenfolge behalten
        gesehen = set()
        funde = [f for f in funde if not (f in gesehen or gesehen.add(f))]
        ergebnis.append((name, richtwert, funde))
    return ergebnis


def fmt(k, probe=None):
    def zeile(label, wert, pwert=None, hinweis=""):
        p = f"   (Probe: {pwert})" if pwert is not None else ""
        return f"  {label:<47}{wert}{p}{('   ' + hinweis) if hinweis else ''}"

    seiten = max(k["woerter"] / 400, 0.25)
    out = []
    out.append(f"Umfang: {k['woerter']} Wörter, {k['saetze']} Sätze, {k['absaetze']} Absätze (≈ {seiten:.1f} Seiten à 400 Wörter)")
    out.append("")
    out.append("Rhythmus")
    out.append(zeile("Satzlänge Mittel / Median / Streuung", f"{k['satz_mittel']:.1f} / {k['satz_median']:.0f} / {k['satz_std']:.1f}",
                     None if not probe else f"{probe['satz_mittel']:.1f} / {probe['satz_median']:.0f} / {probe['satz_std']:.1f}",
                     "Streuung unter 8 ist gleichförmig" if k['satz_std'] < 8 else ""))
    out.append(zeile("Satzlänge Spanne", f"{k['satz_min']}–{k['satz_max']}", None if not probe else f"{probe['satz_min']}–{probe['satz_max']}"))
    out.append(zeile("Anteil Kurzsätze (≤5) / Langsätze (≥30)", f"{k['kurz_anteil']:.0%} / {k['lang_anteil']:.0%}",
                     None if not probe else f"{probe['kurz_anteil']:.0%} / {probe['lang_anteil']:.0%}",
                     "Kaum Kurzsätze: Überkorrektur prüfen" if k["kurz_anteil"] < 0.05 else ""))
    out.append(zeile("Absatzlänge Mittel / Streuung (Wörter)", f"{k['abs_mittel']:.0f} / {k['abs_std']:.0f}",
                     None if not probe else f"{probe['abs_mittel']:.0f} / {probe['abs_std']:.0f}",
                     "Streuung unter 40 % des Mittels ist gleichförmig" if k['abs_mittel'] and k['abs_std'] < 0.4 * k['abs_mittel'] else ""))
    out.append(zeile("Einzeiler-Absätze", k["einzeiler"], None if not probe else probe["einzeiler"],
                     "Richtwert: 0–1 pro Kapitel" if k["einzeiler"] > 1 else ""))
    out.append(zeile("Absätze mit Pointen-Ende (kurz od. <½ Mittel)", f"{len(k['pointen_enden'])} von {k['absaetze']} ({k['pointen_anteil']:.0%})",
                     None if not probe else f"{probe['pointen_anteil']:.0%}",
                     "Richtwert: unter 25 %" if k["pointen_anteil"] >= 0.25 else ""))
    out.append(zeile("Fragmente (≤3 Wörter)", len(k["fragmente"]), None if not probe else len(probe["fragmente"]),
                     f"Richtwert: höchstens {max(1, round(seiten / 3))}" if len(k["fragmente"]) > max(1, round(seiten / 3)) else ""))
    out.append(zeile("Anaphern (3 Sätze, gleicher Anfang)", len(k["anaphern"]), None if not probe else len(probe["anaphern"]),
                     "Richtwert: höchstens 1 pro Kapitel" if len(k["anaphern"]) > 1 else ""))
    out.append("")
    out.append("Interpunktion")
    out.append(zeile("Gedankenstriche pro 1000 Wörter", f"{k['gedankenstriche_pt']:.1f} ({k['gedankenstriche']})",
                     None if not probe else f"{probe['gedankenstriche_pt']:.1f}",
                     "Richtwert ohne Profil: unter 2,5" if k["gedankenstriche_pt"] >= 2.5 else ""))
    out.append(zeile("Doppelpunkte im Satz pro 1000 Wörter", f"{k['doppelpunkte_pt']:.1f}", None if not probe else f"{probe['doppelpunkte_pt']:.1f}",
                     "Richtwert ohne Profil: unter 3" if k["doppelpunkte_pt"] >= 3 else ""))
    out.append(zeile("Semikolons pro 1000 Wörter", f"{k['semikola_pt']:.1f} ({k['semikola']})", None if not probe else f"{probe['semikola_pt']:.1f}",
                     "Richtwert ohne Profil: unter 2,5 (Ersatz-Tick für Gedankenstriche)" if k["semikola_pt"] >= 2.5 else ""))
    out.append(zeile("Fragezeichen", k["fragen"], None if not probe else probe["fragen"]))
    out.append(zeile("Kursivierungen", k["kursiv"], None if not probe else probe["kursiv"]))
    return "\n".join(out)


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    pfad = argv[1]
    kurz = "--kurz" in argv
    probe = None
    if "--vergleich" in argv:
        i = argv.index("--vergleich")
        probe = kennzahlen(lade(argv[i + 1]))
    text = lade(pfad)
    k = kennzahlen(text)
    print(f"Prüfung: {pfad}")
    print(fmt(k, probe))
    print()
    if not kurz and k["pointen_enden"]:
        print("Absatzenden, die wie Pointen gebaut sind (Kurzsatz oder deutlich kürzer als der Absatz):")
        for s in k["pointen_enden"]:
            print(f"  · {s}")
        print()
    if not kurz and k["anaphern"]:
        print("Anaphern:")
        for s in k["anaphern"]:
            print(f"  · {s}")
        print()
    print("Musterfunde (Zahl der Sätze mit Treffer; Richtwert in Klammern)")
    for name, richtwert, funde in treffer(k["_saetze"]):
        if not funde:
            continue
        print(f"  {name}: {len(funde)}   ({richtwert})")
        if not kurz:
            for f in funde[:12]:
                print(f"      · {f}")
            if len(funde) > 12:
                print(f"      · … und {len(funde) - 12} weitere")
    print()
    print("Lesetest danach: erste Sätze aller Absätze hintereinander lesen (Gliederungstest), "
          "letzte Sätze aller Absätze hintereinander lesen (Pointentest).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
