#1
def maxSubarray(inputArray):
    t = 0
    res = 0
    for i in inputArray:
        if t+i>=0:
            t+=i
        else:
            t=0
        res = max(res, t)
    return res

# 2
def maxSubarray(a):
    m = max(a)
    for i in range(2,len(a)):
        for j in range(len(a)-i):
            m = max(m,sum(a[j:j+i]))
    return max(m,0)

# 3
def maxSubarray(inputArray):
    max_summa = -math.inf
    for k in range(1, len(inputArray) + 1):
        start = 0
        end = k - 1
        while end <= len(inputArray) - 1:
            if start == 0:
                summa = sum(inputArray[start:end + 1])
            else:
                summa = summa - inputArray[start - 1] + inputArray[end]
            if summa > max_summa:
                max_summa = summa
            start += 1
            end += 1
    return max_summa if max_summa >= 0 else 0