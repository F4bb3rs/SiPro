import sys #importieren von Modul sys
import aclib as ac #importieren von Modul aclib und als ac ansprechbar machen

if len(sys.argv) != 4: #wenn sys.argv nicht 4 Elemente enthält
    print("Parameter Fehler")
    exit(1)

mode = sys.argv[1] #Übergabeparameter 1 in mode
key = sys.argv[2] #Übergabeparameter 2 in key
path = sys.argv[3] #Übergabeparameter 3 in path

if not path.endswith(".txt"): #wenn path nicht mit .txt endet
    print("Dateityp Fehler")
    exit(2)

try: #Ausnahmebehandlung einleiten
    f = open(path, "r") #öffnen ner Datei in path mit Leserechten
    text = f.read() #auslesn des Inhalt der Datei un in text speichern
except IOError: #Abfangen von Fehlern beim öffnen der Datei
    print("Datei Fehler")
    exit(3)

if len(key) != 2: #wenn key nicht 2 lang ist
    print("Schlüssel Fehler")
    exit(4)
if not (key[0].isalpha() & key[1].isalpha()): #wenn key nicht nur Buchstaben enthält
    print("Schlüssel Fehler")
    exit(5)


a = ac.decode(key[0])[0] #in a 1., in Zahl geänderte, Stelle von key schreiben
b = ac.decode(key[1])[0] #in a 2., in Zahl geänderte, Stelle von key schreiben

if mode == "e": #wenn in mode e steht
    print(ac.acEncrypt(a, b, text)) #Ausgabe der Rückgabe von ac.Encrypt in aclib mit Übergabeparametern a, b, text
elif mode == "d": #wenn in mode d steht
    print(ac.acDecrypt(a, b, text)) #Ausgabe der Rückgabe von ac.Decrypt in aclib mit Übergabeparameter a, b, text
else: #wenn in mode weder e noch d steht
    print("Modus Fehler")
    exit(6)

