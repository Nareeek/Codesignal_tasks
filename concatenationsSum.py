from itertools import product as pr


def concatenationsSum(a):
    su = 0

    b = list(pr(a, repeat=2))

    for i in b:
        su += int(str(i[0]) + str(i[1]))
    return su


print(concatenationsSum([1000000, 1000000, 1000000, 1000000]))
