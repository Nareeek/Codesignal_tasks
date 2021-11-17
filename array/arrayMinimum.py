def arrayMinimum(inputArray):

    indexOfMinimum = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] < inputArray[indexOfMinimum]:
            indexOfMinimum = i
    return inputArray[indexOfMinimum]
