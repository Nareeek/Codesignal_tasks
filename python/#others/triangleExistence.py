def triangleExistence(sides):
    return max(sides)<sum(sides)-max(sides)

def triangleExistence(a):
    a.sort()
    return a[0] + a[1] > a[2]
    
