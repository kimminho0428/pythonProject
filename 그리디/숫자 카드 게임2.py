n, m = map(int, input().split())
datas = []
nums = []

for i in range(n):
    datas.append(list(map(int, input().split())))

for data in datas:
    data.sort()
    nums.append(data[0])

nums = sorted(nums, reverse=True)

print(nums[0])
