def solution(phone_number):
    answer = 0

    for i in phone_number:

        if len(phone_number) == 11:
            answer = 1
        elif len(phone_number) == 13:
            answer = 2
        elif phone_number == "+82-10-" and len(phone_number) == 16:
            answer = 3
        else:
            answer = -1

    return answer


print(solution("01012345678"))
print(solution("010-1212-333"))
print(solution("+82-10-3434-2323"))
print(solution("+82-010-3434-2323"))


