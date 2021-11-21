def divisorsSubset(subset, n):
    def d(s, n):
        for i in range(len(s)):
            if (n % s[i] != 0):
                return False
        return True
        
    c = 0
    for i in range(1, n + 1):
        if d(subset,i):
            c += 1
    return c