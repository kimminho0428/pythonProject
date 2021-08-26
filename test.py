# 개미 입력
n1, n2 = map(int, input().split())
ants1 = list(input())
ants2 = list(input())
dir = {}
t = int(input())

for ant in ants1:
    dir[ant] = 0
for ant in ants2:
    dir[ant] = 1

ants1.reverse()
ants1.extend(ants2)

for _ in range(t):
    i = 0
    while i < len(ants1) - 1:
        if dir[ants1[i]] == 0 and dir[ants1[i+1]] == 1:
            ants1[i], ants1[i+1] = ants1[i+1], ants1[i]
            i += 1
        i += 1

for ant in ants1:
    print(ant, end='')