def rightmostRoundNumber(inputArray):
    maxroundpos = -1
    for i in range(len(inputArray)):
        if inputArray[i] % 10 == 0:
            maxroundpos = i
    return maxroundpos