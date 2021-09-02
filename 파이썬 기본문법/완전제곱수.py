m = int(input())
n = int(input())
# 완전제곱수를 담는 리스트
square = []
i = 1

# 완전 제곱수 범위에 있는 수를 리스트에 추가
while i ** 2 <= n:
    if m <= i**2 <= n:
        square.append(i**2)
    i += 1

# 완전제곱수 리스트에 아무것도 없으면 -1 출력
if square == []:
    print(-1)
else:
    print(sum(square))
    print(square[0])