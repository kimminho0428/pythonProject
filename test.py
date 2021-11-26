def solution(number, k):
    answer = []

    for num in number:
        if k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)


    return ''.join(answer[:len(answer) - k])

print(solution("1924", 2))