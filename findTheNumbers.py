# 1
def findTheNumbers(a):
    import collections
    c = collections.Counter(a)
    res = []
    for i,j in c.items():
        if j == 1:
            res.append(i)
    return sorted(res)


# 2
def findTheNumbers(a):
    s = set()
    for n in a:
        s ^= {n}
    return sorted(s)
