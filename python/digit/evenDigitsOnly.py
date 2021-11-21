def evenDigitsOnly(n):
    n = str(n)
    '''for i in n:
        if int(i) % 2 != 0:
            return False'''
    b = [0 for i in n if int(i) % 2 != 0]

    return all(False for i in n if int(i) % 2 != 0), b


print(evenDigitsOnly(248622))
