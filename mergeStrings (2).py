def mergeStrings(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    t = []

    while len(s1) != 0 or len(s2) != 0:
        if len(s1) > 0 or len(s2) > 0:
            if s1.count(s1[0]) < s2.count(s2[0]):
                t.append(s1[0])
                s1.remove(s1[0])
            elif s1.count(s1[0]) > s2.count(s2[0]):
                t.append(s2[0])
                s2.remove(s2[0])
            else:
                if ord(s1[0]) <= ord(s2[0]):
                    t.append(s1[0])
                    s1.remove(s1[0])
                else:
                    t.append(s2[0])
                    s2.remove(s2[0])
        if len(s1) == 0:
            for i in range(len(s2)):
                t.append(s2[0])
            break
        elif len(s2) == 0:
            for i in range(len(s1)):
                t.append(s1[i])
            break
    t = "".join(t)
    return t


print(mergeStrings("ougtaleegvrabhugzyx", "wvieaqgaegbxg"))
