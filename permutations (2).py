from itertools import permutations as p


inp = list(range(6))
q = 0
for z in p(inp):
    q += 1
    print(q, end = ") (")