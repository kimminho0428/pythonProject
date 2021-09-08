def solution(msg):
    answer = []
    dic = {}

    # A부터 Z까지 딕셔너리에 추가
    for i in range(26):
        dic[chr(65 + i)] = i + 1

    # 딕셔너리에 없는 단어이면 새롭게 추가, 마지막 단어는 바로 answer에 append하고 종료
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break

        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c


    return answer

print(solution('ABABABABABABABAB'))