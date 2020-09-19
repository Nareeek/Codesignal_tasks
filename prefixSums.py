def prefixSums(a):
    b = []
    summ = 0
    for x in a:
        summ += x
        b.append(summ)
    return b
