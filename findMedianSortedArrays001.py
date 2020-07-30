def findMedianSortedArrays(input1, input2):
        # if input1 length is greater than switch them so that input1 is smaller than input2.
        if len(input1) > len(input2):
            return findMedianSortedArrays(input2, input1)
        x = len(input1)
        y = len(input2)

        low = 0
        high = x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
            # if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
            
            maxLeftX = float("-inf") if partitionX == 0 else input1[partitionX - 1]
            minRightX = float("inf") if partitionX == x else input1[partitionX]

            maxLeftY = float("-inf") if partitionY == 0 else input2[partitionY - 1]
            minRightY = float("inf") if partitionY == y else input2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # We have partitioned array at correct place
                # Now get max of left elements and min of right elements to get the median in case of even length combined array size
                # or get max of left for odd length combined array size.
                
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
                
            elif maxLeftX > minRightY: # we are too far on right side for partitionX. Go on left side.
                high = partitionX - 1
            
            else: # we are too far on left side for partitionX. Go on right side.
                low = partitionX + 1
            
x = [1, 3, 8, 9, 15]
y = [7, 11, 18, 19, 20, 25]

print(findMedianSortedArrays(x, y))