def sortedSquaredArray(array):
    m = min(array, key=abs)
    out_array = []

    for i in range(len(array)):
        out_array.append(m ** 2)
        array.remove(m)
        m = min(array, key=abs, default=0)

    return out_array

print(sortedSquaredArray([-6, -4, 1, 2, 3, 5]))