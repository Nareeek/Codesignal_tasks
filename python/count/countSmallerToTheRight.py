# 1
# brute force method 90%
"""
For nums = [3, 8, 4, 1], the output should be
countSmallerToTheRight(nums) = [1, 2, 1, 0].
"""

def countSmallerToTheRight(nums):
    s=[]
        
    for i in range(len(nums)):
        a=0
        for j in range(i,len(nums)):
            if nums[i]>nums[j]:
                a+=1
        s.append(a)
        
        
    return sum(s)