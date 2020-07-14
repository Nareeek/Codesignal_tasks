# 1
def concatSumStrings(a):
    s = 0
    for i in range(len(a)):
        for j in range(len(a)):
            x = str(a[i]) + str(a[j])
            s += int(x)
    return s


# 2
def concatSumStrings(a):
    s = 0
    for i in a:
        for j in a:
            s += int(str(i) + str(j))
    return s


# 3
def concatSumStrings(a):
    import numpy as np
    a = [str(w) for w in a]
    x = np.array(a)
    y = np.array(a).reshape(len(a), 1)
    xy = np.core.defchararray.add(x, y)
    return np.sum(np.array(xy, dtype=int))

# test time
# a = np.arange(1050) # 1050 < 10^9 !!!
# t = time.time()
# concatSumStrings(a)
# print('sec >> ', time.time()-t)

# sec >> 3.9193031787872314
