def nearestPrime(nar):
    """
    Find the min nearest Prime number
    """
    chk_prime(nar)
    if chk_prime(nar):
        return nar
    else:
        count = 1
        while count < nar:
            holder1 = nar - count
            holder2 = nar + count
            holder1_chk = chk_prime(holder1)
            holder2_chk = chk_prime(holder2)
            if holder1_chk and holder2_chk:
                return min(holder1, holder2)
            elif holder1_chk and not holder2_chk:
                return holder1
            elif holder2_chk and not holder1_chk:
                return holder2
            else:
                count += 1


def chk_prime(n):
    """
    Checks if a number is prime or not
    """
    if n > 1:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False


print(nearestPrime(99999992))