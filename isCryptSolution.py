def tver(text, ss):
    L = []
    i = j = 0
    s = ""
    while i < len(ss) and j < len(text):
        if ss[i][0] == text[j]:
            L.append(ss[i][1])
            i = 0
            j += 1
        else:
            i += 1
    for i in range(len(L)):
        s += L[i]
    return s
def isCryptSolution(crypt, solution):
    a = tver(crypt[0], solution)
    b = tver(crypt[1], solution)
    c = tver(crypt[2], solution)
    if (len(a) > 1 and a[0] == "0") or (len(b) > 1 and b[0] == "0") or (len(c) > 1 and c[0] == "0"):
        return False
    return int(a) + int(b) == int(c)
    

print(isCryptSolution(["WASD", "IJKL", "AOPAS"], [["W","2"], ["A","0"],
                                                  ["S","4"], ["D","1"],
                                                  ["I","5"], ["J","8"],
                                                  ["K","6"], ["L","3"],
                                                  ["O","7"], ["P","9"]]))





