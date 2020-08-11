def isTandemRepeat(s):
    return s[:len(s) // 2] * 2 == s


#2
def isTandemRepeat(s):
    n = len(s)
    for i in range(n//2 + 1):
        if s[i:] == s[:i]:
            return True
    return False