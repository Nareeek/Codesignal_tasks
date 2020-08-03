def f(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
def isOneSwapEnough(s):
    ok = False
    c = list(s)
    for i in range(len(c)):
        for j in range(i, len(c)):
            c[i], c[j] = c[j], c[i]
            if f(''.join(c)):
                ok = True
            c[i], c[j] = c[j], c[i]
    return ok