def containsCloseNums(nums, k):
    d = {}

    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = {i}
        else:
            d[nums[i]].add(i)

    return d


print(containsCloseNums([5, 32, 1, 3, 5, 2], 3))
