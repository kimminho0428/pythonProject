array = []
for i in range(1, 10):
    array.append(int(input()))
print(max(array))
print(array.index(max(array)) + 1)
