# 영어이름을 names에 입력받고 name_cnt에 영어 이름에 포함된 알파벳 대문자 수를 저장한다.
names = input()
name_cnt = [0 for _ in range(26)]

for name in names:
    name_cnt[ord(name)-65] += 1

odd = 0
odd_alpha = ''
alpha = ''
# for문을 돌면서 홀수인 알파벳 대문자가 몇 개 있는지 확인하고 홀수 알파벳과 짝수 알파벳을 저장한다.
for i in range(26):
    if name_cnt[i] % 2 == 1:
        odd += 1
        odd_alpha += chr(i+65)
    alpha += chr(i+65) * (name_cnt[i] // 2)

# 홀수가 2개 이상이면 팰린드롬을 만들 수 없기 때문에 아임소리한수를 출력, 홀수가 1개 이하라면 짝수 알파벳 + 홀수 알파벳 + 짝수알파벳 역순 출력
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alpha+odd_alpha+alpha[::-1])
