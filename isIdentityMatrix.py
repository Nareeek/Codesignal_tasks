def isIdentityMatrix(matrix):
    for i in range(len(matrix[0])):
        if matrix[i][i] == 1:
            matrix[i][i] = 0
            if any(matrix[i]):
                return False
        else: return False
    return True