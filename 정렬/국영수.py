import sys
n = int(sys.stdin.readline())
array = []
for i in range(n):
    input_data = sys.stdin.readline().split()
    array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))
array = sorted(array, key = lambda student:(-student[1], student[2], -student[3], student[0]))

for student in array:
    print(student[0])