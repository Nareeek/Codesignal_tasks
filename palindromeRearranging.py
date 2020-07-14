# 1
def palindromeRearranging(inp):
    q = 0
    for i in range(len(inp)):
        if inp.count(inp[i]) % 3 == 0:
            q += 1
            if q == 2:
                return False

    return True


# 2
def palindromeRearranging(inp):
    a = []
    for i in set(inp):
        a.append(inp.count(i) % 2)

    return sum(a) <= 1


print(palindromeRearranging("abbcabb"))
