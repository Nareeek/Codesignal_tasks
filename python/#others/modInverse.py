# 1
import math


def modInverse(n, m):
    if math.gcd(n, m) != 1:
        return -1
    x1, x2, y1, y2, _m = 1, 0, 0, 1, m
    while m:
        n, q, m = m, *divmod(n, m)
        x1, y1, x2, y2 = x2, y2, x1 - q * x2, y1 - q * y2
    return x1 if x1 > 0 else x1 + _m


print(modInverse(9831, 27871198))


# 2
def modInverse(n, m):
    g, x, _ = euclid_algo(n, m)
    return x % m if g == 1 else -1


def euclid_algo(a, b):
    if a == 0:
        return (b, 0, 1)
    g, x, y = euclid_algo(b % a, a)
    return (g, y - b // a * x, x)


print(modInverse(9831, 27871198))