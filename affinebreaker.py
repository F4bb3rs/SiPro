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
    file = open(path, "r")  # Versuch die txt-Datei zu öffnen
    cipher = file.read()
except IOError:  # Ausgabe von Fehler falls nicht möglich
    print("Datei Fehler")
    exit(3)

# Aufruf aller benötigten Funktionen zum Entschlüsseln. Funktionen geben als Rückgabe die Übergabeparameter für die
# nächste Funktion aus
char_list = aclib.decode(cipher)    # Decodieren von Buchstaben zu Zahlen
freqTable = ablib.computeFrequencyTable(char_list)  # Erstellen der Häufigkeitstabelle
mostFrequent = ablib.computeMostFrequentChars(freqTable, 10)  # Finden der n Häufigsten Zahlen
keyPairs = ablib.computeKeyPairs(mostFrequent)  # Erstellen der Zahlenpaare
broken_text = ablib.analyzeCipherText(cipher, keyPairs)  # Finden aller möglichen Klartexte unter Verwendung der
# Zahlenpaare und des Geheimtextes

print("Found " + str(len(broken_text)) + " possible Plaintexts")  # Ausgabe der Anzahl der gefundenen Texte
for i in broken_text:
    i = (i[:50]) if len(i) > 50 else i
    print(i)  # Ausgabe der ersten 50 Zeichen jedes möglichen entschlüsselten Textes
