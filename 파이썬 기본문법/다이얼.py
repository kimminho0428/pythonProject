# 다이얼 넘버
Dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# 알파벳 입력
alpha = list(input())

# 걸리는 시간
result = 0
for i in alpha:
    for j in Dial:
        # 만약에 입력받은 값이 Dial에 있으면 index에서 3초를 더해준다.
        if i in j:
            result += Dial.index(j) + 3
print(result)


