def leastFactorial(n):
    p = 1
    k = 1
    while p < n:
        k += 1
        p *= k
    return p

# 2
def leastFactorial(n):

    factorial = 1
    k = 2
    while factorial < n:
        factorial *= k
        k += 1
    return factorial
