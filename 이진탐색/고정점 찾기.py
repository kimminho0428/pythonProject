n = int(input())
array = []
for i in range(n-(n-1)):
    array.extend(list(map(int, input().split())))

start = 0
end = len(array)
idx = -1

while start <= end:
    mid = (start + end) // 2
    if array[mid] == mid:
       print(array[mid])
       break
    elif array[mid] < mid:
        start = mid + 1
    elif array[mid] > mid:
        end = mid - 1
print(idx)




