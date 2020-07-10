def palindromeRearranging(inp):
    a = []
    for i in set(inp):
        a.append(inp.count(i) % 2)

    return sum(a) <= 1

print(palindromeRearranging("abbcabb"))