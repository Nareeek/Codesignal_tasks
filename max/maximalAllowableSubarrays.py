def maximalAllowableSubarrays(inputArray, maxSum):
    for i in range(len(inputArray)):
            summ = inputArray[i]
            for j in range(i + 1, len(inputArray)):
                summ += inputArray[j]
                if summ > maxSum:
                    inputArray[i] = j - 1
                    break
            if summ <= maxSum:
                inputArray[i] = len(inputArray) - 1

    return inputArray