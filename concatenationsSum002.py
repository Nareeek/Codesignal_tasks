from itertools import product


def concatenationsSum(a):
    a = list(product(a, repeat = 2))
    #print(a)
    b = ["".join(list(map(str, i))) for i in a]
    #print(b)
    c = sum(list(map(int, b)))
    print(c)
    