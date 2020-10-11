def arrayMinimumAboveBound(inputArray, bound):

    best = -1
    for i in range(len(inputArray)):
        if (inputArray[i] > bound and
                (best == -1 or inputArray[i] < best)):
            best = inputArray[i]

    return best
