def extractEachKth(inputArray, k):
    nar = list(inputArray)
    for i in range(1, len(nar) // k + 1):
        inputArray.remove(nar[k * i - 1])
    return inputArray


def extractEachKth(inputArray, k):
    del inputArray[k - 1::k]
    return inputArray


print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
