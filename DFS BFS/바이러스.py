n = int(input()) # 컴퓨터 수
m = int(input()) # 연결된 쌍의 수

maps = [[0] * n for _ in range(n)]
visited = [False] * n


def go(x):
    global count
    # 컴퓨터 수에서
    for i in range(n):
        if maps[x][i] == 1 and not visited[i]:
            visited[i] = True

            count += 1
            go(i)


for i in range(m):
    w, h = map(int, input().split(' '))
    maps[w - 1][h - 1] = 1
    maps[h - 1][w - 1] = 1

count = 0
visited[0] = True
go(0)
print(count)