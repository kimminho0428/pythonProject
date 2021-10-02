def solution(array, commands):
    # 1. 우선 반복문을 사용해 commands 2차원 배열을 command에 1차원 배열로 따로 저장해줍니다.
    # 2. new_array에 i번째부터 j번째까지 배열을 복사해줍니다.
    # 3. 그 다음 sort()함수를 써서 정렬해줍니다.
    # 4. 이제 k번째 수를 찾아서 answer배열에 저장해줍니다.
    # * 주의할점 : 만약 new_array가 [2,5,3]일 경우, 2~5까지 자르고 3번째 수를 구해주는 것입니다.
    #                 여기서 command[0]째부터 command[1]번째까지 잘라준다고 생각하여
    #                 배열을 저장해줄때 new_array = array[command[0]:command[1]]  이렇게 짠다면
    #                 command[2]:command[5] 이렇게 나오게 됩니다. => 3번째부터 5번째수까지 잘리게됨.
    #                 n번째부터 자른다고 하면 n-1번째 인덱스부터 잘라주어야합니다!!!!!
    answer = []
    for command in commands:
        new_array = array[command[0] - 1:command[1]]
        new_array.sort()
        answer.append(new_array[command[2] - 1])

    return answer