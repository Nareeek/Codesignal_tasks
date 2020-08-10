def caesarBoxCipherEncoding(inputString):

    n = int(math.sqrt(len(inputString)))
    ans = ''
    for i in range(n):
        for j in range(n):
            ans += inputString[j * n + i]

    return ans