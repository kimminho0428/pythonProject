Day = 0
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeklist = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split())
for i in range(x-1):
    Day = Day + arr[i] # Day와 월별 총 Day 합치기
Day = (y + Day) % 7 # 요일 계산
print(weeklist[Day])
