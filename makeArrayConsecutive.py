def makeArrayConsecutive(sequence):
    a = min(sequence)
    b = max(sequence)
    L = []
    while a < b:
        if a + 1 not in sequence:
            L.append(a + 1)
        a += 1
    return L



# 2
def makeArrayConsecutive(sequence):
    M = max(sequence)
    m = min(sequence)
    res = []
    for i in range(m, M):
        if i not in sequence:
            res.append(i)
    return res