from itertools import product


# 1
def concatenationsSum(a):
    return sum(list(map(int, ["".join(list(map(str, i))) for i in list(product(a, repeat=2))])))


# 2
def concatenationsSum(a):
    p = []
    for i in range(len(a)):
        for j in range(len(a)):
            p.append(str(a[i]) + str(a[j]))

    summ = 0
    for i in range(len(p)):
        summ += int(p[i])

    return p, summ


print(concatenationsSum([10, 2]))

# 3
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


# 4
def concatenationsSum(a):
    su = 0

    b = list(product(a, repeat=2))

    for i in b:
        su += int(str(i[0]) + str(i[1]))
    return su


print(concatenationsSum([1000000, 1000000, 1000000, 1000000]))


# 5
def concatenationsSum(a):
    a = list(product(a, repeat=2))
    # print(a)
    b = ["".join(list(map(str, i))) for i in a]
    # print(b)
    c = sum(list(map(int, b)))
    print(c)
