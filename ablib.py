import aclib  # importiere die Bibliothek aclib


def computeFrequencyTable(char_list):
    frequency_table = {}  # Leeres Dictionary erstellen
    char_list.sort()  # Eingabe aufsteigend sortieren
    for i in char_list:  # ?ber Eingabeliste iterienen
        if i in frequency_table:  # Wenn es den Eintrag in dem Dictionry schon gibt,
            frequency_table[i] += 1  # wird die Anzahl f?r den Eintrag um 1 erh?ht
        else:
            frequency_table[i] = 1  # Ansonsten wir ein neuer Eintrag erstellt
    return frequency_table  # Gebe das Dictionary mit den enthaltenen Zahlen und ihrer H?ufigkeit zur?ck


def printFrequencyTable(freq_table):
    for x in freq_table: #f?r alle Schl?ssel
        print(chr(x+97), " : ", freq_table[x])#Ausgabe von Schl?ssel als Kleinbuchstabe mit zugeh?rigem Wert


def computeMostFrequentChars(freq_table, n):
    mostFrequent = []  # Leere Liste erstellen
    print(freq_table)
    sortedTable = sorted(freq_table.items(), key=lambda x: (x[1], x[0]), reverse=True)  # Dictionary wird absteigend
    print(sortedTable)
    # sortiert, zuerst nach der H?ufigkeit und bei gleicher H?ufigkeit nach den Zahlen selbst
    for i in range(0, n):  # F?r die gew?nschte Anzahl der h?ufigsten Zahlen,
        mostFrequent.append(sortedTable[i][0])   # werden die Zahlen ohne ihre H?ufigkeit in die Liste geschrieben
    return mostFrequent  # Gebe die Liste mit den h?ufigsten Zahlen zur?ck


def computeKeyPairs(char_list):
    keyPairs = []  # Leere Liste f?r die Zahlenpaare erstellen
    for i in char_list:  # F?r jede Zahl:
        char_clone = char_list[:]  # Erstelle eine neue zu char_list identische Liste.
        char_clone.remove(i)  # Entferne aktuellen char aus der Liste, damit er nicht mit sich selbst gepaart wird
        for j in char_clone:  # i wird mit jedem anderen char zu einem Paar kombiniert
            keyPairs.append((i, j))
    return keyPairs  # Gebe die Liste mit den m?glichen Keys





def analyzeCipherText(cipher_text, char_pairs):
    possible_plains = []  # Leere Liste f?r m?gliche Klartexte erstellen
    for pair in char_pairs:  # F?r alle Paare wir durchgef?hrt:
        a = (3 * (pair[1] - pair[0])) % 26  # Berechnung von a des Keys
        b = (pair[0] - 4 * a) % 26  # Berechnung von b des Keys
        decoded = aclib.acDecrypt(a, b, cipher_text)  # Versuche das Entschl?sseln des textes mit a und b als Key und
        # der ?bergabe als Text. Zuweisung der R?ckgabe zu decoded
        if isinstance(decoded, str) and len(decoded) > 0:  # Kontrolle ob in decoded Text steht
            possible_plains.append(decoded)  # ,wenn ja wird ein neuer Eintrag in der Liste mit den m?glichen Klartexten
            # erzeugt
    return possible_plains  # Gebe die Liste mit den Klartexten zur?ck
