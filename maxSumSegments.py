# 1
def maxSumSegments(inputArray):
    result = [0 for i in range(len(inputArray))]
    
    for i in range(1, len(inputArray) + 1):
        summ = 0
        mxSum = 0
        index = -1
        
        for j in range(len(inputArray)):
            summ += inputArray[j]
            if j >= i:
                summ -= inputArray[j - i]
            if j >= i - 1 and (index == -1 or summ > mxSum):
                mxSum = summ
                index = j - i + 1
        result[i - 1] = index    

    return result

# 2
def maxSumSegments(inputArray):

    result = []
    for i in range(1, len(inputArray) + 1):
        sum = 0
        mxSum = 0
        index = -1
        for j in range(len(inputArray)):
            sum += inputArray[j]
            if j >= i:
                sum -= inputArray[j - i]
            if j >= i - 1 and (index == -1 or sum > mxSum):
                mxSum = sum
                index = j - i + 1
        result.append(index)
    return result
