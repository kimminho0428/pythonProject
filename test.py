def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) > 1:
            answer += 1
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + 2 * second)
        else:
            return -1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
