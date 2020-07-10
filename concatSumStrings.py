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
