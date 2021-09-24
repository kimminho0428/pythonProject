n = int(input())
num = int(input())
board = [[0] * n for _ in range(n)]

# 아래 -> 오른 -> 위 -> 왼
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = [0, 0]
y, x, dirs, cnt = 0, 0, 0, n * n

while True:
    board[y][x] = cnt
    if board[y][x] == num:
        result = [y + 1, x + 1]

    if y == n // 2 and x == n // 2:
        break

    ny, nx = y + dy[dirs], x + dx[dirs]

    # 방향을 바꿔야 하는 경우
    # 1. 범위를 벗어나거나, 이미 방문한 경우
    if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] != 0:
        dirs = (dirs + 1) % 4
        ny, nx = y + dy[dirs], x + dx[dirs]

    cnt -= 1
    y, x = ny, nx

for l in board:
    print(*l)
print(*result)









