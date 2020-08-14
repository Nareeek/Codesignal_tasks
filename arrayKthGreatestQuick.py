def arrayKthGreatestQuick(inputArray, k):

    pos = random.randint(0, len(inputArray) - 1)
    left = []
    right = []

    if len(inputArray) == 1:
        return inputArray[0]

    for i in range(len(inputArray)):
        if inputArray[i] <= inputArray[pos]:
            left.append(inputArray[i])
        else:
            right.append(inputArray[i])

    return sorted(left + right)[::-1][k-1]