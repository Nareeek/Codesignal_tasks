def sumOfDivisors(n):
    if n==1:
        return 1
    s = 0
    i = 1
    while i*i <= n:
        if n%i==0:
            k = n/i
            s += k + i%k
        i+=1
    return s