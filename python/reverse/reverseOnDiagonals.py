def reverseOnDiagonals(m):
    for i in range(len(m)/2):
        m[i][i],m[len(m)-i-1][len(m) - i -1] = m[len(m) - i -1][len(m) - i -1], m[i][i]
        m[i][len(m) - i -1],m[len(m)-i-1][i] = m[len(m) - i -1][i], m[i][len(m) - i -1]
    return m