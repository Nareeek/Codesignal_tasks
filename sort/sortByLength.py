def sortByLength(inputArray):
    initIndex = []
    for i in range(len(inputArray)):
        initIndex.append(i)
    for i in range(len(inputArray)):
        minIndex = i
        tmp = inputArray[i]
        for j in range(i + 1, len(inputArray)):
            if len(inputArray[j]) < len(inputArray[minIndex]) or len(inputArray[j]) == len(inputArray[minIndex]) and initIndex[j] < initIndex[minIndex]:
                minIndex = j
        inputArray[i] = inputArray[minIndex]
        inputArray[minIndex] = tmp
        tmp2 = initIndex[minIndex]
        initIndex[minIndex] = initIndex[i]
        initIndex[i] = tmp2

    return inputArray
