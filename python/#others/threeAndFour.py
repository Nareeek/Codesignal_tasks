# 1
def threeAndFour(n):
    result = [0]
    for counter in range(1, n):
        if counter % 3 == 0 and counter % 4 == 0:
            result.append(counter)
    return result


# 2
def threeAndFour(n):
    L = []
    i = 0
    while i < n:
        if i % 3 == 0 and i % 4 == 0:
            L.append(i)
        i += 1
    return L
