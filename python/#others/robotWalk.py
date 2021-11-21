# 1
def robotWalk(a):
    x = y = 0
    dx = 0
    dy = 1
    v = {}
    v[(x, y)] = True
    for d in a:
        for i in range(d):
            if x + dx < 0 or y + dy < 0:
                continue
            x += dx
            y += dy
            if (x, y) in v:
                return True
            v[(x, y)] = True
        dx, dy = dy, -dx
    return False


# 2
def robotWalk(a):
    minX = 0
    minY = -1
    maxX = float('inf')
    maxY = float('inf')

    x = 0
    y = 0

    for i in range(len(a)):
        j = i % 4

        if j == 0:
            y += a[i]
            if y >= maxY:
                return True
            maxY = y

        elif j == 1:
            x += a[i]
            if x >= maxX:
                return True
            maxX = x

        elif j == 2:
            y -= a[i]
            if y <= minY:
                return True
            minY = y

        elif j == 3:
            x -= a[i]
            if x <= minX:
                return True
            minX = x

    return False