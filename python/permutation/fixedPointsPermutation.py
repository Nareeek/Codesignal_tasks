def fixedPointsPermutation(permutation):
    s = sorted(permutation)
    co = 0
    for i in range(len(permutation)):
        if permutation[i] == s[i]:
            co += 1
    return co