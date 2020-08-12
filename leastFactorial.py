def leastFactorial(n):
    p = 1
    k = 1
    while p < n:
        k += 1
        p *= k
    return p