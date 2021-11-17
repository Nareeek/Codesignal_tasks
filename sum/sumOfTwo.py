def sumOfTwo(a, b, v):
    d = {}
    for i in range(len(a)):
        d[v - a[i]] = 1
    for i in range(len(b)):
        if b[i] in d:
            return True
    return False


a = [1, 2, 3]
b = [10, 20, 30, 40]
v = 42

print(sumOfTwo(a, b, v))
print()
