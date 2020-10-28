def gcdNaive(a, b):

    gcd = 1
    for divisor in range(2, min(a, b) + 1):
        if a % divisor == 0 and b % divisor == 0:
            gcd = divisor

    return gcd


def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)


a = 26
b = 91

print(gcd(a, b))