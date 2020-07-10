def modInverse(n, m):
    g, x, _ = euclid_algo(n, m)
    return x % m if g == 1 else -1

def euclid_algo(a, b):
    if a == 0:
        return (b, 0, 1)
    g, x, y = euclid_algo(b % a, a)
    return (g, y - b // a * x, x)

print(modInverse(9831, 27871198))