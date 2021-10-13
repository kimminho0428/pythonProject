def solution(s):
    answer = s
    answer = answer.replace("zero", "0")
    answer = answer.replace("one", "1")
    answer = answer.replace("two", "2")
    answer = answer.replace("three", "3")
    answer = answer.replace("four", "4")
    answer = answer.replace("five", "5")
    answer = answer.replace("six", "6")
    answer = answer.replace("seven", "7")
    answer = answer.replace("eight", "8")
    answer = answer.replace("nine", "9")

    # 2번째 방법
    num_s = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
             'nine': 9}

    for item in num_s.items():
        answer = answer.replace(item[0], str(item[1]))

    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))