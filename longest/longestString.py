def longestString(inputArray):

    answer = inputArray[0]
    for i in range(1, len(inputArray)):
        if len(inputArray[i]) > len(answer):
            answer = inputArray[i]
    return answer
