# 1
def arrayMaxConsecutiveSum(inputArray, k):
    crnt_sum = max_sum = sum(inputArray[:k])
    for i in range(len(inputArray) - k):
        crnt_sum = crnt_sum + inputArray[i + k] - inputArray[i]
        max_sum = max(crnt_sum, max_sum)
    return max_sum



# 2
def arrayMaxConsecutiveSum(inputArray, k):
    maxS = s = sum(inputArray[:k])
    
    for i in range(0, len(inputArray) - k):
        s += inputArray[i + k] - inputArray[i]
        maxS = max(maxS, s)

    return maxS