def swapArrayHalves(inputArray):

    for i in range(len(inputArray) // 2):
        tmp = inputArray[i]
        inputArray[i] = inputArray[i + len(inputArray) // 2]
        inputArray[i + len(inputArray) // 2] = tmp
    return inputArray
