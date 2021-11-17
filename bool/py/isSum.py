def isSum(value):
    sum_ = 0
    out = False
    for i in range(value+1):
        sum_ += i
        if sum_ == value:
            out = True
    return out