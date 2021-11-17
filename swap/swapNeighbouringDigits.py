def swapNeighbouringDigits(n):
    n = str(n)
    List = []
    
    for i in range(0, len(n), 2):
        rev = n[i: i + 2][1] + n[i: i + 2][0]
        List.append(rev)
    res = ''.join(List)
    
    return int(res)
    