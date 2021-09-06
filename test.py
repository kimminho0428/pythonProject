def solution(record):
    answer = []
    dic = {}

    for sentence in record:
        # 뮨장을 띄어쓰기별로 구분
        sentence_split = sentence.split()
        # 띄어쓰기가 3개이면 고유아이디(uid)와 닉네임을 딕셔너리에 저장
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]

    for sentence in record:
        sentence_split = sentence.split()
        # Enter와 Leave일때 딕셔너리에 있는 닉네임을 불러와 출력
        if sentence_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dic[sentence_split[1]])
        elif sentence_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dic[sentence_split[1]])

    return(answer)
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))