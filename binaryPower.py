def binaryPower(n, k):
    MOD = 10 ** 7 + 7

    if k == 0:
        return 1
    if k % 2 == 0:
        return binaryPower((n * n) % MOD, k / 2)
    return n * binaryPower((n * n), (k - 1) / 2) % MOD