def sudoku2(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != ".":
                if grid[i].count(grid[i][j]) != 1:
                    return False


    L = []
    for j in range(9):
        for i in range(9):
            L.append(grid[i][j])
        else:
            for k in range(9):
                if L[k] != ".":
                    if L.count(L[k]) != 1:
                        return False
            else:
                L = []

    L = []
    for j in range(7):
        for i in range(7):
            L.append(grid[i][j])
            L.append(grid[i][j + 1])
            L.append(grid[i][j + 2])
            L.append(grid[i + 1][j])
            L.append(grid[i + 1][j + 1])
            L.append(grid[i + 1][j + 2])
            L.append(grid[i + 2][j])
            L.append(grid[i + 2][j + 1])
            L.append(grid[i + 2][j + 2])
            for k in range(9):
                if L[k] != ".":
                    if L.count(L[k]) != 1:
                        return False
            else:
                L = []

    return True

print(sudoku2([[".", ".", ".", "1", "4", ".", ".", "2", "."],
               [".", ".", "6", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", "1", ".", ".", ".", ".", ".", "."],
               [".", "6", "7", ".", ".", ".", ".", ".", "9"],
               [".", ".", ".", ".", ".", ".", "8", "1", "."],
               [".", "3", ".", ".", ".", ".", ".", ".", "6"],
               [".", ".", ".", ".", ".", "7", ".", ".", "."],
               [".", ".", ".", "5", ".", ".", ".", "7", "."]]))
