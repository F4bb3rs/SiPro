def decode(text):
    list = []   #Deklariere Hilfsliste
    for i in text:  #Iteriere alle Zeichen in text
        if i.isalpha(): #Prüfe, ob BUchstabe ist
            list.append(ord(i.lower()) - 97)    #Füge der Liste die zugehoerige Zahl zu.
                                                # 97 werden abgezogen, da das der Unicode Offset von a ist. Wir wollen aber Zahlen von 0 bis 25
    return list


def encode(list):
    string = ""
    for i in list:
        string += chr(i + 97)   #Füge an String den Charakter als Zeichen hinzu. +97, da chr() einen Unicode Wert erwartet
    return string


key_table = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}
#Definiere key_table mit den inversen Elementen

def checkKey(a, b):
    if b > 27 or b < 0: #Prüfe ob der Schluessel b in einem g?ltigen Bereich ist
        print("b out of range: " + str(b))
        return False
    if not a in key_table:  #Prüfe ob a in der key_table Tabelle ist und somit ein inverses besitzt
        print("a not in key_table")
        return False
    return True


def acEncrypt(a, b, plain_text):
    if not checkKey(a, b):  #Prüfe die beiden Schlüssel
        return ""
    secret = [] #Lege Hilfsliste an
    decoded_list = decode(plain_text)   #Dekodiere die einzelnen Buchstaben aus dem plain_text in eine Liste
    for i in decoded_list:  #Iteriere durch einzelen Zahlen der Liste
        secret.append((a * i + b) % 26) #Füge an die HIlfsliste die errechneten "verschlüsselten" Zahlen hinzu
                                        # Hier geschieht die eigentliche Verschluesselung
    secret = encode(secret) #übersetze diese Zahlen wieder in Buchstaben

    return secret.upper()   #Gebe diese Buchstaben als Großbuchstaben zurueck


def acDecrypt(a, b, cipher_text):
    if not checkKey(a, b):  #Prüfe die beiden Schlüssel
        return ""
    secret = []     #Lege Hilfsliste an
    decoded_list = decode(cipher_text)  #Dekodiere die einzelnen Buchstaben aus dem plain_text in eine Liste
    for i in decoded_list:   #Iteriere durch einzelen Zahlen der Liste
        secret.append(((i - b) * key_table[a]) % 26)    #Füge an die Hilfsliste die errechneten klartext Zahlen hinzu
                                                        # Hier geschieht die eigentliche Verschlüsselung
    secret = encode(secret) #Übersetze diese Zahlen wieder in Buchstaben
    return secret
