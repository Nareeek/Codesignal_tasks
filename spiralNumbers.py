# 1
def spiralNumbers(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m


print(spiralNumbers(5))



# 2
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
