def findSubarrayBySum(s, arr):
    cur_sum = 0
    start = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        while cur_sum > s:
            cur_sum -= arr[start]
            start += 1

        if cur_sum == s:
            return [start+1, i+1]

    return [-1]