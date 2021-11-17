def pairsSum(a):
    s = set(a)
    t = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] in s:
                t += 1
    return t