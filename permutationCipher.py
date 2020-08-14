import string


def permutationCipher(password, key):
    table = str.maketrans(string.ascii_lowercase, key)
    return password.translate(table)


print(permutationCipher("iamthebest", "zabcdefghijklmnopqrstuvwxy"))



# 2
def permutationCipher(password, key):
    d = {}
    i = 97 
    for x in key:
        d[chr(i)] = x
        i += 1
    
    return "".join(d[x] for x in password)
