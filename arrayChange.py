def arrayChange(inputArray):

    result = 0

    for i in range(1, len(inputArray)):
        if (inputArray[i] <= inputArray[i - 1]):
            result += inputArray[i - 1] - inputArray[i] + 1
            inputArray[i] = inputArray[i - 1] + 1
    return result