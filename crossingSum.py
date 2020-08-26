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
    
