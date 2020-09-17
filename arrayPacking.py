# 1
def arrayPacking(a):

    res = 0
    for i in range(len(a)):
        res |= a[i] << (i * 8)

    return res

# 2
def arrayPacking(a):
    return int.from_bytes(a, 'little')


print(arrayPacking([24, 85, 0]))

