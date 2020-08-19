# 1
def commonCharacterCount(s1, s2):
    map1 = {}
    map2 = {}
    answer = 0

    for i in range(len(s1)):
        char = s1[i]
        if char in map1:
            map1[char] += 1
        else:
            map1[char] = 1

    for i in range(len(s2)):
        char = s2[i]
        if char in map2:
            map2[char] += 1
        else:
            map2[char] = 1

    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)
        if char in map1 and char in map2:
            answer += min(map1[char], map2[char])
    return answer



# 2
def commonCharacterCount(s1, s2):
    d1 = {}
    d2 = {}
    for v1, v2 in zip(set(s1), set(s2)):
        d1[v1] = s1.count(v1)
        d2[v2] = s2.count(v2)
    
    print(d1)
    print(d2)

print(commonCharacterCount("aabcc", "adcaa"))