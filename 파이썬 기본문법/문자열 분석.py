import sys

while True:
    line = sys.stdin.readline().rstrip("\n")

    if not line:
        break

    # 소문자, 대문자, 숫자, 공백
    l, u, d, s = 0, 0, 0, 0
    for i in line:
        if i.islower():
            l += 1
        if i.isupper():
            u += 1
        if i.isdigit():
            d += 1
        if i.isspace():
            s += 1
    print(l, u ,d, s)