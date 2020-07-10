def mutateTheArray(n, a):
    b = []
    if n == 1:
        return a
    for i in range(n):
        if i == 0:
            b.append(0 + a[i] + a[i + 1])
        elif i == n - 1:
            b.append(a[i - 1] + a[i] + 0)
            return b
        else:
            b.append(a[i - 1] + a[i] + a[i + 1])
            print()
