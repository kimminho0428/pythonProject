def solution(routes):
    answer = 1
    # routes를 고속도로 진입시점을 기준으로 정렬을 한다.
    # 그 이유는 맨마지막의 진입시점에 카메라를 한대 설치하고 모든 차량의 나가는시점이 그 이후면 카메라를 1대만 설치해도 되기 때문이다.
    routes.sort(key=lambda x: x[0], reverse=True)

    now = routes[0][0]
    # 시작점은 이미 포함시켰기 때문에 첫번째 이후의 값을 for문으로 탐색
    for i in routes[1:]:
        # 만약 나가는 시점이 now현재 설치되어있는 카메라 시점보다 크거나 같다면 새로운 단속카메라를 설치할 필요가 없기 때문에 무시하고 넘어간다.
        if i[1] >= now:
            continue
        # 나가는 시점이 now현재 설치되어있는 카메라 시점보다 작다면 새로운 카메라를 설치해야한다.
        # 카메라를 최대한 다른 차량도 포함될수 있도록 고속도로 진입시점에 설치를 한다.
        else:
            now = i[0]
            answer += 1

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))