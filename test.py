m = int(input())
n = int(input())
square = []
i = 1
while i ** 2 <= n:
    if m <= i**2 <= n:
        square.append(i**2)
    i += 1

if square == []:
    print(-1)
else:
    print(sum(square))
    print(square[0])
