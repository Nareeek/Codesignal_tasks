def specialPolynomial(x, n):
    pow_x = 0
    y = 0
    while y < n:
        pow_x += 1
        y += x ** pow_x
        
    return pow_x - 1
        