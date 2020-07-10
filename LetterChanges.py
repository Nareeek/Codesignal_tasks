def LetterChanges(str):
    a = []
    for i in range(len(str)):
        if str[i].isalpha() and str[i] != "z":
            a.append(chr(ord(str[i]) + 1))
        else:
            a.append(str[i])
    for i in range(len(a)):
        if a[i] in "a,e,i,o,u":
            a[i] = a[i].upper()
    a = "".join(a)
    return a


# keep this function call here
print(LetterChanges("hello*3"))
