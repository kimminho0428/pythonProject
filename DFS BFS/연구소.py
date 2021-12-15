import sys
import copy

# sys.setrecursionlimit(10000)
# sys.stdin = open('./test.txt', 'r')
input = sys.stdin.readline

n, m = 0, 0
data = []
result = 0
virusList = []
# 아래, 위, 오른쪽, 왼쪽
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 모든 방향으로 바이러스 전파
def virus(x, y, copyed):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if copyed[nx][ny] == 0:
                # 해당 위치에 바이러스 배치 하고, 다시 재귀적으로 수행
                copyed[nx][ny] = 2
                virus(nx, ny, copyed)


# 안전 영역 크기 계산
def safe(temp):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt


def dfs(start, depth):
    global result
    # 울타리가 3개 설치된 경우
    if depth == 3:
        # data를 temp에 넣어주고
        temp = copy.deepcopy(data)

        # 바이러스를 퍼트린 다음
        for i in range(len(virusList)):
            [virusX, virusY] = virusList[i]
            virus(virusX, virusY, temp)

        # 안전한 영역을 계산
        result = max(result, safe(temp))
        return

    # 2차원 배열에서 숫자를 0부터 n * m 까지 증가시킬 때 (i/m), (i % m)을 좌표로 하면 2차원 배열의 모든 인덱스를 탐색
    for i in range(start, n * m):
        x = (int)(i / m)
        y = (int)(i % m)

        if data[x][y] == 0:
            data[x][y] = 1
            dfs(i + 1, depth + 1)
            data[x][y] = 0

# if __name__=="__main__"이라는 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 실행되길 원하는 코드들을 넣어주는 것
if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        data.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if data[i][j] == 2:
                virusList.append([i, j])

dfs(0, 0)
print(result)