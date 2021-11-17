def comfortableNumbers(l, r):
    c = 0
    for a in range(l,r+1):
        for b in range(a,r+1):
            aS, bS = sum(map(int,str(a))), sum(map(int,str(b)))
            if a != b and b in range(a-aS,a+aS+1) and a in range(b-bS,b+bS+1): c += 1
    return c


'''
import itertools


def comfortableNumbers(L, R):
    def is_comfortable(a,b):
        s = sum(int(d) for d in str(a))
        return a - s <= b <= a + s
    
    cnt = 0
    for a, b in itertools.combinations(range(L, R + 1), 2):
            if is_comfortable(a, b) and is_comfortable(b, a):
                cnt += 1
                
    return cnt
'''