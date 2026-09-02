# prosa: ein Claude-Code-Skill für deutschen Fließtext ohne Claudismen

Ein Skill für Claude Code (ausgelegt auf Claude Opus), der deutsche Prosa schreibt und überarbeitet, ohne die typischen Stilmuster von Sprachmodellen: Pointe an jedem Absatzende, „nicht X, sondern Y", Dreierreihen mit Anapher, bedeutungsschwere Details, abgewehrte Einwände, Kreisschluss. Gedacht für Bücher (Sachbuch und Erzähltext), Essays und Blog-Posts. Optional mit Stilprofil aus einer Textprobe.

## Installation

Den Ordner `prosa/` kopieren nach

- `~/.claude/skills/prosa/` (für alle Projekte) oder
- `<Projekt>/.claude/skills/prosa/` (nur dieses Projekt).

Claude Code lädt die `SKILL.md` automatisch, wenn die Aufgabe zur Beschreibung passt. Manuell aufrufen mit `/prosa`.

Das Prüfskript braucht Python 3 ohne weitere Abhängigkeiten.

## Aufbau

```
prosa/
├── SKILL.md                         Arbeitsweise, Standardwerte, Budgets
├── references/
│   ├── claudismen.md                Katalog der Muster mit Belegen aus echten Opus-Texten
│   ├── handwerk.md                  Was stattdessen: Regeln guter deutscher Prosa je Textform
│   ├── stilprofil-vorlage.md        Vorlage für ein Stilprofil aus Textproben
│   └── ueberarbeitung.md            Bestehende Texte überarbeiten, kapitelweise mit Subagenten
└── scripts/
    └── pruefung.py                  Mechanische Prüfung: Rhythmus, Interpunktion, Musterfunde
```

## Verwendung

**Schreiben.** „Schreib ein Kapitel über … für mein Sachbuch." Der Skill greift, liest seine Referenzen, schreibt, prüft mit dem Skript und liefert den Text.

**Mit Stilprobe.** „Hier sind zwei Kapitel von mir (kapitel1.md, kapitel2.md). Leg ein Stilprofil an und schreib dann Kapitel 3 über …" Der Skill legt `stilprofil.md` im Projektordner an, zeigt es, und schreibt danach. Das Profil überstimmt die Standardwerte des Skills, etwa bei Gedankenstrichen, Anrede oder Pointendichte. Es lässt sich von Hand bearbeiten.

**Überarbeiten.** „Der Text klingt nach KI, überarbeite ihn." Inhalt bleibt, Formulierungen dürfen großflächig geändert werden. Für ganze Manuskripte: „Überarbeite alle Kapitel in manuskript/ kapitelweise." Der Skill legt eine Kontextdatei an, startet je Kapitel einen Subagenten mit frischem Kontext und gleicht danach Übergänge, Namen und Ersatz-Tics ab.

**Prüfen.** `python3 prosa/scripts/pruefung.py text.md` gibt Kennzahlen (Satzlängenstreuung, Absätze mit Pointen-Ende, Gedankenstriche pro 1000 Wörter, …) und Musterfunde mit Satzzitaten aus. Mit `--vergleich stilprobe.md` stehen die Werte der Probe daneben.

## Tests

In `tests/` liegen Vergleichstexte aus der Entwicklung, alle von Claude Opus geschrieben:

- `baseline/`: drei Texte ohne Skill (Sachbuchkapitel, Romanszene, Blog-Post). Aus ihnen stammen die Belege im Katalog.
- `with-skill/`: dieselben drei Aufgaben mit der ersten Fassung des Skills. Hier zeigten sich die Überkorrekturen (keine Kurzsätze, Semikolons, Inventar-Stil, kopierte Beispiele), die jetzt in `claudismen.md`, Teil G stehen.
- `with-skill-v2/`: dieselben Aufgaben mit der aktuellen Fassung.
- `ueberarbeitung/`: der Baseline-Blog-Post, mit dem Skill überarbeitet, plus Inhaltsabgleich.
- `stilprobe/`: ein Stilprofil aus einem gemeinfreien Tucholsky-Text und ein damit geschriebener Post. Zeigt, wie das Profil die Standardwerte überstimmt.

Prüfen lässt sich jeder Text mit `python3 prosa/scripts/pruefung.py tests/<ordner>/<datei>.md`.

## Herkunft

Die Ebenen-Idee (Struktur schlägt Wortliste) und das Stilprofil folgen dem englischen Skill [unslop](https://github.com/asavvin-pixel/unslop). Sachtext-Muster wurden mit dem deutschen Skill [vermenschlichen](https://github.com/j-landeck/vermenschlichen_skill) und der Wikipedia-Seite „Anzeichen für KI-generierte Inhalte" abgeglichen. Die Belege im Katalog stammen aus eigenen Testläufen mit Claude Opus.
