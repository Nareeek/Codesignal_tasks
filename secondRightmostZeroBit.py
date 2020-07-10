def secondRightmostZeroBit(n):
    return (((n + 1) | n) - n)


print(secondRightmostZeroBit(39))

print()
print("{0:08b}".format(39))
print("+       1")
print("{0:08b}".format(40))
print("|")
print("{0:08b}".format(39 | 40))
print("--")
print("{0:08b}".format((39 | 40) - 39))
