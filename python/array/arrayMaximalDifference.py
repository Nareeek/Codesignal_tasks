def arrayMaximalDifference(inputArray):
    dif = 0
    for x in inputArray:
        for y in inputArray:
            dif = max(dif, (x - y))
    return dif

