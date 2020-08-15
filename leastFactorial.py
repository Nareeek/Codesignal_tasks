def leastFactorial(n):
    p = 1
    k = 1
    while p < n:
        k += 1
        p *= k
    return p

# 2
def leastFactorial(n):
    t = 1
    i = 2
    while t < n:
        t *= i
        i += 1
    return t