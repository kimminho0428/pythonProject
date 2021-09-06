n = int(input())

for _ in range(n):
    arr = list(map(list, input().split()))
    for i in arr:
        print("".join(i[::-1]), end=" ")