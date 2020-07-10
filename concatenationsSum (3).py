from itertools import product


def concatenationsSum(a):
    return sum(list(map(int, ["".join(list(map(str, i))) for i in list(product(a, repeat=2))])))
