def sortByString(s, t):
    res = ""
    for x in t:
        if x in s:
            res += s.count(x) * x
    
    return res