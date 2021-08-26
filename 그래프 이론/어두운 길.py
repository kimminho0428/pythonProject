# 특정한 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트노드를 찾을때까지 재귀적으로 수행
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 특정한 원소가 속한 두 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집과 도로 입력
n, m = map(int, input().split())

# 초기 노드 리스트 초기화
parent = [0] * (n + 1)

# 부모 노드의 초기 노드는 자기자신
for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0
total = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용순으로 오름차순 정렬
edges.sort()

# 노드들을 확인
for edge in edges:
    cost, a, b = edge
    total += cost
    # 사이클이 아닐때만 cost 추가
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total - result)
