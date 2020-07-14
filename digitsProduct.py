# 1
def prod_dig(digit):
    pr = 1
    for i in str(digit):
        pr *= int(i)
    return pr


def digitsProduct(p):
    if p == 0:
        return 10

    for i in range(200):
        for j in range(200):
            if prod_dig(i * j) == p:
                return i * j, i, j
    return -1


print(digitsProduct(450))


# 2
def digitsProduct(product):
    answerDigits = []
    answer = 0

    if product == 0:
        return 10

    if product == 1:
        return 1

    for divisor in range(9, 1, -1):
        while product % divisor == 0:
            product /= divisor
            answerDigits.append(divisor)

    if product > 1:
        return answer - 1

    for i in range(len(answerDigits) - 1, -1, -1):
        answer = 10 * answer + answerDigits[i]
    return answer


print(digitsProduct(243))  # 12 - 26  #450-2559  243-399
