# 1
def extractEachKth(inputArray, k):
    o = []
    i = 1
    for n in inputArray:
        if i % k:
            o += n,
        i += 1
    return o


# 2
def extractEachKth(inputArray, k):
    nar = list(inputArray)
    for i in range(1, len(nar) // k + 1):
        inputArray.remove(nar[k * i - 1])
    return inputArray

# 3
def extractEachKth(inputArray, k):
    del inputArray[k - 1::k]
    return inputArray


# 4
def extractEachKth(inputArray, k):

    result = []
    for i in range(len(inputArray)):
        if (i + 1) % k != 0:
            result.append(inputArray[i])
    return result


print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))



