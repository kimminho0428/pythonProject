x = int(input())
line = 1

while x > line:
    x -= line # 입력받은 수가 해당 라인의 몇 번째 수인지 나타냄
    line += 1

# line이 짝수일 때
if line % 2 == 0:
    a = x # 분자
    b = line - x + 1 # 분모
else:
    a = line - x + 1
    b = x

print(a, '/', b, sep="")