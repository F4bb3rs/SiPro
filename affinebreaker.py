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
    file = open(path, "r")  # Versuch die txt-Datei zu ?ffnen
    cipher = file.read()
except IOError:  # Ausgabe von Fehler falls nicht m?glich
    print("Datei Fehler")
    exit(3)

# Aufruf aller ben?tigten Funktionen zum Entschl?sseln. Funktionen geben als R?ckgabe die ?bergabeparameter f?r die
# n?chste Funktion aus
char_list = aclib.decode(cipher)    # Decodieren von Buchstaben zu Zahlen
freqTable = ablib.computeFrequencyTable(char_list)  # Erstellen der H?ufigkeitstabelle
mostFrequent = ablib.computeMostFrequentChars(freqTable, 6)  # Finden der n H?ufigsten Zahlen
keyPairs = ablib.computeKeyPairs(mostFrequent)  # Erstellen der Zahlenpaare
broken_text = ablib.analyzeCipherText(cipher, keyPairs)  # Finden aller m?glichen Klartexte unter Verwendung der
# Zahlenpaare und des Geheimtextes

print("Found " + str(len(broken_text)) + " possible Plaintexts")  # Ausgabe der Anzahl der gefundenen Texte
for i in broken_text:
    i = (i[:50]) if len(i) > 50 else i
    print(i)  # Ausgabe der ersten 50 Zeichen jedes m?glichen entschl?sselten Textes
