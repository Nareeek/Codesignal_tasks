# 1
def arrayPreviousLess(items):

    result = []
    for i in range(len(items)):
        substitute = -1
        for j in range(i, -1, -1):
            if items[j] < items[i]:
                substitute = items[j];break
        result.append(substitute)

    return result


# 2
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