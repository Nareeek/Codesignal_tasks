def giftSafety(g):
    c = 0
    for i in range(len(g) - 2):
        c += len(set(g[i:i+3])) < 3
    return c