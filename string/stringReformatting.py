def stringReformatting(s, k):
    s = s.split('-')
    s = ''.join(s)
    s = s[::-1]
    p = ''
    while len(s) > 0:
        p += s[:k] + '-'
        s = s[k:]
    return p[:-1][::-1]