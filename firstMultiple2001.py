def firstMultiple2(divisors, start):
    while 1:
        for x in divisors:
            if start % x == 0:
                return start
        start += 1 