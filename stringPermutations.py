from itertools import permutations as per


def stringPermutations(s):
    s = list(s)
    s.sort()
    s = per(s)
    s = set(s)
    s = list(s)
    s.sort()
    S = []
    for i in range(len(s)):
        S.append("".join(s[i]))
    return S


print(stringPermutations("ABA"))
