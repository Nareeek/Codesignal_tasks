def doubleSwap(t, a, b):
    d = {a:b, b:a}
    List = []
    for x in t:
        List.append(d.get(x, x))
    return ''.join(List)



print(doubleSwap("aabbcccaqabb", "a", "b"))