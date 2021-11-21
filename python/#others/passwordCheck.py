def passwordCheck(inputString):
    c = s = d = 0
    l = (len(inputString) >= 5)
    
    for x in inputString:
        if x.isupper():
            c += 1
        if x.islower():
            s += 1
        if x.isdigit():
            d += 1
            
    return bool(l and c and s and d)
            
    