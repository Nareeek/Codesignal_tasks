# 1
import numpy as np

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print(np.matrix(grid))


def possible(y, x, n):
    global grid

    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


print(possible(4, 4, 3))
print(possible(4, 4, 5))


def solve():
    global grid

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return

    print(np.matrix(grid))
    input("More?")


solve()



# 2
def sudoku2(grid):
    rev_grid = list(zip(*grid))
    gr = []

    for i in range(9):
        if impossible(grid[i]) or impossible(rev_grid[i]):
            return False
    for j in range(0, 9, 3):
        for i in range(0, 9, 3):
            for k in [0, 1, 2]:
                for z in [0, 1, 2]:
                    gr.append(grid[i + k][j + z])
            if impossible(gr):
                return False
            gr = []

    return True


def impossible(List):
    for x in List:
        if x.isdigit():
            if List.count(x) > 1:
                return True
    return False


print(sudoku2([['.', '.', '.', '1', '4', '.', '.', '2', '.'],
               ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
               ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
               ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
               ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
               ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
               ['.', '.', '.', '5', '.', '.', '.', '7', '.']]))


# 3
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
