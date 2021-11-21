def maxSubmatrixSum(matrix, n, m):
    result = 0
  
    for i in range(len(matrix)):
        if i + n > len(matrix):
            break
        for j in range(len(matrix[0])):
            if j + m > len(matrix[0]):
                break
            sum = 0
            
            for x in range(n):
                for y in range(m):
                    sum += matrix[i + x][j + y]
            if (i == 0 and j == 0 or sum > result):
                result = sum
    return result
