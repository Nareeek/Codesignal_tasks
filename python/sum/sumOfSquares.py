def sumOfSquares(n):
    a = 0
    for i in range(n + 1):
        a+= i**2

    return a

# 2
def sumOfSquares(n):
    return sum([i ** 2 for i in range(1, n + 1)])