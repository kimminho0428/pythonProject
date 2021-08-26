n = input()
length1 = int(len(n)/2)
length2 = int(len(n))
sum1 = 0
sum2 = 0
status = ""
for i in range(length1):
    sum1 += int(n[i])

for i in range(length1, length2):
    sum2 += int(n[i])

if sum1 == sum2:
  status = "LUCKY"
else:
  status = "READY"

print(status)




