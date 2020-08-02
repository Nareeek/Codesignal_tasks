def commonCharacterCount(s1, s2):
    d1 = {}
    d2 = {}
    for v1, v2 in zip(set(s1), set(s2)):
        d1[v1] = s1.count(v1)
        d2[v2] = s2.count(v2)
    
    print(d1)
    print(d2)

print(commonCharacterCount("aabcc", "adcaa"))