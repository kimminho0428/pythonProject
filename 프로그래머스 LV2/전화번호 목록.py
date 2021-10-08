def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # phone_book 배열에 첫번째 문자열이 두번째 문자열보다 작아야한다.
        if len(phone_book[i]) < len(phone_book[i+1]):
            # 두번째 문자열에서 첫번째 문자열의 길이만큼 비교할 때 같으면 False 출력 후 for문 종료
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))