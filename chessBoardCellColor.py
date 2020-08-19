# 1
def chessBoardCellColor(cell1, cell2):

    def getX(pos):
        return ord(pos[0]) - ord('A')
    def getY(pos):
        return ord(pos[0]) - ord('1')

    sum1 = getX(cell1[0]) + getY(cell1[1])
    sum2 = getX(cell2[0]) + getY(cell2[1])
    if sum1 % 2 == sum2 % 2:
        return True
    return False



# 2
def chessBoardCellColor(cell1, cell2):
    if ((ord(cell1[0]) % 2 == ord(cell2[0]) % 2) and (int(cell1[1]) % 2 == int(cell2[1]) % 2)):
        return True
    if ((ord(cell1[0]) % 2 != ord(cell2[0]) % 2) and (int(cell1[1]) % 2 != int(cell2[1]) % 2)):
        return True
    return False


print(chessBoardCellColor("A1", "C3"))
