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

# Aufruf aller benötigten Funktionen zum entschlüsseln
char_list = aclib.decode(cipher)    # decodieren von Buchstaben zu Zahlen
freqTable = ablib.compute_frequencyTable(char_list)  # erstellen der Häufigkeitstabelle
mostFrequent = ablib.computeMostFrequentChars(freqTable, 10)  # finden der n Häufigsten Zahlen
keyPairs = ablib.computeKeyPairs(mostFrequent)  # erstellen der Zahlenpaare
broken_text = ablib.analyzeCipherText(cipher, keyPairs)  # finden aller möglichen Klartexte unter Verwendung der
# Zahlenpaare und des anfänglichen verschlüsselten Textes

print("Found " + str(len(broken_text)) + " possible Plaintexts")  # ausgabe der Anzahl der gefundenen Texte
for i in broken_text:
    i = (i[:50]) if len(i) > 50 else i
    print(i)  # Ausgabe der ersten 50 Zeichen jedes möglichen entschlüsselten Textes
