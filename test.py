import heapq

def solution(operations):
    heap = []
    for operation in operations:
        o = operation.split(' ')

        if o[0] == 'I':
            heapq.heappush(heap, int(o[1]))
        else:
            if len(heap) > 0:
                if o[1] == '1':
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                else:
                    heapq.heappop(heap)

    if heap:
        return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
    else:
        return [0, 0]


print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I 16", "D 1"]))
