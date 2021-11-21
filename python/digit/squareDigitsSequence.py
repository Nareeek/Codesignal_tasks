# 1
def squareDigitsSequence(a0):

    cur = a0
    was = set()

    while not (cur in was):
        was.add(cur)
        nxt = 0
        while cur > 0:
            nxt += (cur % 10) * (cur % 10)
            cur //= 10
        cur = nxt

    return len(was) + 1


print(squareDigitsSequence(103))


# 2 ?
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
