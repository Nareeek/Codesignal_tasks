# 1
def areSimilar(a, b):
    if sorted(a) != sorted(b):
        return False
    d = {}
    for i in range(len(a)):
        if a[i] != b[i]:
            d[a[i]] = b[i]
    v = list(d.values())
    k = list(d.keys())
    q = 0

    print(v)
    print(k)
    for i in range(len(v)):
        for j in range(len(k)):
            if v[i] == k[j]:
                if v[j] == k[i]:
                    if q < 2:
                        q += 1
                    else:
                        break

    return q


print(areSimilar([4, 6, 3], [3, 4, 6]))


# 2
def areSimilar(a, b):
    if a == b:
        return True
    for i in range(len(a)):
        if a[i] != b[i]:
            for j in range(i, len(a) - 1):
                a[i], a[j + 1] = a[j + 1], a[i]
                if a == b:
                    return True
                else:
                    a[i], a[j + 1] = a[j + 1], a[i]
    return False


print(areSimilar([1, 2, 2], [2, 1, 1]))
