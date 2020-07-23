def differentDigitsNumberSearch(inputArray):
    for a in inputArray:
        n = str(a)
        if len(set(n)) == len(n):
            return a
    return -1