# 1
def sortByHeight(a):
    for i in range(len(a)):
        minIndex = -1
        if a[i] == -1:
            continue
        for j in range(i, len(a)):
            if a[j] != -1:
                if minIndex == -1 or a[j] < a[minIndex]:
                    minIndex = j
        a[minIndex], a[i] = a[i], a[minIndex]
    return a



print([-1, 150, 190, 170, -1, -1, 160, 180])


# 2
def sortByHeight(a):
    for i in range(len(a)):
        minIndex = -1
        tmp = a[i]
        if a[i] == -1:
            continue
        for j in range(i, len(a)):
            if a[j] != -1:
                if minIndex == -1 or a[j] < a[minIndex]:
                    minIndex = j
        a[i] = a[minIndex]
        a[minIndex] = tmp
    return a
