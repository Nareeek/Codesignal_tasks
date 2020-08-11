def sudoku2(grid):
    r = [set() for _ in range(9)]
    c = [set() for _ in range(9)]
    b = [set() for _ in range(9)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            k = i // 3 * 3 + j // 3
            
            d = grid[i][j]
            if d != ".":
                if d in r[i] or d in c[j] or d in b[k]:
                    return False
                r[i].add(d)
                c[j].add(d)
                b[k].add(d)
    return True