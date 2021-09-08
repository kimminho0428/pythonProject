def solution(files):
    tmp = []
    head, number, tail = '', '', ''

    for file in files:
        for i in range(len(file)):
            # 숫자가 나오면 그 이전은 무조건 HEAD, 이후는 NUMBER, TAIL로 다시 구분
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                # NUMBER와 TAIL 구분 (숫자 안나오면 TAIL)
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                tmp.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    tmp = sorted(tmp, key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(i) for i in tmp]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
