def sumOfCoprimes(m):

    ans = 0
    for p in range(2, m + 1):
        a = p
        b = m
        while a > 0:
            tmp = b % a
            b = a
            a = tmp

        if b == 1:
            ans += p

    return ans