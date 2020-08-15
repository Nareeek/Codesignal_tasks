def allLongestStrings(inputArray):
    l = len(max(inputArray, key=len))
    L = []
    for i in inputArray:
        if len(i) == l:
            L.append(i)
    return L



# 2
def allLongestStrings(inputArray):

    answer = [inputArray[0]]
    for i in range(1, len(inputArray)):
        if len(inputArray[i]) == len(answer[0]):
            answer.append(inputArray[i])
        if len(inputArray[i]) > len(answer[0]):
            answer = [inputArray[i]]
    return answer
