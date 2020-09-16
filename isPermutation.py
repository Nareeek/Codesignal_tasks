# 1
def isPermutation(n, inputArray):

    countOccurences = []

    for i in range(n):
        countOccurences.append(0)

    for i in range(0, len(inputArray)):
        if inputArray[i] - 1 < 0 or inputArray[i] - 1 >= n:
            return False
        countOccurences[ inputArray[i] - 1 ] += 1

    for i in range(n):
        if countOccurences[i] != 1:
            return False
    return True



# 2
def isPermutation(n, inputArray):
  for i in range(1,n+1):
    if i not in inputArray:
      return False
  return True