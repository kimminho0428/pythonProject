A, P = map(int, input().split())
D = [A]
index = 0
while True:
    current = str(D[index])
    next = 0
    for position_num in current:
        next += int(position_num) ** P
    D.append(next)

    if D.count(next) == 2:
        next_index = D.index(next)
        print(len(D[:next_index]))
        break

    index += 1