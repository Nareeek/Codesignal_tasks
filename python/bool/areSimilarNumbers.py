# 1
def areSimilarNumbers(a, b, divisor):
    return (a % divisor == b % divisor == 0) or (a % divisor != 0 and b % divisor != 0)
 
 
# 2
def areSimilarNumbers(a, b, divisor):
    if (a % divisor == 0 and b % divisor == 0
      or a % divisor != 0 and b % divisor != 0):
        return True
    return False
