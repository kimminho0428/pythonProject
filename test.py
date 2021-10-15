def solution(lottos, win_nums):
    answer = []

    count = 7

    for i in lottos:
        if i == 0:
            count -= 1
        elif i in win_nums:
            count -= 1
    if count > 6:
        answer.append(6)
    else:
        answer.append(count)

    count = 7
    for j in lottos:
        if j in win_nums:
            count -= 1
    if count > 6:
        answer.append(6)
    else:
        answer.append(count)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))