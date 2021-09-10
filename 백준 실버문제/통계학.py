from collections import Counter
import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))
print(round(sum(array) / len(array)))

array.sort()
median = array[len(array)//2]
print(median)

# most_common()은 빈도수가 높은 순으로 리스트 안의 튜플형태로 반환해준다.
k = Counter(array).most_common()

# 만약 입력값이 하나면, 그게 최빈값이 되므로 예외처리
if len(array) > 1:
    # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
    if k[0][1] == k[1][1]:
        print(k[1][0])

    else:
        print(k[0][0])
else:
    print(array[0])

area = max(array) - min(array)
print(area)
