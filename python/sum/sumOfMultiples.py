def sumOfMultiples(n, k):
    summ = 0
    
    for i in range(k, n + 1):
        if i % k == 0:
            summ += i
    return summ

# 2
def sumOfMultiples(n, k):
    return sum([i for i in range(n + 1) if i % k == 0])

# 3
def sumOfMultiples(n, k):
    r = 0
    m = 1
    while k*m <= n:
        r += k * m
        m += 1
    return r