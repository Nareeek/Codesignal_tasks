# 1 dynamic programming
# O(n)-space, O(n)-time

def maxSubArray(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1,len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
        #print(dp)
    return max(dp)

nums = [-2,1,-3,7,-2,2,1,-5,4]
print(maxSubArray(nums))




# 2 dynamic programming
# O(1)-space, O(n)-time

def Kadane(arr,n): 

   current_maximum = arr[0]
   maximum_so_far =arr[0]
      
   for i in range(1,n): 
      current_maximum = max(arr[i], current_maximum + arr[i]) 
      maximum_so_far = max(maximum_so_far,current_maximum)
          
   return maximum_so_far 
  
arr = [-2,1,-3,7,-2,2,1,-5,4]
print(Kadane(arr, len(arr)))



#3
def maxSubarray(inputArray):
    t = 0
    res = 0
    for i in inputArray:
        if t+i>=0:
            t+=i
        else:
            t=0
        res = max(res, t)
    return res
