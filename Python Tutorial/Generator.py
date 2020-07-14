def new(dict):
    for x, y in dict.items():
        yield x, y


a = {1: "HI", 2: "Welcome"}
b = new(a)

print(b)

print(next(b))
print()

print(next(b))
print()

print(next(b))
print()
