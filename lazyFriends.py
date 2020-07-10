def lazyFriends(houses, maxDist):
    ans = []
    l = 0
    r = 0
    for i in range(len(houses)):
        while houses[i] - houses[l] > maxDist:
            l += 1
        while (r + 1 < len(houses)
               and houses[r + 1] - houses[i] <= maxDist):
            r += 1
        ans.append(r - l)
    return ans
