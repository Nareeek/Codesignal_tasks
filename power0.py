def power(x, exponent):
    result = 1
    for count in range(exponent):
        result *= x
    return result