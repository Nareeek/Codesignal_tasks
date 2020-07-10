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
