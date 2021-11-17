def sumOfCubes(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i * i
    return result
