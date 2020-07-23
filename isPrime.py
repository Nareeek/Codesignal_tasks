def isPrime(n):
    divisor = 2
    while n > divisor:
        if n % divisor == 0:
            return False
        else:
            divisor += 1
    return True