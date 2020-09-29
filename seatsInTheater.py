def seatsInTheater(nCols, nRows, col, row):
    return (nRows - row) * (nCols - (col - 1))
    
    behind = nCols - col + 1
    side = nRows - row
    return behind * side