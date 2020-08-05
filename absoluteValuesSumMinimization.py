def absoluteValuesSumMinimization(a):
    d = {}
    sum = 0
    m = 0
    for i in range(len(a)):
        for j in range(len(a)):
            sum += abs(a[j] - a[i])
        d[a[i]] = sum
        sum = 0
    for i in d:
        m = min(i, m)
    return d, m


print(absoluteValuesSumMinimization([2, 4, 7]))


# 2
def absoluteValuesSumMinimization(a):

    indexOfMinimum = -1
    minimalSum = float('inf')

    for i in range(len(a)):
        curSum = 0
        for j in range(len(a)):
            curSum += abs(a[j] - a[i])
        if curSum < minimalSum:
            minimalSum = curSum
            indexOfMinimum = i

    return a[indexOfMinimum]