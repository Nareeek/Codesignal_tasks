def quadraticEquation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return []
    x1 = (-b + abs(d ** 0.5)) / 2 * a
    x2 = (-b - abs(d ** 0.5)) / 2 * a
    if d == 0:
        return [x1]
    elif d > 0:
        if x1 < x2:
            return [x1, x2]
        else:
            return [x2, x1]


print(quadraticEquation(2, 2, 0))
