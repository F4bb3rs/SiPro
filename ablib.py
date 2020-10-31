import aclib  # importiere die Bibliothek aclib


def computeFrequencyTable(char_list):
    frequency_table = {}  # Leeres Dictionary erstellen
    char_list.sort()  # Eingabe aufsteigend sortieren
    for i in char_list:  # Über Eingabeliste iterienen
        if i in frequency_table:  # Wenn es den Eintrag in dem Dictionry schon gibt,
            frequency_table[i] += 1  # wird die Anzahl für den Eintrag um 1 erhöht
        else:
            frequency_table[i] = 1  # Ansonsten wir ein neuer Eintrag erstellt
    return frequency_table  # Gebe das Dictionary mit den enthaltenen Zahlen und ihrer Häufigkeit zurück


def printFrequencyTable(freq_table):
    for x in freq_table: #für alle Schlüssel
        print(chr(x+97), " : ", freq_table[x])#Ausgabe von Schlüssel als Kleinbuchstabe mit zugehörigem Wert


def computeMostFrequentChars(freq_table, n):
    mostFrequent = []  # Leere Liste erstellen
    sortedTable = sorted(freq_table.items(), key=lambda x: (x[1], x[0]), reverse=True)  # Dictionary wird absteigend
    # sortiert, zuerst nach der Häufigkeit und bei gleicher Häufigkeit nach den Zahlen selbst
    for i in range(0, n):  # Für die gewünschte Anzahl der häufigsten Zahlen,
        mostFrequent.append(sortedTable[i][0])   # werden die Zahlen ohne ihre Häufigkeit in die Liste geschrieben
    return mostFrequent  # Gebe die Liste mit den häufigsten Zahlen zurück


def computeKeyPairs(char_list):
    keyPairs = []  # Leere Liste für die Zahlenpaare erstellen
    for i in char_list:  # Für jede Zahl:
        char_clone = char_list[:]  # Erstelle eine neue zu char_list identische Liste.
        char_clone.remove(i)  # Entferne aktuellen char aus der Liste, damit er nicht mit sich selbst gepaart wird
        for j in char_clone:  # i wird mit jedem anderen char zu einem Paar kombiniert
            keyPairs.append((i, j))
    return keyPairs  # Gebe die Liste mit den möglichen Keys





def analyzeCipherText(cipher_text, char_pairs):
    possible_plains = []  # Leere Liste für mögliche Klartexte erstellen
    for pair in char_pairs:  # Für alle Paare wir durchgeführt:
        a = (3 * (pair[0] - pair[1])) % 26  # Berechnung von a des Keys
        b = (pair[1] - 4 * a) % 26  # Berechnung von b des Keys
        decoded = aclib.acDecrypt(a, b, cipher_text)  # Versuche das Entschlüsseln des textes mit a und b als Key und
        # der Übergabe als Text. Zuweisung der Rückgabe zu decoded
        if isinstance(decoded, str) and len(decoded) > 0:  # Kontrolle ob in decoded Text steht
            possible_plains.append(decoded)  # ,wenn ja wird ein neuer Eintrag in der Liste mit den möglichen Klartexten
            # erzeugt
    return possible_plains  # Gebe die Liste mit den Klartexten zurück
