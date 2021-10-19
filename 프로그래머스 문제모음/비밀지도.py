def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for i in range(n):
        # bin함수를 통해 10진수를 2진수로 바꾸고 첫번째 위치부터 마지막 위치까지의 이진수를 bin 배열에 넣어준다.
        # [2:]로 슬라이싱 하는 이유는 0번째가 ob라는 객체가 출력되기 때문에 1번째부터 출력되도록 한다.
        arr1_bin.append(bin(arr1[i])[2:])
        arr2_bin.append(bin(arr2[i])[2:])
        # 1이 아닌 곳은 0으로 넣어준다.
        arr1_bin[i] = ('0' * (n - len(arr1_bin[i]))) + arr1_bin[i]
        arr2_bin[i] = ('0' * (n - len(arr2_bin[i]))) + arr2_bin[i]

        tmp = ''
        for p in range(n):
            # 이진수로 된 2개의 배열에서 하나씩 비교하며 1이 있으면 #, 0이 있으면, 공백을 채워준다.
            if arr1_bin[i][p] == '1' or arr2_bin[i][p] == '1':
                tmp += '#'
            elif arr1_bin[i][p] == '0' and arr2_bin[i][p] == '0':
                tmp += ' '
        answer.append(tmp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))