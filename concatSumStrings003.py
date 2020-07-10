def concatSumStrings(a):
    s = 0
    for i in range(len(a)):
        for j in range(len(a)):
            x = str(a[i]) + str(a[j])
            s += int(x)
    return s
