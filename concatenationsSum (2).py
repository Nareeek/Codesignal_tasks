d = {}


def concat_elem_sum(array, element):
    sum = 0
    if element not in d:
        for i in array:
            sum += int(element + str(i))
        d[element] = sum
        return sum
    else:
        return d[element]


def concatenationsSum(a):
    s = []
    for i in range(len(a)):
        s.append(concat_elem_sum(a, str(a[i])))
    return sum(s)


print(concatenationsSum([10, 2]))
