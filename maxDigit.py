def maxDigit(n):

    result = 0
    while n > 0:
        result = max(result, n % 10)
        n = n // 10

    return result