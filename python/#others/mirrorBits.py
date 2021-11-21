# 1
def mirrorBits(a):

    b = 0
    while a > 0:
        b <<= 1
        b |= a % 2
        a >>= 1

    return b

# 2
def mirrorBits(a):
    binary = bin(a)[2:]
    return int(binary[::-1], 2)