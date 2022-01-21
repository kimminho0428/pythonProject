n, m = map(int, input().split())
datas = []
result = 0
for i in range(n):
    datas.append(list(map(int, input().split())))

for data in datas:
    data.sort()
    result = max(result, data[0])

print(result)