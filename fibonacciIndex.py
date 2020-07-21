def fibonacciIndex(n):
    i = 0
    a, b = 0, 1
    while len(str(a)) < n:
        a,b = b, a + b
        i += 1
    return i