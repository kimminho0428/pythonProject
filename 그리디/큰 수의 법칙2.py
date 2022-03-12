import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]
count = 0
sum = 0

for i in range(m):
    if count != k:
        count += 1
        sum += first

    else:
        sum += second
        count = 0

print(sum)