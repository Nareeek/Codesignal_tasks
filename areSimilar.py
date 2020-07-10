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