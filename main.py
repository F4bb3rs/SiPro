def compute_frequencyTable(char_list):
    frequency_table = {} #Dictionary anlegen
    char_list.sort() #Eingabe aufsteigend sortieren
    for i in char_list: # Über Eingabeliste iterienen
        if i in frequency_table: #Wenn es den Eintrag in dem Dictionry schon gibt
            frequency_table[i] += 1 #++
        else:
            frequency_table[i] = 1 # Eintrag anlegen


compute_frequencyTable([4, 8, 13, 11, 0, 13, 6, 4, 17, 19, 4, 23, 19, 14, 7, 13, 4, 18,8, 13, 13])


def computeMostFrequentChars(freq):
