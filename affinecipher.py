import sys

import aclib as ac

modus = sys.argv[1]
key = sys.argv[2]
path = sys.argv[3]

if len(sys.argv) != 4:
    print("Parameter Fehler")
    exit(1)

f = open(path, "r")
text = f.read()

if len(key) != 2:
    print("Schlüssel Fehler")
    exit(2)

a = ac.decode(key[0])[0]
b = ac.decode(key[1])[0]

if modus == "e":
    print(ac.acEncrypt(a, b, text))
elif modus == "d":
    print(ac.acDecrypt(a, b, text))
else:
    print("Modus Fehler")


#def compute_frequencyTable(char_list):
