def lineEncoding(s):
    l = []
    L = []
    for i in s:
        S = str(s.count(i)) + i if s.count(i) != 1 else i
        if S not in l:
            l.append(S)

    return "".join(l)


print(lineEncoding("wwwwwwwawwwwwww"))
