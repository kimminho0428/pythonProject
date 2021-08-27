n = int(input())

list = [i + 1 for i in range(n)]
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()
