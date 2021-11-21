def solution(n, lost, reserve):
    answer = 0
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    return n - len(set_lost)

print(solution(5, [2, 4], [1, 3, 5]	))
print(solution(5, [2, 4], [3]))