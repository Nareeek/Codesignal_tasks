# 1
def nextSecond(currentTime):
    x,y,z = currentTime[0],currentTime[1],currentTime[2]
    z = (z+1)%60
    if z == 0:
        y=(y+1)%60
    else:
        y = y
    if y == 0:
        x = (x+1)%24
    else:
        x = x
    return [x,y,z]


# 2
def nextSecond(currentTime):
    h, m, s = currentTime
    s += 1
    if s == 60:
        s = 0
        m += 1
    
    if m == 60:
        m = 0
        h += 1
        
    if h == 24:
        h = 0
        
    return h, m, s