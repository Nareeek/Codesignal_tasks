def onlyEvenNumbers(left, right):
    result = []
    for i in range(left, right + 1):
        if i % 2 == 0:
            result.append(i)
    return result