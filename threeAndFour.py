def threeAndFour(n):
    L = []
    i = 0
    while i < n:
        if i % 3 == 0 and i % 4 == 0:
            L.append(i)
        i += 1
    return L
