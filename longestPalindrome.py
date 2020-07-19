def longestPalindrome(s: str) -> str:
    def is_polindrom(string):
        if string == string[::-1]:
            return True
        return False
    
    L = []
    
    i = j = 0
    
    while i < len(s):
        while j <= len(s):
            if is_polindrom(s[i:j]):
                L.append(s[i:j])
            j += 1
        i += 1
        j = i
    
    return L


print(longestPalindrome("bb"))
print(longestPalindrome("a"))
print(longestPalindrome("babad"))


