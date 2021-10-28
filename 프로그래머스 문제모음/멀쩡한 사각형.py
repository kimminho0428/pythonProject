import math


def solution(w, h):
    # math.gcd는 최대공약수를 구하는 함수
    return w * h - (w + h - math.gcd(w, h))

print(solution(8, 12))