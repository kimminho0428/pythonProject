import sys
import copy

input = sys.stdin.readline

n, m = 0, 0
data = []
result = 0
virusList = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y, copyed):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if copyed[nx][ny] == 0:
                copyed[nx][ny] = 2
                virus(nx, ny, copyed)



def safe(temp):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1

    return cnt

def dfs(start, depth):
    global result

    if depth == 3:
        temp = copy.deepcopy(data)

        for i in range(len(virusList)):
            [virusX, virusY] = virusList[i]
            virus(virusX, virusY, temp)

        result = max(result, safe(temp))
        return

    for i in range(start, n * m):
        x = (int)(i / m)
        y = (int)(i % m)
        if data[x][y] == 0:
            data[x][y] = 1
            dfs(i + 1, depth + 1)
            data[x][y] = 0


if __name__=="__main__":
    n, m = map(int, input().split())
    for i in range(n):
        data.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if data[i][j] == 2:
                virusList.append([i, j])

dfs(0, 0)
print(result)