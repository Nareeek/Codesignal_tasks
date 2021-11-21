
import functools
import sys
sys.setrecursionlimit(10000)

def biggestPlus(matrix):
    if all(matrix[i]=='1'*len(matrix[i]) for i in range(len(matrix))):
        return (min(len(matrix), len(matrix[0]))-1)//2
        
    r = len(matrix)
    c = len(matrix[0])

    @functools.lru_cache(None)
    def left(i, j):
        if i == 0 or i == r-1 or j == 0 or j == c-1 or matrix[i][j] == '0':
            return int(matrix[i][j])
        return 1+left(i, j-1)

    @functools.lru_cache(None)
    def right(i, j):
        if i == 0 or i == r-1 or j == 0 or j == c-1 or matrix[i][j] == '0':
            return int(matrix[i][j])
        return 1+right(i, j+1)

    @functools.lru_cache(None)
    def up(i, j):
        if i == 0 or i == r-1 or j == 0 or j == c-1 or matrix[i][j] == '0':
            return int(matrix[i][j])
        return 1+up(i-1, j)

    @functools.lru_cache(None)
    def down(i, j):
        if i == 0 or i == r-1 or j == 0 or j == c-1 or matrix[i][j] == '0':
            return int(matrix[i][j])
        return 1+down(i+1, j)

    res = 0
    for i in range(1, r-1):
        for j in range(1, c-1):
            if matrix[i][j] == '1':
                lv = left(i, j)
                rv = right(i, j)
                uv = up(i, j)
                dv = down(i, j)
                res = max(res, min(lv, rv, uv, dv)-1)
    return res
