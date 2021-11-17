# 1
def arrayMaximalAdjacentDifference(a):
    return max([abs(a-b) for a, b in zip(a[1:],a[:-1])])



# 2
def arrayMaximalAdjacentDifference(inputArray):
    r = abs(inputArray[1] - inputArray[0])
    for i in range(2, len(inputArray)): r = max(r, abs(inputArray[i] - inputArray[i-1]))
    return r