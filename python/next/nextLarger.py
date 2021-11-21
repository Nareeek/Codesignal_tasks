import time

def nextLarger(a):
    start = time.process_time()
    rev = reversed(a)
    seen = [-1]
    temp = []
    
    for num in rev:
        for c in seen:
            if c > num:
                temp = [c] + temp
                break
        else:
            temp = [-1] + temp
            
        if num in seen:
            seen.remove(num)
            
        seen = [num] + seen
    
    end = time.process_time()
    
    print(end - start)
    
    return temp

#print(nextLarger(range(10000)[::-1]))

print(nextLarger([6, 7, 7, 3, 8, 5, 6, 10, 25])) # [7, 8, 8, 8, 10, 6, 10, 25, -1]
print(nextLarger([6, 7, 3, 8])) # [7, 8, 8, -1]

