# 1
def largestNumber(n):

    res = 0

    for i in range(n):
        res = res * 10 + 9

    return res

# 2
def largestNumber(n):
    return int('1' + '0'*n) - 1


