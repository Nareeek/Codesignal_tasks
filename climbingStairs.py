import time
import timeit

a = time.time()


def climbingStairs(n):
    a = 0
    b = 1
    for i in range(n + 1):
        temp, a = a, b
        b += temp
    return a


print(climbingStairs(380))

ex = timeit.timeit("""
def climbingStairs(n):
    a = 0
    b = 1
    for i in range(n + 1):
        temp, a = a, b
        b += temp
    return a

    a = climbingStairs(38)""", number=1)
print(ex)

b = time.time()
print(b - a)
