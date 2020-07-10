from fractions import gcd
def modInverse(n, m):
    if gcd(n,m) != 1:
        return -1
    x1 , x2, y1 , y2 ,_m = 1,0,0,1, m
    while m:
        n , q , m = m , *divmod(n,m)
        x1,y1,x2,y2 = x2,y2,x1 - q * x2,y1 - q * y2
    return x1 if x1 > 0 else x1 + _m


print(modInverse(9831, 27871198))