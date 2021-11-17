# 1
def isPower(n):

    if n == 1:
        return True

    for i in range(2, n):
        if n % i == 0:
            tmp = n
            while n % i == 0:
                n /= i
            if n == 1:
                return True
            n = tmp
    return False


# 2
def isPower(n):
    for a in range(int(n ** 0.5) + 1):
        for b in range(int(math.log(n, 2)) + 1):
            if a ** b == n:
                return True
    return False