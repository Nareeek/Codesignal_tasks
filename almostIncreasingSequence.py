def almostIncreasingSequence(s):
    while len(s) != 0 and s[:len(s) // 2] == sorted(set(s[:len(s) // 2])):
        s = s[len(s) // 2:]

    while len(s) != 0 and s[len(s) // 2:] == sorted(set(s[len(s) // 2:])):
        s = s[:len(s) // 2]

    for i in range(len(s)):
        if s[:i] + s[i + 1:] == sorted(set(s[:i] + s[i + 1:])):
            return True

    return False if len(s) != 0 else True


print(almostIncreasingSequence([1, 3, 5, 1, 80, 100, 120, 140, 141, 1200, 12544, 12121211]))
