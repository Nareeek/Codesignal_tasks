def spiralMatrixPrint(row, col, arr):
    # Defining the boundaries of the matrix.
    top = 0
    bottom = row-1
    left = 0
    right = col - 1

    # Defining the direction in which the array is to be traversed.
    dir = 0
    
    while (top <= bottom and left <=right):    
        if dir ==0:
            for i in range(left,right+1): # moving left->right
                print (arr[top][i], end=" ")

            # Since we have traversed the whole first
            # row, move down to the next row.
            top +=1
            dir = 1

        elif dir ==1:
            for i in range(top,bottom+1): # moving top->bottom
                print (arr[i][right], end=" ")

            # Since we have traversed the whole last
            # column, move down to the previous column.
            right -=1 
            dir = 2
            
        elif dir ==2:
            for i in range(right,left-1,-1): # moving right->left
                print (arr[bottom][i], end=" ")

            # Since we have traversed the whole last
            # row, move down to the previous row.
            bottom -=1
            dir = 3
            
        elif dir ==3:
            for i in range(bottom,top-1,-1): # moving bottom->top
                print (arr[i][left], end=" ")
            # Since we have traversed the whole first
            # column, move down to the next column.
            left +=1
            dir = 0

# Driver code
# Change the following array and the corresponding row and
# column arguments to test on some other input
array = [[33,29,-15,-20,-41,-1,34,20,-41,44], 
 [14,-11,-27,-35,29,-14,34,-41,49,19], 
 [-12,-44,44,-43,-13,-6,40,-24,-6,8], 
 [-40,4,27,2,2,15,38,4,-13,15], 
 [-42,3,5,10,15,34,-18,-22,9,38]]
spiralMatrixPrint(10, 5, array)

