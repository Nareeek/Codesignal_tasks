#1
def isIncreasingDigitsSequence(n):
    d = n%10
    while n>0:
        n//=10
        nd = n%10
        if nd>=d:return False
        d = nd
    return True

# 2
def isIncreasingDigitsSequence(n):
    for x in range(len(str(n))-1):
        if int(str(n)[x+1])<=int(str(n)[x]):
            return False
    return True
