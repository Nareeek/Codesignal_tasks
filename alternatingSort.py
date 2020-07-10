def alternatingSort(a):
    a1 = a[: len(a) // 2]
    a2 = a[len(a) // 2:]
    a2.reverse()
    a3 = []
    b = []
    if len(a) % 2 != 0:
        if len(a1) > len(a2):
            a3.append(a1[-1])
            a1.remove(a1[-1])
        else:
            a3.append(a2[-1])
            a2.remove(a2[-1])

    for i in range(len(a1)):
        b.append(a1[i])
        b.append(a2[i])

    if len(a3) != 0:
        b.append(a3[0])

    return sorted(set(b)) == b
