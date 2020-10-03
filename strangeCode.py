def strangeCode(s, e):
    prevSymb = '-'
    res = ""

    while s < e - 1:
        s += 1
        e -= 1
        if prevSymb == '-':
            prevSymb = 'a'
            res += str(prevSymb)
        else:
            prevSymb = ('b' if prevSymb == 'a' else 'a')
            res += str(prevSymb)

    return res