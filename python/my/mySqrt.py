def mySqrt(n):

    left = 1
    right = n + 1
    while left < right - 1:
        middle = (left + right) // 2
        if middle * middle <= n:
            left = middle
        else:
            right = middle

    return left
