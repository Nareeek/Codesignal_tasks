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