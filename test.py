s = input()
result = int(s[0])
for i in range(1, len(s)):
    count = int(s[i])
    if result <= 1 or count <= 1:
        result += count
    else:
        result *= count

print(result)