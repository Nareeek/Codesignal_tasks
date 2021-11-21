def polygonPerimeter(matrix):
    perimeter = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i - 1 < 0 and matrix[i][j]:
                perimeter += 1
                
            if i + 1 == len(matrix) and matrix[i][j]:
                perimeter += 1
                
            if j - 1 < 0 and matrix[i][j]:
                perimeter += 1
                
            if j + 1 == len(matrix[0]) and matrix[i][j]:
                perimeter += 1
                
            if matrix[i][j] and 0 <= i - 1:
                if not matrix[i - 1][j]:
                    perimeter += 1
                    
            if matrix[i][j] and i + 1 < len(matrix):
                if not matrix[i + 1][j]:
                    perimeter += 1
                    
            if matrix[i][j] and 0 <= j - 1:
                if not matrix[i][j - 1]:
                    perimeter += 1
                    
            if matrix[i][j] and j + 1 < len(matrix[0]):
                if not matrix[i][j + 1]:
                    perimeter += 1
                    
    return perimeter