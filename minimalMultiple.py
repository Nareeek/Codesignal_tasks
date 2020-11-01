# 1
def minimalMultiple(divisor, lowerBound):
    while 1:
        if lowerBound % divisor == 0:
            return lowerBound
        lowerBound += 1
        
        
# 2
def minimalMultiple(divisor, lowerBound):

    if lowerBound % divisor == 0:
        return lowerBound
    return lowerBound + (-lowerBound) % divisor
