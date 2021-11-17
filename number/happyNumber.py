def happy(n):
    ret = 0
    while n > 0:
        ret += (n % 10) ** 2
        n //= 10
    return ret
def happyNumber(n):
    cnt = 0
    while n != 1 and cnt < 10000:
        cnt += 1
        n = happy(n)
    return n == 1


# 2
def happyNumber(n):
    nums = [n]
    while True:
        s = sum([int(i)*int(i) for i in list(str(n))])
        print s
        if s == 1:
            return True
        elif s in nums:
            return False
        else:
            nums.append(s)
        n = s
    return True