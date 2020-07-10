def get_shortest_unique_substring(arr, str):
  
  string = str
  
  s = 0
  S = 0
  
  if len(string) == 0:
    return ""
  if len(arr) == 1:
    if len(string) == 1:
      if string[0] == arr[0]:
        return string[0]
      else:
        return ""
      

  
  for i in arr:
    s += ord(i)
  print(s)
  for i in range(len(string) - len(arr)):
    S = sum((map(ord, string[i: i + len(arr)])))

    if S == s:
      return string[i: i + len(arr)]
    
    
    
    
    
print(get_shortest_unique_substring(["A","B","C"], "ADOBECODEBANCDDD"))