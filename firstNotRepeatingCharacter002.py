def firstNotRepeatingCharacter(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for x in d:
        if d[x] == 1:
            return x
    return "_"