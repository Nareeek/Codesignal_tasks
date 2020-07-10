def countSumOfTwoRepresentations2(n, l, r):
    dic = {n:n for n in range(l, r + 1)}
    s = set()
    
    for i in range(l, (r + 1) // 2 + 1):
        if (n - dic[i]) in dic:
            s.add(dic[i])
    return len(s)

print(countSumOfTwoRepresentations2(6,2,4))