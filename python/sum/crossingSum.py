# 1
def crossingSum(m, a, b):
    s = 0
    for i in range(len(m)):
        s+=m[i][b]
    s+=sum(m[a])
        
    return(s-m[a][b])

# 2
def crossingSum(matrix, a, b):
    sum = 0
    for i in range(len(matrix[0])):
        sum += matrix[a][i]
        
    for j in range(len(matrix)):
        sum += matrix[j][b]
        
    sum -= matrix[a][b]
    
    return sum
    
# 3
def crossingSum(matrix, row, column):

    result = 0
    for i in range(len(matrix)):
        result += matrix[i][column]
    for i in range(len(matrix[0])):
        result += matrix[row][i]
    result -= matrix[row][column]

    return result
