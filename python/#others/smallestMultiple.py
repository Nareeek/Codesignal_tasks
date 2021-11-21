def smallestMultiple(left, right):
    res = 1
    while 1:
        for i in range(left, right + 1):
            if res % i != 0:
                break
        else:
            return res
        res += 1


# 2

L,R = eval(dir()[0])
r = 1

while R >= L:
    if r % R:
        r *= R
    R -=1
return r