def isLuckyNumber(n):
    for num in str(n):
        if int(num) in (1,2,3,5,6,8,9,0):
            return False
    return True