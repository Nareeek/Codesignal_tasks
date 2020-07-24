def isSumOfConsecutive(n):
    
    for i in range(1, n):
        sum = 0
        
        for j in range(i, n):
            sum += j
            
            if sum == n:
                return True
                
            if sum > n:
                break
    
    return False


'''
def isSumOfConsecutive(n):
    if bin(n).count("1") == 1:
        return False
    
    return True
'''