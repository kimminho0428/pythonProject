n = int(input())
array = []
for i in range(n):
    num = int(input())
    if num == 0:
        array.pop()
    else:
        array.append(num)
print(sum(array))