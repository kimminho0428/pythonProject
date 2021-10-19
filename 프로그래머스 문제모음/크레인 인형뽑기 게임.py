def solution(board, moves):
    stacklist = []
    answer = 0

    # move를 통해 인형을 바구니에 담기
    for move in moves:
        for i in range(len(board)):
            # 아무것도 들어있지 않은 0을 제외하고 인덱스이므로 move에서 -1을 뺀 위치에 있는 인형을 바구니로 옮김
            if board[i][move - 1] != 0:
                stacklist.append(board[i][move - 1])
                board[i][move - 1] = 0

                # 바구니에 2개이상 담은 인형 중 순서대로 뒤에 2개가 연속적으로 같으면 인형 터뜨리고 2개인형 더하기
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))