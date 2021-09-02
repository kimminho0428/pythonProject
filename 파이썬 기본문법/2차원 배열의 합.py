# 누적합 풀이
n, m = map(int, input().split())
array = []
dp = [[0] * (m + 1) for _ in range(n+1)]
for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        # print(array[i-1][j-1], dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        # dp[i-1][j-1]은 dp[i][j-1]과 dp[i-1][j]의 누적합을 구할 때 사용됐으므로
        # 2번 더해지므로 한번 빼줌 (본래값 + 왼쪽 + 위쪽 - 대각선)
        dp[i][j] = array[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    # dp[x][j=1]과 dp[i-1][y]에서 겹치는 부분 dp[i-1][j-1] 더해주기
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])