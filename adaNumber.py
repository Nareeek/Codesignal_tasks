def adaNumber(line):
    l = line.replace('_', '')
    n = l
    b = 10
    
    try:
        if '#' in l:
            a = l.split('#')
            if len(a) != 3:
                return False
            n = a[1]
            b = int(a[0])
            if b < 1 or b > 16:
                return False
    except:
        return False
        
    try:
        n = int(n, b)
        return True
    except:
        return False


a = []

a += 4,
a += 5,
print(a)