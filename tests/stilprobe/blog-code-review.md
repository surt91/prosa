# Ratschläge für einen schlechten Code-Reviewer

Lass den Pull Request erst einmal liegen. Drei Tage sind ein guter Anfang, eine Woche ist besser. Der Kollege hat inzwischen zwei andere Sachen im Kopf und muss seinen eigenen Code erst wieder lesen – von vorn, mit dem Ticket daneben –, bevor er dir überhaupt antworten kann. Das erzieht.

Wenn du ihn dann doch aufmachst, schau zuerst nach, wer ihn gestellt hat. Beim Werkstudenten ist Strenge geboten, beim Kollegen mit dem Konferenzvortrag Nachsicht. So sparst du dir das Lesen – und ein Urteil hast du trotzdem.

Und der Autor mag das: dass über seine Arbeit der Name im Git-Log entscheidet; dass er nie erfährt, was du vom Ganzen hältst, dafür aber alles über Zeile 43. Nur nichts über das Ganze sagen!

Lies nie den ganzen Diff – das kostet ja Zeit. Das Beste ist, du nimmst die erste geänderte Datei und die letzte. Was dazwischen liegt, macht der andere schon richtig, und wenn nicht, fällt es in der Produktion auf, wo man es ohnehin gründlicher untersucht als in jedem Review …

Kommentiere Formatierung: Einrückung, Klammern, die Reihenfolge der Importe. Der Linter tut es auch, aber der Linter bekommt kein Lob.

Frag nach dem Warum und schlag nie etwas vor: „Warum hast du das hier so gelöst?" Sechs Wörter, ein Fragezeichen, und der andere darf eine Woche raten, was du gemeint hast, ob es ein Vorwurf war oder Neugier, ob er umbauen soll oder nur antworten. Sehr richtig! Für Erklärungen gibt es die Dokumentation, und die schreibt ja auch keiner.

Schick deine Anmerkungen einzeln, im Abstand von zwanzig Minuten. Dreiundzwanzig Benachrichtigungen an einem Vormittag – so weiß er, dass an ihn gedacht wird.

Halte jede Anmerkung kurz, damit sie länger hält: „Das ist falsch." Zwei Wörter, keine Stelle, kein Grund. Der andere darf dann selbst suchen, was du gemeint hast, und findet auf dem Weg vielleicht noch etwas, das du gar nicht gesehen hattest.

Und wenn du etwas grundsätzlich anders haben willst, dann schreib es nicht oben hin, wo es jeder sieht, sondern erst, nachdem du, wie sich das gehört, achtzehn Anmerkungen zu Variablennamen, zur Reihenfolge der Argumente und zu jenem Leerzeichen gesetzt hast, für das der Formatter zuständig wäre, den ihr im Vorjahr nach einer Diskussion eingeführt habt, an die sich keiner mehr erinnert; und dann setz die Bemerkung über den Umbau, der vier Tage dauern wird, in den vorletzten Kommentar unter einer Testdatei, die niemand aufklappt … so ungefähr. Du siehst, es geht.

Verlange Tests, aber sag nicht, welche!

Nenne ein Entwurfsmuster beim Namen und erkläre es nicht. Wer es nicht kennt, kann nachschlagen; und wer im Review etwas lernt, hat das Verfahren sowieso missverstanden.

Vergleiche mit deinem eigenen Code: „In meinem Service machen wir das anders." Mehr braucht es nicht. Welcher Service, warum anders, und ob das hier überhaupt passt, kann sich jeder selbst zusammenreimen.

Halte dir bei allem, was du sagst, eine Tür offen. „Ich hätte es vielleicht anders gemacht, aber mach ruhig, wie du willst." So bist du nie schuld, weder wenn er es ändert noch wenn er es lässt.

Blockiere! Es kostet dich nichts.

Und dann, wenn er dreimal nachgefragt hat und sein Zweig anfängt, gegen den Hauptzweig zu treiben, gib dein Häkchen und schreib „LGTM" darunter – vier Sekunden nach dem letzten Push, bei sechshundert geänderten Zeilen. Das freut alle. Du hast schließlich auch zu tun.

Rede nie mit ihm. Ein Review ist Schriftverkehr, weil doch geschrieben wird. Zwei Leute an einem Bildschirm klären in zehn Minuten, was über Kommentare zwei Tage braucht; aber wer weiß das schon nach elf Jahren im Beruf. Schreib ruhig weiter. Der Kanal ist ja da, und du bist der Zuständige.

## Ratschläge für einen guten Code-Reviewer

Erst das Ticket. Dann der Diff. Dann der Diff noch einmal, von unten nach oben.

Am selben Tag antworten, spätestens am nächsten Morgen.

Sag, was du geändert haben willst, und sag dazu, ob es eine Bedingung ist oder eine Meinung. Beides ist erlaubt. Nur die Verwechslung nicht.

Was eine Maschine anmerken kann, merkt die Maschine an. Dafür habt ihr sie eingerichtet.

Wenn du zwanzig Kommentare geschrieben hast, hör auf und setz dich mit ihm hin.

Ein Review ist ein Gespräch zwischen zwei Leuten, die denselben Code warten werden. Einer davon bist du.

Der Code, den du heute durchwinkst, ist der Code, den du im Januar debuggst.
