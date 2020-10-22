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


def acEncrypt(a, b, plain_test):
    y = []
    decoded_list = decode(plain_test)
    for i in decoded_list:
        y.append((a * i + b) % 26)
    secret = encode(y)
    print(secret.upper())
    return secret.upper()

def acEncrypt(a, b, plain_test):
    y = []
    decoded_list = decode(plain_test)
    for i in decoded_list:
        y.append((a * i + b) % 26)
    secret = encode(y)

    return secret.lower()

def acDecrypt(a, b, plain_test):
    y = []
    decoded_list = decode(plain_test)
    for i in decoded_list:
        y.append(((i - b) * key_table[a]) % 26)
    secret = encode(y)
    #print(secret.upper())
    return secret.lower()


