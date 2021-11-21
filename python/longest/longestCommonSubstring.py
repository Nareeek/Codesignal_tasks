# 1
def longestCommonSubstring(s, t):
    if len(t) > len(s):
        t, s = s, t
        
    l = len(t)
    if t in s:
        return l
        
    if t[:-1] in s:
        return l - 1
        
    m = 0
    for i in range(min(l, 10000)):
        while (t[i: i + m + 1] in s) and ((i + m) < l):
            m += 1
            
    return m


# 2
s, t = eval(dir()[0])
if len(t) > len(s):
    t,s = s,t
l = len(t)
if t in s:
    return l
if t[:-1] in s:
    return l-1  
m = 0
for i in range(min(l, 10000)):
    while t[i:i+m+1] in s and i+m<l:
        m+=1
return m