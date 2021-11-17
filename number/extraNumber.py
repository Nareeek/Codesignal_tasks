def extraNumber(a, b, c):
    return a ^ b ^ c

# 2
def extraNumber(a, b, c):
    ret = [a, b, c]
    ret.sort()
    return (a + b + c - 2 * ret[1])

# 3
def extraNumber(a, b, c):
    if a == b:
        return c
    if b == c:
        return a
    return b