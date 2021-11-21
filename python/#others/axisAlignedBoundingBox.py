# 1
def axisAlignedBoundingBox(x, y):

    minX = x[0]
    maxX = x[0]
    minY = y[0]
    maxY = y[0]

    for i in range(1, len(x)):
        minX = min(x[i], minX)
        maxX = max(x[i], maxX)
        minY = min(y[i], minY)
        maxY = max(y[i], maxY)

    return (maxX - minX) * (maxY - minY)


# 2
def axisAlignedCirclesBoundingBox(x, y, r):

    minX = x[0] - r[0]
    maxX = x[0] + r[0]
    minY = y[0] - r[0]
    maxY = y[0] + r[0]

    for i in range(1, len(x)):
        minX = min(x[i] - r[i], minX)
        maxX = max(x[i] + r[i], maxX)
        minY = min(y[i] - r[i], minY)
        maxY = max(y[i] + r[i], maxY)

    return (maxX - minX) * (maxY - minY)
