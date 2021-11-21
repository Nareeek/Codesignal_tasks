def extractMatrixColumn(matrix, column):
    extract = []
    for i in range(0,len(matrix)):
        extract.append(matrix[i][column])
    
    return extract