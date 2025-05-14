def solve(n, nums):
	res = float("inf")
	nums.sort()

	for i in range(1, n)):
		res = min(res, nums[i] - nums[i - 1])

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	nums = list(map(int, input().split()))
	print(solve(n, nums))