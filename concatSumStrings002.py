def concatSumStrings(a):
    s = 0
    for i in a:
        for j in a:
            s += int(str(i) + str(j))
    return s
