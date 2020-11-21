def leastSignificantBit(n):

    ans = 1
    while ((n & 1) == 0):
        n >>= 1
        ans <<= 1

    return ans
