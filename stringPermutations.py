import itertools

def stringPermutations(s):
    data = []
    for i in itertools.permutations(s):
        data.append("".join(list(i)))
    return sorted(list(set(data)))


#2
def stringPermutations(s):
    if len(s) < 2:
        return [s]
    else:
        P = []
        for i in range(len(s)):
            for p in stringPermutations(s[:i] + s[i+1:]):
                P.append(s[i] + p)
        return sorted(set(P))