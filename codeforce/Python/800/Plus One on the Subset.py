def solve(n, nums):
	res = 0
	mx = max(nums)

	for i in range(n):
		res = max(res, mx - nums[i])

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	nums = list(map(int, input().split()))
	print(solve(n, nums))