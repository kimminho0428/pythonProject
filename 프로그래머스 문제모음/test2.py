def solution(M, load):
    answer = 0
    truck = []
    load.sort()

    while len(load):
        truck.append(load.pop(0))
        if sum(truck) >= M:
            answer += 1
        else:
            truck.append(load.pop(0))

    return answer


print(solution(10, [2, 3, 7, 8]))
print(solution(5, [2, 2, 2, 2, 2]))
print(solution(20, [16, 15, 9, 17, 1, 3]))
