def areFollowingPatterns(strings, patterns):
    hash1 = dict()
    hash2 = dict()

    for i, (x, y) in enumerate(zip(strings, patterns)):
        try:
            p1 = hash1[x]
        except:
            p1 = i
            hash1[x] = i
        try:
            p2 = hash2[y]
        except:
            p2 = i
            hash2[y] = i
        if p1 != p2:
            return False

    return True


print(areFollowingPatterns(["a", "b", "a", "a", "c"], ["a", "b", "a", "c", "a"]))
