from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 그래프 정보
data = [] # 바이러스 정보

for i in range(n):
    graph.append(list(map(int, input().split())))
    # 바이러스가 존재하면 바이러스 정보 추가
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

# 낮은 번호부터 증식
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 상, 하, 좌, 우 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()

    if s == target_s:
        break
    # 4가지 방향에서 추가
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
print(graph[target_x-1][target_y-1])






