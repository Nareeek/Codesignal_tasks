def primeFactors2(n):
    factors = []
    divisor = 2

    while n != 1:
        if n % divisor == 0:
            factors.append(divisor)
        while n % divisor == 0:
            n /= divisor
        divisor += 1
        if divisor * divisor > n and n > 1:
            factors.append(n)
            factors.sort()
            break

    return factors
