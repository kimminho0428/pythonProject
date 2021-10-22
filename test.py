def solution(phone_number):
    answer = 0

    if len(phone_number) == 11 and phone_number not in '-' and phone_number[0] in '0' and phone_number[1] in '1' \
            and phone_number[2] in '0':
        answer = 2
    elif len(phone_number) == 13 and phone_number[3] in '-' and phone_number[8] in '-':
        answer = 1
    elif len(phone_number) == 16 and phone_number[0] in '+' and phone_number[1] in '8' and phone_number[2] in '2'\
            and phone_number[3] in '-' and phone_number[4] in '1' and phone_number[5] in '0' and phone_number[6] in '-'\
            and phone_number[11] in '-':
        answer = 3
    else:
        answer = -1

    return answer

print(solution("01012345678"))
print(solution("010-1212-3333"))
print(solution("+82-10-3434-2323"))
print(solution("+82-010-3434-2323"))

