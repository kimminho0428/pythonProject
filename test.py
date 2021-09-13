def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j+1)
            sub.append(j-1)
        sub = sub

    return sup.count(target)

print(solution([1, 1, 1, 1, 1], 3))