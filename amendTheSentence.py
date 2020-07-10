def amendTheSentence(s):
    s = list(s);
    a = []

    for i in range(len(s)):
        if s[i].isupper():
            a.append(i)
            s[i] = s[i].lower()

    ss = list(s)
    i = 0
    j = -1 if a[0] == 0 else 0

    while i < len(a):
        if a[i] != 0:
            ss.insert(a[i] + j, ".")
            j += 1;
            i += 1
        else:
            j += 1;
            i += 1

    return " ".join("".join(ss).split("."))


print(amendTheSentence("codesignalIsAwesome"))
