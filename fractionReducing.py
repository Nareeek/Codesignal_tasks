def fractionReducing(fraction):
    n, d = fraction
    m = math.gcd(n, d)
    return n // m, d // m