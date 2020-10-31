import sys  #Importiere sys um Arugmente einlesen zu können
import aclib as ac  #Importiere unsere Funktionen

if len(sys.argv) != 4:  #Prüfe Argument auf Länge
    print("Parameter Fehler")
    exit(1)

mode = sys.argv[1]  #Weise Argumente Variablen zu
key = sys.argv[2]
path = sys.argv[3]

if not path.endswith(".txt"):   #Prüfe Dateipfad auf Endung/Dateityp
    print("Dateityp Fehler")
    exit(2)

try:    #Versuche die Datei zum Lesen zu öffnen
    f = open(path, "r")
    text = f.read()
except IOError:
    print("Datei Fehler")
    exit(3)

if len(key) != 2:   #Prüfe Schlüssel auf Länge
    print("Schlüssel Fehler")
    exit(4)
if not (key[0].isalpha() & key[1].isalpha()):   #Prüfe ob Schlüssel nur Buchstaben sind
    print("Schlüssel Fehler")
    exit(5)

a = ac.decode(key[0])[0]    #Wandle Buchstaben in Unicode um, [0] da decode eine Liste zurückgibt
b = ac.decode(key[1])[0]

if mode == "e": #Je nach Eingabemodus wird
    print(ac.acEncrypt(a, b, text)) #Verschlüsselt
elif mode == "d":
    print(ac.acDecrypt(a, b, text)) #Oder entschlüsselt
else:
    print("Modus Fehler")
    exit(6)
