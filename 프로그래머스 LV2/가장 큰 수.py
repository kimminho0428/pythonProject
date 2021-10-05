def solution(numbers):
    # 0. key point
    numbers_str = list(map(str, numbers))  # 1. int형의 list를 map을 사용하여 string으로 치환한 뒤, list로 변환한다.
    numbers_str.sort(key=lambda num: num * 3, reverse=True)  # 2. num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교한다.

    return str(int(''.join(numbers_str)))
    # 이를 reverse = True를 통해 내림차순 해주면 6,2,10이 된다. 이것을 ‘‘.join(num)을 통해 문자열을 합쳐주면 된다.
    # int로 변환한 뒤, 또 str로 변환해주는 이유?
    # 모든 값이 0일 때(즉, ‘000’을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다.


print(solution([6, 10, 2]))  # result : 6210
print(solution([3, 30, 34, 5, 9]))  # result : 9534330
print(solution([0, 0, 0, 0]))  # result : 0
