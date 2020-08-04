def allLongestStrings(inputArray):
    l = len(max(inputArray, key=len))
    L = []
    for i in inputArray:
        if len(i) == l:
            L.append(i)
    return L
