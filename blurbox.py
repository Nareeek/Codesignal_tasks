image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]
nn = []
nar = []
for i in range(len(image) - 2):
    for j in range(len(image[0]) - 2):
        nar1 = image[i][j] + image[i][j + 1] + image[i][j + 2]
        nar2 = image[i + 1][j] + image[i + 1][j + 1] + image[i + 1][j + 2]
        nar3 = image[i + 2][j] + image[i + 2][j + 1] + image[i + 2][j + 2]
        nn.append((nar1 + nar2 + nar3) // 9)
    nar.append(nn)
    nn = []

print(nar)
