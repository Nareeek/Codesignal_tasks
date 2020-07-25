def rotateImage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

'''
def rotateImage(a):
    return [ list(i) for i in list(zip(*a[::-1]))]

'''

'''
def rotateImage(a):
    a = list(zip(*a))
    
    for i in range(len(a)):
        a[i] = a[i][::-1]    
    
    return a
'''


print(rotateImage([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]))
