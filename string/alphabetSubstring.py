# 1
def alphabetSubstring(s):
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            return False
        if ord(s[i]) != ord(s[i - 1]) + 1:
            return False
        
    return True


# 2
def alphabetSubstring(s):
    v = 'abcdefghijklmnopqrstuvwxyz'
    return s in v

