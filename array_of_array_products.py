def array_of_array_products(arr):
  length = len(arr)
  if (length == 0) or (length == 1):
    return []
  
  productArr = []
  product = 1
  
  for i in range(length):
    productArr.append(product)
    product *= arr[i]
    
  product = 1
  
  for i in range(length - 1, -1, -1):
    productArr[i] *= product
    product *= arr[i]
    
  return productArr
    

print(array_of_array_products([2,2]))