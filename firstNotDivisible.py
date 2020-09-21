def firstNotDivisible(divisors, start):
    while True:
        a = False
        for i in divisors:
            if start % i == 0:
                a = True
        if not a:
            return start
        start += 1