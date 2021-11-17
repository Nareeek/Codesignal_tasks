def is_prime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # This is checked so that we can skip middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    for i in range(5, int(n ** 0.5) + 1, 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
    return True

T = int(input())
while (T > 0):
    number = int(input())
    if (is_prime(number)):
        print("Prime")
    else:
        print("Not prime")
    T -= 1
