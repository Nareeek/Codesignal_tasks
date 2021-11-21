def isDiagonalMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] and i != j:
                return False
    return True
