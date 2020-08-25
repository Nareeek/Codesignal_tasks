def largestDistance(a):

    mx = [a[0], a[1]]
    mn = [a[1], a[0]]
    for i in range(len(a)):
        k = i % 2
        if a[i] > mx[k]:
            mx[k] = a[i]
        elif a[i] < mn[k]:
            mn[k] = a[i]
    return max(mx[0] - mn[0], mx[1] - mn[1])

print(largestDistance([0, 1, 1, 2]))
