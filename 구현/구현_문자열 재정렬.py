s = input()
length = int(len(s))
sum = 0
a = []
for i in range(length):
    if ord(s[i]) >= 65:
        a.append(s[i])
    elif(ord(s[i]) < 65):
        sum += int(s[i])
a.sort()
sum = str(sum)
print("".join(a)+sum)


