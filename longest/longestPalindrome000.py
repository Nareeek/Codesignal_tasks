def longestPalindrome(s):
    if not s:
        return ""
    
    start = 0
    end = 0
    
    for i in range(len(s)):
        len1 = expandFromMiddle(s, i, i)
        len2 = expandFromMiddle(s, i, i + 1)
        
        lenn = max(len1, len2)
        
        if lenn > (end - start):
            start = i - ((lenn - 1) // 2)
            end = i + (lenn // 2)
    return s[start: end + 1]

def expandFromMiddle(s, left, right):
    if (not s) or left > right:
        return 0
    
    while (left >= 0 and right < len(s) and s[left] == s[right]):
        left -= 1
        right += 1
    
    return right - left - 1


print(longestPalindrome("babad"))
