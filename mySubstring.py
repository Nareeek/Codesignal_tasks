def mySubstring(inputString, l, r):

    result = []
    for i in range(l, r+1):
        result.append(inputString[i])
    return ''.join(result)