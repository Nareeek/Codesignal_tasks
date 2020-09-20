def treeDiameter(n, tree):
    
    # get the max depth of the tree from the root (it could be any node, really)
    # then take a node at max depth from the root and find the max depth from that node
    # return the latter
    
    if tree == []:
        return 0
    
    adjacentNodes = {} # node (int) -> list of adjacent nodes (list)
    for item in tree:
        n1, n2 = item[0], item[1]
        if n1 in adjacentNodes:
            adjacentNodes[n1].append(n2)
        else:
            adjacentNodes[n1] = [n2]
        if n2 in adjacentNodes:
            adjacentNodes[n2].append(n1)
        else:
            adjacentNodes[n2] = [n1]
    
    startNode = tree[0][0]
    lst1 = BFS(startNode, adjacentNodes, 0, n)
    
    return BFS(lst1[0], adjacentNodes, 0, n)[1]

    
# returns a list of two elements: [someNodeAtMaxDepth, maxDepth]
def BFS(startNode, adjacentNodes, depth, n):
    
    visited = set()
    visited.add(startNode)
    queue = [[startNode, depth]]
    
    while len(visited) < n:
        item = queue.pop(0)
        for node in adjacentNodes[item[0]]:
            if node not in visited:
                queue.append([node,item[1]+1])
                visited.add(node)
    
    return max(queue, key=lambda item: item[1])