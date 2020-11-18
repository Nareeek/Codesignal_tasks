# 1
def kthDigit(n, k):
    numDigits = 0
    number = n
    while number:
        numDigits += 1
        number //= 10

    indexFromLast = numDigits - k + 1

    while n:
        indexFromLast -= 1
        if indexFromLast == 0:
            return n % 10
        n //= 10

    return -1


# 2
def kthDigit(n, k):
    try:
        return int(str(n)[k - 1])
    except IndexError:
        return -1

# 3
def kthDigit(n, k):
    t = [int(e) for e in str(n)]
    if len(t)>=k:
        return t[k-1]
    else:
        return -1
    
# 4
def kthDigit(n, k):
    if (len(str(n))<k):
        return -1
    return int(str(n)[k-1])
