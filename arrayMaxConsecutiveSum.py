def arrayMaxConsecutiveSum(inputArray, k):
    crnt_sum = max_sum = sum(inputArray[:k])
    for i in range(len(inputArray) - k):
        crnt_sum = crnt_sum + inputArray[i + k] - inputArray[i]
        max_sum = max(crnt_sum, max_sum)
    return max_sum