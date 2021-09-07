def solution(cacheSize, cities):
    # 캐시저장하는 배열생성
    cache = []
    time = 0
    for city in cities:
        # 도시이름은 대문자, 소문자를 구분하지 않으므로 소문자로 구성
        city = city.lower()
        if cacheSize:
            # 캐시배열에 입력도시가 없으면 캐시배열에 도시를 추가하고 시간은 5초 증가, 캐시사이즈를 초과하면 첫번째 캐시 꺼내기
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5
            # 캐시배열에 이미 입력도시가 있으면 그 입력도시의 인덱스를 찾아서 꺼내고 캐시배열에 추가, 시간은 1초 증가
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
        # 캐시사이즈가 0인 경우 캐시미스가 발생하여 시간에 5초만 계속 더해준다.
        else:
            time += 5
    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))