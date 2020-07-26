def isIncreasingDigitsSequence(n):
    for x in range(len(str(n))-1):
        if int(str(n)[x+1])<=int(str(n)[x]):
            return False
    return True