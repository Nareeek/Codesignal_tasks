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
