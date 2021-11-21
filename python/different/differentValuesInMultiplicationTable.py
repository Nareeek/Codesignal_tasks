# 1
def differentValuesInMultiplicationTable(n, m):
    s = set()
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s.add(i * j)
        
    return len(s)



#2
def differentValuesInMultiplicationTable(n, m):
    result = 0
    for value in range(1, n * m + 1):
        for i in range(1, min(n, m) + 1):
            if value % i == 0 and value / i <= max(n, m):
                result += 1
                break
    return result

# 3
def differentValuesInMultiplicationTable2(n, m):
    s = set()
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s.add(i * j)
        
    return len(s)
