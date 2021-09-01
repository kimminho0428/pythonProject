x = int(input())
line = 1
while x > line:
    x -= line # 입력받은 수가 해당 라인의 몇 번째 수인지 나타냄
    line += 1
if line % 2 == 0: # line이 짝수일 때
    a = line - x + 1 # 분자
    b = x # 분모
else:
    a = x
    b = line - x + 1
print(a, "/" , b, sep="")