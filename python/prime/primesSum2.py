def primesSum2(n):
    a = numpy.ones(n + 2)
    s = 0
    for i in range(2, n + 1):
        if a[i]:
            s += i
            a[i::i] = 0
    return s