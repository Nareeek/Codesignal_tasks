def countPairsWithDifference(k, a):
    a = sorted(a)
    c = 0
    i = 0
    j = 0
    lena = len(a)
    while(i < lena):
        if a[i] - a[j] == k:
            # print a[i], a[j]
            d1 = 1
            d2 = 1
            while True:
                if i+1 < lena and a[i+1] == a[i]:
                    i += 1
                    d1 += 1
                elif a[j+1] == a[j]:
                    j += 1
                    d2 += 1
                else:
                    i += 1
                    j += 1
                    c += d1*d2
                    break
            
        elif a[i] - a[j] > k:
            j += 1
        else:
            i += 1
    return c%(10**9 + 7)