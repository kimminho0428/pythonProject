def solution(s):
    answer = len(s)

    for slice in range(1, len(s) // 2 + 1):
        result = ""
        count = 1
        compare = s[0:slice]

        for i in range(slice, len(s), slice):
            if compare == s[i:i + slice]:
                count += 1
            else:
                if count == 1:
                    result += compare
                    compare = s[i:i + slice]
                else:
                    result += (str(count) + compare)
                    count = 1
                    compare = s[i:i + slice]

        if count == 1:
            result += compare
        else:
            result += (str(count) + compare)

        answer = min(answer, len(result))

    return answer

print(solution("aabbaccc"))