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
