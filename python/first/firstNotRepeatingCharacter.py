# 1
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

# 2
def firstNotRepeatingCharacter(a):
    L = {}
    for i in range(97, 123):
        if a.count(chr(i)) == 1:
            L[a.index(chr(i))] = chr(i)
    return "_" if len(L) == 0 else L[min(L)]


print(firstNotRepeatingCharacter("abddfgtgadesdgvb"))
