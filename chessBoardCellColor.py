def chessBoardCellColor(cell1, cell2):
    if ((ord(cell1[0]) % 2 == ord(cell2[0]) % 2) and (int(cell1[1]) % 2 == int(cell2[1]) % 2)):
        return True
    if ((ord(cell1[0]) % 2 != ord(cell2[0]) % 2) and (int(cell1[1]) % 2 != int(cell2[1]) % 2)):
        return True
    return False

print(chessBoardCellColor("A1", "C3"))