def rightTriangle(sides):

    def sqr(value):
        return value * value

    sides.sort()
    if sqr(sides[0]) + sqr(sides[1]) == sqr(sides[2]):
        return True
    return False
