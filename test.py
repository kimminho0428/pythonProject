def solution(answers):
    # 가장 많은 문제를 맞힌 사람을 나타내는 리스트
    answer = []
    # 수포자 1
    answer1 = [1, 2, 3, 4, 5]
    # 수포자 2
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # 수포자 3
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자가 맞은 수를 기록하는 배열
    cnt = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == answer1[i % 5]:
            cnt[0] += 1
        if answers[i] == answer2[i % 5]:
            cnt[1] += 1
        if answers[i] == answer3[i % 10]:
            cnt[2] += 1

    max_cnt = max(cnt)

    for i in range(3):
        if max_cnt == cnt[i]:
            answer.append(i+1)

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
