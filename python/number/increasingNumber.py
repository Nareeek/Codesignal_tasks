def increasingNumber(x, n):
    for i in range(1, n + 1):
        if x % i != 0:
            x = (x // i + 1) * i
    return x