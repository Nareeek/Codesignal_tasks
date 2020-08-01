def isPower(n):
    for a in range(int(n ** 0.5) + 1):
        for b in range(int(math.log(n, 2)) + 1):
            if a ** b == n:
                return True
    return False