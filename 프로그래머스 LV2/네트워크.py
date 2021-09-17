def solution(n, computers):
    # 1
    answer = 0  # 네트워크의 개수를 저장할 변수
    bfs = []  # 탐색을 위한 큐
    visited = [0] * n  # 방문한 노드를 체크해 둘 리스트

    # 2
    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)  # 큐에 첫 노드(인덱스) 추가
        visited[x] = 1  # 첫 노드 방문 표시

        # 3
        while bfs:  # 큐가 값이 존재하면 반복문 수행

            # 3-1
            node = bfs.pop(0)  # 큐의 앞에서부터 노드(인덱스) 꺼내기
            visited[node] = 1

            # 3-2
            for i in range(n):  # 꺼낸 노드의 인접 노드를 방문하기 위한 반복문 수행
                # 3-2-1
                if visited[i] == 0 and computers[node][i] == 1:  # 인접 노드이고, 방문된 적이 없는 경우
                    bfs.append(i)  # 큐에 추가
                    visited[i] = 1  # 방문했음을 표시
        answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))