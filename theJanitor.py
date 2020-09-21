# 1
def theJanitor(word):

    left = [0] * 26
    right = [0] * 26
    was = [0] * 26
    for i in range(26):
        left.append(0)
        right.append(0)
        was.append(False)

    for i in range(len(word)):
        c = ord(word[i]) - ord('a')
        if not was[c]:
            was[c] = 1
            left[c] = i
        right[c] = i

    ans = []
    for i in range(26):
        ans.append(right[i] - left[i] + 1 if was[i] else 0)
    return ans

# 2
def theJanitor(word):
    z = [0]*26
    for i in set(word):
        z[ord(i)-97] = len(word)-word.index(i)-word[::-1].index(i)
        
    return z

