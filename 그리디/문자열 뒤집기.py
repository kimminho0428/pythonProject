def solution(s):
    count = {"0": 0, "1": 0}  # 연속된 0과 1의 개수
    last = -1  # 최근 숫자. 0과 1만 존재하므로 -1로 초기화
    for i in s:
        if last != i:  # 연속되지 않은 값이 나오면 실행. ex) 0000'1'
            count[i] += 1  # 해당하는 i의 값 추가
            last = i  # 다른 값이 나왔으므로, 최근 숫자 갱신
    return min(count.values())


print(solution("0001100"))  # 1
print(solution("1000110"))  # 2
print(solution("0110110110111111110111111"))  # 5
print(solution("0" * int(1e7)))  # 0

#2번째 방법
data = input()
count0 = 0
count1 = 0
if data[0] == '1':
    count0 += 1
else:
    count1 += 1
for i in range(len(data)-1):
   if data[i] != data[i+1]:
      if data[i+1] == '1':
        count0 += 1
      else:
        count1 += 1
print(min(count0,count1))
