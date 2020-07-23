def chessBoardCellColor(cell1, cell2):
    x = ord(cell1[0]) - ord(cell2[0])
    y = ord(cell1[1]) - ord(cell2[1])
    
    return (x + y) % 2 == 0
    