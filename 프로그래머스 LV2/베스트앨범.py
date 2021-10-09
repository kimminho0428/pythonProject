def solution(genres, plays):
    answer = []
    playDic = {}  # {장르 : 총 재생 횟수}
    dic = {}  # {장르 : [(플레이 횟수, 고유번호)]}

    # 해시 만들기
    for i in range(len(genres)):
        playDic[genres[i]] = playDic.get(genres[i], 0) + plays[i]
        dic[genres[i]] = dic.get(genres[i], []) + [(plays[i], i)]

    # 재생 횟수 내림차순으로 장르별 정렬
    genreSort = sorted(playDic.items(), key=lambda x: x[1], reverse=True)

    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        dic[genre] = sorted(dic[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in dic[genre][:2]]

    return answer

# 1.해시 만들기
#   1-1. playDic : { 장르 : 총 재생 횟수 } 형태로 해시를 만듦
#   1-2. dic : { 장르 : [(플레이 횟수, 고유번호)]} 형태로 해시를 만듦
# 2. playDic을 재생 횟수 내림차순으로 장르별 정렬
#   2-1. playDic을 items()라는 함수를 사용해 튜플로 만듦. x[1]이니까 '총 재생 횟수'를 기준으로 내림차순(reverse = True) 정렬
# 3. 이번엔 dic을 재생횟수 내림차순 & 인덱스 오름차순 정렬
#   3-1. -x[0]의 마이너스는 내림차순의 의미
#   3-2. answer에 장르별로 최대 2개의 고유번호 추가
# 즉, 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트 값')을 사용하면 된다!!
# 딕셔너리(dictionary)는 items()함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있습니다.

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))