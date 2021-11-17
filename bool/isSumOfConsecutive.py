# 1
def isSumOfConsecutive2(n):
    s = c = 0
    i = tmp = 2

    while n // i - i // 2 > 0:
        k = n // i

        if i % 2:
            s = k - (i // 2)

        for j in range(i // 2, -(i // 2), -1):
            s += k + j

        if s == n:
            c += 1

        tmp += 1
        i = tmp
        s = 0

    return c


print(isSumOfConsecutive2(99))


# 2
def isSumOfConsecutive(n):
    for start in range(1, n):
        number = n
        subtrahend = start
        while number > 0:
            number -= subtrahend
            subtrahend += 1
        if number == 0:
            return True
    return False


print(isSumOfConsecutive(42))


# 3
def isSumOfConsecutive2(n):
    ctr = 0
    
    for i in range(1, n):
        s = 0
        for j in range(i, n):
            s += j
            if s > n:
                break
                
            if s == n:
                ctr += 1
    return ctr

# 4
def isSumOfConsecutive(n):
    
    for i in range(1, n):
        sum = 0
        
        for j in range(i, n):
            sum += j
            
            if sum == n:
                return True
                
            if sum > n:
                break
    
    return False


'''
def isSumOfConsecutive(n):
    if bin(n).count("1") == 1:
        return False
    
    return True
'''

