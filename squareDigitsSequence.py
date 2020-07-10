def squareDigitsSequence(a0):
    d = []
    s = 0

    while 1:
        for i in str(a0):
            s += int(i) ** 2

        if s in d:
            return len(d) + 1
        d.append(s)
        a0 = s
        s = 0


print(squareDigitsSequence(103))
