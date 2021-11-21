def fastSymmetrization(a):
    n = len(a)
    m = len(a[0])
    for i in range(n):
        for j in range(m):
            s = {a[i][j], a[i][m-j-1], a[n-i-1][j], a[n-i-1][m-j-1]}
            if len(s) != 1:
                s.discard("*")
                if len(s) != 1:
                    return []
                a[i][j] = a[i][m-j-1] = a[n-i-1][j] = a[n-i-1][m-j-1] = s.pop()
    return a