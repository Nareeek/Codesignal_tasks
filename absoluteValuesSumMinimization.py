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