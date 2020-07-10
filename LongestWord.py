def LongestWord(sen):
    a = sen.split()
    Nar = []
    nar = []
    i = 0
    j = 0
    while i < len(a):
        while i < len(a[j]):
            if a[j][i].isalpha():
                Nar.append(a[j][i])
                i += 1
            else:
                i += 1
        if j + 1 != len(a):
            j += 1
            nar.append("".join(Nar))
            Nar = []
            i = 0
        else:
            nar.append("".join(Nar))
            break
    h = ""
    i = 0
    while i < len(nar) - 1:
        if len(nar[i]) > len(nar[i + 1]):
            h = nar[i]
            i += 1
        elif len(nar[i]) < len(nar[i + 1]):
            h = nar[i + 1]
            i += 1
        else:
            h = max(nar[i], h)
            i += 1
    return h


# keep this function call here
print(LongestWord("hello world"))
