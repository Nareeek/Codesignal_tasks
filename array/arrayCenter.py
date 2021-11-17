def arrayCenter(a):
    s = sum(a); avg = s / len(a); m = min(a)
    b = []
    for i, v in enumerate(a):
        if abs(v - avg) < m:
            b.append(v)
    return b