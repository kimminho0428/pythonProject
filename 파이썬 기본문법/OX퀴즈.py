t = int(input())
for i in range(t):
    s = input()
    score = 0
    sumScore = 0
    for j in s:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)