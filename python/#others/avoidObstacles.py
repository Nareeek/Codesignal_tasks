def avoidObstacles(inputArray):
    c = 2
    while 1:
        inp = (i % c for i in inputArray)
        if sorted(inp)[0] > 0:
            return c
        c += 1
        

print(avoidObstacles([5, 3, 6, 7, 9]))