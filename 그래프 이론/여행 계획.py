# 특정한 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을때까지 재귀함수 수행
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 특정한 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 수와 여행 계획에 속한 도시의 수 입력
n, m = map(int, input().split())
parent = [0] * (n + 1)

# 부모 노드를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# union 연산을 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        # 합집합 연산을 수행
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력받기
plan = list(map(int, input().split()))

result = True
# 여행계획에 속하는 모든 노드가 루트가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

if result:
    print("YES")
else:
    print("NO")
