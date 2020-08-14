def dotProduct(v1, v2):
    s = 0
    for i, j in zip(v1, v2):
        s += i * j
    return s