def permutationShift(permutation):
    minShift = 0
    maxShift = 0
    for i in range(len(permutation)):
        if permutation[i] - i > maxShift:
            maxShift = permutation[i] - i
        if permutation[i] - i < minShift:
            minShift = permutation[i] - i
    return maxShift - minShift
