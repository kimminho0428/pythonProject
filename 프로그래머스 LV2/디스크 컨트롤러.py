def solution(jobs):
    answer = 0
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬, 소요시간이 작을수록 각 작업들이 기다리는 시간이 줄어든다.

    while len(jobs) != 0:
        for i in range(len(jobs)):
            # jobs 길이만큼 for문을 돌리면서 해당 작업의 요청시간이 start(현재까지 진행된 작업 시간)보다 작으면
            # 즉, 해당 작업이 진행된 시간보다 먼저 요청이 들어왔으면 해당 작업을 진행시키고 jobs 배열에서 지워버린다.
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length

print(solution([[0, 3], [1, 9], [2, 6]]	))