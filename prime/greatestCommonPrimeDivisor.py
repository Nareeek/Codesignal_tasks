import math


def greatestCommonPrimeDivisor(a, b):
    a = math.gcd(a, b)

    i = 2
    while i < a:
        if a % i == 0:
            a //= i
        else:
            i += 1

    return a if a != 1 else -1


print(greatestCommonPrimeDivisor(12, 18))
