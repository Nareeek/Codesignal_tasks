def secondRightmostZeroBit(n):
    return 2 ** (len(bin(n)[2:]) - 1 - bin(n)[2:][:bin(n)[2:].rfind("0")].rfind("0"))


print(secondRightmostZeroBit(83748))
