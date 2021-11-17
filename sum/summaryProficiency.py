def summaryProficiency(a, n, m):
    s=0
    c=0
    for i in range(len(a)):
        if c>=n:
            return s
        if a[i]>=m:
            s+=a[i]
            c+=1
    return s
