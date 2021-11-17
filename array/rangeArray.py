def rangeArray(l, r, step):

    result = []
    while l < r:
        result.append(l)
        l += step
    return result
