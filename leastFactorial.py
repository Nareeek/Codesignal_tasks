def leastFactorial(n):
    f = 1
    i = 2

    while f < n:
        f *= i
        i += 1
        
    return f