def quickSort(a, l, r):
    if l >= r:
        return a

    x = a[l]  # barrier element
    i = l
    j = r

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]

            i += 1
            j -= 1

    quickSort(a, l, j)
    quickSort(a, i, r)

    return a


print("start")
quickSort(list(range(10000))[::-1], 0, len(list(range(10000))) - 1)
print("end")