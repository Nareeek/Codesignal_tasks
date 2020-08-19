# 1
def findMedianSortedArrays(nums1, nums2) -> float:
    if len(nums1) > len(nums2):
        nums1,nums2 = nums2, nums1
        
    # Shorter array is nums1
        
    n1, n2 = len(nums1), len(nums2)
    
    leftHalf = (n1 + n2 + 1) // 2
    
    #Now the minimum contribution nums1 can make to the merged array is 0 and the max contribution is n1 (nums1's length)
    
    minContribution = 0
    maxContribution = n1
    
    # We are essentially finding the last element of the left half of the merged final array, because it is
    # sufficient for finding the median. We do this using binary search.
    
    while minContribution <= maxContribution:
        
        # We are searching in the space [minContribution, maxContribution] for the number of elements nums1 will contribute to the left half
        # of the merged array.Since we know the size of the left half of the merged array, we can calculate the number of elements nums2 will
        # contribute. Thus, we can find the median.
        
        c1 = minContribution + (maxContribution - minContribution) // 2 # Num of elements nums1 contributes
        c2 = leftHalf - c1 # Num of elements nums2 contributes
        
        x, x2, y, y2 = None, None, None, None
        
        if c1 > 0:
            x = nums1[c1-1]
            
        if c2 > 0:
            y = nums2[c2-1]
            
        if c1 < n1:
            x2 = nums1[c1]
        
        if c2 < n2:
            y2 = nums2[c2]
        
        # This is the important part. If x > y2, it means that x will come after y2 in the final merged array.
        # Hence, we need to decrease maxContribution by 1. 
        
        if x and y2 and x > y2:
            maxContribution = c1 - 1
            
        # Similarly, if y>x2, we need to increase num of elements nums2 contributes; hence, increase the number of elemenets nums1 contributes.
        
        elif y and x2 and y > x2:
            minContribution = c1 + 1
        
        # This is the case which happens when we've found our answer
        
        else:
            
            # Here we find out the last element of the left half of the merged array. If x>y, it means
            # that x will be the, median(since it will occur after y in the merged array). SImilar reasoning is applicable for the other case.
            
            leftHalfEnd = None
            
            if not x:
                leftHalfEnd = y
            
            elif not y or x > y:
                leftHalfEnd = x
            
            else:
                leftHalfEnd = y
                
            #Now if the total elements(n1+n2) is odd, we can simply return the leftHalfEnd
            
            if (n1 + n2) % 2:
                return leftHalfEnd
            
            #However, if it is even, we need to find the first element in the right half of the merged array and calculate their mean and return it.
            
            else:
                rightHalfFirst = None
                
                if not x2:
                    rightHalfFirst = y2
                
                elif not y2 or x2 < y2:
                    rightHalfFirst = x2
                
                else:
                    rightHalfFirst = y2
                
                return (rightHalfFirst + leftHalfEnd) / 2
    return -1

print(findMedianSortedArrays([1,2,4,5,6,8,12],[3,6,7,9,15,20,52,362]))



# 2
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
