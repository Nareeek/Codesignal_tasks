def matrixTrace(matrix):

    result = 0
    for i in range(0, len(matrix)):
        result += matrix[i][i]
    return result