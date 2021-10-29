def dfs(x, y, graph):
    if x <= -1 or x >= len(graph) or y <= -1 or y >= len(graph):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

    result = 0
    for i in range(x):
        for j in range(y):
            if dfs(i, j) == True:
                result += 1

print(dfs(3, 3, [[0, 0, 1], [0, 1, 0], [1, 0, 1]]))

