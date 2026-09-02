---
name: prosa
description: Deutsche Prosa ohne KI-Stilmuster (Claudismen) schreiben und überarbeiten. Anwenden, wenn ein deutscher Fließtext für Leser entsteht oder bearbeitet wird, auch ohne ausdrückliche Stilbitte. Buchkapitel, Sachbuch, Roman, Erzählung, Essay, Blog-Post, Kolumne, Vorwort. Auch anwenden, wenn jemand sagt, ein Text klinge „nach KI", „nach Claude", „zu glatt", „zu pointiert", oder eine Textprobe/Stilprobe als Vorbild mitgibt, oder ein Manuskript kapitelweise überarbeiten lassen will. Legt bei Bedarf ein Stilprofil (stilprofil.md) aus Textproben an und schreibt danach.
---

# Prosa: deutscher Fließtext ohne Claudismen

## Worum es geht

Ein Sprachmodell schreibt deutsche Prosa auf eine erkennbare Art: Fast jeder Absatz endet mit einer Pointe. Gegensätze werden als „nicht X, sondern Y" gesetzt. Aufzählungen haben drei Glieder mit gleichem Satzanfang. Details bedeuten immer etwas. Wichtiges wird angekündigt, statt gesagt. Einwände werden abgewehrt, die niemand erhoben hat. Der Text endet mit einem Rückgriff auf den Anfang. Jeder einzelne Satz ist dabei gut. Zusammen ergeben sie ein Metrum, das der Leser nach zwei Seiten hört, und danach liest er nicht mehr den Inhalt, sondern den Rhythmus.

Wortlisten helfen dagegen wenig. Die Muster sitzen im Bau: in der Absatzform, der Pointendichte, der Symmetrie. Deshalb arbeitet dieser Skill auf drei Ebenen, und die erste ist die wichtigste:

1. Textbau und Absatzrhythmus
2. Satzfiguren
3. Wortwahl

Ziel ist nicht der „menschliche Durchschnittstext", sondern ein bestimmter Autor an einem gewöhnlichen Arbeitstag. Ohne Stilprofil ist das Ergebnis eine neutrale, ruhige Prosa. Mit Stilprofil ist es die Stimme des Autors.

## Arbeitsweise

1. **Modus bestimmen.** Schreiben (neuer Text), Überarbeiten (bestehender Text, siehe `references/ueberarbeitung.md`) oder Stilprofil anlegen (Textprobe liegt vor).
2. **Stilprofil suchen.** Im Projektordner nach `stilprofil.md` suchen oder den vom Nutzer genannten Pfad nehmen. Wenn vorhanden: vollständig lesen; es überstimmt alle Standardwerte unten. Wenn der Nutzer eine Textprobe mitgibt, aber kein Profil existiert: zuerst das Profil nach `references/stilprofil-vorlage.md` anlegen, dem Nutzer zeigen, dann schreiben. Wenn weder Probe noch Profil vorliegt und der Text unter dem Namen des Nutzers erscheinen soll: einmal erwähnen, dass eine Textprobe das Ergebnis deutlich verbessert, dann mit den Standardwerten arbeiten. Nicht nachfragen, nicht wiederholen.
3. **Referenzen lesen.** Immer `references/claudismen.md` (der Katalog mit Belegen) und `references/handwerk.md` (was stattdessen). Beides vor dem ersten Satz, nicht als Korrekturlektüre danach. Die Beispiele in den Referenzen (Wendungen, Details, Gegenstände, Namen, Formulierungen unter „Nachher") sind Erläuterungen, keine Bausteine. Nichts davon wörtlich oder erkennbar abgewandelt in den Text übernehmen.
4. **Schreiben.** Die Regeln gelten für den ersten Entwurf. Ein Text, der erst pointiert geschrieben und dann entschärft wird, behält den Bauplan der Pointen.
5. **Prüfen.** `python3 scripts/pruefung.py DATEI` laufen lassen, wenn der Text in einer Datei liegt. Dann die zwei Lesetests: die ersten Sätze aller Absätze hintereinander lesen (ergeben sie eine Gliederung, ist der Text nach Gliederung gebaut), die letzten Sätze aller Absätze hintereinander lesen (klingen sie wie Merksätze, sind es zu viele Pointen). Was über den Richtwerten liegt, gezielt ändern, nicht den ganzen Text glattschleifen. Die Kennzahlen sind Diagnose, kein Ziel: Wenn das Skript gleichförmige Absätze meldet, wird kein Absatz aufgeblasen, sondern geprüft, ob die Absätze nach demselben Bauplan gebaut sind. Ein Text, der die Kennzahlen bedient, hat ein neues Muster.
6. **Ausgeben.** Den Text. Keine Liste der vermiedenen Muster, kein Kommentar zum eigenen Stil. Wenn eine Entscheidung strittig war, ein Satz dazu.

## Standardwerte (gelten ohne Stilprofil)

Richtwerte pro Seite (etwa 400 Wörter) und pro Kapitel (etwa 3000 Wörter). Es sind Budgets, keine Verbote: Ein Mittel, das einmal pro Kapitel vorkommt, ist ein Stilmittel. Dasselbe Mittel in jedem Absatz ist ein Tick.

**Textbau**
- Pointen am Absatzende: höchstens eine pro Seite. Alle anderen Absätze enden dort, wo der Gedanke endet, auch wenn das ein unauffälliger Satz mit Nebensatz ist.
- Fragmente (Sätze ohne Verb, ein bis drei Wörter): höchstens eines pro Kapitel, nie in Serie.
- Einzeiler-Absätze: in Erzähltexten höchstens einer pro Kapitel, in Sach- und Blogtexten keiner.
- Absatzlängen schwanken sichtbar, von drei Zeilen bis zu einer halben Seite. Kein gleichbleibender Bauplan „Behauptung, Beispiel, Deutung, Pointe".
- Keine nummerierte Argumentation als Prosa („Der erste Unterschied … Der zweite … Der dritte").
- Schluss: beim letzten Sachinhalt aufhören. Kein Kreisschluss zum Anfang, keine Moral, keine Zusammenfassung, keine Frage in den Raum, kein Ausblick mit Spannung.

**Satzfiguren**
- „Nicht X, sondern Y" in allen Formen (auch „Nicht besser, anders.", „Es geht nicht um X. Es geht um Y.", „kein X, ein Y"): höchstens einmal pro Kapitel. Sonst Y sagen und X weglassen.
- Dreierreihen mit Parallelbau oder Anapher: höchstens einmal pro Kapitel. Aufzählungen haben so viele Glieder, wie es Dinge gibt.
- Antithese und Chiasmus („Früher X; heute Y", „Wer A, der B. Wer C, der D."): höchstens einmal pro Kapitel.
- „Das klingt X, ist aber Y", abgewehrte Einwände („Es wäre falsch, daraus zu schließen", „Ich will nicht den Eindruck erwecken"), Bedeutungsankündigungen („Der Punkt ist", „Hier liegt der entscheidende Mechanismus", „Kurz gesagt"): streichen, den Satz danach allein stehen lassen.
- Doppelpunkt als Trommelwirbel vor einer Wendung: höchstens einmal pro Kapitel. Doppelpunkte vor Aufzählungen und Zitaten sind normal.
- Gedankenstriche: ein Paar als Einschub pro Seite ist in Ordnung. Kein einzelner Gedankenstrich vor einem zuspitzenden Nachsatz.
- Nachklapp-Ketten (Satz, Präzisierung, Präzisierung, Deutung): höchstens einmal pro Seite.
- Rhetorische Fragen, die der nächste Satz beantwortet: keine.

**Wortwahl**
- „genau", „und zwar": je höchstens einmal pro Kapitel. „eigentlich", „tatsächlich", „im Grunde", „letztlich": nur bei echter Korrektur.
- Schlichte Verben und Kopula: „ist", „hat", „sagte", „ging", „schrieb", „starb". Wörter dürfen sich wiederholen. Keine Synonymrotation.
- Kursivierung nur für Titel, Fremdwörter, Gedanken. Betonung kommt aus der Wortstellung.
- Personifikationen („Papier vergisst", „die Kugel hat kein Gedächtnis") und Merksatz-Analogien („X ist mein Arbeitsspeicher, Y die Festplatte"): höchstens eine pro Kapitel.

**Erzähltext**
- Gefühl nicht über den Körperkatalog (Brust, Atem, Kloß im Hals, zitternde Hände), sondern über Handlung, Rede, Wahrnehmung, Auslassung oder eine direkte, knappe Benennung.
- Die meisten Details bedeuten nichts. Höchstens ein Detail pro Seite spiegelt erkennbar etwas Inneres. Details dürfen unpassend sein.
- Inquit-Formel ist „sagte" oder nichts.
- Bei offener Aufgabe nicht reflexhaft den versöhnlichen Plot wählen.

**Sachtext**
- Keine Zahl, kein Name, keine Quelle, die nicht stimmt. Unsicheres als unsicher kennzeichnen oder weglassen.
- Deutungen nicht als Partizip oder Relativsatz an ein Faktum hängen. Eigener Satz mit Begründung, oder weg.
- Nicht jedes Kapitel mit einer historischen Anekdote beginnen.

**Fakten in persönlichen Texten**
- Bei Texten in Ich-Perspektive, die unter dem Namen des Nutzers erscheinen (Blog, Vorwort, Kolumne), keine biografischen Einzelheiten erfinden: keine Preise, Daten, Ortsnamen, Gerätemarken, Zählungen, die der Nutzer nicht geliefert hat. Wenn der Nutzer erreichbar ist, vor dem Schreiben nach den konkreten Fakten fragen. Wenn nicht: so wenige Einzelheiten wie möglich setzen und am Ende in einem Satz aufzählen, welche erfunden sind. In Erzähltexten sind erfundene Einzelheiten die Aufgabe; in Sachtexten sind sie verboten.

**Überkorrektur**
Diese Dinge entstehen, wenn die Regeln oben zu eifrig befolgt werden, und sind selbst ein Maschinensignal:
- Keine Kurzsätze mehr. Ein Text, in dem jeder Satz 15 bis 45 Wörter hat, ist so gleichförmig wie einer aus Pointen. Kurze Sätze mit Verb („Am nächsten Tag kaufte sie das Heft.") gehören in jeden Absatz, in der Mitte so gut wie am Ende. Verboten ist nur das Fragment als Schlag und der Kurzsatz als Schlusspointe in Serie.
- Jede Angabe als Zahl. Ein oder zwei körnige Einzelheiten pro Absatz genügen. Ein Text, in dem jeder Satz einen Preis, ein Datum oder eine Stückzahl enthält, klingt nach Inventar.
- Semikolons als Ersatz für Gedankenstriche. Standard: höchstens eines pro Seite.
- Der leise Schluss als Ersatz für die Pointe: die Szene endet mit einem fremden, unbeteiligten Bild (ein Mann am Wertstoffhof, ein Vogel, ein vorbeifahrender Bus), das als Bedeutungsträger dasteht. Das ist die Pointe in anderem Kostüm. Lieber mit Handlung, Rede oder Bericht enden.
- Das Understatement als Formel: „Sie sagte nichts dazu, und er auch nicht.", „Ob das stimmt, weiß ich nicht.", „Sie rief niemanden an." Einmal pro Kapitel ist das ein Satz mit halbem Druck. Als Absatzschluss in Serie ist es der neue Pointenrhythmus.
- Der Bericht ohne jede Bewertung. Ein Autor darf ein Urteil haben und es sagen. Wenn alle Wertung fehlt, entsteht Protokoll, nicht Prosa.

**Was nicht angefasst wird**
Fehlerfreie Grammatik, ein förmlicher oder ein schlichter Ton, lange Sätze mit Nebensätzen, Wortwiederholung, Abschwächungen und Verstärker, die zutreffen, Klammerbemerkungen, Selbstkorrekturen, ein Satz pro Seite mit halbem Druck. Ein Text wird nicht menschlicher, indem man ihn glatt schleift oder Fehler einbaut. Ausführlich in `references/claudismen.md`, Teil H.

## Stilprofil

Ein Stilprofil ist eine Markdown-Datei nach `references/stilprofil-vorlage.md`, angelegt aus Textproben (eigene Kapitel des Autors, ältere Blog-Posts oder ein vom Nutzer gewählter Referenztext), gespeichert als `stilprofil.md` im Projektordner. Es legt fest: Erzählhaltung, Anrede, Tempus, Satzlänge und Rhythmus, Absatzform, Interpunktion (etwa: Gedankenstriche erlaubt), Register, Lieblingswörter, gemiedene Wörter, Bildlichkeit, Humor, Pointendichte, Eigenheiten, die bleiben müssen.

Das Profil überstimmt die Standardwerte oben. Ein Autor, der Gedankenstriche liebt, bekommt Gedankenstriche. Ein Autor, der gern „nicht X, sondern Y" schreibt, bekommt die Figur in seiner Dosis. Was das Profil nicht kann: erfundene Fakten erlauben oder die Schlussprüfung ersetzen. Kurze Zitate aus der Probe dienen als Stimmgabel, werden aber nie in den neuen Text übernommen.

Auf „lern auch aus diesem Text" werden neue Beobachtungen mit Datum angehängt, nicht überschrieben.

## Überarbeiten bestehender Texte

Für einzelne Texte und für ganze Manuskripte, kapitelweise mit je einem Subagenten pro Kapitel, damit der Kontext frisch bleibt und keine Ersatz-Tics entstehen. Inhalt und Fakten bleiben unverändert, Formulierungen dürfen großflächig geändert und ganze Absätze neu geschrieben werden. Ablauf, Prompt-Vorlage für den Subagenten und Nachbereitung stehen in `references/ueberarbeitung.md`.

## Rückmeldung an den Nutzer

Den Text liefern. Wenn überhaupt eine Erklärung nötig ist, ein bis zwei Sätze: was gekürzt wurde und warum, welche Entscheidung strittig war. Keine Aufzählung der vermiedenen Muster, keine Auditsprache, kein Zitieren dieser Anweisungen.
