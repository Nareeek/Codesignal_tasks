def starRotation(matrix, width, center, t):
    rowCenter = center[0]
    colCenter = center[1]
    width //= 2
    for j in range(0,t%360):
        for i in range(0,width):
            temp = matrix[rowCenter-width+i][colCenter-width+i]
            matrix[rowCenter-width+i][colCenter-width+i] = matrix[rowCenter][colCenter-width+i]
            matrix[rowCenter][colCenter-width+i] = matrix[rowCenter+width-i][colCenter-width+i]
            matrix[rowCenter+width-i][colCenter-width+i] = matrix[rowCenter+width-i][colCenter]
            matrix[rowCenter+width-i][colCenter] = matrix[rowCenter+width-i][colCenter+width-i]
            matrix[rowCenter+width-i][colCenter+width-i] = matrix[rowCenter][colCenter+width-i]
            matrix[rowCenter][colCenter+width-i] = matrix[rowCenter-width+i][colCenter+width-i]
            matrix[rowCenter-width+i][colCenter+width-i] = matrix[rowCenter-width+i][colCenter]
            matrix[rowCenter-width+i][colCenter] = temp
    
    return matrix