import aclib

def compute_frequencyTable(char_list):
    frequency_table = {} #Dictionary anlegen
    char_list.sort() #Eingabe aufsteigend sortieren
    for i in char_list: # Über Eingabeliste iterienen
        if i in frequency_table: #Wenn es den Eintrag in dem Dictionry schon gibt
            frequency_table[i] += 1 #++
        else:
            frequency_table[i] = 1 # Eintrag anlegen
    return frequency_table



def computeMostFrequentChars(freq_table, n):
    shorter = []
    sortedTable = sorted(freq_table.items(), key=lambda x: (x[1], x[0]), reverse=True)
    for i in range(0, n):
        shorter.append(sortedTable[i][0])
    return shorter

#computeMostFrequentChars({0: 1, 4: 4, 6: 1, 7: 1, 8: 2, 11: 1, 13: 5, 14: 1, 17: 1, 18: 1,19: 2, 23: 1}, 6)


def computeKeyPairs(char_list):
    output = []
    for i in char_list:
        char_clone = char_list[:] # Kopiere Variable, nicht nur Referenz
        char_clone.remove(i)
        for j in char_clone:
            output.append((i, j))
    return output



def analyzeCipherText(cipher_text, char_pairs):
    possible_plains = []
    for pair in char_pairs:
        a = (3 * (pair[0] - pair[1])) % 26
        b = pair[1] - 4 * a
        decoded = aclib.acDecrypt(a, b, cipher_text)
        if isinstance(decoded, str) and len(decoded) > 0:
            possible_plains.append(decoded)
    return possible_plains