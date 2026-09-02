# Überarbeitung bestehender Texte

Für Texte, die schon existieren (eigene Entwürfe, Modellentwürfe, ganze Buchmanuskripte) und die von Claudismen befreit werden sollen. Inhalt und Fakten bleiben, Formulierungen dürfen großflächig geändert werden, ganze Absätze dürfen neu geschrieben werden.

## Grundsätze

1. **Inhalt ist unantastbar.** Jede Tatsache, Zahl, Name, Quelle, Reihenfolge von Ereignissen, jede Figurenhandlung und jeder Dialoginhalt bleibt erhalten. Was der Text behauptet, behauptet er danach noch. Was er nicht behauptet, behauptet er danach auch nicht: keine neuen Beispiele, keine neuen Details, keine neuen Deutungen. In Erzähltexten dürfen Details ersetzt werden (ein Kulissen-Detail durch ein anderes), aber keine Handlung hinzukommen.
2. **Form ist frei.** Sätze umbauen, zusammenziehen, teilen, Absätze neu schneiden, Absatzgrenzen verschieben, Reihenfolge innerhalb eines Absatzes ändern, Pointen streichen, Übergänge ersetzen. Ein Absatz, der nur aus Claudismen besteht, wird komplett neu geschrieben. Kürzen ist erlaubt, wenn das Gestrichene nur Wirkung war (Ankündigung, Deutung, Pointe). Verlängern ist erlaubt, wenn eine Pointe durch eine ausgeführte Erklärung ersetzt wird.
3. **Stimme bleibt oder wird gesetzt.** Wenn ein `stilprofil.md` existiert, wird auf dieses Profil hin überarbeitet. Wenn nicht, bleibt der vorhandene Ton (Register, Anrede, Tempus, Humor) und nur die Muster werden entfernt.
4. **Keine Ersatz-Tics.** Wer jede Pointe durch einen erklärenden Nebensatz ersetzt, hat ein neues Metrum. Wer jedes „nicht X, sondern Y" in „Y, nicht X" verwandelt, hat nichts gewonnen. Die Lösung für eine Figur ist meist ihr Fehlen, nicht ihre Umstellung.

## Ablauf für einen einzelnen Text (bis etwa 3000 Wörter)

1. `claudismen.md` und `handwerk.md` lesen. Stilprofil lesen, falls vorhanden.
2. Text einmal ganz lesen. Dabei nur markieren, nicht ändern.
3. `scripts/pruefung.py` laufen lassen. Die Treffer sind Hinweise, keine Pflicht.
4. Lesetests: erste Sätze aller Absätze hintereinander (Gliederungstest), letzte Sätze aller Absätze hintereinander (Pointentest).
5. Überarbeiten, Absatz für Absatz. Bei jedem Absatz zuerst fragen: Was steht hier an Inhalt? Dann: Wie würde jemand das schreiben, der diesen Inhalt einfach mitteilen will? Dann schreiben. Erst danach mit dem Original vergleichen und prüfen, ob etwas an Inhalt verloren ging.
6. Eigene Fassung mit `pruefung.py` prüfen. Was noch über den Richtwerten liegt, noch einmal ansehen.
7. Inhaltsabgleich: Original und Fassung nebeneinander, Absatz für Absatz. Jede Zahl, jeder Name, jede Behauptung muss wiederzufinden sein. Bei Erzähltexten: jede Handlung, jede Information, die der Leser bekommt.
8. Ausgabe: die Fassung. Keine Änderungsliste, es sei denn, der Nutzer will sie. Wenn eine Entscheidung strittig war (etwa: eine Passage gekürzt, weil sie nur Deutung war), ein Satz dazu.

## Ablauf für lange Texte (Buchmanuskript, mehrere Kapitel)

Der Kontext eines einzigen Agenten reicht nicht für ein Buch, und er verschleißt: Nach dem dritten Kapitel greift der Überarbeiter zu denselben Lösungen wie im ersten und produziert Ersatz-Tics. Deshalb ein Subagent pro Kapitel, jeweils mit frischem Kontext.

### Vorbereitung durch den Hauptagenten

1. Manuskript in Kapitel oder Abschnitte zerlegen, jedes als eigene Datei (etwa `kapitel/03-original.md`). Richtwert: 1500 bis 4000 Wörter pro Einheit. Längere Kapitel an einer Zwischenüberschrift oder einem Szenenwechsel teilen.
2. Stilprofil bereitstellen. Wenn keines existiert, aber der Nutzer eine Stilprobe hat oder ein Kapitel als Vorbild nennt: zuerst Profil anlegen (siehe `stilprofil-vorlage.md`), dem Nutzer zeigen, dann erst überarbeiten. Ohne Profil überarbeitet jeder Subagent in seiner eigenen Auslegung von „neutral", und das Buch klingt danach nach fünf Autoren.
3. Eine Datei `kontext.md` anlegen mit dem, was jeder Subagent wissen muss, ohne das Buch zu lesen: Textform und Zielgruppe, Erzählhaltung und Tempus, Namen und Schreibweisen wiederkehrender Personen, Orte, Begriffe, Fachwörter mit der im Buch gewählten Definition, Konventionen (Zahlen, Anführungszeichen, Anrede). Bei Erzähltexten zusätzlich: Figurenliste mit dem, was der Leser bis zu diesem Kapitel weiß.
4. Ein bis zwei Kapitel zuerst überarbeiten lassen und prüfen, bevor die übrigen laufen. Wenn die ersten beiden gut sind, den Rest parallel starten (drei bis fünf gleichzeitig, mehr bringt Abgleichsaufwand ohne Nutzen).

### Auftrag an den Subagenten

Jeder Subagent bekommt einen eigenständigen Auftrag mit allen Pfaden. Vorlage:

```
Du überarbeitest ein Kapitel eines deutschen [Sachbuchs/Romans/...] und entfernst
Stilmuster maschinell geschriebener Prosa. Inhalt und Fakten bleiben unverändert,
Formulierungen darfst du großflächig ändern, ganze Absätze neu schreiben.

Lies zuerst vollständig:
  - <Pfad zum Skill>/SKILL.md
  - <Pfad zum Skill>/references/claudismen.md
  - <Pfad zum Skill>/references/handwerk.md
  - <Pfad zum Skill>/references/ueberarbeitung.md (Abschnitt „Grundsätze" und
    „Ablauf für einen einzelnen Text")
  - <Projektpfad>/stilprofil.md          (Zielstimme; überstimmt Standardwerte)
  - <Projektpfad>/kontext.md              (Namen, Begriffe, Konventionen)

Dann: <Projektpfad>/kapitel/03-original.md

Arbeitsschritte:
  1. Original lesen, nichts ändern.
  2. python3 <Pfad zum Skill>/scripts/pruefung.py <Projektpfad>/kapitel/03-original.md
  3. Überarbeiten nach dem Ablauf in ueberarbeitung.md. Schreibe die Fassung
     nach <Projektpfad>/kapitel/03-fassung.md.
  4. Prüfe die Fassung mit pruefung.py. Liegt „Absätze mit Kurzsatz-Ende" über
     25 % oder „Nicht X, sondern Y" über 1, noch einmal überarbeiten.
  5. Inhaltsabgleich Absatz für Absatz gegen das Original. Schreibe nach
     <Projektpfad>/kapitel/03-abgleich.md eine Liste aller Stellen, an denen
     Inhalt verloren ging, hinzukam oder sich verschob. Wenn nichts: „vollständig".

Verboten: neue Fakten, Zahlen, Namen, Beispiele, Deutungen. Neue Kulissen-Details
in Erzähltexten nur als Ersatz für gestrichene, nie zusätzlich.

Antworte mit höchstens fünf Sätzen: was du hauptsächlich geändert hast und welche
Entscheidung strittig war.
```

Für den Subagenten dasselbe Modell verwenden wie für das Schreiben; die Referenzen sind auf Opus ausgelegt.

### Nachbereitung durch den Hauptagenten

1. Alle `*-abgleich.md` lesen. Jede gemeldete Verschiebung prüfen und entscheiden.
2. Stichprobe: Aus zwei Kapiteln je einen Absatz Original und Fassung nebeneinanderlegen und selbst vergleichen. Die Abgleichsliste des Subagenten ist eine Selbstauskunft.
3. Kapitelübergänge lesen: den letzten Absatz von Kapitel n und den ersten von Kapitel n+1. Subagenten kennen nur ihr Kapitel; Übergänge können nach der Überarbeitung holpern oder sich wiederholen.
4. Ersatz-Tics über Kapitel hinweg suchen: `pruefung.py` auf die zusammengefügte Fassung anwenden und zusätzlich mit grep nach Wendungen suchen, die in der Fassung neu auftauchen und mehr als zweimal pro Kapitel vorkommen. Ein Subagent, der „nicht X, sondern Y" durch „X. Dabei ist es Y." ersetzt, tut das zehnmal, und der nächste Subagent auch.
5. Wiederkehrende Begriffe und Namen gegen `kontext.md` prüfen (grep). Subagenten variieren Schreibweisen, wenn sie nicht festgelegt sind.
6. Dem Nutzer berichten: welche Kapitel fertig sind, welche Abgleichsmeldungen offen sind, wo Übergänge angefasst wurden. Keine Änderungsstatistik, es sei denn, er fragt.

## Wenn der Nutzer nur eine Passage nennt

„Der Absatz klingt nach KI" oder „mach das weniger pointiert": dann nur diese Passage, mit dem Ablauf für einen einzelnen Text, aber ohne Skript. Die Fassung zurückgeben, dazu ein Satz, was das Muster war, damit der Nutzer es selbst erkennt, wenn es wieder auftaucht.
