def solution(s):
   answer = len(s)  # 최소 길이

   # 자르는 단위 늘려가며 최소 길이 계산
   for slice in range(1, len(s) // 2 + 1):
      result = ""  # 압축된 문자열
      count = 1  # 반복되는 횟수
      compare = s[0:slice]  # 자른 문자열

      # 압축된 문자열 구하기
      for i in range(slice, len(s), slice):
         # 문자열이 반복되는 경우
         if compare == s[i: i + slice]:
            count += 1
         # 더 이상 압축할 수 없는 경우
         else:
            if count == 1:
               result += compare
               compare = s[i: i + slice]
            else:
               result += (str(count) + compare)
               count = 1
               compare = s[i: i + slice]

      # 나머지 문자열 처리
      if count == 1:
         result += compare
      else:
         result += (str(count) + compare)

      answer = min(answer, len(result))  # 최소 길이 계산

   return answer

print(solution("aabbaccc"))
