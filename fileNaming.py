def fileNaming(names):
    i = 0
    q = 0
    while i < len(names):
        if names[i] in names[:i]:
            q = 0
            while q < len(names[:i]):
                if (names[i] + "(" + str(q + 1) + ")") in names[:i]:
                    q += 1
                else:
                    break

            names[i] += "(" + str(q + 1) + ")"
            i += 1
        else:
            i += 1
    return names


print(fileNaming(["dd",
                  "dd(1)",
                  "dd(2)",
                  "dd",
                  "dd(1)",
                  "dd(1)(2)",
                  "dd(1)(1)",
                  "dd",
                  "dd(1)"]))
