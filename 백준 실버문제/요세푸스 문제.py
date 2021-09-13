import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n + 1))
result = "<"
cnt = 0
while q:
    cnt += 1
    # k의 배수번째가 될때
    if cnt % k == 0:
        result += str(q.popleft()) + ", "
    else:
        q.append(q.popleft())

result = result[:-2] + ">"
print(result)

