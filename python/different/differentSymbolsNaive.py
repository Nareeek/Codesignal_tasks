def differentSymbolsNaive(s):

    result = 0

    for i in range(26):
        found = False
        for j in range(len(s)):
            if ord(s[j]) == ord('a') + i:
                found = True
                break
        if found:
            result += 1
    return result
