def factorialsProductTrailingZeros(l, r):
    two = 0
    five = 0
    ctr = 0
    
    for i in range(l, r + 1):
        for j in range(1, i + 1):
            if j % 25 == 0:
                ctr += 1
            if j % 2 == 0:
                two += 1
            if j % 5 == 0:
                five += 1
    ctr += min(two, five)
    
    return ctr
