# 1
def maxPairProduct(a):
    l = list(set(a))
    l.sort()
    lr = reversed(l)
    a_tri = sorted(a)
    for mpp in lr:
        s = math.sqrt(mpp)+1
        for div in [e for e in l if e<s]:
            if mpp%div == 0:
                if mpp/div in a_tri[a_tri.index(div)+1:]:
                    return mpp
    return -1


# 2 106/107 -> 99%

from collections import Counter

def maxPairProduct(a):
    m = Counter(a) # dict ( value : freq )
    a.sort()
    for i in reversed(a):
        for j in a:
            if (j > i) or (j > math.sqrt(i)):
                 break
            elif i % j == 0:
                r = i / j
                if r != j and m[r] > 0:
                    return i
                elif r == j and m[r] > 1:
                    return i
    return -1