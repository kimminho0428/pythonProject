def solution(number, k):
    answer = []  # Stack(스택)

    for num in number:
        # 스택에서 제거해야할 수가 0이상, 스택에서 가장 뒤에 자리의 수가 현재 주어진 수보다 작으면 그 수를 제거한다.
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        # 스택에서 가장 작은 수를 제거하면 나머지는 다 더해준다.
        answer.append(num)

    # 문자열인 스택에서 제거해야할 k만 제외 후 문자열로 조인
    return ''.join(answer[:len(answer) - k])

print(solution("1924", 2))