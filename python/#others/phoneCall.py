# 1
def phoneCall(min1, min2_10, min11, s):

    if s < min1:
        return 0
    for i in range(2, 11):
        if s < min1 + min2_10 * (i - 1):
            return i - 1
    return 10 + (s - min1 - min2_10 * 9) // min11





# 2
def phoneCall(min1, min2_10, min11, s):
    if s >= min1:
        s -= min1
        q = 1
    else:
        return 0

    if s > min2_10 * 9:
        s -= min2_10 * 9
        q = 10
    else:
        return q + s // min2_10

    return q + s // min11


print(phoneCall(10, 1, 2, 20))

