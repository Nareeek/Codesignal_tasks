# 1
def lineEncoding(s):
    l = []
    L = []
    for i in s:
        S = str(s.count(i)) + i if s.count(i) != 1 else i
        if S not in l:
            l.append(S)

    return "".join(l)


print(lineEncoding("wwwwwwwawwwwwww"))


# 2
def lineEncoding(s):

  s += '#'
  cnt = 1
  result = []
  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      cnt += 1
    else:
      if cnt > 1:
        result.append(str(cnt))
      cnt = 1
      result.append(s[i - 1])

  return ''.join(result)