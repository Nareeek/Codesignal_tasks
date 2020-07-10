def mergeStrings(s1, s2):
    itog = ""
    i = 0
    
    while i < (len(s1) + len(s2)):
        if len(s1) == 0:
            itog += s2[i:]
            return itog
        elif len(s2) == 0:
            itog += s1[i:]
            return itog
        
        if s1.count(s1[i]) < s2.count(s2[i]):
            itog += s1[i]
            s1 = s1[i + 1:]
        elif s2.count(s2[i]) < s1.count(s1[i]):
            itog += s2[i]
            s2 = s2[i + 1:]
        elif (s2.count(s2[i]) == s1.count(s1[i])) and (ord(s1[i]) != ord(s2[i])):
            if ord(s1[i]) < ord(s2[i]):
                itog += s1[i]
                s1 = s1[i + 1:]
            elif ord(s2[i]) < ord(s1[i]):
                itog += s2[i]
                s2 = s2[i + 1:]
        elif (s2.count(s2[i]) == s1.count(s1[i])) and (ord(s1[i]) == ord(s2[i])):
            itog += s1[i]
            s1 = s1[i + 1:]
            
    return itog

print(mergeStrings("super","tower"))