def efficientRoadNetwork(n, roads):
    dist = [[4] * n for x in range(n)]
    
    for x in range(n):
        dist[x][x] = 0
    for x, y in roads:
        dist[x][y] = 1
        dist[y][x] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(n):
        for j in range(n):
            if dist[i][j] >= 3:
                return False
    return True
