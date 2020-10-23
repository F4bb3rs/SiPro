import aclib
import sys

path = sys.argv[1]

if len(sys.argv) != 2:
    print("Parameter Fehler")
    exit(1)

if not path.endswith(".txt"):
    print("Dateityp Fehler")
    exit(2)
try:
    file = open(path, "r")
    cipher = file.read()
except IOError:
    print("Datei Fehler")
    exit(3)


char_list = aclib.decode(cipher)
freqTable = aclib.compute_frequencyTable(char_list)
mostFrequent = aclib.computeMostFrequentChars(freqTable, 10)
keyPairs = aclib.computeKeyPairs(mostFrequent)
broken_text = aclib.analyzeCipherText(cipher, keyPairs)

print("Found " + str(len(broken_text)) +  "possible Plaintexts", )
for i in broken_text:
    print(i)
