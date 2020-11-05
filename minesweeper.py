# 1
def neighbors(matrix,i,j,row,col):
    mine = 0
    if not ((i < 1) or (j < 1)):
        if matrix[i - 1][j - 1]:
            mine+=1
    if not (i < 1):
        if matrix[i - 1][j]:
            mine+=1
    if not ((i < 1) or (j >= col-1)):
        if matrix[i - 1][j + 1]:
            mine+=1
    if not (j >= col-1):
        if matrix[i][j + 1]:
            mine+=1
    if not ((i >= row-1) or (j >= col-1)):
        if matrix[i + 1][j + 1]:
            mine+=1
    if not (i >= row-1):
        if matrix[i + 1][j]:
            mine+=1
    if not ((i >= row-1) or (j < 1)):
        if matrix[i + 1][j - 1]:
            mine+=1
    if not (j < 1):
        if matrix[i][j - 1]:
            mine+=1
    return mine
            
def minesweeper(matrix):
    row = len(matrix)
    col = len(matrix[0])
    sol = []
    for i in range(0,row):
        temp = []
        for j in range(0,col):
            temp.append(neighbors(matrix,i,j,row,col))
        sol.append(temp)
    
    return sol



# 2
def minesweeper(matrix):
    res = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= r + x < len(matrix):
                        if 0 <= c + y < len(matrix[0]):
                            res[r][c] += matrix[r + x][c + y]
            res[r][c] -= matrix[r][c]
    return res



# 3
def minesweeper(matrix):
    r = []
    
    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[0]):
                        l += matrix[i + x][j + y]
            r[i].append(l)
    return r

