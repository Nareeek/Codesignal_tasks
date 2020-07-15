from collections import Counter


def stringsConstruction(a, b):
    a, b = Counter(a), Counter(b)
    s = 0

    def check(b):
        s = 0
        for k in a:
            if k not in b:
                return False
            else:
                s += 1
                b[k] -= 1

            if b[k] < 1:
                del b[k]
        return s == len(a)

    while b:
        c = check(b)
        if not c:
            return s
        else:
            s += c

    return s


print(stringsConstruction("abc", "abccba"))
