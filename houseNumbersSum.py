def houseNumbersSum(inputArray):

    numberSum = 0
    i = 0
    while True:
        x = inputArray[i]
        i += 1
        numberSum += x
        if x == 0:
            break
    return numberSum