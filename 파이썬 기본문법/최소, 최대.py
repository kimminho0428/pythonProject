n = int(input())
array = []
for i in range(n - (n - 1)):
    array.extend(list(map(int, input().split())))
print(min(array), end=' ')
print(max(array))