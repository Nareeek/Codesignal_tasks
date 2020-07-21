def arithmeticExpression(a, b, c):
    r = False
    r |= a + b == c
    r |= a - b == c
    r |= a * b == c
    r |= a / b == c
    return r


def arithmeticExpression(a, b, c):
    return c in [a-b, a+b, a/b, a*b]`