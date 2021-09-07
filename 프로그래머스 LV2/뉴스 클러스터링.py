from collections import Counter

def solution(str1, str2):
    # 대문자, 소문자를 따로 구분하지 않으므로 전부 소문자로 구성
    str1_low = str1.lower()
    str2_low = str2.lower()
    str1_lst = []
    str2_lst = []

    # 문자열을 2개를 확인하면서 알파벳인지 체크
    for i in range(len(str1_low) - 1):
        if str1_low[i].isalpha() and str1_low[i + 1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i + 1])
    for j in range(len(str2_low) - 1):
        if str2_low[j].isalpha() and str2_low[j + 1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j + 1])

    # 각 문자열의 개수를 key, value 형태의 딕셔너리 형태로 카운트
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    # 원소값만 추출해 하나의 집합으로 만든다
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    # 유사도를 계산
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))