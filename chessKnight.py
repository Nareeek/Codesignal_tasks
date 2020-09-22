# 1
def chessKnight(cell):
    row = ord(cell[1]) - ord('0')
    column = ord(cell[0]) - ord('a') + 1
    steps = [
            [-2, -1], [-1, -2], [1, -2], [2, -1],
            [2, 1], [1, 2], [-1, 2], [-2, 1]
            ]
    answer = 0

    for i in range(len(steps)):
        tmpRow = row + steps[i][0]
        tmpColumn = column + steps[i][1]
        if (tmpRow >= 1 and tmpRow <= 8 and
            tmpColumn >= 1 and tmpColumn <= 8):
            answer += 1

    return answer


# 2
def chessKnight(cell):
    x = ord(cell[0]) % 97
    y = ord(cell[1]) - ord('0') - 1
    c = 0
    for dx in range(-2, 2+1):
        for dy in range(-2, 2+1):
            if abs(dx * dy) == 2:
                if isValid(x + dx, y + dy):
                    c += 1
    return c

def isValid(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7