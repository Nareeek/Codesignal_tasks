# 1
def maxFraction(numerators, denominators):

    maxFractionIndex = 0
    for i in range(1, len(numerators)):
        if (numerators[i] * denominators[maxFractionIndex] >
                numerators[maxFractionIndex] * denominators[i]):
            maxFractionIndex = i
    return maxFractionIndex


# 2
def maxFraction(n,d):
    return max(range(len(n)), key=lambda x:n[x]/d[x])