# 1
def isIdentityMatrix(matrix):
    for i in range(len(matrix[0])):
        if matrix[i][i] == 1:
            matrix[i][i] = 0
            if any(matrix[i]):
                return False
        else: return False
    return True

# 2
def isIdentityMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if (matrix[i][j] != 1 and i == j
              or matrix[i][j] and i != j):
                return False
    return True
