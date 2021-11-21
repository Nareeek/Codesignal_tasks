# 1
def countSumOfTwoRepresentations(n, l, r):
    result = 0

    for a in range(l, r + 1):
        b = a
        while b <= r:
            if a + b == n:
                result += 1
            b += 1

    return result

# 2
def countSumOfTwoRepresentations2(n, l, r):
    dic = {n: n for n in range(l, r + 1)}
    s = set()

    for i in range(l, (r + 1) // 2 + 1):
        if (n - dic[i]) in dic:
            s.add(dic[i])
    return len(s)


print(countSumOfTwoRepresentations2(6, 2, 4))



# 3
def countSumOfTwoRepresentations3(n, l, r):
    return max(n // 2 - max(l, n - r) + 1, 0)

