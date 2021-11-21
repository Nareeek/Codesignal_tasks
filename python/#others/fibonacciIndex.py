def fibonacciIndex(n):

  a = 0
  b = 1
  i = 0
  while len(str(a)) < n:
    c = a + b
    a = b
    b = c
    i += 1

  return i