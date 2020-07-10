from itertools import permutations as p


def dif(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1


def stringsRearrangement(inp):
    for z in p(inp):
        if sum([dif(x[0], x[1]) for x in zip(z[:], z[1:])]) == len(inp) - 1:
            return True
    return False


print(stringsRearrangement(["abc",
                            "abx",
                            "axx",
                            "abc"]))
