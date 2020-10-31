import ablib
import aclib
import sys

path = sys.argv[1]

if len(sys.argv) != 2:  # Test auf Anzahl der Aurgumente
    print("Argument Fehler")
    exit(1)

if not path.endswith(".txt"):  # Test auf Dateityp
    print("Dateityp Fehler")
    exit(2)
try:
    file = open(path, "r")  # Versuch die txt-Datei zu oeffnen
    cipher = file.read()
except IOError:  # Ausgabe von Fehler falls nicht moeglich
    print("Datei Fehler")
    exit(3)

# Aufruf aller benoetigten Funktionen zum Entschluesseln. Funktionen geben als Rueckgabe die uebergabeparameter fuer die
# naechste Funktion aus
char_list = aclib.decode(cipher)    # Decodieren von Buchstaben zu Zahlen
freqTable = ablib.computeFrequencyTable(char_list)  # Erstellen der Haeufigkeitstabelle
mostFrequent = ablib.computeMostFrequentChars(freqTable, 6)  # Finden der n Haeufigsten Zahlen
keyPairs = ablib.computeKeyPairs(mostFrequent)  # Erstellen der Zahlenpaare
broken_text = ablib.analyzeCipherText(cipher, keyPairs)  # Finden aller moeglichen Klartexte unter Verwendung der
# Zahlenpaare und des Geheimtextes

z = 0
print("Found " + str(len(broken_text)) + " possible Plaintexts")  # Ausgabe der Anzahl der gefundenen Texte
for i in broken_text:
    i = (i[:50]) if len(i) > 50 else i
    z += 1
    if z is 7:
        break
    print(i)  # Ausgabe der ersten 50 Zeichen jedes moeglichen entschluesselten Textes
