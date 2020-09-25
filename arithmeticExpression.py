# 1
def arithmeticExpression(a, b, c):
    r = False
    r |= a + b == c
    r |= a - b == c
    r |= a * b == c
    r |= a / b == c
    return r

# 2
def arithmeticExpression(a, b, c):
    return c in [a-b, a+b, a/b, a*b]


# 3
def arithmeticExpression(a, b, c):

    if a + b == c or a * b == c or b * c == a or a - b == c:
        return True
    return False


