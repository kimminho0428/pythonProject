n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))
dap = 1
for i in range(n - 1):
    for j in range(m - 1):
        k = 1
        while 1:
            if (i + k) == n or (j + k) == m:
                break
            if data[i][j] == data[i + k][j] and data[i][j] == data[i][j + k] and data[i][j] == data[i + k][j + k]:
                dap = max(dap, (k + 1) * (k + 1))
            k += 1
print(dap)
