def solution(priorities, location):
    loc = [i for i in range(len(priorities))]
    final_loc = []

    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            final_loc.append(loc.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))

    return final_loc.index(location) + 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
