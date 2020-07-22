def isSumOfConsecutive2(n):
    ctr = 0
    
    for i in range(1, n):
        s = 0
        for j in range(i, n):
            s += j
            if s > n:
                break
                
            if s == n:
                ctr += 1
    return ctr