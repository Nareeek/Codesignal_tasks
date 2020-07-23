def arrayPreviousLess(a):
    arr = []
    for i in range(len(a)):
        f = 0
        for j in range(i - 1, -1, -1):
            if a[j] < a[i]:
                f = 1
                arr.append(a[j])
                break
                
        if f == 0:
            arr.append(-1)
            
    return arr