n, m = list(map(int, input().split()))
arr = []
arr.extend(list(map(int, input().split())))
print(arr)
count = 0
for i in range(n - 1):
    if (i <= (n - 2)):
        for k in range(i, n):
            if (arr[i] != arr[k]):
                count += 1
            elif (arr[i] == arr[k]):
                count += 0
            else:
                break
print(count)
