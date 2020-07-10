def palindromeRearranging(inp):
    q = 0
    for i in range(len(inp)):
        if inp.count(inp[i]) % 3 == 0:
            q += 1
            if q == 2:
                return False
        
    return True

print(palindromeRearranging("abbcabb"))