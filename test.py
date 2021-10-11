def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0], reverse=True)
    now = routes[0][0]

    for i in routes[1:]:
        if i[1] >= now:
            continue
        else:
            now = i[0]
            answer += 1

    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
