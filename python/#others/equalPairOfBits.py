# 1
def equalPairOfBits(n, m):
    return ~(n ^ m) & -~(n ^ m)



# 2
def equalPairOfBits(n, m):
    b = 1
    while (n & b) != (m & b):
        b <<= 1
    return b
