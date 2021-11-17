def arrayMode(sequence):
    L = [(sequence.count(i), i) for i in set(sequence)]

    return max(L)[1]

'''
from collections import Counter
def arrayMode(s):
    a = Counter(s)
    n = 0
    c = 0
    for k in a:
        if a[k] > c:
            c = a[k]
            n = k
    return n
'''