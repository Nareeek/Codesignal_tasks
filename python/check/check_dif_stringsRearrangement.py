from itertools import permutations as all_possible_ways


def check_dif(tup):
    q = 0
    dif = 0
    for i in range(len(tup) - 1):
        for j in range(len(tup[i])):
            if tup[i][j] != tup[i + 1][j]:
                dif += 1
            if dif > 1:
                return False
        q += dif
        dif = 0
    if q > len(tup) - 1:
        return False
    return q


def stringsRearrangement(inp):
    l = []
    for i in all_possible_ways(inp):
        l.append(check_dif(i))
    return len(inp) - 1 in l


print(stringsRearrangement(["abc",
                            "abx",
                            "axx",
                            "abc"]))
