def solution(name):
    # make_name으로 각 자리의 알파벳을 만들기 위해 움직여야 하는 최소한의 조이스틱 가동횟수를 구한다.
    make_name = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx, answer = 0, 0
    while True:
        # answer에 이 모든 합을 더한다. 이로써 알파벳을 만들기 위한 조이스틱 가동횟수는 모두 구한 것이 된다.
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) == 0:
            break
        left, right = 1, 1
        # 현재 index에서 좌우로 이동방향을 퍼트려 먼저 만나는 방향을 찾는다.
        while make_name[idx - left] == 0:
            left += 1
        while make_name[idx + right] == 0:
            right += 1
        # 그리고 그 방향만치 인덱스를 새로 조정한다.
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer

print(solution("JEROEN"))