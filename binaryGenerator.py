# 1
def binaryGenerator(s):
    new = []
    old = []
    if s[0] == '1':
        old = ['1']
    else:
        old = ['0', '1']
    s=s[1::]
    
    for i in range(0,len(s)):
        new = []
        if s[0] == '1':
            for i in range(len(old)):
                new.append(old.pop(0) + '1')
        else:
            for i in range(len(old)):
                thisVal = old.pop(0)
                new.append(thisVal + '1')
                new.append(thisVal + '0')
        s=s[1::]
        old = [x for x in new]
        
    return sorted(old) 

# 2
def binaryGenerator(s):
    def go(s, ans, st, i):
        if (i >= len(s)):
            ans += [st]
            return
        assert(i < len(s))
        if s[i] == '1':
            go(s, ans, st + '1', i + 1)
            return
        go(s, ans, st + '0', i + 1)
        go(s, ans, st + '1', i + 1)
    ans = []
    go(s, ans, "", 0)
    return ans

# 3
from itertools import combinations

def binaryGenerator(s):
    pos = set()
    opt = []
    
    for i in range(len(s)):
        if s[i] == '0':
            pos.add(i)
        
    for i in range(len(s) + 1):
        for comb in combinations(pos, i):
            init = list(s)
            
            for p in comb:
                init[p] = '1'
                
            opt.append(''.join(init))

    return sorted(opt)

# 4
def binaryGenerator(s, i=0):
    i = s.find("0", i)
    return [s] if i == -1 else binaryGenerator(s, i+1)+binaryGenerator(s[:i]+"1"+s[i+1:], i+1)



print(binaryGenerator("01101"))