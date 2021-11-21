def countInversions(a):
  return mergesort(a)[1] % (1e9 + 7)

def mergesort(a):
  if len(a) < 2: return a, 0
  left,  linvs = mergesort(a[:len(a)//2])
  right, rinvs = mergesort(a[len(a)//2:])
  res, invs = merge(left, right)
  return res, linvs + invs + rinvs

def merge(left, right):
  res, invs = [], 0
  while left and right:
    if left[0] <= right[0]: res += [left.pop(0)]
    else:
      res += [right.pop(0)]
      invs += len(left)
  return res + left + right, invs

