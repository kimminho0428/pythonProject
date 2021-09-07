n = int(input())
count = n
for _ in range(n):
    word = input()
    for i in range(len(word) -1):
        # 해당단어의 인덱스를 찾는데 이때 첫번째 위치의 인덱스를 알려주므로
        # 만약 연속되지않는다면 앞에있는 단어의 인덱스가 뒤에있는 단어의 인덱스보다 크다
        if word.find(word[i]) > word.find(word[i+1]):
            count -= 1
            break
print(count)