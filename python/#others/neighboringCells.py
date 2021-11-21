def neighboringCells(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i > 0):
                matrix[i][j] += 1
            if (j > 0):
                matrix[i][j] += 1
            if (i + 1 < len(matrix)):
                matrix[i][j] += 1
            if (j + 1 < len(matrix[0])):
                matrix[i][j] += 1
    return matrix

# 2
m, = eval(dir()[0])

for _ in ' '*4:
    m = numpy.rot90(m)
    m[1:] += 1

return m

# Add 1 to all rows except first to count
# neighbors directly above. Rotate matrix
# 4 times to count in each direction.