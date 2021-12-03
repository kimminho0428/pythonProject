s = input()
s1 = []
s2 = 0

for st in s:
    if st.isalpha():
        s1.append(st)
    else:
        s2 += int(st)
s1.sort()
s1.append(str(s2))

print(''.join(s1))