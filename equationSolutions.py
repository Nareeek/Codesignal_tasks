def equationSolutions(l, r):

    result = 0
    for a in range(l, r + 1):
        b = l
        while b <= r:
            if a * a * a == b * b:
                result += 1
            b += 1
    return result