def extractEachKth(inputArray, k):
    o = []
    i = 1
    for a in inputArray:
        if i % k:
            o += a,
        i += 1
    return o