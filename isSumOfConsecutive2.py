def isSumOfConsecutive2(n):
    s = c = 0
    i = tmp = 2

    while n // i - i // 2 > 0:
        k = n // i

        if i % 2:
            s = k - (i // 2)

        for j in range(i // 2, -(i // 2), -1):
            s += k + j

        if s == n:
            c += 1

        tmp += 1
        i = tmp
        s = 0

    return c


print(isSumOfConsecutive2(99))
