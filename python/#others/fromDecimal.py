def fromDecimal(b, n):
    s = ""
    while n // b:
        s += str(n % b)
        n //= b
    s += str(n)
    return s[::-1]