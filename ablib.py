import aclib  # importiere die Bibliothek aclib

def compute_frequencyTable(char_list):
    frequency_table = {}  # leeres Dictionary erstellen
    char_list.sort()  # Eingabe aufsteigend sortieren
    for i in char_list:  # Über Eingabeliste iterienen
        if i in frequency_table:  # Wenn es den Eintrag in dem Dictionry schon gibt
            frequency_table[i] += 1  # Anzahl für Eintrag um 1 erhöhen
        else:
            frequency_table[i] = 1  # neuen Eintrag anlegen
    return frequency_table  # gebe das Dictionary mit den enthaltenen Zahlen und ihrer Häufigkeit zurück



def computeMostFrequentChars(freq_table, n):
    shorter = []  # leere Liste erstellen
    sortedTable = sorted(freq_table.items(), key=lambda x: (x[1], x[0]), reverse=True)
    # Dictionary wird absteigend sortiert, zuerst nach der Häufigkeit und bei gleicher Häufigkeit nach den Zahlen selbst
    for i in range(0, n):   # Für die gewünschte Anzahl der häufigsten Zahlen
        shorter.append(sortedTable[i][0])   # werden die Zahlen ohne ihre Häufigkeit in die Liste geschrieben
    return shorter  # gebe die Liste mit den häufigsten Zahlen zurück


def computeKeyPairs(char_list):
    output = []  # leere Liste erstellen
    for i in char_list:  # für jede Zahl
        char_clone = char_list[:]  # Erstelle eine neue neue zu char_list identische Liste.
        # Kopiere Variable, nicht nur Referenz.
        char_clone.remove(i)  # entferne aktuellen char aus der Liste, damit er nicht mit sich selbst gepaart wird
        for j in char_clone:  # i wird mit jedem anderen char zu einem Paar kombiniert
            output.append((i, j))
    return output  # gebe die Liste mit den möglichen Keys


def analyzeCipherText(cipher_text, char_pairs):
    possible_plains = []  # leere Liste erstellen
    for pair in char_pairs:  # für alle Paare wir durchgeführt:
        a = (3 * (pair[0] - pair[1])) % 26  # Berechnung von a des Keys
        b = (pair[1] - 4 * a) % 26  # berechnung von b des Keys
        decoded = aclib.acDecrypt(a, b, cipher_text)  # versuche das Entschlüsseln des textes mit a und b als Key und
        # der Übergabe als Text. Zuweisung der Rückgabe zu decoded
        if isinstance(decoded, str) and len(decoded) > 0:  # Kontrolle ob in decoded Text steht
            possible_plains.append(decoded)  # wenn ja, neuer Eintrag in der Liste mit den möglichen Klartexten
    return possible_plains  # gebe die Liste mit den Klartexten zurück

