def counter(number):
    a = []
    i = 2
    while i <= abs(number):
        if number % i == 0:
            a.append(i)
            number /= i
        else:
            i += 1
    return a


def simplifyRational(numerator, denominator):
    a = counter(numerator)
    b = counter(denominator)
    if numerator == 0:
        return [0, 1]
    if denominator == 0:
        return [1, 0]
    i = 0
    while i < len(a):
        if len(a) == 0:
            break
        if a[i] in b:
            b.remove(a[i])
            a.remove(a[i])
        else:
            i += 1
    p1 = p2 = 1
    for i in a:
        p1 *= i
    for i in b:
        p2 *= i
    if numerator < 0:
        p1 *= -1
    if denominator < 0:
        p2 *= -1
    return [p1, p2] if p2 > 0 else [-p1, -p2]


print(simplifyRational(5235, 1495))

print(simplifyRational(8, -5))

print(simplifyRational(-18, -24))

print(simplifyRational(478, -239))

print(simplifyRational(6, -2))
