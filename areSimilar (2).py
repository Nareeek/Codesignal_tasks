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
