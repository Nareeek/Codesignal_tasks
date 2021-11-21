# 1
def inversePermutation(permutation):
    p = permutation
    x = [0 for x in range(len(p))]
    
    for i in range(len(p)):
        x[p[i] - 1] = i + 1
    
    return x


# 2
def inversePermutation(permutation):
    l=[]
    for i in range(len(permutation)):
        for j in range(len(permutation)):
            if permutation[j]==i+1:
                l.append(j+1)
    return l
                

# 3
def inversePermutation2(arr, size):  
  x = []
  for i in range(0, size): 
    for j in range(0, size):
      if (arr[j] == i + 1):
        x.append(j+1)
        break
  return x



def inversePermutation(permutation):
  return inversePermutation2(permutation, len(permutation))

