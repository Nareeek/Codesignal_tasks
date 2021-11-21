# 1
def caesarBoxCipherEncoding(inputString):

    n = int(math.sqrt(len(inputString)))
    ans = ''
    for i in range(n):
        for j in range(n):
            ans += inputString[j * n + i]

    return ans


# 2
def caesarBoxCipherEncoding(inputString):

    n = int(len(inputString) ** 0.5)
    ans = ''
    for i in range(n):
        for j in range(n):
            ans += inputString[j * n + i]

    return ans
