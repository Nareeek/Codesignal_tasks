def nearestGreater(a):
    # run forwards first
    S = [0]
    b = [-1] * len(a)
    i = 1
    while i < len(a):
        while S and a[S[-1]] < a[i]:
            b[S.pop()] = i
        S.append(i)
        i += 1
    # run backwards
    S = [len(a) - 1]
    i = len(a) - 2
    while i >= 0:
        while S and a[S[-1]] < a[i]:
            j = S.pop()
            # check if the forwards pass value doesn't
            # exist or is further away
            if b[j] == -1 or b[j] - j >= j - i:
                b[j] = i
        S.append(i)
        i -= 1
    return b