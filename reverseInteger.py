def reverseInteger(x):
    if x < 0:
        s = "-"
        ss = str(x)[1:]
    else:
        ss = str(x)
    
    if x < 0:
        sss = s + ss[::-1]
    else:
        sss = ss[::-1]
    
    return int(sss)
        
