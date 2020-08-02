# 1
def almostIncreasingSequence(s):
    while len(s) != 0 and s[:len(s) // 2] == sorted(set(s[:len(s) // 2])):
        s = s[len(s) // 2:]

    while len(s) != 0 and s[len(s) // 2:] == sorted(set(s[len(s) // 2:])):
        s = s[:len(s) // 2]

    for i in range(len(s)):
        if s[:i] + s[i + 1:] == sorted(set(s[:i] + s[i + 1:])):
            return True

    return False if len(s) != 0 else True


print(almostIncreasingSequence([1, 3, 5, 4, 80, 100, 120, 140, 141, 1200, 12544, 12121211]))


# 2
def almostIncreasingSequence(sequence):
    found = False
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            if found:
                return False
            found = True

            if i == 1 or i == len(sequence) - 1:
                continue
            elif sequence[i] > sequence[i - 2]:
                sequence[i - 1] = sequence[i - 2]
            elif sequence[i - 1] >= sequence[i + 1]:
                return False

    return True


print(almostIncreasingSequence([0, -2, 5, 6]))


# 3
def is_strictly_increasing(List):
    for i in range(1, len(List)):
        if List[i] <= List[i - 1]:
            return False
    return True


def almostIncreasingSequence(s):
    q = 0
    for i in range(len(s)):
        if is_strictly_increasing(s[:i] + s[i + 1:]):
            q += 1
    print(q)
    return q == 1


print(almostIncreasingSequence([0, -2, 5, 6]))
