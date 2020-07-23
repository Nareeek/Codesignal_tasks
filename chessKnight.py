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