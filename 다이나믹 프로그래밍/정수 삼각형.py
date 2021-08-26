n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_down = 0
        else:
            left_down = dp[i-1][j-1]

        if j == i:
            right_down = 0
        else:
            right_down = dp[i-1][j]

        dp[i][j] = dp[i][j] + max(left_down, right_down)

print(max(dp[n-1]))

