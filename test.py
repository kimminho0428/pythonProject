def solution(numbers, target):
    answer = 0
    # 시작점, 인덱스를 큐에 삽입
    queue = [[numbers[0], 0], [-1 * numbers[0], 0]]
    n = len(numbers)
    while queue:
        tmp, idx = queue.pop()
        idx += 1
        if idx < n:
            # 인덱스 값을 증가시킨 뒤 숫자가 담긴 배열의 크기보다 작으면 노드 +1, 노드 -1을 한 값과 인덱스를 큐에 삽입
            queue.append([tmp + numbers[idx], idx])
            queue.append([tmp - numbers[idx], idx])
        else:
            # 큐에 들어간 노드가 타겟에 도착하면 answer +1이 증가
            if tmp == target:
                answer += 1
    return answer

print(solution([1, 1, 1, 1, 1], 3))

