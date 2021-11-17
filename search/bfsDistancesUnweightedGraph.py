def bfsDistancesUnweightedGraph(matrix, startVertex):

    visited = []
    queue = []
    distance = []

    for i in range(len(matrix)):
        visited.append(False)
        distance.append(0)

    visited[startVertex] = True
    queue.append(startVertex)
    while len(queue) > 0:
        currentVertex = queue.pop(0)
        visited[currentVertex] = True
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                visited[nextVertex] = True
                distance[nextVertex] = 1 + distance[currentVertex]
                queue.append(nextVertex)

    return distance