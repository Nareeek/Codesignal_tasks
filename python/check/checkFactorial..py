def checkFactorial(n):
    f = 1
    i = 1
    while f < n:
        i += 1
        f *= i
    return f == n