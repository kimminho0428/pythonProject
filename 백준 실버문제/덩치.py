n = int(input())
array = []
for _ in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

for i in array:
    rank = 1
    for j in array:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

