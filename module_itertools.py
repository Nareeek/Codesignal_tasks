from itertools import islice
from itertools import count, cycle, repeat  # infinite iterators
from itertools import dropwhile, takewhile  # similar to infinite iterators (return iterator not a list)...
from itertools import chain
from itertools import tee  # copy the given iterator n times
from itertools import product, permutations
from itertools import combinations, combinations_with_replacement

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

print()

# chain
print("chain: ")

a = take(5, chain(range(2), range(5, 10)))
print(a)

print()

# concatenate two iterators (from_iterable)
print("chain:from_iterable: ")

it = (range(x, x ** x) for x in range(2, 4))
a = take(12, chain.from_iterable(it))
print(a)

print()

# tee - create a copy of given iterators
print("tee: copy iterator")

it = range(3)
a, b, c = tee(it, 3)

print(list(a))
print(list(b))
print(list(c))

print()

# don't use iterator itself after copy
print("using iterator after copy:")

it = iter(range(3))
a, b = tee(it, 2)
used = list(it)

print("a: ", list(a))
print("b: ", list(b))
print("used: ", used)

print()

# use iterable (not iterator) for tee
print("using iterable (not iterator) for every iterators:")

it = range(3)
a, b = tee(it, 2)
used = list(it)

print("a: ", list(a))
print("b: ", list(b))
print("used: ", used)

print()

# combinations

print("product:")
a = product("ABC", repeat=2)
print("ABC: ", list(a))

b = product("AB", repeat=3)
print("AB: ", list(b))

print()

print("permutation: ")
a = permutations("AB")
print(list(a))

print()

print("combinations: ")
a = combinations("ABC", 2)
print("ABC: ", list(a))

print()

print("combinations with replacement: ")
b = combinations_with_replacement("ABC", 2)
print("ABC: ", list(b))
