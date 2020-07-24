def makeArrayConsecutive(sequence):
    a = min(sequence)
    b = max(sequence)
    L = []
    while a < b:
        if a + 1 not in sequence:
            L.append(a + 1)
        a += 1
    return L