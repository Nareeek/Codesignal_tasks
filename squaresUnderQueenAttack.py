def squaresUnderQueenAttack(n, queens, queries):
    a = set()
    b = set()
    c = set()
    d = set()
    
    for x,y in queens:
        a.add(x)
        b.add(y)
        c.add(x+y)
        d.add(x-y)
        
    o = []
    for x,y in queries:
        o += x in a or y in b  or (x + y) in c or (x - y) in d,
    return o