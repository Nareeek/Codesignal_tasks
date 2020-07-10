def candles1(candlesNumber, makeNew):
    n = candlesNumber
    m_N = makeNew
    
    s = 0
    left = 0
    
    while n > 0:
        s += n
        if left // m_N:
            s += 1
            left %= m_N
            
        left += n % m_N
        n //= m_N
    
    return s
     


def candles2(candlesNumber, makeNew):
    return candlesNumber + (candlesNumber - 1) // (makeNew - 1)


print(candles1(7, 2))

'''
dic = {}

for i in range(1, 16):
    for j in range(2, 6):
        c1 = candles1(i, j)
        c2 = candles2(i, j)
        
        if c1 == c2:
            dic[(i,j)] = True
        else:
            dic[(i,j)] = (c1, c2)
q = 0
for i in dic:
    if dic[i] != True:
        q += 1
        print(i)
        print(dic[i])

print(q)
'''