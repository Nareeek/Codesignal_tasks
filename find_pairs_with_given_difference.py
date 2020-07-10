def find_pairs_with_given_difference(arr, k):
  
  def is_valid(current, other):
    return current==other+k
    
  out = []
  
  for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
      if is_valid(arr[i], arr[j]):
        out.append([arr[i],arr[j]])
  
  return out

print(find_pairs_with_given_difference([1,5,11,7], 4))