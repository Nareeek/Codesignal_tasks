def maxFraction(n,d):
    return max(range(len(n)), key=lambda x:n[x]/d[x])