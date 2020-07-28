def create2DArray(lengths):
    o = []
    for a in lengths:
        o += list(range(a)),
    return o