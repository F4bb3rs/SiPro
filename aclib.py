def decode(text):
    list = []
    for i in text:
        if i.isalpha():
            list.append(ord(i.lower()) - 97)
    return list


def encode(list):
    string = ""
    for i in list:
        string += chr(i + 97)
    return string


key_table = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}

def checkKey(a,b):
    if abs(b) > 27:
        print("b out of range" + str(b))
        return False
    if not a in key_table:
        print("a not in key_table")
        return False
    return True

def acEncrypt(a, b, plain_text):
    if not checkKey(a, b):
        return ""
    secret = []
    decoded_list = decode(plain_text)
    for i in decoded_list:
        secret.append((a * i + b) % 26)
    secret = encode(secret)

    return secret.upper()


def acDecrypt(a, b, cipher):
    if not checkKey(a, b):
        return ""
    secret = []
    decoded_list = decode(cipher)
    for i in decoded_list:
        secret.append(((i - b) * key_table[a]) % 26)
    secret = encode(secret)
    return secret.lower()





#cipher= "MVLCDIUEGCXHDEKWSXMLUMEILCJWCVWKXVRCXPSEMVKEEKEGCXHDGMDKGMLFCSLIEKWSXKWCOJSLKXEUELKOUCSDCVLOIAKOCVKUUCSDCVLKNJIVDIVDPCLLCOHMVKUCSDCVLESXZMZKWXUJLCYXIJFUFCHDEYXKILJXCOMEKIELFKLKWFVCHCYULCJXCZMDKEKWSXMLUMVWUPKXEJIWKIOIBMVYHUKVCSYFVCHMLKXILSXKKNMELEIPCSLFCGLCMOJHKOKVLWXUJLCYXIJFUIVDFCGLCMVWCXJCXILKMLMVLCXKIHGCXHDEUELKOE"
#char_list = aclib.decode(cipher)
#freqTable = compute_frequencyTable(char_list)
#mostFrequent = computeMostFrequentChars(freqTable, 10)
#keyPairs = computeKeyPairs(mostFrequent)
#analyzeCipherText(cipher, keyPairs)

