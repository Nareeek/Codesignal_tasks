def rounders(n):
    N = str(n)[::-1][:-1]
    
    up = 0
    s = ""
       
    for i in N:
        if int(i) + up < 5:
            up = 0
        else:
            up = 1
        
        s += "0"
    
    if up:
        s += str( int( str(n)[0]) + 1 )
        
            
    return int(s[::-1])

print(rounders(14445))