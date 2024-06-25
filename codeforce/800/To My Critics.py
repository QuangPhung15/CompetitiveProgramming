def solve(nums):
	nums.sort()

	if (nums[1] + nums[2] >= 10):
		return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	nums = list(map(int, input().split()))
	print(solve(nums))