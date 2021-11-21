def fillShortestPaths(a):
    r = [row.count('s') for row in a].index(1)
    c = a[r].index('s')
    dist = ans(r, c, a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if ans(i, j, a) + minP(i, j, r, c) == dist:
                a[i][j] = '#'
    a[r][c] = 's'
    return a

def minP(r0, c0, r1, c1):
    return max(abs(r0-r1), abs(c0-c1))

def ans(r, c, a):
    return min(r, c, len(a) - r - 1, len(a[0]) - c - 1)