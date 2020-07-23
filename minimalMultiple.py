def minimalMultiple(divisor, lowerBound):
    while 1:
        if lowerBound % divisor == 0:
            return lowerBound
        lowerBound += 1