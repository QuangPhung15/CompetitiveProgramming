def solve(n, nums):
	res = 0
	mx = max(nums)

	for i in range(n):
		res += mx - nums[i]

	return res

n = int(input())
nums = list(map(int, input().split()))
print(solve())