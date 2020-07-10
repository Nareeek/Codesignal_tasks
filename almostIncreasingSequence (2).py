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
