def firstNotRepeatingCharacter(a):
    L = {}
    for i in range(97, 123):
        if a.count(chr(i)) == 1:
            L[a.index(chr(i))] = chr(i)
    return "_" if len(L) == 0 else L[min(L)]


print(firstNotRepeatingCharacter("abddfgtgadesdgvb"))
