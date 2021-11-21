# 1
def secondRightmostZeroBit(n):
    return (((n + 1) | n) - n)


# 2
def secondRightmostZeroBit(n):
    return 2 ** (len(bin(n)[2:]) - 1 - bin(n)[2:][:bin(n)[2:].rfind("0")].rfind("0"))


print(secondRightmostZeroBit(39))
print(secondRightmostZeroBit(83748))
print()
print("{0:08b}".format(39))
print("+       1")
print("{0:08b}".format(40))
print("|")
print("{0:08b}".format(39 | 40))
print("--")
print("{0:08b}".format((39 | 40) - 39))
