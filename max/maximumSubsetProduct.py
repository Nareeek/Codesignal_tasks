def maximumSubsetProduct(a):
    count = 0
    min = -float('inf')
    
    for x in a:
        if x < 0:
            count += 1
            min = max(min, x)
    
    first = (count & 1) == 0 # even or odd
    second = (1 if len(a) < 2 else min)
    
    return int(first or second)
    