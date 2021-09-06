natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)      # 850 + 8 + 5 + 0
    generated_num.add(i) # 생성자가 있는 숫자들

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)