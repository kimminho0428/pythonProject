word = input()
array = [0] * 10
for i in range(len(word)):
    num = int(word[i])
    if num == 6 or num == 9:
        if array[6] < array[9]:
            array[6] += 1
        else:
            array[9] += 1
    else:
        array[num] += 1

print(max(array))