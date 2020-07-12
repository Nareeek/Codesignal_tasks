from itertools import islice
from itertools import count, cycle, repeat  # infinite iterators
from itertools import dropwhile, takewhile  # similar to infinite iterators (return iterator not a list)...

xs = range(10)
a = list(islice(xs, 3))
b = list(islice(xs, 3, None))
c = list(islice(xs, 3, 8, 2))

# islice
print("islice:")

print(a)  # xs[:3]
print(b)  # xs[3:]
print(c)  # xs[3:8:2]


def take(n, iterable):
    return list(islice(iterable, n))


d = list(take(3, (range(10))))
print(d)

print()

# infinite iterators
print("infinite iterators:")

a = take(3, count(0, 5))
b = take(3, cycle([1, 2, 3]))
c1 = take(3, repeat(42))
c2 = take(3, repeat(42, 2))  # not infinite

print(a)
print(b)
print(c1)
print(c2)

print()

# similar infinite iterators, return iterators
print("dropwhile-takewile:")

a = list(dropwhile(lambda x: x < 5, range(10)))
b = list(takewhile(lambda x: x < 5, range(10)))

print(a)
print(b)
