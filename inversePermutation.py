def inversePermutation(permutation):
    p = permutation
    x = [0 for x in range(len(p))]
    
    for i in range(len(p)):
        x[p[i] - 1] = i + 1
    
    return x