import heapq

def solution(operations):
    heap = []

    for operation in operations:
        o = operation.split(' ')  # 명령어 값 분리하여 저장

        # 명령어에 따라 처리하는 부분
        if o[0] == 'I':
            heapq.heappush(heap, int(o[1]))  # 명령어가 'I 숫자'인 경우
        else:
            if len(heap) > 0:
                # 명령어가 'D 1'인 경우
                if o[1] == '1':
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                # 명령어가 'D -1'인 경우
                else:
                    heapq.heappop(heap)

    # 최대값, 최소값 리턴
    if heap:
        return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
    else:
        return [0, 0]

    # heapq.nlargest(n , iterable) : 데이터 집합(iterable)에서 n개의 가장 큰 요소로 구성된 리스트를 반환
    # heapq.nsmallest(n, iterable) : 데이터 집합(iterable)에서 n개의 가장 작은 요소로 구성된 리스트를 반환


print(solution(["I 7", "I 5", "I -5", "D -1"]))
