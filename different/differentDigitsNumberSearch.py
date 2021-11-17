# 1
def differentDigitsNumberSearch(inputArray):

    for i in range(len(inputArray)):
        cur = inputArray[i]
        was = [False] * 10
        ok = True
        while cur > 0:
            if was[cur % 10]:
                ok = False
                break
            was[cur % 10] = True
            cur //= 10
        if ok:
            return inputArray[i]

    return -1



# 2
def differentDigitsNumberSearch(inputArray):
    for a in inputArray:
        n = str(a)
        if len(set(n)) == len(n):
            return a
    return -1