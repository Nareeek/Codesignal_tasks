def calculationsWithCoins(a, b, c):
    s = set([a,b,c,a+b,a+c,b+c,a+b+c])
    return len(s)