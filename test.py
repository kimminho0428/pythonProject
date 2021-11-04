def solution(N, number):
    dp = [[]]
    for i in range(1, 9):
        temp = []
        for j in range(1, i):
            # j번 사용한 경우의 수 원소 iteration
            for k in dp[j]:
                # i-j번 사용한 경우의 수 원소 iteration
                for l in dp[i - j]:
                    # 더하기
                    temp.append(k + l)
                    if k - l >= 0:
                        # 빼기
                        temp.append(k - l)
                    # 곱하기
                    temp.append(k * l)
                    if l != 0 and k != 0:
                        # 나누기
                        temp.append(k // l)

        # 숫자를 그대로 이어 붙인 케이스
        temp.append(int(str(N) * i))
        if number in temp:
            return i
        dp.append(list(set(temp)))
    return -1

print(solution(5, 12))