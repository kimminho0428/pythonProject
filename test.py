dish = list(input())
count = 0

for i in range(len(dish)):
    if i == 0:
        count = 10
    elif dish[i] == dish[i-1]:
        count += 5
    else:
        count += 10
print(count)