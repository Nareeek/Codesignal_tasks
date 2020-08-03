def insideCircle(point, center, radius):

    def sqr(value):
        return value * value

    if sqr(point[0] - center[0]) + sqr(point[1] - center[1]) <= sqr(radius):
        return True
    return False