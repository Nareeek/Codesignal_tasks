# 1
def reverseVowelsOfString(s):
    vowelIndices = []
    for character in range(len(s)):
        if s[character] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            vowelIndices.append(character)
    if len(vowelIndices)==0:return s
    s = list(s)
    for index in range(len(vowelIndices)//2):
        s[vowelIndices[index]], s[vowelIndices[-index-1]] = s[vowelIndices[-index-1]], s[vowelIndices[index]]
    return "".join(s)

# 2
def reverseVowelsOfString(s):
    s = list(s)
    vowels = "aeiouAEIOU"
    f = []
    for i in range(len(s)):
        if s[i] in vowels:
            f.append(s[i])
            s[i] = 0

    for i in range(len(s)):
        if s[i] == 0:
            s[i] = f[-1]
            f = f[:-1]
            
    return ''.join(s)
    
