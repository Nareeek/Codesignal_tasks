def matrixTransposition(matrix):
    a = list(zip(*matrix))
    return a

# 2 
def matrixTransposition(matrix):

    result = []
    for j in range(len(matrix[0])):
        result.append([])
        for i in range(len(matrix)):
            result[j].append(matrix[i][j])
    return result