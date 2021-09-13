from collections import deque
n, k = map(int, input().split())
q = deque(range(1, n+1))
cnt = 0
result = "<"
while q:
    cnt += 1
    if cnt % k == 0:
        result += str(q.popleft()) + ", "
    else:
        q.append(q.popleft())
result = result[:-2] + ">"
print(result)