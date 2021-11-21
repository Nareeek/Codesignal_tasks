def equilibriumPoint(a):
    x, y = 0, sum(a)
    
    for i, v in enumerate(a):
        y -= v
        
        if x == y:
            return i + 1
            
        x += v
        
    return -1

print(equilibriumPoint([10, 5, 3, 5, 2, 2, 6, 8]))