def powersOfTwo(n):
    a = []
    while n:
        p = int(math.log(n, 2))
        a += 2**p,
        n -= 2**p
    return sorted( a )