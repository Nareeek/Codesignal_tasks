def FindIntersection(strArr):
    a, b = strArr[0], strArr[1]
    a1 = []
    b1 = []
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i].isdigit() and not a[i + 1].isdigit():
            a1.append(a[i])
            i += 1
        elif a[i].isdigit() and a[i + 1].isdigit():
            a1.append(a[i] + a[i + 1])
            i += 2
        else:
            i += 1
        if b[j].isdigit() and not b[j + 1].isdigit():
            b1.append(b[j])
            j += 1
        elif b[j].isdigit() and b[j + 1].isdigit():
            b1.append(b[j] + b[j + 1])
            j += 2
        else:
            j += 1
    i = 0
    j = 0
    while i < len(a1) and j < len(b1):
        if a1[i] == b1[j]:
            c.append(a1[i])
            i += 1
            j += 1
        elif a1[i] != b1[j] and j + 1 < len(a1):
            j += 1
        else:
            j = i
            i += 1
    strArr = ",".join(c)

    return strArr


print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))
