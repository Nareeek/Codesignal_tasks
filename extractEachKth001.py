def extractEachKth(inputArray, k):
    o = []
    i = 1
    for n in inputArray:
        if i % k:
            o += n,
        i += 1
    return o
