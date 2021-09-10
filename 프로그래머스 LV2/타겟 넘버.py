# stack을 이용한 dfs여도 마찬가지!
def solution(numbers, target):
    answer = 0
    # 시작점, 인덱스를 큐에 삽입
    queue = [[numbers[0], 0], [-1 * numbers[0], 0]]
    n = len(numbers)
    while queue:
        # 인덱스 값을 증가시킨 뒤 숫자가 담긴 배열의 크기보다 작으면 노드 +1, 노드 -1을 한 값과 인덱스를 큐에 삽입
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

print(solution([1, 1, 1, 1, 1], 3))