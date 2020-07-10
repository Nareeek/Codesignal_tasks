def concatenationsSum(a):
    p = []
    for i in range(len(a)):
        for j in range(len(a)):
            p.append(str(a[i]) + str(a[j]))
            
    summ = 0
    for i in range(len(p)):
        summ += int(p[i])
        
    return p, summ
            
            
print(concatenationsSum([10, 2]))