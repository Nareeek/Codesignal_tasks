def isLuckyNumber(n):
    for num in str(n):
        if int(num) in (1,2,3,5,6,8,9,0):
            return False
    return True

# 2

def isLuckyNumber(n):
    while n > 0:
        tmpDigit = n % 10
        if tmpDigit != 7 and tmpDigit != 4:
            return False
        n = n // 10
    return True


