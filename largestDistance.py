def largestDistance(a):
    Max = 0
    
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                Max = max(Max, abs(a[i] - a[j]))
    return Max


print(largestDistance([0, 1, 1, 2]))