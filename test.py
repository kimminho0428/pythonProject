def solution(n, computers):
    answer = 0  # 네트워크의 개수를 저장할 변수
    # 탐색을 위한 큐
    bfs = []
    # 방문한 노드를 체크해 둘 리스트
    visited = [0] * n
    while 0 in visited:
        x = visited.index(0)
        # 큐에 첫 노드 추가
        bfs.append(x)
        # 첫 노드 방문 표시
        visited[x] = 1

        # 큐가 값이 존재하면 반복문 수행
        while bfs:
            # 큐의 앞에서부터 노드(인덱스) 꺼내기
            node = bfs.pop(0)
            visited[node] = 1

            # 꺼낸 노드의 인접 노드를 방문하기 위한 반복문 수행
            for i in range(n):
                # 인접 노드이고, 방문한 적이 없는 경우
                if visited[i] == 0 and computers[node][i] == 1:
                    # 큐에 추가
                    bfs.append(i)
                    # 방문했음을 표시
                    visited[i] = 1
        answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))