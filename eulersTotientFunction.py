# 1
def eulersTotientFunction(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)
        
        
def gcd(p,q):
    while q != 0:
        p, q = q, p % q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1


# 2
def eulersTotientFunction(n):
    divisor = 2
    result = n

    while divisor * divisor <= n:
        if n % divisor == 0:
            while n % divisor == 0:
                n /= divisor
            result -= result / divisor
        divisor += 1
    if n > 1:
        result -= result / n

    return result