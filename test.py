word = input().lower()
word_list = list(set(word)) # 중복제거 후 집합으로 저장
cnt = [] # 개수를 세는 리스트
for i in word_list:
     count = word.count(i) # 단어의 개수를 셈
     cnt.append(count) # 카운트 한 단어의 개수를 리스트에 저장

if cnt.count(max(cnt)) >= 2: # 카운트 한 단어의 개수 최댓값이 2개 이상이면 물음표
    print("?")
else: # 그렇지 않으면 단어 리스트의 인덱스를 이용하여 단어 대문자 출력
    print(word_list[(cnt.index(max(cnt)))].upper())
