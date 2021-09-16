# 첫째줄에 A, P를 입력합니다.
A, P = map(int, input().split())

# 수열 D를 리스트 변수로 선언합니다.
# 처음엔 A로 시작하므로 A를 넣어줍니다.
D = [A]

# 수열 D의 인덱스를 저장하는 변수를 선언합니다.
# 0부터 시작하므로 0으로 초기화합니다.
index = 0

# 똑같은 숫자가 나올 때까지 반복합니다.
while True:
    # 수열 D에서 현재 인덱스의 숫자를 문자열 형태로 저장하는 변수를 선언합니다.
    current = str(D[index])
    # 다음에 들어올 숫자를 저장할 변수를 선언합니다.
    next = 0

    # 다음 숫자를 구하기 위해 현재 숫자의 각 자리수를 반복해줍니다.
    for position_num in current:
        # 다음 숫자 변수에 현재 자리수의 P제곱을 더해줍니다.
        next += int(position_num) ** P

    # 수열 D에 다음 숫자를 넣어줍니다.
    D.append(next)

    # 수열 D에서 들어온 숫자가 반복된다면
    if D.count(next) == 2:
        # 이번엔 들어온 숫자의 인덱스를 저장하는 변수를 선언합니다.
        next_index = D.index(next)
        # 수열 D에서 이번에 들어온 숫자와 똑같은 숫자의 이전까지의 길이를 출력합니다.
        print(len(D[:next_index]))
        # 반복문을 탈출합니다.
        break

    # 인덱스에 1을 더해줍니다.
    index += 1