def solution(lottos, win_nums):
    answer = []
    count = 7

    # 지워진 숫자(0)가 모두 맞을 경우(최고 순위)
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

    # 지워진 숫자가 모두 틀릴 경우(최저 순위)
    for j in lottos:
        if j in win_nums:
            count -= 1
    if count > 6:
        answer.append(6)
    else:
        answer.append(count)

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
