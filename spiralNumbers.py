def direction(List, row, column, tiv, direction):
    
    if direction == "left_Right":
        while column < (len(List[row]) - 1):
            if List[row][column + 1] == 0:
                List[row][column + 1] = tiv + 1
                column += 1
                tiv += 1
            else:
                break
    elif direction == "right_Left":
        while column > 0:
            if List[row][column - 1] == 0:
                List[row][column - 1] = tiv + 1
                column -= 1
                tiv += 1
            else:
                break
    elif direction == "up_Down":
        while row < len(List) - 1:
            if List[row + 1][column] == 0:
                List[row + 1][column] = tiv + 1
                row += 1
                tiv += 1
            else:
                break
    elif direction == "down_Up":
        while row > 0:
            if List[row - 1][column] == 0:
                List[row - 1][column] = tiv + 1
                row -= 1
                tiv += 1
            else:
                break

    return tiv, row, column


def spiralNumbers(n):
    l = [[0 for j in range(n)] for i in range(n)]
    r = 0
    c = -1
    t = 0
    while t < (n ** 2):
        t, r, c = direction(l, r, c, t, "left_Right")
        t, r, c = direction(l, r, c, t, "up_Down")
        t, r, c = direction(l, r, c, t, "right_Left")
        t, r, c = direction(l, r, c, t, "down_Up")
        
    return l

print(spiralNumbers(10))