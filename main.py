def compute_frequencyTable(char_list):
    frequency_table = {} #Dictionary anlegen
    char_list.sort() #Eingabe aufsteigend sortieren
    for i in char_list: # Über Eingabeliste iterienen
        if i in frequency_table: #Wenn es den Eintrag in dem Dictionry schon gibt
            frequency_table[i] += 1 #++
        else:
            frequency_table[i] = 1 # Eintrag anlegen
    return frequency_table

#compute_frequencyTable([4, 8, 13, 11, 0, 13, 6, 4, 17, 19, 4, 23, 19, 14, 7, 13, 4, 18,8, 13, 13])


def computeMostFrequentChars(freq_table, n):
    shorter = {}
    for i in range(0, n):
        shorter[i] = sorted(freq_table.items(), key=lambda x: (x[1], x[0]), reverse=True)[i]
        #print( str(i) + " : " + str(shorter[i]))
    return shorter

#computeMostFrequentChars({0: 1, 4: 4, 6: 1, 7: 1, 8: 2, 11: 1, 13: 5, 14: 1, 17: 1, 18: 1,19: 2, 23: 1}, 6)


def computeKeyPairs(char_list):
    output = []
    for i in char_list:
        print("i = " + str(i))
        char_clone = char_list[:] # Kopiere Variable, nicht nur Referenz
        char_clone.remove(i)
        for j in char_clone:
            output.append((i, j))
    print(output)
    return output

#computeKeyPairs([13,4,19])

def analyzeCipherText(cipher_text, char_pairs):
    for pair in char_pairs:
        a = (3 * (pair[0] - pair[1])) % 26
        b = pair[1] - 4 * a

